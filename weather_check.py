from weather_forecast import getWeather
from time import sleep as sl

def weatherService():
    print('Starting weather forecast service...')
    filename = 'weather_data.json' #lo script json_to_csv.py è fatto apposta per convertire il json in csv per essere letto da excel

    while True:
        weather = getWeather()

        #salva i dati
        with open(filename, 'a') as f: # DA INSERIRE PERCORSO
            print(str(f.write(str(weather).replace('\'','\"') + '\n')) + ' caratteri') #stampa la lunghezza della stringa che ha scritto per verificare se ci sono stati eventuali problemi
            f.close()
            
        sl(60*60) #aspetta 1h
        print('Nuovo ciclo')
    
if __name__ == "__main__":
    weatherService()