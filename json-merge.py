import os
import json

# Ana klasör yolunu belirleyin
ana_klasor_yolu = "C:/Users/ilker/tweet-scraper/all-json"

# Hedef klasör yolunu belirleyin
hedef_klasor_yolu = "C:/Users/ilker/Desktop/merged-json"

# İlçe klasörlerinin listesini alın
ilce_klasorleri = [os.path.join(ana_klasor_yolu, il_klasoru, ilce_klasoru)
                   for il_klasoru in os.listdir(ana_klasor_yolu)
                   if os.path.isdir(os.path.join(ana_klasor_yolu, il_klasoru))
                   for ilce_klasoru in os.listdir(os.path.join(ana_klasor_yolu, il_klasoru))
                   if os.path.isdir(os.path.join(ana_klasor_yolu, il_klasoru, ilce_klasoru))]

# Her ilçe için json dosyalarını birleştirin ve yeni bir dosyaya kaydedin
for ilce_klasoru in ilce_klasorleri:
    ilce_adi = os.path.basename(ilce_klasoru)
    birlesmis_veri = []
    for dosya_adi in os.listdir(ilce_klasoru):
        if dosya_adi.endswith(".json"):
            dosya_yolu = os.path.join(ilce_klasoru, dosya_adi)
            with open(dosya_yolu, "r", encoding="utf-8") as f:
                dosya_verisi = json.load(f)
            birlesmis_veri.extend(dosya_verisi)
    hedef_dosya_yolu = os.path.join(hedef_klasor_yolu, f"{ilce_adi}.json")
    with open(hedef_dosya_yolu, "w", encoding="utf-8") as f:
        json.dump(birlesmis_veri, f, ensure_ascii=False, indent=4)
