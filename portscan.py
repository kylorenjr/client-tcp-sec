#fazendo um ports scan em python
import socket
import sys

portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]  #portas comuns que serão verificadas
host = sys.argv[1]  #host passado como argumento, "arg 1"

for porta in portas:
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(1)  #define um timeout de 1 segundo para evitar longas esperas
   
    code  = meusocket.connect_ex((sys.argv[1], porta))

    if code == 0:
        meusocket.connect((host, porta))

        try:
            banner = meusocket.recv(1024).decode().replace("\n", "")
        except:
            banner = "Nenhum banner identificado"

        print(porta, banner)

        meusocket.close()


#implementar o banner grabbing
''' 
















  '''