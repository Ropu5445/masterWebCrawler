from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json

url = "https://www.gigantti.fi/gaming/tietokonekomponentit/naytonohjaimet?filter=31158:N%C3%A4yt%C3%B6nohjain"
addLink = "https://www.gigantti.fi"
result = []
index = 0
options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
drivers = soup.find_all(class_="product-tile__link kps-link")
titles = soup.find_all(class_="product-name lift-above-gradient product-name--plp-view kps-link ng-star-inserted")
prices = soup.find_all(class_="product-tile__price price--inline price price--100 price--apply-margin ng-star-inserted")

for card in drivers:
    title = titles[index]
    price = prices[index]
    link = card['href']

    driver_data = {
        "title": title.text.strip(),
        "price": price.text.strip().replace('€', ''),
        "link": addLink + link
    }
    result.append(driver_data)

    index += 1
driver.close()
with open('public/data/gigantti.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, indent=2, ensure_ascii=False)

print("Crawl results saved to json file")