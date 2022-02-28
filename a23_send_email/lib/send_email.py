# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: send_email.py
@Time: 2022-02-28 14:58
@Last_update: 2022-02-28 14:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def send_email(
        mail_sender, mail_license, receiver, title, send_text,
        mail_host='smtp.163.com', port=25):
    """向目标邮箱发送邮件"""
    receivers = [receiver]

    mm = MIMEMultipart('related')

    subject_content = title
    mm['From'] = f"opensea_monitor<{mail_sender}>"
    mm["To"] = f"you<{receiver}>"
    mm["Subject"] = Header(subject_content, 'utf-8')

    body_content = send_text
    message_text = MIMEText(body_content, 'plain', 'utf-8')
    mm.attach(message_text)

    stp = smtplib.SMTP()
    stp.connect(mail_host, port)
    stp.set_debuglevel(1)
    stp.login(mail_sender, mail_license)
    stp.sendmail(mail_sender, receivers, mm.as_string())
    stp.quit()

