from bs4 import BeautifulSoup
import requests
import webbrowser as wb
import json



def checkMokki():
    sivu = 1

    breakPoint = False

    JulkaisuAjat = []
    Hinnat = []
    AsuntojenKoot = []
    Linkit = []
    sijainnit=[]
    
    while True:

        if breakPoint:
            break
        url = f"https://www.etuovi.com/myytavat-loma-asunnot?haku=M2076311718&sivu={sivu}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content,"html.parser")
    
        JulkaisuAika=soup.find_all('span', class_="MuiChip-label MuiChip-labelSmall mui-style-tavflp")
        Hinta=soup.find_all('div', class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4 MuiGrid-grid-md-4 mui-style-j3iqgs")
        Koko=soup.find_all('div',class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-true MuiGrid-grid-md-4 mui-style-66utdc")
        linkki=soup.find_all('a',class_="mui-style-1hvv1xy e3qdyeq2")
        sijainti=soup.find_all('h4',class_="MuiTypography-root MuiTypography-body1 e3qdyeq9 erq801z0 mui-style-jit781")
       
        for x in linkki:
            Linkit.append("https://www.etuovi.com"+ x['href'])
    
        for x in Hinta:
            Hinnat.append(str(x.text).replace('Hinta',''))
    
        for x in Koko:
            AsuntojenKoot.append(str(x.text).replace('Koko',''))
     
        for x in sijainti:
            sijainnit.append(str(x.text))
            
        for x in JulkaisuAika:
            JulkaisuAjat.append(x.text)
            if 'vko' in x.text:
                breakPoint=True
                break
        print(f"sivu{sivu}")  
        sivu+=1 

    #poistaa listoilt kaikki mitä ei haluta nähä
    checked = 0
    for x in JulkaisuAjat:
        if 'Uusi' in JulkaisuAjat[checked]:
            print(f"{JulkaisuAjat[checked]}\n{Hinnat[checked]}\n{AsuntojenKoot[checked]}\n{Linkit[checked]}\n{sijainnit[checked]}\n\n")
            checked+=1
        else:
            sijainnit.pop(checked)
            Linkit.pop(checked)
            AsuntojenKoot.pop(checked)
            Hinnat.pop(checked)
            JulkaisuAjat.pop(checked)
    
    
    yhistetyt = [sijainnit,Linkit,AsuntojenKoot,Hinnat]
    
    tiedot = []
    
    for x in zip(*yhistetyt):
        rivi={'Sijainti':x[0],'Linkit':x[1],'AsuntojenKoot':x[2],'Hinnat':x[3],}
        tiedot.append(rivi)
        
    tiedot.pop()
    
    with open('public/data/mokit.json','w') as f:
        json.dump(tiedot,f,indent=4)

checkMokki()


