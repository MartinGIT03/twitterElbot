from datetime import date
import json

today = date.today()

ZONES = ['SE1', 'SE2', 'SE3', 'SE4']

def elZone(date, hour):
    with open(date) as file:
        data = json.load(file)
    return round(data[int(hour)]["SEK_per_kWh"], 2) # Here you can change the formating
    
def readContent(day, month, hour, path):
    data = []
    for zone in ZONES:
        date = path + "/" + month + "-" + day + "_" + zone + ".json"
        data.append(elZone(date, hour))
    
    print(hour, "timme")
    print(data, "data")
    return data


#download()
#readContent()
