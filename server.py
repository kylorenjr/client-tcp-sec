#servidor em python
import socket
import sys

porta = int(sys.argv[1]) #porta passada como argumento, "arg 1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #se deixar em branco tem o mesmo efeito! add ipv4 e tcp
s.bind(("0.0.0.0", porta))
s.listen(1)
print("Aguardando conexão na porta {}".format(porta))

s2, endereco = s.accept()
print("Conectado com {}".format(endereco))

while True:
    msg = s2.recv(1024).decode()
    print(msg)

    msg2 = input() + "\n"
    s2.send(msg2.encode())
