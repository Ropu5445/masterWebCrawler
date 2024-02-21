#!!!Sinun saatttaa pitää tehdä .json tiedosto nimellä AnssinAsunnotOikotie.json

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

BaseUrl = "https://asunnot.oikotie.fi/myytavat-asunnot?pagination=1&locations="
Place = ["%5B%5B64,6,%22Helsinki%22%5D%5D","%5B%5B359,6,%22Sipoo%22%5D%5D","%5B%5B359,6,%22Hollola%22%5D%5D","%5B%5B359,6,%22Salo%22%5D%5D"]
AddSearch = "&size%5Bmin%5D=200&buildingType%5B%5D=4&buildingType%5B%5D=8&buildingType%5B%5D=32&buildingType%5B%5D=128&cardType=100&price%5Bmin%5D=2000000"
weDone = 1
y = 0
Cost = []
Name = []
Year = []
Space = []
Links = []
JsonData = []

while True:
    i = 0
    CostI = 0

    url = f"{BaseUrl}{Place[y]}{AddSearch}"
    
    driver = webdriver.Chrome()

    driver.get(url)

    scroll_count = 2

    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.08)

    page_source = driver.page_source


    soup = BeautifulSoup(page_source, "html.parser")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    weDone+=1
    y+=1
    NameSearch = soup.find_all(class_="card-v2-text-container__text card-v2-text-container__text--bold")
    CostSpaceSearch = soup.find_all(class_="card-v2-text-container__title ng-star-inserted")
    hrefHelp = soup.find_all(class_="ot-card-v2")
    

    for result in NameSearch:
        NameTxt = str(NameSearch[i].text)
        print(NameTxt.strip())
        Name.append(NameTxt.strip())
        CostTxt = str(CostSpaceSearch[CostI].text)
        SpaceTxt = str(CostSpaceSearch[CostI-1].text)
        Cost.append(CostTxt)
        Space.append(SpaceTxt)
        href = hrefHelp[i].get("href")
        Links.append(href)
        
        #Oikotieltä ei ollut näkyvissä asunno rakentamisvuotta, joten laitan sen vaan ei tiedossa kaikkiin...
        Year.append("Asunnon rakentamisvuosi ei ole tiedossa")
        
        i+=1
        CostI+=2
    
    if weDone > 4:
        print("Sivut käyty läpi")
        break

k = 0
print("\n______________________________________________")
for item in Name:
    print("Position: " + str(k+1) + "\n" +Name[k]+ "    " + Cost[k]+ "    " + Space[k]+ "    " + Year[k]+ "\n" + Links[k]+
        "\n______________________________________________")
 
    data = {
        "Name": Name[k],
        "Cost": Cost[k],
        "Space": Space[k],
        "Year made" : Year[k],
        "Link": Links[k]
        }
    
    JsonData.append(data)
    
    json_data = json.dumps(JsonData, indent=4, ensure_ascii=False)
    with open('./public/data/anssinAsunnotOikotie.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    k+=1