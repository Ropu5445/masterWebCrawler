from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


baselink = "https://www.jimms.fi"
current_page = 1
i = 1

data = {}
result = []

while True:
    noMoreDrivers = False
    url = f"https://www.jimms.fi/fi/Product/List/000-00P/komponentit--naytonohjaimet?p={current_page}&ob=5&fg=000-213&fg=000-21D&fg=000-22X&fg=000-23W&fg=000-254&fg=000-258&fg=000-25T&fg=000-25U&fg=000-25V"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    current_page += 1
    soup = BeautifulSoup(page_source, "html.parser")
    drivers = soup.find_all(class_="product-box-name")
    prices = soup.find_all(class_ = "price__amount")
    links = soup.find_all(class_="w-100 d-grid mt-2")
    isAvailable = soup.find_all(class_="availability-text d-flex align-items-center")
    value = 0
    for graphdriver in drivers:
        driverName = graphdriver.text.strip()
        driverLink = baselink+links[value].find('a')['href']
        driverPrice = prices[value].text.strip()
        availability = isAvailable[value]
        availability = availability.text.strip().replace('fiber_manual_record','')
        if availability in ['\nVarastossa', '\nVarastossa 4 kpl', '\nVarastossa 3 kpl', '\nVarastossa 2 kpl', '\nVarastossa 1 kpl']:
            print(f"{i}. {driverName}\n{driverPrice}\n{driverLink}\n{availability}\n")
        else:
            noMoreDrivers = True
            driver.close()
            break

        data = {
                "id": i,
                "make": 'Nvidia',
                "name": driverName,
                "link": driverLink,
                "price": driverPrice,
            }
        result.append(data)
        i += 1
        value += 1
    json_data = json.dumps(result, indent=4, ensure_ascii=False)
    print("Json successful")
    with open('jimms.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    next_pagelink = soup.find('a', class_='product-list__pagination')
    if noMoreDrivers == True:
        break
current_page = 1
while True:
    noMoreDrivers = False
    url = f"https://www.jimms.fi/fi/Product/List/000-00P/komponentit--naytonohjaimet?p={current_page}&ob=5&fg=000-0LP"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    current_page += 1
    soup = BeautifulSoup(page_source, "html.parser")
    drivers = soup.find_all(class_="product-box-name")
    prices = soup.find_all(class_ = "price__amount")
    links = soup.find_all(class_="w-100 d-grid mt-2")
    isAvailable = soup.find_all(class_="availability-text d-flex align-items-center")
    value = 0
    for graphdriver in drivers:
        driverName = graphdriver.text.strip()
        driverLink = baselink+links[value].find('a')['href']
        driverPrice = prices[value].text.strip()
        availability = isAvailable[value]
        availability = availability.text.strip().replace('fiber_manual_record','')
        if availability in ['\nVarastossa', '\nVarastossa 4 kpl', '\nVarastossa 3 kpl', '\nVarastossa 2 kpl', '\nVarastossa 1 kpl']:
            print(f"{i}. {driverName}\n{driverPrice}\n{driverLink}\n{availability}\n")
        else:
            noMoreDrivers = True
            driver.close()
            break

        data = {
                "id": i,
                "make": 'AMD',
                "name": driverName,
                "link": driverLink,
                "price": driverPrice,
            }
        result.append(data)
        i += 1
        value += 1
    json_data = json.dumps(result, indent=4, ensure_ascii=False)
    print("Json successful")
    with open('public/data/jimms.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    next_pagelink = soup.find('a', class_='product-list__pagination')
    if noMoreDrivers == True:
        break