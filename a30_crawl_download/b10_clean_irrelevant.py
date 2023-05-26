# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b10_clean_irrelevant.py
@Time: 2023-01-31 17:59
@Last_update: 2023-01-31 17:59
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import os
import shutil


if __name__ == '__main__':
    data_dir = '/home/freshield/Downloads/documentchecker/'
    del_path_list = []
    for root, dirs, files in os.walk(data_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # 大小过滤
            # file_size = os.path.getsize(file_path)
            # if file_size < 30000:
            #     del_path_list.append(file_path)
            # # 名称过滤
            # if '&username=Demo' in file_name:
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称uv过滤
            # if 'uv.jpeg' in file_name:
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称uv过滤
            # if 'ir.jpeg' in file_name:
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称thumbnail.jpeg过滤
            # if 'thumbnail.jpg' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称9_0_过滤
            # if '9_0_' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称barcode过滤
            # if 'barcode' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称uv_过滤
            # if 'uv_' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称nanoprint过滤
            # if 'nanoprint' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称magnetic过滤
            # if 'magnetic' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称9_1_过滤
            # if '9_1_' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称10_1_过滤
            # if '10_1_' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称10_0_过滤
            # if '10_0_' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # # 名称holographic过滤
            # if 'holographic' in file_name.lower():
            #     print(file_path)
            #     del_path_list.append(file_path)
            # 名称pearles过滤
            if 'pearles' in file_name.lower():
                print(file_path)
                del_path_list.append(file_path)

    print(len(del_path_list))

    for del_path in del_path_list:
        os.remove(del_path)
