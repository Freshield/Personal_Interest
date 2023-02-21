#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: b1_head_firwst.py
@Time: 2019-01-29 11:54
@Last_update: 2019-01-29 11:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='8888',
    db='test_mysqlclient'
)

cur = conn.cursor()

# cur.execute('create table student(id int, name varchar(20),class varchar(30),age varchar(10))')

cur.execute('insert into student values(2,"Tom","2class","9")')

cur.execute('update student set class="3class" where name="Tom"')

cur.execute('select * from student')
print(cur.fetchall())

cur.execute('delete from student where age="9"')

sqli = 'insert into student values(%s,%s,%s,%s)'

cur.executemany(sqli, [
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),
    ])

cur.execute('select * from student')
print(cur.fetchall())

cur.close()
conn.commit()
conn.close()