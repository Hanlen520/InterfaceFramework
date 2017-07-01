#coding=utf-8

import hashlib

class EncryptMD5(object):
    def __init__(self):
        pass

    @classmethod
    def encrypt_md5(cls, text):
        """
        :函数功能: 实现MD5加密
        :参数:
            text: string，被加密的内容
        :返回值: string，加密后的内容
        """
        m5 = hashlib.md5()
        m5.update(text)
        return m5.hexdigest()