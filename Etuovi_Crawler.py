#!!!Sinun saatttaa pitää tehdä .json tiedosto nimellä AnssinAsunnotEtuovi.json

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

BaseUrl = "https://www.etuovi.com/myytavat-asunnot/"
Place = ["espoo/westend","kirkkonummi","kauniainen"]
AddSearch = ["?haku=M2076010192","?haku=M2076012376","?haku=M2076012134"]
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

    url = f"{BaseUrl}{Place[y]}{AddSearch[y]}"
    
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
    NameSearch = soup.find_all(class_="MuiTypography-root MuiTypography-body1 e3qdyeq9 erq801z0 mui-style-jit781")
    CostSearch = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4 MuiGrid-grid-md-4 mui-style-j3iqgs")
    SpaceSearch = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-true MuiGrid-grid-md-4 mui-style-66utdc")
    YearMade = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-3 MuiGrid-grid-md-4 mui-style-7nn1vd")
    hrefHelp = soup.find_all(class_="mui-style-1hvv1xy e3qdyeq2")
    

    for result in CostSearch:
        Slicer = slice(5)
        NameTxt = str(NameSearch[i].text)
        Name.append(NameTxt.strip())
        CostTxt = str(CostSearch[i].text)
        CostSliced = CostTxt[Slicer]
        head, sep, tail = CostTxt.partition("€")
        Cost.append(CostSliced + ": " + head[5:] + "€")
        YearMadeTxt = str(YearMade[i].text)
        YearSliced = YearMadeTxt[Slicer]
        if YearMadeTxt[5:].find("-") == 0:
            Year.append("Rakennusvuosi ei ole tiedossa")
        else:
            Year.append(YearSliced + " - " + YearMadeTxt[5:])
        SpaceTxt = str(SpaceSearch[i].text).replace("Koko","")
        Space.append(SpaceTxt)
        href = hrefHelp[i].get("href")
        Links.append("https://www.etuovi.com"+str(href))
        
        i+=1
    
    if weDone > 3:
        print("Sivut käyty läpi")
        break

k = 0
print(  "\n______________________________________________")
for item in Name:
    print("Position: " + str(k+1) + "\n"
        +Name[k]+ "    " + Cost[k]+ "    " + Space[k]+ "    " + Year[k]+"\n"+Links[k]+
          "\n______________________________________________")
 
    data = {
        "Name": Name[k],
        "Cost": Cost[k][6:].strip(),
        "Space": Space[k],
        "Year made" : Year[k],
        "Link": Links[k]
        }

    JsonData.append(data)
    
    json_data = json.dumps(JsonData, indent=4, ensure_ascii=False)
    with open('./public/data/anssinAsunnotEtuovi.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    k+=1