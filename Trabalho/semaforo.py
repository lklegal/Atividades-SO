import threading
import random
import time

class Fila:
    def __init__(self):
        self.dados = [random.randint(0, 100) for _ in range(10)]
        self.inicio = 0
        self.fim = len(self.dados)-1
        self.ocupados = 10

    def remover(self):
        removido = None
        if self.ocupados > 0:
            removido = self.dados[self.inicio]
            self.dados[self.inicio] = -1
            self.inicio = (self.inicio + 1) % len(self.dados)
            self.ocupados -= 1
        return removido
    
    def adicionar(self, valor):
        if self.ocupados < len(self.dados):
            self.fim = (self.fim + 1) % len(self.dados)
            self.dados[self.fim] = valor
            self.ocupados += 1
            return valor
        return None

    def mostrar(self):
        valores = ""
        i = self.inicio
        while True:
            if(i == self.fim):
                valores += str(self.dados[i])
                break
            elif self.ocupados == 0:
                break
            else:
                valores += str(self.dados[i]) + " "
            i = (i + 1) % len(self.dados)
        return valores
    
lock = threading.Lock()
    
def operacoes(fila:Fila):
    for i in range(100):
        inicio = time.time()
        adicionado = random.randint(0, 100)
        lock.acquire()
        removido = fila.remover()
        adicionado = fila.adicionar(adicionado)
        lock.release()
        elementos = fila.mostrar()
        fim = time.time()
        tempo = fim-inicio
        print(threading.current_thread().name + ": Libera recursos para o processo " + str(removido) + ", poe o processo " + str(adicionado) + " na fila. Fila de processos: " + elementos)
        print("Taxa instantanea de " + str(int(1/tempo)) + " processos liberados por segundo.")

if __name__ == "__main__":
    comando = -1
    fila = Fila()
    t1 = threading.Thread(target=operacoes, name="Thread 1", args=(fila, ))
    t2 = threading.Thread(target=operacoes, name="Thread 2", args=(fila, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
