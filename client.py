import socket

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# TODO: Receive it on args
HOST = '127.0.01'
PORT = 5432

#Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Receive encoded public key
encoded_public_key = s.recv(1480)

#Import public key
public_key = RSA.import_key(encoded_public_key)
public_cipher_rsa = PKCS1_OAEP.new(public_key)

#Encrypt info with public key
enc_session_key = public_cipher_rsa.encrypt(b"uma informacao confidencial")

#Send encrypted data to Server
s.send(enc_session_key)