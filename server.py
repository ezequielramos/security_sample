import socket
import hashlib

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

from tokens import valid_tokens

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
enc_hash_info = conn.recv(1480)
enc_info = conn.recv(1480)

print('dado encriptado')
print('hash: %s' % enc_hash_info)
print('info: %s' % enc_info)

#Decrypt info using private key
hash_info = private_cipher_rsa.decrypt(enc_hash_info)
info = private_cipher_rsa.decrypt(enc_info)

print('dado decriptado')
print('hash: %s' % hash_info)
print('info: %s' % info)

hash_secret_info = bytes(hashlib.sha256(info).hexdigest(), 'UTF8')

print('Hashs combinam. O dado esta integro.' if hash_info == hash_secret_info else 'Os hashs não combinam. O dado esta comprometido quanto integridade.')

#bytes to str
info = info.decode()

if info not in valid_tokens:
    print('Token não é valido')
    exit()

print('Realizando comunicação com %s.' % valid_tokens[info])