import cloudscraper 
from bs4 import BeautifulSoup as bs
import json
import numpy as np

scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 

def Haku(url,Maker):
    result =[]
    response = scraper.get(f"{url}")
    if response.status_code == 200:
        response.encoding = 'utf-8'
        content = response.text
        processed_content = bs(content, "html.parser") 
        
        pages = processed_content.find_all("div",  class_="site-active-results-container")
        pagenum = ((int(str(pages).split(": ")[1].split("<")[0])-1)/25)+1    
        
        nayttis_lasku = 1
        current_page = 1
        while current_page <= pagenum:
            response = scraper.get(f"{url}&pn={current_page}")
            response.encoding = 'utf-8'
            content = response.text

            processed_content = bs(content, "html.parser")
        
            if response.status_code == 200:
                links = processed_content.find_all("a",  class_="site-product-link")
                prices = processed_content.find_all("div",  class_="col-xs-12 col-sm-12 price-container")

                for link, price in zip(links, prices):
                    print(f"{nayttis_lasku} .Näyttis nro ")
                    
                    split_text = link.text.split(" - Näytönohjaimet")
                    driver_name = split_text[0].replace("\n","")
                    print(f"    {driver_name}")

                    lines = price.text.split('\n')
                    third_from_bottom = lines[-3]
                    driver_price = third_from_bottom.split(' ')[0]
                    driver_price = driver_price.replace('\u00a0', ' ')
                    print(f"    {driver_price}")
                    
                    driver_link = f"https://www.proshop.fi{link['href']}"
                    print(f"    {driver_link}") 

                    data = {
                        #"id": nayttis_lasku,
                        "Name": driver_name,
                        "Price": driver_price,
                        "Link": driver_link,
                        "Make" : Maker,
                        
                    }
                    result.append(data)           
                    nayttis_lasku += 1   
            else:
                print("Ei päästy sivulle")                         
            print((f"{url}&pn={current_page}"))
            current_page += 1
        print("Resultit annettu")
        return result

Url_Nvidia ="https://www.proshop.fi/Naeytoenohjaimet?f~grafikkort_videoudganggrafikprocessorleverandor=nvidia-geforce-rtx-4070~nvidia-geforce-rtx-4070-super~nvidia-geforce-rtx-4070-ti~nvidia-geforce-rtx-4070-ti-super~nvidia-geforce-rtx-4080~nvidia-geforce-rtx-4090&inv=1&pre=0"
Url_Amd = "https://www.proshop.fi/Naeytoenohjaimet?inv=1&pre=0&f~grafikkort_videoudganggrafikprocessorleverandor=amd-radeon-rx-7900-xt~amd-radeon-rx-7900-xtx"
Result_Nvidia = Haku(Url_Nvidia,"Nvidia")
Result_Amd = Haku(Url_Amd,"Amd",)
Result_Final = np.hstack((Result_Nvidia, Result_Amd))
Result_Final = Result_Final.tolist()

with open('Proshop.json', 'w') as json_file:
    json.dump(Result_Final, json_file, indent=4)
