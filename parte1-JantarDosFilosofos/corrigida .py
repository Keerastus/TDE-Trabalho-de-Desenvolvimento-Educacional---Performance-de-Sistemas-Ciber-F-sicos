import threading
import time
import random

class Filosofo:
    def __init__(self, id):
        self.id = id
        self.estado = 0
        self.esquerda = id
        self.direita = (id + 1) % 5
        self.primeiro = min(self.esquerda, self.direita)
        self.segundo = max(self.esquerda, self.direita)
        self.refeicoes = 0        
        self.continuar = True    

    def pensar(self):
        self.estado = 0
        print(f"Filósofo {self.id} está pensando.")
        time.sleep(random.uniform(0.1, 0.2))

    def com_fome(self):
        self.estado = 1
        print(f"Filósofo {self.id} está com fome.")

    def comer(self):
        self.estado = 2
        print(f"Filósofo {self.id} está comendo.")
        time.sleep(random.uniform(0.5, 2))
        self.refeicoes = self.refeicoes + 1    

    def pegarPrimeiro(self, garfo):
        garfo[self.primeiro].ocupado.acquire()

    def pegarSegundo(self, garfo):
        garfo[self.segundo].ocupado.acquire()

    def largarPrimeiro(self, garfo):
        garfo[self.primeiro].ocupado.release()

    def largarSegundo(self, garfo):
        garfo[self.segundo].ocupado.release()
# ------------------------------------------------------------

class Garfo:
    def __init__(self, id):
        self.id = id
        self.ocupado = threading.Lock()
# ------------------------------------------------------------

def runFilosofo(filosofo, mesa):
    while filosofo.continuar:      
        filosofo.pensar()
        filosofo.com_fome()
        filosofo.pegarPrimeiro(mesa)
        time.sleep(2)
        filosofo.pegarSegundo(mesa)
        filosofo.comer()
        filosofo.largarPrimeiro(mesa)
        filosofo.largarSegundo(mesa)
# ------------------------------------------------------------

filosofos = []
mesa = []
threads = []

for i in range(5):
    filosofos.append(Filosofo(i))
    mesa.append(Garfo(i))
# ------------------------------------------------------------

for i in range(5):
    t = threading.Thread(target=runFilosofo, args=(filosofos[i], mesa))
    threads.append(t)

for t in threads:
    t.start()
time.sleep(30)

for f in filosofos:
    f.continuar = False

for t in threads:
    t.join()

print()
print("Fim do jantar, sem impasse.")
for f in filosofos:
    print(f"Filósofo {f.id} comeu {f.refeicoes} vezes.")
# ------------------------------------------------------------