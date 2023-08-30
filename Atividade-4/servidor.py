import socket
import threading
import datetime

def conexao_cliente(client,address):
    
    while (True):    
        data = client.recv(2048)
        '''
        PROTOCOLO
        '''
        mensagem = data.decode()
        if (mensagem!='/sair'):
            if mensagem == "d":
                client.sendall(str(datetime.datetime.now().date()).encode())
            elif mensagem == "h":
                client.sendall(str(datetime.datetime.now().time()).encode())
            elif mensagem == "dh":
                client.sendall(str(datetime.datetime.now()).encode())
            else:
                client.sendall("Requisição inválida.".encode())
        else:
            client.sendall('0'.encode())
            break
    #Fechando o socket
    client.close()

sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada
sock.listen(1)

#Iniciando protocolo

while True:
    client, address = sock.accept()
    conexao = threading.Thread(target=conexao_cliente,args=(client,address,))
    conexao.start()