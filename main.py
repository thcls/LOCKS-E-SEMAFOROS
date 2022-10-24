import threading
from random import randint
import time

semaforo = threading.Semaphore(3)


def atendercliente(i):
    semaforo.acquire()
    tempo = randint(3,10)
    time.sleep(tempo)
    semaforo.release()
    print("Nº {} terminou".format(i))
list = []
for i in range(0,30):
    list.append(threading.Thread(target=atendercliente, args=(i,)))
    list[i].start()

for i in list:
    i.join()
