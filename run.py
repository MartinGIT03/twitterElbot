#!/usr/bin/python

import twitterBot
import formating
import getFiles

import wget
import json

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from config import * # imports variables from config.py, this file needs to be configured

now = datetime.now()

WEBBPAGE = "https://www.elprisetjustnu.se/api/v1/prices/"
ZONES = ["SE1", "SE2", "SE3", "SE4"]

day = now.strftime("%d")
month = now.strftime("%m")
hour = now.strftime("%H")
year = now.strftime("%Y")

# path = f"{path}" # gets first path from config file

# At startup the code will first run the functions atRestart() and main().
# The code continues to run due to the scheduler 

# getFiles.downloadAndRemove(day, month, year, path) # runs once at startup

def main():
    day = now.strftime("%d")
    month = now.strftime("%m")
    hour = now.strftime("%H")
    year = now.strftime("%Y")

    if hour == "00":
        getFiles.downloadAndRemove(day, month, year, path) # Removes and downloads new and old .json files

    dataList = formating.readContent(day, month, hour, path)

    message  = "\n" + "\N{High Voltage Sign}" + "Data hämtad från elprisetjustnu.se" + "\N{High Voltage Sign}" 
    message += "\n" + "kr/kwh" 
    for i in range(0, len(dataList)):
       message += "\n" + ZONES[i] + ": " +str(dataList[i])

    message  += "\n" + "\N{High Voltage Sign}" + "Data hämtad från elprisetjustnu.se" + "\N{High Voltage Sign}" 
    print(message)
    # runBot = twitterBot.bot(message)

def atRestart(day, month, hour, path):
        getFiles.downloadAndRemove(day, month, year, path) # Removes and downloads new and old .json files

atRestart(day, month, hour, path)
main()

#scheduler = BlockingScheduler()
#scheduler.add_job(main, 'interval', hours=1)
#scheduler.start()

