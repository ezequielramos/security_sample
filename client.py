import socket
import hashlib
import sys

from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

if len(sys.argv) < 5:
    print('You need to specify all parameter. Ex.:\n\n python client.py 127.0.0.1 5432 abc123 1')
    exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
TOKEN = sys.argv[3]
DATA_ID = sys.argv[4]

#Generate a symmetric key
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)

s = None
public_cipher_rsa = None

def send_secret_info(data):
    global s, public_cipher_rsa

    #Encrypt info with public key
    secret_info = bytes(data, 'UTF8')
    hash_secret_info = bytes(hashlib.sha256(secret_info).hexdigest(), 'UTF8')

    enc_hash_info = public_cipher_rsa.encrypt(hash_secret_info)
    enc_info = public_cipher_rsa.encrypt(secret_info)

    #Send encrypted data to Server
    s.send(enc_hash_info)
    s.recv(2)
    s.send(enc_info)
    s.recv(2)

def receive_secret_info():
    global s, cipher_suite

    #Receive encrypted info from client
    enc_hash_info = s.recv(1480)
    s.send(b'ok')
    enc_info = s.recv(1480)
    s.send(b'ok')

    print('dado encriptado')
    print('hash: %s' % enc_hash_info)
    print('info: %s' % enc_info)

    #Decrypt info using private key
    hash_info = cipher_suite.decrypt(enc_hash_info)
    info = cipher_suite.decrypt(enc_info)

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

def server_communication():
    global s, public_cipher_rsa

    #Connect to Server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    #Receive encoded public key
    encoded_public_key = s.recv(1480)

    #Import public key
    public_key = RSA.import_key(encoded_public_key)
    public_cipher_rsa = PKCS1_OAEP.new(public_key)


    send_secret_info(symmetric_key.decode())
    send_secret_info(TOKEN)
    token_res = receive_secret_info()

    if token_res == 'nok':
        print('Token inválido.')
        return

    send_secret_info(DATA_ID)

    secret_info = receive_secret_info()

    print(secret_info)

try:
    server_communication()
except ConnectionResetError:
    print('Perdeu conexão com servidor.')
except ConnectionRefusedError:
    print('Servidor não existe.')