from selenium import webdriver
from bs4 import BeautifulSoup
import json


driver = webdriver.Chrome()


driver.get("https://www.finnair.com/fi-fi/kohteet/eurooppa/suomi")


driver.implicitly_wait(10)


soup = BeautifulSoup(driver.page_source, "html.parser")


kohteet = soup.find_all('h3', class_="font-heading-5 nordic-blue-900-text mr-clear-y")
hinnat = soup.find_all('span', class_="nordic-blue-900-text font-heading-2 ng-star-inserted")
linkit = soup.find_all('a', class_="no-decoration ng-star-inserted")


print("Kohteiden määrä:", len(kohteet))
print("Hintojen määrä:", len(hinnat))
print("Linkkien määrä:", len(linkit))


helsinki_indeksi = -1
for i in range(len(kohteet)):
    if kohteet[i].text.strip() == "Helsinki":
        helsinki_indeksi = i
        break

if helsinki_indeksi != -1:
    del kohteet[helsinki_indeksi]
    del linkit[helsinki_indeksi]


assert len(kohteet) == len(linkit)

tiedot = {}

with open('public/data/kotimaanmatkat.json', 'w') as f:
    f.write('[\n')

for i in range(len(kohteet)):
    kaupunki = kohteet[i].text.strip()
    hinta = hinnat[i].text.strip()
    linkki = "https://www.finnair.com" + linkit[i]['href']
    

    tiedot = {
        'kaupunki': kaupunki,
        'hinta': hinta,
        'linkki': linkki
    }

    with open('public/data/kotimaanmatkat.json', 'a') as f:
        json.dump(tiedot, f, indent=4)
        
        if i < len(kohteet) - 1:
            f.write(',\n')
            
with open('public/data/kotimaanmatkat.json', 'a') as f:
    f.write('\n]')

driver.quit()


print(json.dumps(tiedot, indent=4))


