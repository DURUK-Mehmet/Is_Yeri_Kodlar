null=""
data = [{"mahalleId":7366,"ad":"Akçatepe","uyari":null},{"mahalleId":4485,"ad":"Ayniye","uyari":null},{"mahalleId":7367,"ad":"Boyundere","uyari":null},{"mahalleId":4486,"ad":"Bulanık","uyari":null},{"mahalleId":4488,"ad":"Çamlıca","uyari":null},{"mahalleId":7369,"ad":"Çiftlik","uyari":null},{"mahalleId":4487,"ad":"Cumhuriyet","uyari":null},{"mahalleId":7382,"ad":"Elçiler","uyari":null},{"mahalleId":4489,"ad":"Fethiye","uyari":null},{"mahalleId":7371,"ad":"Havutlu","uyari":null},{"mahalleId":7372,"ad":"Kaşlıca","uyari":null},{"mahalleId":7374,"ad":"Köseli","uyari":null},{"mahalleId":7375,"ad":"Meryemuşağı","uyari":null},{"mahalleId":7376,"ad":"Öğütlü","uyari":null},{"mahalleId":4490,"ad":"Reşadiye","uyari":null},{"mahalleId":4491,"ad":"Salah","uyari":null},{"mahalleId":7377,"ad":"Tepecik","uyari":null},{"mahalleId":74015,"ad":"Ünlüce","uyari":null},{"mahalleId":7379,"ad":"Yalankoz","uyari":null},{"mahalleId":7380,"ad":"Yaylımlı","uyari":null},{"mahalleId":7383,"ad":"Yeşilyurt","uyari":null}]


#######
mahalleIds = [d['mahalleId'] for d in data]

with open('wordlist/adıyaman-tut-1989.txt', 'w') as f:
    for mahalleId in mahalleIds:
        f.write(str(mahalleId) + '\n')

