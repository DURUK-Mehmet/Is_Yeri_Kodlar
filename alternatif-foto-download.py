from urllib.parse import urlparse
import os
import time
from pydub import AudioSegment
import json
import pandas as pd
import requests

for i in range(0,200):
    data = ""

    ilce_json_yolu = f"C:/Users/ilker/Desktop/elazığ-merkez-mahalleler/{i}.json"
    image_folder = f"C:/Users/ilker/Desktop/elazığ-merkez-foto/elazığ-merkez-foto-{i}"

    with open(ilce_json_yolu, "r", encoding="utf-8") as f:
        data = json.load(f)

    for json_verisi in data:
        # burada json_verisi üzerinde işlemler yapabilirsiniz
        askiKodu = json_verisi['askiKodu']
        yapi_kimlik_no = json_verisi['yapi_kimlik_no']
        il = json_verisi['il']
        ilce = json_verisi['ilce']
        mahalle = json_verisi['mahalle']
        aciklama = json_verisi['aciklama']
        foto = json_verisi['fotograflar']

        df = pd.DataFrame(data)

        if foto:
            for i, j in zip(foto, range(len(foto))):
                parse = urlparse(i)
                print(foto)
                if parse.scheme in ['http', 'https'] and requests.get(i).status_code == 200:
                    dosya_adi1 = f"{askiKodu}-{yapi_kimlik_no}-{il}-{ilce}-{mahalle}-{aciklama}-{j}.jpg"
                    dosya_yolu = os.path.join(image_folder, dosya_adi1)

                    # image_folder yolunda klasör yoksa, oluştur
                    if not os.path.exists(image_folder):
                        os.makedirs(image_folder)

                    with open(dosya_yolu, "wb") as f:
                        f.write(requests.get(i).content)

                else:
                    print("Fotoğraf Bulunamadı")
