# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_split_file.py
@Time: 2022-10-13 15:54
@Last_update: 2022-10-13 15:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from PyPDF2 import PdfFileReader, PdfFileWriter


if __name__ == '__main__':
    file_path = '/home/freshield/projects/Backup_files/works/resume/web3后端_统一title_20221017/于洋Fresh.pdf'
    pdf_file = PdfFileReader(file_path)
    writer = PdfFileWriter()

    for i in range(2):
        writer.add_page(pdf_file.getPage(i))

    with open('test.pdf', 'wb') as f:
        writer.write(f)


