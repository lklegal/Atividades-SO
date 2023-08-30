import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
while (True):    
    message = input("Digite d para data, h para hora ou dh paa data e hora: ")
    #Enviando mensagem ao servidor
    sock.sendall(message.encode('utf-8'))
    data = sock.recv(2048)
    mensagem = data.decode()
    if mensagem!='0':
        #Imprimindo a mensagem recebida
        print(data.decode())
    else:
        sock.close()
        break
