# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_analyse_opensea.py
@Time: 2022-02-28 11:56
@Last_update: 2022-02-28 11:56
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import logging
from concurrent.futures import ProcessPoolExecutor
from lib.set_logger import set_logger
from config import project_names
from lib.run_single_project import run_single_project


if __name__ == '__main__':
    set_logger()
    logging.info('begin the bot')

    logging.info('Init the items info')
    with ProcessPoolExecutor(len(project_names)) as executor:
        executor.map(run_single_project, project_names)

