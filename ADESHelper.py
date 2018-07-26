# encoding:utf-8
"""
:param key:
        The secret key to use in the symmetric cipher.
        It must be 8 byte long. The parity bits will be ignored.
:type key: bytes/bytearray/memoryview

**iv** (*byte string*) --
            (Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
            and ``MODE_OPENPGP`` modes).
For ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB`` it must be 8 bytes long.
:encrypt_test:
plaintext : bytes/bytearray/memoryview
            The piece of data to encrypt.
            It can be of any length.

"""
import base64
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import base64
import json
import os


class Crypt(object):
	secret_key = '1234567812345678'
	iv = '1234567812345678'

	def encypt(self, s):
		# 加密
		PADDING = '\0'
		pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
		print('输出byte string类型：')
		print(str.encode(self.iv))
		cipher = AES.new(str.encode(pad_it(self.secret_key)), AES.MODE_CBC, str.encode(self.iv))
		print('b')
		msg = cipher.encrypt(str.encode(pad_it(s)))
		print('c')
		print("输出加密后的类型：")
		print(type(msg))
		return base64.b64encode(msg)  # python3不太一样：因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码。

	def descypt(self, s):
		# 解密
		PADDING = '\0'
		pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
		cipherX = AES.new(str.encode(pad_it(self.secret_key)), AES.MODE_CBC, str.encode(self.iv))
		bytedt = base64.b64decode(s)
		print("base64.b64decode后的类型:")
		print(type(bytedt))
		print(bytedt)
		y = cipherX.decrypt(bytedt)
		print("decrypt解密后的bytes：")
		print(type(y))
		print(y)
		# return str(y, encoding='utf-8').strip('\0')
		return str(y).strip('\0')


key = '11111111'
iv = '12345678'
padding = '\0'


class DESTest(object):
	def __init__(self):
		if len(key) == 8:
			self.key = key
		if len(iv) > 0:
			self.iv = iv

	def encrypt(self, encrypt_str):
		pad_it = lambda s: s + (8 - len(s) % 8) * padding
		cipher = DES.new(str.encode(self.key), DES.MODE_CBC, str.encode(self.iv))
		print('b')
		msg = cipher.encrypt(str.encode(pad_it(encrypt_str)))
		print('c')
		print("输出加密后的类型：")
		print(type(msg))
		return base64.b64encode(msg)

	def decrypt(self, deccrypt_text):
		# pad_it = lambda s: s + (8 - len(s) % 8) * padding
		cipher = DES.new(str.encode(self.key), DES.MODE_CBC, str.encode(self.iv))
		s = base64.b64decode(deccrypt_text)
		y = cipher.decrypt(s)
		return y



s = input("请输入明文：")
print("输出明文的长度：")
print(type(s))
print(len(s))

# s1 = eval(s)
# print(type(s1))
# print(len(s1))

s2 = json.dumps(s)
print(type(s2))
print(len(s2))

obj = Crypt()
a = obj.encypt(s2)
print("输出加密后的密文：")
print(a)

b = obj.descypt(a)
# paramt=str(ret,'UTF-8').replace('\n','')
# b=obj.descypt('0tp9fj2yP+frszS+si9Tv/tCq/ykQI0dkVNMnLNhKcRE/wN51CVy4De3oXI+OYB8zfan0pFVekl2\r\n8D7JIfdmX9SkNgrhcQOTcLJH0r/L6kvUWiGhj6AeJXkZqWIwcks+vsg5/2lxXzZv0ogDW5ZIUg=='.replace("\n", ""))
print("输出解密后的明文：")
print(b)

if __name__ == '__main__':
	s = DESTest().encrypt("sfsdfs")
	print s
	print DESTest().decrypt(s)
