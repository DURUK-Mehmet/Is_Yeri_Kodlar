from urllib.parse import urlparse
import os
import json
import pandas as pd
import requests

data = ""

ilce_json_yolu = "C:/Users/ilker/Desktop/gaziantep-karkamış.json"
image_folder = "C:/Users/ilker/Desktop/gaziantep-karkamış"

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

              # remove the downloaded photo link from the JSON data
              json_verisi['fotograflar'].remove(i)
          else:
              print("Fotoğraf Bulunamadı")


import os

# Müzik dosyasının bulunduğu klasörün yolu
klasor_yolu = "C:/Users/ilker/Desktop"

# Klasördeki tüm dosyaları listele
dosyalar = os.listdir(klasor_yolu)

# Sadece müzik dosyalarını ayıkla (örneğin .mp3, .wav, .ogg uzantılı dosyalar)
muzik_dosyalari = [dosya for dosya in dosyalar if dosya.endswith(".mp3") or dosya.endswith(".wav") or dosya.endswith(".ogg")]

# İlk müzik dosyasını çal
ilk_muzik_dosyasi = muzik_dosyalari[0]
os.startfile(os.path.join(klasor_yolu, ilk_muzik_dosyasi))

