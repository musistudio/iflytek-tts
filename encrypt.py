from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import hashlib


class PrpCrypt(object):

    def __init__(self, myAES):
        self.myAES = myAES.encode('utf-8')
        self.MODE = AES.MODE_ECB

    def encrypt(self, text):
        cryptor = AES.new(self.myAES, self.MODE)
        pad_pkcs7 = pad(text.encode('utf-8'), AES.block_size, style='pkcs7')
        encrypt_aes = cryptor.encrypt(pad_pkcs7)
        encrypted_text = base64.b64encode(encrypt_aes).decode('utf-8')
        return encrypted_text


    def decrypt(self, text):
        cryptor = AES.new(self.myAES, self.MODE)
        plain_text = cryptor.decrypt(base64.b64decode(text))
        text = bytes.decode(plain_text).rstrip('\n').rstrip('\xc6').rstrip('\x00').rstrip('\x06')
        return text

    def md5(self, text):
        m2 = hashlib.md5()
        m2.update(text.encode('utf-8'))
        return m2.hexdigest()



