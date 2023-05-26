import json
import wget
import os
import subprocess

from os.path import exists

from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(1)

from config import * # imports variables from config.py, this file needs to be configured

DELTADAY = datetime.strftime(yesterday, '%d') 
DELTAMONTH = datetime.strftime(yesterday, '%m')
DELTAYEAR = datetime.strftime(yesterday, '%Y')

ZONES = ["SE1", "SE2", "SE3", "SE4"]

#now = datetime.now()

#year = now.strftime("%Y");


def downloadAndRemove(day, month, year, path):
    for zone in ZONES:
        # Downloads .json files
        url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{zone}.json"
        print(url)
        fileName = f"{month}-{day}_{zone}.json"
        checkIfExists = f"{path}/{fileName}"
        if exists(checkIfExists) == False:
            wget.download(url, path)

        #subprocess.run(["wget", "-r", "-nc", "-P", path, url])

        

        #data = wget.download(url)
        
        # Removes old files
        #dayBeforeNow = f"https://www.elprisetjustnu.se/api/v1/prices/{DELTAYEAR}/{DELTAMONTH}-{DELTADAY}_{zone}.json"
        yesterday = f"{path}/{DELTAMONTH}-{DELTADAY}_{zone}.json"
        try:
            os.remove(yesterday)
        except:
            pass


