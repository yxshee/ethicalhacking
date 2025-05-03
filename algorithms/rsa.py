# RSA implementation using PyCryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

def encrypt(data):
    return cipher.encrypt(data.encode())

def decrypt(enc_data):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    return cipher.decrypt(enc_data).decode()

if __name__ == '__main__':
    msg = 'HelloRSA'
    enc = encrypt(msg)
    print('Encrypted:', enc)
    print('Decrypted:', decrypt(enc))
