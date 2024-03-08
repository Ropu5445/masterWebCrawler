# Master WebCrawler Projekti
## Projektin Asennus
Kloonaa git repo ja asenna tarvittavat node moduulit
```
git clone https://github.com/Ropu5445/masterWebCrawler.git
npm install
```
Tämän jälkeen tee python venv ja aktivoi se.
```
python -m venv venv
./venv/Scripts/activate
python -m pip install -r requirements.txt
```
Korvaa flight.py ja scrape.py tiedostot `venv\Lib\site-packages\google_flight_analysis` kansiossa, saman nimisillä python scripteillä jotka löytyvät projektikansiossa.

## Python scriptien käyttö
> [!NOTE]
> Muista aktivoida venv ennen python scriptien käyttöä, komennolla `./venv/Scripts/activate`

Voi käynnistää kaikki python scriptit komennolla.
```
python scrapers_runner.py
```
## Serverin ja Verkkosivun käyttö
Voit käyttää sivustoa käynnistämällä serverin nodella ja menemällä [localhost](http://localhost:80) sivulle.
```
node server.js
```

![Esimerkki verkkosivusta](./screenshots/example.png?raw=true "Esimerkki verkkosivusta")
