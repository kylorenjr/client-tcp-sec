#client de tcp/ip com python
import socket
import sys

host = sys.argv[1]
porta = int(sys.argv[2])

s = socket.socket()
s.connect((host, porta))
print("conectado com server {} na porta {}".format(host, porta))

while True:
    msg = input() + "\n"
    s.send(msg.encode())

    resposta = s.recv(1024).decode()
    print(resposta)
    if not resposta:
        print("Conexão encerrada pelo servidor.")
        break