import socket
import hashlib

from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

from tokens import valid_tokens
from data import get_data

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

def receive_secret_info():
    global conn
    
    #Receive encrypted info from client
    enc_hash_info = conn.recv(1480)
    conn.send(b'ok')
    enc_info = conn.recv(1480)
    conn.send(b'ok')

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

    print()
    print('Hashs combinam. O dado esta integro.' if hash_info == hash_secret_info else 'Os hashs não combinam. O dado esta comprometido quanto integridade.')
    print()

    #bytes to str
    info = info.decode()
    return info

def send_secret_info(info):
    global conn, cipher_suite

    info = bytes(info, 'UTF8')
    hash_info = bytes(hashlib.sha256(info).hexdigest(), 'UTF8')

    hash_secret_info = cipher_suite.encrypt(hash_info)
    secret_info = cipher_suite.encrypt(info)
    
    conn.send(hash_secret_info)
    conn.recv(2)
    conn.send(secret_info)
    conn.recv(2)


symmetric_key = receive_secret_info()
cipher_suite = Fernet(symmetric_key)

token = receive_secret_info()
if token not in valid_tokens:
    print('Token não é valido')
    exit()

client_id = valid_tokens[token]

print()
print('Realizando comunicação com %s.' % client_id)
print()

data_id = receive_secret_info()
data = get_data(data_id)

if data == None:
    print('Esse dado não existe.')
    exit()

if client_id not in data['owner']:
    print('Cliente não tem acesso para acessar esta informacao.')
    exit()

send_secret_info(data['text'])