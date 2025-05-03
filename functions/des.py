# Data Encryption Standard (DES) implementation using PyCryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
cipher = DES.new(key, DES.MODE_ECB)

def encrypt(data):
    return cipher.encrypt(pad(data.encode(), DES.block_size))

def decrypt(enc_data):
    return unpad(cipher.decrypt(enc_data), DES.block_size).decode()

if __name__ == '__main__':
    text = 'HelloDES'
    enc = encrypt(text)
    print('Encrypted:', enc)
    print('Decrypted:', decrypt(enc))
