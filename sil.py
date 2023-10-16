# import csv

# # CSV dosyasının adını ve yolunu belirtin
# dosya_adı = "train_final.csv"

# # Silmek istediğiniz satırların başlangıç indeksi (100. satır)
# baslangic_indeksi = 100

# # CSV dosyasını okuyun ve geçici bir liste oluşturun
# gecici_satırlar = []

# with open(dosya_adı, "r", newline="", encoding="utf-8") as csv_dosya:
#     csv_okuyucu = csv.reader(csv_dosya)
    
#     for indeks, satır in enumerate(csv_okuyucu):
#         # Silmek istediğiniz satırları atlayın (belirtilen indeksin altındaysa)
#         if indeks < baslangic_indeksi:
#             gecici_satırlar.append(satır)

# # CSV dosyasını yeniden yazın ve geçici listeyi kullanarak silinmiş satırları atlayın
# with open(dosya_adı, "w", newline="", encoding="utf-8") as csv_dosya:
#     csv_yazıcı = csv.writer(csv_dosya)
#     csv_yazıcı.writerows(gecici_satırlar)

# print("100. satır ve sonrası başarıyla silindi.")


import csv

# CSV dosyasının adını ve yolunu belirtin
dosya_adı = "train_final_hundred.csv"

# Yeni sütunların adlarını belirtin
yeni_sutunlar = ["menu1", "menu2", "menu3", "menu4", "menu5", "menu6", "menu7", "menu8", "menu9"]


# Yeni sütunların varsayılan değerini belirtin (0)
yeni_sutun_degeri = 0

# CSV dosyasını okuyun ve mevcut verileri alın
mevcut_veriler = []

with open(dosya_adı, "r", newline="", encoding="utf-8") as csv_dosya:
    csv_okuyucu = csv.reader(csv_dosya)
    mevcut_veriler = [satır for satır in csv_okuyucu]

# Yeni sütunların başlıklarını ekleyin
mevcut_veriler[0].extend(yeni_sutunlar)

# Yeni sütunların değerlerini ekleyin (tüm satırlar için 0)
for satır in mevcut_veriler[1:]:
    satır.extend([str(yeni_sutun_degeri) for _ in yeni_sutunlar])

# CSV dosyasını yeniden yazın ve yeni sütunları içeren verileri kaydedin
with open(dosya_adı, "w", newline="", encoding="utf-8") as csv_dosya:
    csv_yazıcı = csv.writer(csv_dosya)
    csv_yazıcı.writerows(mevcut_veriler)

print("Yeni sütunlar başarıyla eklendi ve değerleri 0 olarak ayarlandı.")
