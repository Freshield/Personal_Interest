import numpy as np

a = np.arange(12).reshape((3,2,2))
print a
b = a.transpose(2,1,0)
print b.shape
print b
print a[0,1,0]
print b[0,1,0]

a = 1
b = [2,2]
c = map(float, ([b[0]] + [a] + [a]))
print c

print 370 / 5 * 3