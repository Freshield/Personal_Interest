# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: logs.py
@Time: 2023-03-25 20:46
@Last_update: 2023-03-25 20:46
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
import re
import traceback
import datetime
import logging
import sys
from config import LOGS_NUM, LOGS_STREAM_LEVEL, LOGS_FILE_LEVEL, LOGS_DIR_PATH
import colorlog

try:
    import codecs
except ImportError:
    codecs = None


class MultiprocessHandler(logging.FileHandler):
    def __init__(self, filename: str, when='D', backupCount=0, encoding=None, delay=False):
        self.prefix = filename
        self.backupCount = backupCount
        self.when = when.upper()
        self.extMath = r"^\d{4}-\d{2}-\d{2}"

        self.when_dict = {
            'S': "%Y-%m-%d-%H-%M-%S",
            'M': "%Y-%m-%d-%H-%M",
            'H': "%Y-%m-%d-%H",
            'D': "%Y-%m-%d"
        }

        self.suffix = self.when_dict.get(when)
        if not self.suffix:
            print('The specified date interval unit is invalid: ', self.when)
            sys.exit(1)

        self.filefmt = os.path.join(LOGS_DIR_PATH, "%s-%s.log" % (self.prefix, self.suffix))

        self.filePath = datetime.datetime.now().strftime(self.filefmt)

        _dir = os.path.dirname(self.filefmt)
        try:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception as e:
            print('Failed to create log file: ', e)
            print("log_path：" + self.filePath)
            sys.exit(1)

        if codecs is None:
            encoding = None

        logging.FileHandler.__init__(self, self.filePath, 'a+', encoding, delay)

    def shouldChangeFileToWrite(self):
        _filePath = datetime.datetime.now().strftime(self.filefmt)
        if _filePath != self.filePath:
            self.filePath = _filePath
            return True
        return False

    def doChangeFile(self):
        self.baseFilename = os.path.abspath(self.filePath)
        if self.stream:
            self.stream.close()
            self.stream = None

        if not self.delay:
            self.stream = self._open()
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)

    def getFilesToDelete(self):
        dir_name, _ = os.path.split(self.baseFilename)
        file_names = os.listdir(dir_name)
        result = []
        prefix = self.prefix + '-'
        for file_name in file_names:
            if file_name[:len(prefix)] == prefix:
                suffix = file_name[len(prefix):-4]
                if re.compile(self.extMath).match(suffix):
                    result.append(os.path.join(dir_name, file_name))
        result.sort()

        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        try:
            if self.shouldChangeFileToWrite():
                self.doChangeFile()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def write_log():
    log_colors_config = {
        'DEBUG': 'white',  # cyan white
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }

    # 获取主函数文件名
    # log_name = traceback.extract_stack()[0].filename
    # log_name = os.path.splitext(os.path.split(log_name)[-1])[0]
    log_name = 'web3'

    logger = logging.getLogger()
    logger.setLevel(LOGS_FILE_LEVEL)
    # formatter = '%(asctime)s ｜ %(levelname)s ｜ %(filename)s ｜ %(funcName)s ｜ %(module)s ｜ %(lineno)s ｜ %(message)s'
    fmt = logging.Formatter(
        '%(asctime)s｜%(levelname)s|%(filename)s｜%(lineno)s｜%(message)s')
    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s%(asctime)s｜%(levelname)s|%(filename)s｜%(lineno)s｜%(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S',
        log_colors=log_colors_config
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(LOGS_STREAM_LEVEL)
    stream_handler.setFormatter(console_formatter)

    file_handler = MultiprocessHandler(log_name, when='D', backupCount=LOGS_NUM)
    file_handler.setLevel(LOGS_FILE_LEVEL)
    file_handler.setFormatter(fmt)
    file_handler.doChangeFile()

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logging.getLogger("urllib3").setLevel(logging.ERROR)

    return logger


LOGGER = write_log()

if __name__ == "__main__":
    message = 'test writing logs'
    LOGGER.info(message)
    LOGGER.debug(message)
    LOGGER.error(message)
