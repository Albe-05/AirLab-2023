# AirLab 2023
 Questa repository contiene alcuni script in python per semplificare e migliorare l'utilizzo della centralina fornita dall'università di Padova in collaborazione con l'**INFN**.
 
 ## Descrizione singoli programmi
- [START_UP.py](https://github.com/Albe-05/AirLab-2023/blob/main/START_UP.py) programma parent per i vari sub-processi di acquisizione dati, crea un thread per ogni programma
- [dots_to_commas.py](https://github.com/Albe-05/AirLab-2023/blob/main/dots_to_commas.py) converte le misurazioni nei file TSV ogni ```.``` in ```,``` perché excel altrimenti non lo riconosce come separatore per il decimale
- [weather_check.py](https://github.com/Albe-05/AirLab-2023/blob/main/weather_check.py) sfruttando le API di [OpenWeather](https://openweathermap.org/api) acquisisce e salva in formato JSON alcuni dati relativi al meteo (ad intervalli di 1h, comunque facilmente modificabili)
- [json_to_csv.py](https://github.com/Albe-05/AirLab-2023/blob/main/json_to_csv.py) converte il file JSON con i dati metereologici in file TSV
- [send_file_async.py](https://github.com/Albe-05/AirLab-2023/blob/main/send_file_async.py) definito un certo intervallo di tempo, se la centralina è connessa ad internet il programma invia automaticamente tutte le nuove misurazioni ad un server FTP, continua automaticamente
- [tot_lines.py](https://github.com/Albe-05/AirLab-2023/blob/main/tot_lines.py) script curioso per ottenere il numero totale di righe di tutti i file, conteggiando quindi il numero di misurazioni effettuate
- gli altri script sono semplicemente driver e moduli
