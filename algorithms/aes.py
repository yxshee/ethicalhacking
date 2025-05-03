from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'16byteaeskey1234'

def encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct

def decrypt(enc_data):
    iv = enc_data[:AES.block_size]
    ct = enc_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

if __name__ == '__main__':
    text = 'HelloAES'
    enc = encrypt(text)
    print('Encrypted:', enc)
    print('Decrypted:', decrypt(enc))
