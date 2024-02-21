import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

urlNvidia = "https://www.verkkokauppa.com/fi/search?query=nvidia+rtx+40&list=0&filter=category%3Agraphics_processors&filter=AvailableImmediatelyAllChannels%3Aimmediately_shippable&filter=pim_graphics_processor%3AGeForce+RTX+4080+16GB&filter=pim_graphics_processor%3AGeForce+RTX+4090&filter=pim_graphics_processor%3AGeForce+RTX+4070+Ti+SUPER&filter=pim_graphics_processor%3AGeForce+RTX+4070+Ti&filter=pim_graphics_processor%3AGeForce+RTX+4070+SUPER&filter=pim_graphics_processor%3AGeForce+RTX+4070"
urlRadeon = "https://www.verkkokauppa.com/fi/search?query=radeon+7900&list=0&filter=category%3Agraphics_processors&filter=AvailableImmediatelyAllChannels%3Aimmediately_shippable&filter=pim_graphics_processor%3ARadeon+RX+7900+XT&filter=pim_graphics_processor%3ARadeon+RX+7900+XTX"
addLink = "https://www.verkkokauppa.com"
result = []
options = Options()
options.add_argument("-headless")
def Haku(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    index = 0
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    drivers = soup.find_all(class_="sc-eqUAAy fUzhuB sc-67f7iw-0 lkeYKD sc-qccots-0 gpgYKe")
    prices = soup.find_all(class_="CurrentData-sc-1eckydb-0 eZOgvz")
    
    for x in drivers:
        title = x.text
        price = prices[index]
        link = x['href']
        driverData = {
            "index": index + 1,
            "title": title,
            "price": price.text.strip().replace('€', ''),
            "link": addLink + link
        }
        result.append(driverData)
        index += 1
    driver.close()
    with open('verkkokauppa.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=2, ensure_ascii=False)

def Start():
    while True:
        maker = input("Valitse 1. Nvidia tai 2. Radeon: ")
        if maker == "1":
            Haku(urlNvidia)
            break
        elif maker == "2":
            Haku(urlRadeon)
            break
        else:
            Start()
            
Start()