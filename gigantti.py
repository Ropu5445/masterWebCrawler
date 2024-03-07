from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

urlNvidia = "https://www.gigantti.fi/gaming/tietokonekomponentit/naytonohjaimet?filter=31158:N%C3%A4yt%C3%B6nohjain&filter=ArticleAssignments.AssignmentSystem.Brand:Gainward&filter=ArticleAssignments.AssignmentSystem.Brand:PNY&filter=ArticleAssignments.AssignmentSystem.Brand:Palit&filter=ArticleAssignments.AssignmentSystem.Brand:EVGA"
urlRadeon = "https://www.gigantti.fi/gaming/tietokonekomponentit/naytonohjaimet?filter=31158:N%C3%A4yt%C3%B6nohjain&filter=ArticleAssignments.AssignmentSystem.Brand:Asus"
addLink = "https://www.gigantti.fi"
result = []

def Haku(url, make):
    index = 0
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    drivers = soup.find_all(class_="product-list__cell product-tile-ff-wc-wrapper ng-star-inserted")
    titles = soup.find_all(class_="product-name lift-above-gradient product-name--plp-view kps-link ng-star-inserted")
    prices = soup.find_all(class_="product-tile__price price--inline price price--100 price--apply-margin ng-star-inserted")
    links = soup.find_all(class_="product-tile__link kps-link")

    for card in drivers:
        title = titles[index]
        price = prices[index]
        link = links[index]
        index += 1
        print(title)
        driver_data = {
            "Tuote": title.text.strip(),
            "Hinta": price.text.strip().replace('€', '').replace(',', '.'),
            "Linkki": addLink + link['href'],
            "Valmistaja": make,
        }
        result.append(driver_data)

    driver.close()

# Loopataan urlit
urls_to_crawl = [urlRadeon, urlNvidia]
for url in urls_to_crawl:
    Haku(url, 'AMD' if 'AMD' in url else 'Nvidia')

with open('public/data/gigantti.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, indent=2, ensure_ascii=False)

print("Crawl results saved to json file")
