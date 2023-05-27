from datetime import datetime
from config import * # imports variables from config.py, this file needs to be configured
import getFiles

now = datetime.now()

day = now.strftime("%d")
month = now.strftime("%m")
hour = now.strftime("%H")
year = now.strftime("%Y")

def atRestart(day, month, hour, path):
        getFiles.downloadAndRemove(day, month, year, path) # Removes and downloads new and old .json files

atRestart(day, month, hour, path)
print("Downloaded new data")