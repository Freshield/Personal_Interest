# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: send_email.py
@Time: 2023-03-28 21:24
@Last_update: 2023-03-28 21:24
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
import smtplib
from email.mime.text import MIMEText
from config import MAIL_PASS

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "opensea_monitor@163.com"  # 用户名
sender = 'opensea_monitor@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['opensea_monitor@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def send_email(title, content=''):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, MAIL_PASS)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    send_email()
