from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def encrypt(data, pub_key_bytes):
    cipher = PKCS1_OAEP.new(RSA.import_key(pub_key_bytes))
    return cipher.encrypt(data.encode())

def decrypt(enc_data, priv_key_bytes):
    cipher = PKCS1_OAEP.new(RSA.import_key(priv_key_bytes))
    return cipher.decrypt(enc_data).decode()

if __name__ == '__main__':
    private_key, public_key = generate_keys()
    msg = 'HelloRSA'
    enc = encrypt(msg, public_key)
    print('Encrypted:', enc)
    print('Decrypted:', decrypt(enc, private_key))
