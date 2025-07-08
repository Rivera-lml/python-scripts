import threading 

# shared variable
saldo = 0
lock = threading.Lock()  # create a lock

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # block the access to avoid race conditions
            saldo += dinero
    
hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}") # expected balance: 