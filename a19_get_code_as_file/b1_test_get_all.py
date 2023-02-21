#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_test_get_all.py
@Time: 2020-04-08 16:15
@Last_update: 2020-04-08 16:15
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



def get_str_list_from_file(file_path):
    rst_list = []
    in_cote = False
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for num, line in enumerate(lines):

            if '"""' in line:
                if in_cote is False:
                    in_cote = True
                else:
                    in_cote = False
                continue
            elif in_cote:
                continue
            elif len(line.strip()) == 0:
                continue
            elif '#' in line:
                continue

            if len(line) > 50:
                line_list = line.split(' ')
                count = 0
                index = 0
                index_list = [0]
                for tmp in line_list:
                    count += len(tmp)+1
                    if count > 50:
                        index_list.append(index-1)
                        count = 0
                    index += 1
                for i in range(len(index_list)):
                    if i != len(index_list) - 1:
                        tmp_line = ' '.join(line_list[index_list[i]:index_list[i+1]]) + '\n'
                    else:
                        tmp_line = ' '.join(line_list[index_list[i]:])
                    rst_list.append(tmp_line)
            else:
                rst_list.append(line)
    # index = 0
    # return_list = []
    # for num, line in enumerate(rst_list):
    #     if len(line.strip()) != 0:
    #         index = index % 50
    #         line = '%d    %s' % (index+1, line)
    #         index += 1
    #         return_list.append(line)
    # rst_list = ['%-4d  %s' % (num+1, line) for (num, line) in enumerate(rst_list) if len(line) != 0]
    # rst_list = ['  %s' %  line for (num, line) in enumerate(rst_list) if len(line) != 0]

    return rst_list


if __name__ == '__main__':
    file_path = 'data/file.txt'
    file_list = get_str_list_from_file(file_path)
    rst_lines = ''.join(file_list)
    with open('data/rst_file1.txt', 'w') as f:
        f.write(rst_lines)