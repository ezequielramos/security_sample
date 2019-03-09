from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

print(private_key.exportKey())
print()
print(public_key.exportKey())

print()
print("-" * 35)
print()

public_cipher_rsa = PKCS1_OAEP.new(public_key)
enc_session_key = public_cipher_rsa.encrypt(b"uma informacao confidencial")

print('dado encriptado')
print(enc_session_key)

print()
private_cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = private_cipher_rsa.decrypt(enc_session_key)

print('dado decriptado')
print(session_key)