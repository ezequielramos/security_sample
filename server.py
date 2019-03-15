import socket

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

# TODO: Receive it on args
HOST = '127.0.01'
PORT = 5432

#Generate RSA Keys
random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
private_cipher_rsa = PKCS1_OAEP.new(private_key)
public_key = private_key.publickey()

#Connect to Client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, _ = s.accept()

#Send encoded public key to client
conn.send(public_key.exportKey())

#Receive encrypted info from client
enc_session_key = conn.recv(1480)

print('dado encriptado')
print(enc_session_key)
print()

#Decrypt info using private key
session_key = private_cipher_rsa.decrypt(enc_session_key)

print('dado decriptado')
print(session_key)