import threading
from send_file_async import ftpAsync
from weather_check import weatherService

# Creiamo un thread per ogni programma
t1 = threading.Thread(target=ftpAsync)
t2 = threading.Thread(target=weatherService)
#t3 = threading.Thread(target=AirLab) #programma di acquisizione dei dati di AirLab

# Avviamo i due thread
t1.start()
t2.start()
#t3.start()

# Aspettiamo che i thread terminino l'esecuzione
t1.join()
t2.join()
#t3.join()