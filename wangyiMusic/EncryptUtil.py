'''
@author：KongWeiKun
@file: EncryptUtil.py
@time: 18-1-20 下午1:33
@contact: 836242657@qq.com
'''
import os
import time

'''
加密解密
'''
from Crypto.Cipher import AES
import base64


def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:size]

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    ciphertext = str(ciphertext,encoding='utf-8')
    return ciphertext

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
    return format(rs, 'x').zfill(256)



def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    reTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return reTime