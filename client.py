#client de tcp/ip com python
import socket

host = "localhost"
porta = 8080

s = socket.socket()
s.connect((host, porta))

msg = "mensagem de teste"
s.send(msg.encode())