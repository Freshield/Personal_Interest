# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: AESCipher.py
@Time: 2023-03-05 22:55
@Last_update: 2023-03-05 22:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Crypto.Cipher import AES
import base64

# 加密函数
def aes_encrypt(key, data):
    # 将key转换成16、24、32位的字符串，不足的以空格补齐
    key = key.ljust(32, ' ')
    # 将data转换成16的倍数，不足的以空格补齐
    data = data.ljust(16 * (len(data) // 16 + 1), ' ')
    # 进行加密
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    # 将加密后的数据进行base64编码
    encrypted_data = base64.b64encode(encrypted_data).decode('utf-8')
    return encrypted_data

# 解密函数
def aes_decrypt(key, encrypted_data):
    # 将key转换成16、24、32位的字符串，不足的以空格补齐
    key = key.ljust(32, ' ')
    # 对加密后的数据进行base64解码
    encrypted_data = base64.b64decode(encrypted_data)
    # 进行解密
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    # 去除解密后的数据中的空格
    decrypted_data = decrypted_data.strip()
    return decrypted_data


# 测试
if __name__ == '__main__':
    key = '1234567890123456345345'
    data = 'Hello, world!'
    encrypted_data = aes_encrypt(key, data)
    print('加密后的数据：', encrypted_data)
    decrypted_data = aes_decrypt(key, encrypted_data)
    print('解密后的数据：', decrypted_data)
