import numpy as np
import dicom
import os
import matplotlib.pyplot as plt
from glob import glob
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage
from skimage import morphology
from skimage import measure
from skimage.transform import resize
from sklearn.cluster import KMeans
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *

import plotly
plotly.offline.init_notebook_mode()

#
#The helper function
#Loop over the image files and store everything into a list.
#conver the voel value to HU
#
output_path = working_path = 'Output/dujie_CT/'
#output_path = working_path = 'Output/'
id = 0
#data_path = 'Data/sample_images/5267ea7baf6332f29163064aecf6e443/'
#data_path = 'Data/sample_images/0acbebb8d463b4b9ca88cf38431aac69/'
data_path = 'Data/dujie_CT/'

#Read the files and set the thickness as the first one value
def load_scan(path):
    #each slice in slices is a dic of many info like:
    #patient's name, id, image position,orientation and so on
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    #!!!Here should be multiple -1, otherwise the image is reverse
    #!!!Different data has different sequence
    slices.sort(key= lambda x: int(x.InstanceNumber * -1))
    #the thickness is same in all of the data
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness

    return slices

#Take the pixel array from the slice, and process the image
def get_pixels_hu(scans):
    #put data as a two dimensions
    #here only use the slice's pixel array data which size is (512,512)
    image = np.stack([s.pixel_array for s in scans])
    #Convert to int16 (from sometimes int16),
    #should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)

    #Set outside-of-scan pixels to 1
    #The intercept is usually -1024, so air is approximately 0
    #!!! why only image equals -2000?and air should equals to -1000 !!!
    image[image == -2000] = 0

    #Convert to Hounsfield units (HU)
    #!!! take the first data as some templete?
    #Ans: yes, because the rescaleIntercept are same
    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)
    image[image < -1500] = -1024


    return np.array(image, dtype=np.int16)

#Read files, transfer to images and save
def prepare_datalist():

    #!!!the /*.dcm can be *.dcm!!!
    g = glob(data_path + '/*.dcm')

    print 'Total of %d DICOM images. \nFirst 5 filenames:' % len(g)
    print '\n'.join(g[:5])
    patient = load_scan(data_path)
    #imgs shape is (134,512,512)
    imgs = get_pixels_hu(patient)
    np.save(output_path + "fullimages_%d.npy" % (id), imgs)

#show the images' values as the histogram
def show_histogram():
    file_used = output_path + 'fullimages_%d.npy' % id
    imgs_to_process = np.load(file_used).astype(np.float64)

    plt.hist(imgs_to_process.flatten(), bins=50, color='c')
    plt.xlabel('Hounsfield Units (HU)')
    plt.ylabel('Frequency')
    plt.show()

#Show the images as subplots
def sample_stack(stack, rows=6, cols=6, start_with=10, show_every=3):
    fig,ax = plt.subplots(rows,cols,figsize=[12,12])
    #from 10, show each 3 images
    for i in range(rows*cols):
        ind = start_with + i * show_every
        ax[int(i/rows),int(i%rows)].set_title('slice %d' % ind)
        ax[int(i/rows),int(i%rows)].imshow(stack[ind],cmap='gray')
        ax[int(i/rows),int(i%rows)].axis('off')
    plt.show()

#Show the images as subplots, driver
def display_image_stack():
    file_used = output_path + 'fullimages_%d.npy' % id
    imgs_to_process = np.load(file_used).astype(np.float64)
    sample_stack(imgs_to_process)

#Show the slice thickness
def show_thick():
    patient = load_scan(data_path)
    #The thickness is the first and second slice position diff, and set all of the slice equally
    print 'Slice Thickness: %f' % patient[0].SliceThickness
    #The pixel spacing is in the plane not the depth
    #usually it is 370mm x 370mm, and 512 x 512 voxels, so 370 / 512 = 0.723
    print 'Pixel Spacing (row, col): (%f, %f) ' % (patient[0].PixelSpacing[0], patient[0].PixelSpacing[1])
    print len(patient)
    print 370. / 512.

#The image reshaping
#!!!There have some problem about the resize factor
def resample(image, scan, new_spacing=[1,1,1]):
    #Determine current pixel spacing
    #float the data
    #SliceThickness is the depth, PixelSpacing is the width and length
    #The plus is take the slicethickness and pixelspacing into three values vector
    spacing = map(float, ([scan[0].SliceThickness] + scan[0].PixelSpacing))
    #spacing (3,1), (thickness, width, length)
    spacing = np.array(list(spacing))

    #to get the resize factor so that the new shape is integer
    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    #np.round is cut the decimal, like 3.3333 -> 3.
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_sapcing = spacing / real_resize_factor

    image = scipy.ndimage.interpolation.zoom(image,real_resize_factor)

    return image, new_spacing

#The image reshaping testing
#!!!There have some problem about the resize factor
def my_resample(image, scan, new_spacing=[1,1,1]):
    #Determine current pixel spacing
    #float the data
    #SliceThickness is the depth, PixelSpacing is the width and length
    #The plus is take the slicethickness and pixelspacing into three values vector
    spacing = map(float, ([scan[0].PixelSpacing[0]] + [scan[0].SliceThickness] + [scan[0].SliceThickness]))
    #spacing (3,1), (thickness, width, length)
    spacing = np.array(list(spacing))

    #to get the resize factor so that the new shape is integer
    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    #np.round is cut the decimal, like 3.3333 -> 3.
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_sapcing = spacing / real_resize_factor

    image = scipy.ndimage.interpolation.zoom(image,real_resize_factor)

    return image, new_spacing

#The image reshaping, driver
def resampling():
    patient = load_scan(data_path)
    file_used = output_path + 'fullimages_%d.npy' % id
    imgs_to_process = np.load(file_used).astype(np.float64)
    print 'Shape before resampling\t', imgs_to_process.shape
    imgs_after_resample, spacing = resample(imgs_to_process, patient, [1,1,1])
    print 'Shape after resampling\t', imgs_after_resample.shape

def make_mesh(image, threshold=-300, step_size=1):

    print 'Transposing surface'
    #transposing the dimension, like(2,3,3) -> (3,3,2)
    p = image.transpose(2,1,0)

    print 'Calculating surface'
    verts, faces, norm, val = measure.marching_cubes(p, threshold, step_size=step_size, allow_degenerate=True)
    return verts, faces

def plotly_3d(verts, faces):
    #zip function let the 3 layer(r,g,b) into tunple and distribute to x,y,z
    x,y,z = zip(*verts)

    print 'Drawing'

    #Make the colormap single color since the axes are positional not intensity
    #colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
    colormap = ['rgb(236,236,212)','rgb(236,236,212)']

    fig = FF.create_trisurf(x=x,
                            y=y,
                            z=z,
                            plot_edges=False,
                            colormap=colormap,
                            simplices=faces,
                            backgroundcolor='rgb(64,64,64',
                            title="Interactive Visualization"
                            )
    iplot(fig)

def plt_3d(verts, faces):
    print 'Drawing'
    x, y, z = zip(*verts)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    #Fancy indexing: 'verts[faces]' to generate a collection of trangles
    mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
    face_color = [1, 1, 0.9]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_zlim(0, max(z))
    ax.set_axis_bgcolor((0.7,0.7,0.7))
    plt.show()

#Standardize the pixel values
def make_lungmask(img, display=False):
    row_size = img.shape[0]
    col_size = img.shape[1]

    mean = np.mean(img)
    std = np.std(img)
    img = img - mean
    img = img / std

    #Find the average pixel value near the lungs
    #to renormalize washed out images
    middle = img[int(col_size / 5):int(col_size / 5 * 4), int(row_size / 5):int(row_size / 5 * 4)]
    mean = np.mean(middle)
    max = np.max(img)
    min = np.min(img)

    #To improve threshold finding, I'm moving the
    #underflow and overflow on the pixel spectrum
    img[img == max] = mean
    img[img == min] = mean

    #Using Kmeans to separate foreground (soft tissue / bone) and background (lung/air)
    kmeans = KMeans(n_clusters=2).fit(np.reshape(middle, [np.prod(middle.shape),1]))
    centers = sorted(kmeans.cluster_centers_.flatten())
    threshold = np.mean(centers)
    #if value < threshold, set value to 1.0, else 0.0
    thresh_img = np.where(img<threshold,1.0,0.0)

    #First erode away the finer elements, then dilate to include some of the pixels
    # surrounding the lung.
    #We don't want to accidentally clip the lung
    eroded = morphology.erosion(thresh_img, np.ones([3,3]))
    dilation = morphology.dilation(eroded, np.ones([8,8]))

    # Different labels are displayed in different colors
    labels = measure.label(dilation)

    mask = dilation
    """
    #get all of the unique values in data
    label_vals = np.unique(labels)
    regions = measure.regionprops(labels)
    good_labels = []
    for prop in regions:
        B = prop.bbox
        if B[2] - B[0] < row_size / 10 * 9 and B[3] - B[1] < col_size / 10 * 9 and B[0] > row_size / 5 and B[2] < \
                col_size / 5 * 4:
            good_labels.append(prop.label)
        mask = np.ndarray([row_size, col_size], dtype=np.int8)
        mask[:] = 0

    #After just the lungs are left, we do another large dilation
    #in order to fill in and out the lung mask

    for N in good_labels:
        mask = mask + np.where(labels == N, 1, 0)
    """
    #one last dilation
    mask = morphology.dilation(mask, np.ones([10,10]))



    #Show the images
    if display:
        fig, ax = plt.subplots(3, 2, figsize=[12, 12])
        ax[0,0].set_title('Original')
        ax[0,0].imshow(img, cmap='gray')
        ax[0,0].axis('off')
        ax[0,1].set_title('Threshold')
        ax[0,1].imshow(thresh_img, cmap='gray')
        ax[0,1].axis('off')
        ax[1,0].set_title('After Erosion and Dilation')
        ax[1,0].imshow(dilation, cmap='gray')
        ax[1,0].axis('off')
        ax[1,1].set_title('Color Labels')
        ax[1,1].imshow(labels)
        ax[1,1].axis('off')
        ax[2,0].set_title('Final Mask')
        ax[2,0].imshow(mask, cmap='gray')
        ax[2,0].axis('off')
        ax[2,1].set_title('Apply Mask on Original')
        ax[2,1].imshow(mask*img, cmap='gray')
        ax[2,1].axis('off')

        plt.show()

    return mask * img



#prepare_datalist()
#show_histogram()
#display_image_stack()
#show_thick()
#resampling()

"""
patient = load_scan(data_path)
file_used = output_path + 'fullimages_%d.npy' % id
imgs_to_process = np.load(file_used).astype(np.float64)
print(imgs_to_process.shape)
print(np.max(imgs_to_process))
print(np.min(imgs_to_process))
imgs_cut = imgs_to_process[:,200:350,:]
print(imgs_cut.shape)
print(np.max(imgs_cut))
print(np.min(imgs_cut))
print 'Shape before resampling\t', imgs_cut.shape
imgs_after_resample, spacing = resample(imgs_cut, patient, [1,1,1])
print 'Shape after resampling\t', imgs_after_resample.shape
#verts, faces = make_mesh(imgs_cut,350,2)
#plt_3d(verts, faces)
"""

"""
#patient = load_scan(data_path)
#file_used = output_path + 'fullimages_%d.npy' % (id)
#imgs_to_process = np.load(file_used).astype(np.float64)
#imgs_after_resample, spacing = resample(imgs_to_process, patient, [1,1,1])
#np.save(output_path + "resampleimages_%d.npy" % (id), imgs_after_resample)
file_used = output_path + 'resampleimages_%d.npy' % (id)
imgs_after_resample = np.load(file_used).astype(np.float64)
verts, faces = make_mesh(imgs_after_resample,350,2)
plt_3d(verts, faces)
"""

"""
file_used = output_path + 'maskedimages_%d.npy' % (id)
imgs_to_process = np.load(file_used).astype(np.float64)
verts, faces = make_mesh(imgs_to_process,0,2)
plt_3d(verts, faces)
"""

"""
patient = load_scan(data_path)
imgs_to_process = get_pixels_hu(patient)
imgs_after_resample, spacing = resample(imgs_to_process, patient, [1,1,1])
sample_stack(imgs_after_resample)
"""


#patient = load_scan(data_path)
#imgs_to_process = get_pixels_hu(patient)
#imgs_after_resample, spacing = resample(imgs_to_process, patient, [1,1,1])
file_used = output_path + 'resampleimages_%d.npy' % (id)
imgs_after_resample = np.load(file_used).astype(np.float64)
masked_lung = []
for img in imgs_after_resample:
    masked_lung.append(make_lungmask(img))

sample_stack(masked_lung, show_every=10)

np.save(output_path + 'maskedimages_%d.npy' % (id), masked_lung)
""""""

"""
#patient = load_scan(data_path)
#imgs_to_process = get_pixels_hu(patient)
#imgs_after_resample, spacing = resample(imgs_to_process, patient, [1,1,1])
#np.save(output_path + 'resampleimages_%d.npy' % (id), imgs_after_resample)
file_used = output_path + 'resampleimages_%d.npy' % (id)
imgs_after_resample = np.load(file_used).astype(np.float64)
img = imgs_after_resample[560]
make_lungmask(img,display=True)
"""