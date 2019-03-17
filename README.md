# security_sample

## TRABALHO PRÁTICO 1

- Através de sockets (Python 2.7), implementar uma comunicação cliente-servidor entre 2 nós. Considerar:
  - Soluções para Autenticação
    - Autenticação(usuário, senha, verificação por HASH,umavia,duasvias, token,etc?)
  - Soluções para Confidencialidade
    - Criptografia Simétrica ou Assimétrica(Diffie-Helmann, GPG, RSA,etc?)
  - Soluções para Integridade(das mensagens trocadas)
    - Toda comunicação confirmada por HASH (SHA-256 bits, por exemplo) entre cliente e servidor
  - Soluções para Controle de Acesso 
    - Não é necessário implementar Tolerância a Falhas
  - Toda comunicação entre cliente e servidor (sockets) é síncrona
    - timeouts devem ser tratados no cliente

- Funcionalidades do “software”:
  - O nó cliente, que interage com um usuário, envia desafios (inteiros, strings?) para o servidor. O servidor, por sua vez, deve ser capaz de respondê-los corretamente. 
  - O cliente decide quando deve encerrar a comunicação com o servidor
  - A solução deve ser implementada na linguagem Python 2.7 (ou 3.x)
  - Apresentar as soluções de segurança implementadas (para a sala -não necessita PPT)
  - Apresentar a execução (e o código) ao professor 
  - Enviar o código python via Moodle na data acordada

- Detalhes:

  - Disponível no Moodle: 2 slides sobre sockets TCP no Python 2.7
  - Implementar sobre máquinas virtuais
  - 11/03 – Espaço para desenvolvimento
  - 14/03 – Espaço para desenvolvimento
  - 18/03 – Apresentação

## How to build it:

Construido para versão Python3.5.2+. É recomendado que se utilize uma "virtualenv" para construir o projeto. Para verificar se ele já está instalado execute o seguinte comando:

```
$ python3 -m virtualenv --version`
```

Caso não funcione, instale o virtualenv na máquina:

```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
```

Então execute o seguinte para criar a virtualenv:

```
$ python3 -m virtualenv pyenv3
```

Para ativar o ambiente virtual execute:

```
$ source pyenv3/bin/activate
```

Com o ambiente virtual ativo, execute o seguinte comando para instalar todas as depêndencias:

```
(pyenv3) $ python -m pip install -r requirements.txt
```

## How to run it:

Certifique-se que o ambiente virtual esta ativo executando:

```
$ source pyenv3/bin/activate
```

### How to run client:

```
$ python client.py <server_ip> <server_port> <client_token> <data_id>
```

### How to run server:

```
$ python server.py <server_ip> <server_port>
```