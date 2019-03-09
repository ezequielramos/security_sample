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