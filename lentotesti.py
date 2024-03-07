from google_flight_analysis.scrape import *
from json import loads, dumps, dump
import json

##JOS TULEE JOKU HASSUINEN "3.05 PM is not in tämä yks formaatti" nii mene flight.py rivi 120 ja laita väli %M ja %p väliin, kokeile uusiksi (ei tule toimimaa silloinkaa) ja ota se väli pois

#tämä käyttää airporttien IATA 3 kirjaimisia koodeja originissa ja destinationissa
#päivämäärät ovat YYYY-MM-DD muodossa



def toColorado():
    #coloradomatka
    
    result = Scrape('HEL', 'DEN', '2024-06-01', '2024-06-26') 
    
    ##öh?
    result.type 
    result.origin 
    result.dest 
    result.date 
    
    #ota data
    ScrapeObjects(result)
    valmis=result.data
    print(valmis)
    
    
    #laitetaan jsoniin
    results = valmis.to_json(orient="records")
    
    a11=loads(results)

    with open('./public/data/ulkomaidenmatkatCOL.json',"w", encoding="utf-8") as f:
        dump(a11, f)
    
def toFrance():
    #ranskamatka
    
    result = Scrape('HEL', 'ORY', '2024-06-01', '2024-06-26') 
    result.type 
    result.origin 
    result.dest 
    result.date 
    
    ScrapeObjects(result)
    valmis=result.data
    print(valmis)
    
    results = valmis.to_json(orient="records")
    
    a11=loads(results)

    with open('./public/data/ulkomaidenmatkatFRN.json',"w", encoding="utf-8") as f:
        dump(a11, f)
    
def toSwitzer():
    #sveitsimatka
    
    result = Scrape('HEL', 'GVA', '2024-06-01', '2024-06-26') 
    result.type 
    result.origin 
    result.dest 
    result.date 
    
    ScrapeObjects(result)
    valmis=result.data
    print(valmis)
    
    results = valmis.to_json(orient="records")
    
    a11=loads(results)

    with open('./public/data/ulkomaidenmatkatSVT.json',"w", encoding="utf-8") as f:
        dump(a11, f)
    
def toAustria():
    #austriamatka
    
    result = Scrape('HEL','INN', '2024-06-01', '2024-06-26') 
    result.type 
    result.origin 
    result.dest 
    result.date 
    
    ScrapeObjects(result)
    valmis=result.data
    print(valmis)
    
    results = valmis.to_json(orient="records")
    
    a11=loads(results)

    with open('./public/data/ulkomaidenmatkatAST.json',"w", encoding="utf-8") as f:
        dump(a11, f)
    
def toCanada():
    #kanadamatka
    
    result = Scrape('HEL', 'YVR', '2024-06-01', '2024-06-26') 
    result.type 
    result.origin 
    result.dest 
    result.date 
    
    ScrapeObjects(result)
    valmis=result.data
    print(valmis)
    
    results = valmis.to_json(orient="records")
    
    a11=loads(results)

    with open('./public/data/ulkomaidenmatkatCND.json',"w", encoding="utf-8") as f:
        dump(a11, f)
    
    
toColorado()
toFrance()
toSwitzer()
toAustria()
toCanada()

