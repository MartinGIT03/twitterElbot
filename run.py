import scraper
import twitterBot
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import os 
import time 

def run():
    try:
        time.sleep(20)
        scraper.main()
        time.sleep(2)
        message = "\N{High Voltage Sign}" + "Svenska elpriser just nu!" + "\N{High Voltage Sign}" + "\n" + "öre/kwh"
        if os.path.getsize("electricityPrices.json")  > 0:
            with open("electricityPrices.json", "r") as file:
                data = json.load(file)
                listOfPrices = []
                listOfNames = []
                for index in range(11, 15):
                    listOfNames.append(data[index]["Region"]) 
                    listOfPrices.append(str(round(data[index]["Price"]*1.090, 1))) 
                for index in range(0, 4):
                    message += "\n" + listOfNames[index]+ ": " + listOfPrices[index]
                message += "\n" + "\N{High Voltage Sign}" + "Data hämtad från Svenska kraftnät" + "\N{High Voltage Sign}" 
                print(message)

                twitterBot.bot(message)
        else: # ifall ingen data hämtas
            run() 
    except Exception as error: 
        with open("error.txt", "w") as file:
            file.write(str(error))
run()

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', hours=1)
scheduler.start()
