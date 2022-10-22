from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json


def main():
    
    url = 'https://www.svk.se/om-kraftsystemet/kontrollrummet/'
    
    display = Display(visible=0, size=(800, 600))
    display.start()

    s=Service('/usr/lib/chromium-browser/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(5)

    browser.get(url)
   
    kakKnapp = browser.find_element("xpath", '/html/body/div[1]/div/section/button[2]')
    kakKnapp.click()

    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div/div[2]/div/div/div/div/figure/div/div/div[1]/div[2]/div/div[1]/button[3]')))
    button.location_once_scrolled_into_view
    button.click()
    
    element = browser.find_element("xpath", '//*[@id="Agsid-6"]/table/tbody')
    priceList = []
    i = 0
    REGION = ""
    PRICE = 0

    rows = element.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        element = row.find_elements(By.TAG_NAME, 'td')
        for data in element:
            data = data.get_attribute("innerHTML")
            print(data)
            if i % 2 == 0: # even
                REGION = data
            else: # odd
                PRICE = data.replace(',', '.')
                PRICE = float(PRICE)
                tempList = {"Region": REGION, "Price": PRICE}
                priceList.append(tempList)

            i = i + 1
            
    print(priceList)
    with open("electricityPrices.json", "w") as file:
        json.dump(priceList, file, indent=6)

    browser.close()
