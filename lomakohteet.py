import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver


data = {}
results = []
kummonmulli = None
currentpage = 1
i = 1
while True:
    driver = webdriver.Chrome()
    url = f"https://www.nettimokki.com/vuokramokit/?attr__electric_sauna=1&attr__wood_sauna=1&attr__internet=1&attr__fireplace_decoration=1&attr__ac_unit=1&page={currentpage}"
    driver.get(url)
    time.sleep(1)

    pagesource = driver.page_source
    soup = BeautifulSoup(pagesource, "html.parser")
    links = soup.find_all(class_="content-wrapper")
    cottages = soup.find_all(class_="card-list-title")
    prices = soup.find_all(class_="card-list-price")


    for value, cottage in enumerate(cottages):
        cottageName = cottage.text
        i+=1
        if value < len(prices):

            cottagePrice = prices[value].text.strip()
            cottagePrice = cottagePrice.replace("Alkaen", "")
            cottagePrice = cottagePrice.replace(" ", "")
            cottagePrice = cottagePrice.replace("\n", "")
            cottagePrice = cottagePrice.replace("\xa0", "")
            cottagePrice = cottagePrice.replace("€/vrk", "")
            mokinhinta = float(cottagePrice)
            cottageLinks = links[value] ['href']
            print(f'{i}.{cottageName} {cottagePrice}\n{cottageLinks}')
        else:
            print(f'Error: No price found for {cottageName}\n')
            cottagename = kummonmulli
        data={
        'mökki': cottageName,
        'mökin hinta €/vrk': mokinhinta,
        'linkki mökkiin': cottageLinks}
        if not cottageName.startswith(('Tarkista vuoden 2024 loma-ajat!', 'Tutustu Nettimökin uusiin kohteisiin!', 'Esittelyssä 50 upeaa kohdetta!','Nettimökin käyttöehdot päivittyvät','Katso 40 upeaa uutuuskohdetta valikoimastamme!')):
            results.append(data)
        json_data = json.dumps(results, indent=4, ensure_ascii=False)
        with open('public/data/cottages.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    driver.close()
    currentpage += 1 
    nextpagelink = soup.find('li', class_='pagination-next')
    if not nextpagelink:
        break