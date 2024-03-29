import json
from selenium import webdriver
from bs4 import BeautifulSoup

STEAM_SEARCH_URL = 'https://store.steampowered.com/search/?sort_by=Released_DESC&category1=998&os=win&supportedlang=english%2Crussian%2Cfinnish&filter=popularnew&ndl=1'
STEAM_GAME_URL = 'https://store.steampowered.com/app/{}/'

class Game:
    def __init__(self, title, release_date, metacritic_score, price, image, url):
        self.title = title
        self.release_date = release_date
        self.metacritic_score = metacritic_score
        self.price = price
        self.image = image
        self.url = url

def main():
    with webdriver.Chrome() as driver:
        add_birthday_cookie(driver)
        games = [get_game_data(driver, game_id) for game_id in get_games_ids(driver)]

        save_to_json("public/data/games.json", games)
        print(f'Games scraped ({len(games)} found)')

def add_birthday_cookie(driver):
    driver.get("https://store.steampowered.com")
    cookie = {'name': 'birthtime', 'value': '0', 'path': '/', 'max-age': 315360000}
    driver.add_cookie(cookie)

def get_games_ids(driver):
    soup = get_page_soup(driver, STEAM_SEARCH_URL)
    return [game_element.get("data-ds-appid") for game_element in soup.find_all('a', {'data-ds-appid': True})]

def get_game_data(driver, game_id):
    soup = get_page_soup(driver, f'{STEAM_GAME_URL.format(game_id)}')

    title = get_text_content(soup, 'div.apphub_AppName') or "N/A"
    release_date = get_text_content(soup, 'div.release_date div.date') or "N/A"
    metacritic_score = get_text_content(soup, 'div#game_area_metascore div.score') or "N/A"
    price = get_numeric_price(soup, 'div.game_purchase_price') or 0.0
    image = soup.find("img", class_ = "game_header_image_full")["src"] or "N/A"
    url = f'https://store.steampowered.com/app/{game_id}/'

    return Game(title, release_date, metacritic_score, price, image, url)

def get_page_soup(driver, url):
    driver.get(url)
    
    return BeautifulSoup(driver.page_source, "html.parser")

def get_text_content(soup, selector):
    element = soup.select_one(selector)
    return element.text.strip() if element else None

def get_numeric_price(soup, selector):
    element = soup.select_one(selector)
    raw_price_text = element.text.strip() if element else ""
    
    if raw_price_text.lower() in ['free to play', 'free'] or not raw_price_text:
        return 0

    numeric_price = raw_price_text.split('€')[0].replace(',', '.')

    try:
        return float(numeric_price)
    except ValueError:
        return None

def save_to_json(filename, game_list):
    with open(filename, 'w') as json_file:
        game_list_data = [vars(game) for game in game_list]
        json.dump(game_list_data, json_file, indent=2)
        print(f"Games results saved to {filename}")

if __name__ == "__main__":
    main()
