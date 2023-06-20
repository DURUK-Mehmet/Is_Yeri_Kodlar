import requests
import json
import pandas as pd
import os
from urllib.parse import urlparse

# Set the directory where you want to save the images
directory = "C:/Users/ilker/Desktop/images/"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


url_iller = "https://hasartespit.csb.gov.tr/query/cities"

response_iller = requests.get(url_iller)
data_iller = json.loads(response_iller.content)
cities = data_iller['items']


city_id = 46
city_name = "elazığ"
url_ilce = f"https://hasartespit.csb.gov.tr/query/counties?cityId={city_id}"

response_ilce = requests.get(url_ilce)
data_ilce = json.loads(response_ilce.content)
counties = data_ilce['items']

for county in counties:
    county_id = county['id']
    county_name = county['ad']
    url_mahalleler = f"https://hasartespit.csb.gov.tr/query/districts?countyId={county_id}"

    response_mahalle = requests.get(url_mahalleler)
    data_mahalle = json.loads(response_mahalle.content)
    mahalleler = data_mahalle['items']

    for mahalle in mahalleler:
        mahalle_id = mahalle['mahalleId']
        mahalle_name = mahalle['ad']
        url_binalar = f"https://hasartespit.csb.gov.tr/query/AddressQuery?IlId={city_id}&IlceId={county_id}&MahalleId={mahalle_id}"

        response_bina = requests.get(url_binalar)
        data_bina = json.loads(response_bina.content)

        print(f"City: {city_name}, County: {county_name}, Mahalle: {mahalle_name}")
        print(data_bina)

        if data_bina[0]:
            s = dict(data_bina[0])
            il = s['il']
            ilce = s['ilce']
            mahalle = s['mahalle']
            foto = s['fotograflar']
            uid = s['uid']
            yapi_kimlik_no = s['yapi_kimlik_no']
            dosya_adi = f"{il}-{ilce}-{mahalle}.xlsx"
            # df = pd.DataFrame(data_bina)
            # df.to_excel(dosya_adi, index=False)
            say=0
            if foto:
                for i, j in zip(foto, range(len(foto))):
                    parse = urlparse(i)
                    if parse.scheme in ['http', 'https'] and requests.get(i).status_code == 200:
                        dosya_adi1 = f"{il}-{ilce}-{mahalle}-{uid}-{yapi_kimlik_no}-{j}.jpg"
                        with open(dosya_adi1, "wb") as f:
                            f.write(requests.get(i).content)
                    else:
                        say=say+1
                        print("Fotoğraf Bulunamadı",say)
