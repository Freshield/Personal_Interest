# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b8_modify_fiel_name.py
@Time: 2023-01-27 12:44
@Last_update: 2023-01-27 12:44
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
from tqdm import tqdm


if __name__ == '__main__':
    data_dir = 'data/download/documentchecker/passport'
    nation_info_path = 'data/contry_code.json'
    with open(nation_info_path, 'r') as f:
        nation_info_dict = json.loads(f.read())

    tq = tqdm(os.listdir(data_dir), 'processing files...')
    for file_name in tq:
        # ensure file path is file
        file_path = os.path.join(data_dir, file_name)
        if not os.path.isfile(file_path):
            continue
        # get code and nation name
        code = file_name.split('_')[0]
        if code not in nation_info_dict:
            continue
        nation_name = nation_info_dict[code]
        # create dir
        save_dir = os.path.join(data_dir, nation_name)
        os.makedirs(save_dir, exist_ok=True)
        # create new name
        end_part = file_name.split(f'{code}_')[-1]
        new_path = os.path.join(save_dir, f'{nation_name}_{end_part}')
        shutil.move(file_path, new_path)
