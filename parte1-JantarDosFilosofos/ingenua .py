import threading
import time 
import random

class Filosofo:
    def __init__(self, id):
        self.id = id
        self.estado = "pensando" 
        self.esquerda = id
        self.direita = (id + 1) % 5
        self.garfos_na_mao = 0    

    def pensar(self):
        self.estado = "pensando"
        print(f"Filósofo {self.id} está pensando.")
        time.sleep(random.uniform(0.1, 0.2))

    def com_fome(self):
        self.estado = "com fome"
        print(f"Filósofo {self.id} está com fome.")

    def comer(self):
        self.estado =  "comendo"
        print(f"Filósofo {self.id} está comendo.")
        time.sleep(random.uniform(0.5, 2))

    def pegarGarrfoE(self, garfo):
        garfo[self.esquerda].ocupado.acquire()
        self.garfos_na_mao = 1      
        print(f"Filósofo {self.id} pegou o garfo {self.esquerda}.")    

    def pegarGarrfoD(self, garfo):
        garfo[self.direita].ocupado.acquire()
        self.garfos_na_mao = 2     
        print(f"Filósofo {self.id} pegou o garfo {self.direita}.")     

    def largarGarrfoE(self, garfo):
        garfo[self.esquerda].ocupado.release()  

    def largarGarrfoD(self, garfo):
        garfo[self.direita].ocupado.release()
        self.garfos_na_mao = 0     
# ------------------------------------------------------------

class Garfo:
    def __init__(self, id):
        self.id = id
        self.ocupado = threading.Lock()
# ------------------------------------------------------------

def runFilosofo(filosofo, mesa):
    while True:
        filosofo.pensar()
        filosofo.com_fome()
        filosofo.pegarGarrfoE(mesa)
        time.sleep(2)
        filosofo.pegarGarrfoD(mesa)
        filosofo.comer()
        filosofo.largarGarrfoE(mesa)
        filosofo.largarGarrfoD(mesa)
# ------------------------------------------------------------

N = 5
filosofos = [];
mesa = [];
threads = [];

for i in range(N):
    filosofos.append(Filosofo(i))
    mesa.append(Garfo(i))
# ------------------------------------------------------------

for i in range(N):
    t = threading.Thread(target=runFilosofo, args=(filosofos[i], mesa), daemon=True)
    threads.append(t)

for t in threads:
    t.start()

while True:
    time.sleep(3)
    travados = 0
    for f in filosofos:
        if f.estado == "com fome" and f.garfos_na_mao == 1:
            travados = travados + 1
    if travados == N:
        print()
        print("IMPASSE (DEADLOCK): todos com fome, cada um com um garfo na mão.")
        for f in filosofos:
            print(f"Filósofo {f.id} segura o garfo {f.esquerda} e espera o garfo {f.direita}.")
        break
# ------------------------------------------------------------ 