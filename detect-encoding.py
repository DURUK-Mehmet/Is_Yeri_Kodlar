# import chardet
#
# with open("C:/Users/ilker/tweet-scraper/all-json/adiyaman/adiyaman-besni/2.json", "rb") as f:
#     dosya_verisi = f.read()
#     dosya_kodlamasi = chardet.detect(dosya_verisi)["encoding"]
#
# print("Dosya kodlaması:", dosya_kodlamasi)
import os
import json
ana_klasor_yolu = "C:/Users/ilker/Desktop/all-json/Elazig/Merkez"
hedef_klasor_yolu = "C:/Users/ilker/Desktop/merged-json"

birlesmis_veri = []
for dosya_adi in os.listdir(ana_klasor_yolu):
    if dosya_adi.endswith(".json"):
        dosya_yolu = os.path.join(ana_klasor_yolu, dosya_adi)
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            dosya_verisi = json.load(f)
        birlesmis_veri.extend(dosya_verisi)
hedef_dosya_yolu = os.path.join(hedef_klasor_yolu, f"elazığ-merkez.json")
with open(hedef_dosya_yolu, "w", encoding="utf-8") as f:
    json.dump(birlesmis_veri, f, ensure_ascii=False, indent=4)