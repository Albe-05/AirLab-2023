from time import time, sleep
from ftp import sendFiles
import os

def toSend():
    """sends files to the server and updates 'last_check.txt'
    """    
    sendFiles() #invia i file
        
    #aggiorna il file con l'ultimo invio
    with open('last_check.txt', 'a') as f:
        f.write(f'\n{int(time())}')

def ftpAsync():
    #genera il file in caso sia assente
    with open('last_check.txt', 'a') as f:
        f.close()

    while True:
        with open('last_check.txt', 'r') as f:
            # Move the cursor to the end of the file
            f.seek(0, os.SEEK_END)

            # Find the last line by searching for the last newline character
            pos = f.tell()
            while pos > 0 and f.read(1) != '\n':
                pos -= 1
                f.seek(pos, os.SEEK_SET)

            # legge l'ultima linea del file, se non è presente un tempo in UNIX assume un valore pari a 0
            try:
                last_line = int(f.readline())
            except ValueError:
                last_line = 0

            # verifica se è passato un tempo indicato (tempo attuale - ultimo invio) > del tempo in secondi che devo aspettare --> se si, sono passati più di x secondi
            if (int(time()) - last_line) > 3600*4: #sono passate più di 4 ore
                toSend()
                print('invio i file')
                
            else:
                print('non invio i file')
        
        sleep(3600/2) #prossimo ciclo di controllo tra 30min
    
if __name__ == "__main__":
    ftpAsync()