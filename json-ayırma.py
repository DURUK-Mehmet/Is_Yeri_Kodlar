import json

json_yolu = "C:/Users/ilker/Desktop/kopya-elazığ-Merkez.json"

with open(json_yolu, "r", encoding="utf-8") as f:
    veriler = json.load(f)

parca_sayisi = 1000
veri_parcalari = [veriler[i:i+parca_sayisi] for i in range(0, len(veriler), parca_sayisi)]

for i, veri_parcasi in enumerate(veri_parcalari):
    with open(f'kopya-elazığ-Merkez{i}.json', 'w') as f:
        json.dump(veri_parcasi, f)
