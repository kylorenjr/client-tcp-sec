#fazendo um ports scan em python
import socket
import sys

portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]  #portas comuns que serão verificadas

for porta in portas:
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(1)  #define um timeout de 1 segundo para evitar longas esperas
   
    code  = meusocket.connect_ex((sys.argv[1], porta))

    if code == 0:
        print("Porta {} aberta".format(porta)) 

#implementar o banner grabbing
''' 
















  '''