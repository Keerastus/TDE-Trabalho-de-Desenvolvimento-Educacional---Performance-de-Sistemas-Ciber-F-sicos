import threading
import time
import faulthandler

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def parte3thread1():
    print("Thread 1: Tentando adquirir A", flush=True)
    LOCK_A.acquire()
    print("Thread 1: A adquirido, tentando adquirir B", flush=True)
    time.sleep(0.5)
    LOCK_B.acquire()
    print("Thread 1: B adquirido", flush=True)
    LOCK_B.release()
    LOCK_A.release()

def parte3thread2():
    print("Thread 2: Tentando adquirir A", flush=True)
    LOCK_A.acquire()
    print("Thread 2: A adquirido, tentando adquirir B", flush=True)
    time.sleep(0.5)
    LOCK_B.acquire()
    print("Thread 2: B adquirido", flush=True)
    LOCK_B.release()
    LOCK_A.release()

if __name__ == "__main__":
    faulthandler.dump_traceback_later(3, exit=True)
    t1 = threading.Thread(target=parte3thread1, name="T1")
    t2 = threading.Thread(target=parte3thread2, name="T2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("fim", flush=True)