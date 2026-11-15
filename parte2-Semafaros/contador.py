import threading
import time

t = 8
m = 200000

contador = 0
semaforo = threading.Semaphore(1)


# sem semaforo
def incrementar():
    global contador

    for i in range(m):
        contador += 1


# com semaforo
def incrementarSemaforo():
   global contador

   for i in range(m):
       semaforo.acquire()

       try:
           contador += 1
       finally:
           semaforo.release()


threads = []

inicio = time.perf_counter()

for i in range(t):

    # thread = threading.Thread(target=incrementar)

    thread = threading.Thread(target=incrementarSemaforo)

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

fim = time.perf_counter()

print("esperado: ", t*m)
print("total:", contador)
print("tempo:", fim - inicio)