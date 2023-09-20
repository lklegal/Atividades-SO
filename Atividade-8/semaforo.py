import threading
import time
import random

semaforo = threading.Semaphore(3)

def caixa():
    semaforo.acquire()
    print(threading.currentThread().getName())
    time.sleep(random.randint(3,10))
    semaforo.release()

if __name__=="__main__":
    threads = []
    for i in range(30):
        threads.append(threading.Thread(target=caixa))
        threads[i].start()

    for i in range(30):
        threads[i].join()