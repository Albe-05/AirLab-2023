import json
import csv
from dots_to_commas import dotToCommas

filename = 'C:\\Users\\zarpe\\Downloads\\weather_data.json'

def delErrors():
    with open(filename, 'r') as f: # open file
        lines = f.readlines()
    with open(filename, 'w') as f: # rewrites file
        for line in lines:
            f.write(line) if 'Error' not in line else ''
    print(f"fatto: {filename}")

def converter():
    header = ['query_time', 'clouds_perc', 'time', 'humidity', 'pressure', 'temp', 'temp_max', 'temp_min', 'visibility', 'weather_descr', 'wind_deg', 'wind_gust', 'wind_speed']
    rows = []
    
    with open('C:\\Users\\zarpe\\Downloads\\weather_data.json', 'r') as file:
        jsons = file.readlines()
        #esempio di stringa di dato del tempo jsons = ['''{"query_time": 1678404430, "clouds_perc": 100, "time": 1678404430, "main": {"humidity": 83, "pressure": 1005, "temp": 10.28, "temp_max": 12.15, "temp_min": 8.09}, "visibility": 10000, "weather_descr": "overcast clouds", "wind": {"deg": 18, "gust": 1.33, "speed": 1.24}}''' ]
        
        for json_file in jsons:
            newRow = []
            line = json.loads(json_file)
            
            for value in line.values():
                
                if type(value) == int or type(value) == str:
                    newRow.append(value)
                    
                elif type(value) == dict:
                    for subValue in value.values():
                        newRow.append(subValue)

            print(newRow)
            rows.append(newRow)

    with open('C:\\Users\\zarpe\\Downloads\\weather_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter = "\t")
        writer.writerow(header)
        writer.writerows(rows)

delErrors()
converter()
dotToCommas(filename)