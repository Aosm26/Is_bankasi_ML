# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# # Veri setinizi okuyun
# data = pd.read_csv('100satır.csv')

# # Label Encoding işlemi yapılacak sütunları seçin (örneğin 'carrier' ve 'devicebrand' sütunları)
# sütunlar = ['devicebrand']

# # LabelEncoder nesnesini oluşturun
# label_encoder = LabelEncoder()

# # Seçili sütunları dönüştürün ve veri setine geri ekleyin
# for sütun in sütunlar:
#     data[sütun] = label_encoder.fit_transform(data[sütun])
#     print(sütun)

# # Veri setini tekrar kaydedin
# data.to_csv('100satirsutun.csv', index=False)


import csv

# CSV dosyasının yolunu belirtin
dosya_yolu = 'converted.csv'

# CSV dosyasını açın ve satır satır okuyun
with open(dosya_yolu, mode='r', newline='', encoding='utf-8') as dosya:
    csv_okuyucu = csv.reader(dosya)
    for satir in csv_okuyucu:

        # Her satırı virgülle ayrılmış değişkenlere ayırın
        degiskenler = satir[0].split(',')
        # print(degiskenler[-3:])
        menuler = degiskenler[-3:]
        
        # Elde edilen değişkenleri kullanabilirsiniz
        for menu in menuler:
            print(menu)


gelen_veri = "4454fdss4dsfds"
sayisal_veri = ""

for karakter in gelen_veri:
    if karakter.isdigit():  # Karakter bir sayı ise
        sayisal_veri += karakter

sayisal_deger = int(sayisal_veri)
print(sayisal_deger)
