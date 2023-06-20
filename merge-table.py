# import pandas as pd
# import os
#
# # Birleştirilecek dosyaların bulunduğu klasörün yolu
# folder_path = 'C:/Users/ilker/tweet-scraper/all-json/adiyaman'
#
# # Tüm Excel dosyalarının adlarını bir listeye kaydedin
# files = os.listdir(folder_path)
# excel_files = [f for f in files if f.endswith('.xlsx')]
#
# # Excel dosyalarını birleştirmek için boş bir DataFrame oluşturun
# merged_data = pd.DataFrame()
#
# i=0
# # Tüm Excel dosyalarını birleştirin
# for file in excel_files:
#     print(i)
#     i=i+1
#     # Her dosyayı okuyun
#     data = pd.read_excel(os.path.join(folder_path, file))
#     # Okunan verileri birleştirin
#     merged_data = pd.concat([merged_data, data])
#
# # Birleştirilmiş verileri bir Excel dosyasına yazın
# merged_data.to_excel('C:/Users/ilker/Desktop/adıyaman.xlsx', index=False)


import pandas as pd
import os

# Ana klasörün yolu
folder_path = 'C:/Users/ilker/tweet-scraper/all-json/Osmaniye'

# Tüm alt klasörleri dolaşarak Excel dosyalarını birleştir
def merge_excel_files(folder_path):
    count = 0
    # Ana klasördeki tüm klasörleri listele
    folder_list = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    # Tüm alt klasörleri dolaşarak Excel dosyalarını birleştir
    merged_data = pd.DataFrame()
    for folder in folder_list:
        # Her klasördeki Excel dosyalarını listele
        excel_files = [f for f in os.listdir(folder) if f.endswith('.xlsx')]
        # Her Excel dosyasını okuyarak birleştir
        for file in excel_files:
            count = count + 1
            print(count)
            data = pd.read_excel(os.path.join(folder, file))
            merged_data = pd.concat([merged_data, data])

    # Birleştirilmiş verileri bir Excel dosyasına yazın
    merged_data.to_excel('C:/Users/ilker/Desktop/osmaniye.xlsx', index=False)


merge_excel_files(folder_path)
