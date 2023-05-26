# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t0_dirty_work.py
@Time: 2023-01-26 17:30
@Last_update: 2023-01-26 17:30
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
import json
import shutil


if __name__ == '__main__':
    # file_path = '../data/contry_code.txt'
    # with open(file_path, 'r') as f:
    #     element_str = f.read()

    # element_str = element_str.replace('</option>', '</option>\n')
    # with open(file_path, 'w') as f:
    #     f.write(element_str)
    # exit()

    # element_str_list = element_str.split('\n')
    # code_dict = dict()
    # for line in element_str_list:
    #     code = line.split('value="')[-1].split('">')[0]
    #     name = line.split('">')[-1].split('</option>')[0].replace(' ', '')
    #     code_dict[code] = name
    #
    # with open(file_path.replace('.txt', '.json'), 'w') as f:
    #     f.write(json.dumps(code_dict, indent=4))

    # data_dir = '../data'
    # file_path_dict = {
    #     'canada': 'ca_driver_license_element.json',
    #     'usa': 'us_driver_license_element.json',
    #     'mexico': 'mexico_driver_license_element.json',
    #     'tribes': 'tribes_driver_license_element.json'
    # }
    #
    # driver_license_dict = dict()
    # for nation, file_name in file_path_dict.items():
    #     file_path = os.path.join(data_dir, file_name)
    #     with open(file_path, 'r') as f:
    #         data_dict = json.loads(f.read())
    #     for code, name in data_dict.items():
    #         driver_license_dict[code] = {'name': name, 'nation': nation}
    #
    # print(json.dumps(driver_license_dict, indent=4))
    # with open('../data/driver_license_info.json', 'w') as f:
    #     f.write(json.dumps(driver_license_dict, indent=4))

    # file_path = '../data/contry_code.json'
    # with open(file_path, 'r') as f:
    #     info_dict = json.loads(f.read())
    #
    # rst_dict = dict()
    # for code, name in info_dict.items():
    #     rst_dict[code] = name.replace('/', '_').replace(',', '_')
    #
    # print(json.dumps(rst_dict, indent=4))
    # with open(file_path, 'w') as f:
    #     f.write(json.dumps(rst_dict, indent=4))

    # data_dir = '../data/download/documentchecker/driver_license'
    # for file_name in os.listdir(data_dir):
    #     file_path = os.path.join(data_dir, file_name)
    #     if 'British' in file_path:
    #         save_path = file_path.replace('%20', '')
    #         print(save_path)
    #         print(file_path)
    #         # shutil.move(file_path, save_path)
    #         exit()

    file_path = '../data/driver_license_info.json'
    with open(file_path, 'r') as f:
        driver_license_dict = json.loads(f.read())
    rst_dict = dict()
    for code, sub_dict in driver_license_dict.items():
        name, nation = sub_dict['name'], sub_dict['nation']
        rst_dict[name] = {'code': code, 'nation': nation}

    with open(file_path, 'w') as f:
        f.write(json.dumps(rst_dict, indent=4))



