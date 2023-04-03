import time
import requests

def getWeather():
    """tempo attuale a Bassano Del Grappa

    Returns:
        dictionary: weather = {
            'clouds_perc'
            'dt'
            'time'
            'main': {'humidity'
                    'pressure'
                    'temp'
                    'temp_max'
                    'temp_min'}
            'visibility'
            'weather_descr'
            'wind': {'deg' 
                    'gust' 
                    'speed'}
        }
        or 'Error'
    """    
    #Import the requests library and define the API key and the URL of the API:
    api_key = 'acdfc3a8060f0f5662dcfdcc0024ab89'
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric' #API docs link https://openweathermap.org/api

    id = 3182297 #id di bassano del grappa, basta cercare la città è l'id si trova nel url

    #Use the requests.get() method to send a GET request to the API, with the location and API key as parameters:
    try:
        response = requests.get(url.format(id, api_key))
    except requests.exceptions.ConnectionError:
        return 'Error'

    if response.status_code == 200:
        json = response.json()

        temperature = json['main']['temp']
        description = json['weather'][0]['description']

        print('Temperature:', temperature, '°C')
        print('Description:', description)
        #pprint(response.json())
        
        weather = { #se i dati vogliono essere successivamente letti da excel vanno poi convertiti da json a csv, sarebbe meglio salvare tutto subito in csv
            "clouds_perc": json['clouds']['all'],
            "data_time": json['dt'], #momento della misurazione dei dati da parte dell'api (è in formato UNIX)
            
            "main": {"humidity": json['main']['humidity'],
                    "pressure": json['main']['pressure'],
                    "temp": json['main']['temp'],
                    "temp_max": json['main']['temp_max'],
                    "temp_min": json['main']['temp_min']},
            
            "visibility": json['visibility'],
            "weather_descr": json['weather'][0]['description'],
            
            "wind": {"wind_deg": json['wind']['deg'], 
                    "wind_gust": json['wind']['gust'], 
                    "wind_speed": json['wind']['speed']}
        }
        
        return weather
    else:
        print('Error getting weather data')
        print(response.status_code)
        return 'Error ' + time.time() #ritorna Errore e momento della misurazione