# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: MsgRsaCryptor.py
@Time: 2023-03-29 14:01
@Last_update: 2023-03-29 14:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import rsa
import base64
from io import BytesIO
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


class MsgRsaCryptor(object):
    """对信息进行加解密的类"""
    def __init__(self, self_priv_key_file, other_pub_key_file):
        self.self_priv_key = rsa.PrivateKey.load_pkcs1(open(self_priv_key_file).read().encode())
        self.other_pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(open(other_pub_key_file).read().encode())
        self.decrypt_length = 1024 // 8
        self.encrypt_length = self.decrypt_length - 11

    def encrypt_data(self, text: str) -> str:
        ret = BytesIO()
        text_bytes = BytesIO(text.encode("utf-8"))
        encrypt_segment = text_bytes.read(self.encrypt_length)
        while encrypt_segment:
            ret.write(rsa.encrypt(encrypt_segment, self.other_pub_key))
            encrypt_segment = text_bytes.read(self.encrypt_length)
        return base64.b64encode(ret.getvalue()).decode('utf-8')

    def decrypt_data(self, text: str) -> str:
        ret = BytesIO()
        text_bytes = base64.b64decode(text.encode("utf-8"))
        text_byte_fragments = self._text_bytes_split(text_bytes, self.decrypt_length)
        for fragment in text_byte_fragments:
            ret.write(rsa.decrypt(fragment, self.self_priv_key))
        return ret.getvalue().decode()

    def _text_bytes_split(self, text_bytes: bytes, per_size: int) -> list:
        max_legth = len(text_bytes)
        ret = list()
        current_index = 0
        while current_index < max_legth:
            ret.append(text_bytes[current_index: current_index + per_size])
            current_index += per_size
        return ret


if __name__ == '__main__':
    msg = "789"
    public_key_file = "../data/secret_data/phone_public.pem"
    private_key_file = '../data/secret_data/server_private.pem'
    msg_cryptor = MsgRsaCryptor(private_key_file, public_key_file)
    # encrypt_text = msg_cryptor.encrypt_data(msg)
    # print(encrypt_text)
    # exit()
    # encrypt_text = "CqhM97j+rAXXCUdGrrJhEDDRQjCUI57411r8GZhNgWKahaJgx4xPj0jdGgcCAKWLTSz9284Gbl2qThdnvywKSOqGDYlTOHFOmbE31J1DqTi7flqKnnHAFfaYaPCU20F/sDfoouhWOz4IV5ifyMGWWulpwIozz1lOSw5/v7Q6yw4="
    encrypt_text = 'U0RyUu03zs5qJEIPlTm8U8vA4XZ/KiWjMUESn3OtiQ4+Kzilvp4hYYCLTPURiDIVUcgG0ZMhDKq+mkhsLmEasM1+o4BsMOuKPGht1NlIT0UlTwDjdOPz1qE/wo3iExmscFrmyPzETZlKQ0s2QjVnAaHhsWb16eRxew8EH0yJfOQ='
    encrypt_text = 'mFgvm0EbGXsJIIQueczmFIdTa0008zXND8li9yAeRKVkfWX0oxODBU56GIYPIOiI+RirW4oVVOpiIsVS/N+4ErSgqMiRubgy31vrQfLLvIjKq3Entwf7Mgz8cOxiz1v6TnQaUJRVrqDrgxfPmFxbKCNaj9QxuAJJt7MfgrPiZ7U='
    decrypt_text = msg_cryptor.decrypt_data(encrypt_text)
    print(decrypt_text)
    print(msg == decrypt_text)