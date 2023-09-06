# from Crypto.Cipher import AES
# from cryptography.hazmat.primitives import padding
# import base64
# import binascii
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives.ciphers import algorithms
# from binascii import b2a_hex, a2b_hex
#
# class aesCrypt():
#     def __init__(self,key,encode_):
#         self.encode_ = encode_
#         self.model = AES.MODE_ECB
#         self.key = self.add_16(key)
#         self.BS = AES.block_size
#         self.aes = AES.new(self.key, self.model)
#         self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
#         self.unpad = lambda s: s[0:-ord(s[-1])]
#         # 创建一个aes对象
#
#         # 这里的密钥长度必须是16、24或32，目前16位的就够用了
#
#     def add_16(self, par):
#         par = par.encode(self.encode_)
#         while len(par) % 16 != 0:
#             par += b'\x00'
#         return par
#
#     def aesencrypt(self, text):
#         text = self.pad(text)
#
#         text = self.add_16(text)
#
#         self.encrypt_text = self.aes.encrypt(text)
#         #return base64.encodebytes(self.encrypt_text).decode().strip()
#         return binascii.hexlify(self.encrypt_text).decode("utf8")
#
#     def aesdecrypt(self, text):
#         text = base64.decodebytes(text.encode(self.encode_))
#         self.decrypt_text = self.aes.decrypt(text)
#         return self.decrypt_text.decode(self.encode_).strip('\0')



import base64
import json
import binascii
import requests
from Crypto.Cipher import AES
import hashlib
from data import readConfig
class encryptData:
    def __init__(self):
        self.user=readConfig.readConfig()
        key=self.user.get_user('appSecret')
        self.key = key.encode("utf-8")  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        #msg = str(base64.b64encode(res), encoding="utf8")
        msg= binascii.hexlify(res).decode("utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)

    def getMd5(self,text):
        md5=hashlib.md5()
        md5.update(text.encode("utf8"))
        value=md5.hexdigest()
        value=value.upper()
        return value


if __name__ == '__main__':
    aes=encryptData()
    #c="b87a4192c3de0b5e25b8c2bdb6505933"
    #b="湖州云海房地产开发有限公司"
    #c=aes.encrypt(b)
    #print(c)
    c='I34Na9HobuNQ4aRVapp_keyV5cdTGEMVHcc2o5Lid_cardd9e34046d346cac6380a758be38e13b1e2af9ce2e3b6c79c8712c755ff45f29bmobilefb54f43bbfb4319662d50499df735d05name282497f487dc7253afe8eeef0b04d49etimestamp1605574116362'
    d=aes.getMd5(c)
    print(d)