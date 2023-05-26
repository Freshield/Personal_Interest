# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t3_generate_rsa_keys.py
@Time: 2023-03-29 11:36
@Last_update: 2023-03-29 11:36
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Crypto import Random
from Crypto.PublicKey import RSA


if __name__ == '__main__':
    key_name = 'phone'

    random_generator = Random.new().read
    rsa = RSA.generate(1024, random_generator)

    private_pem = rsa.exportKey()
    with open(f'../data/secret_data/{key_name}_private.pem', 'w') as f:
        f.write(private_pem.decode('utf-8'))

    public_pem = rsa.publickey().exportKey()
    with open(f'../data/secret_data/{key_name}_public.pem', 'w') as f:
        f.write(public_pem.decode('utf-8'))
