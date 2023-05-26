# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: AESCipher.py
@Time: 2023-03-07 21:39
@Last_update: 2023-03-07 21:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import hashlib
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b"".decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def decrypt_string(self, enc):
        enc = base64.b64decode(enc)
        return self.decrypt(enc).decode('utf8')


if __name__ == '__main__':
    encrypt = "P37w+VZImNgPEO1RBhJ6RtKl7n6zymIbEG1pReEzghk="
    cipher = AESCipher("test key")
    print("明文:\n{}".format(cipher.decrypt_string(encrypt)))
    # 明文:hello world