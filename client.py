import socket
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# TODO: Receive it on args
HOST = '127.0.01'
PORT = 5432
TOKEN = 'abc123'

#Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Receive encoded public key
encoded_public_key = s.recv(1480)

#Import public key
public_key = RSA.import_key(encoded_public_key)
public_cipher_rsa = PKCS1_OAEP.new(public_key)

#Encrypt info with public key
secret_info = bytes(TOKEN, 'UTF8')
hash_secret_info = bytes(hashlib.sha256(secret_info).hexdigest(), 'UTF8')

enc_hash_info = public_cipher_rsa.encrypt(hash_secret_info)
enc_info = public_cipher_rsa.encrypt(secret_info)

#Send encrypted data to Server
s.send(enc_hash_info)
s.send(enc_info)