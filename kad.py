import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

data=pd.read_csv('train_final.csv')
columnnames=['id','month','n_seconds_1','n_seconds_2','n_seconds_3','carrier','devicebrand','feature_0','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6','feature_7','feature_8','feature_9','feature_10','feature_11','feature_12','feature_13','feature_14','feature_15','feature_16','feature_17','feature_18','feature_19','feature_20','feature_21','feature_22','feature_23','feature_24','feature_25','feature_26','feature_27','feature_28','feature_29','feature_30','feature_31','feature_32','feature_33','feature_34','feature_35','feature_36','feature_37','feature_38','feature_39','feature_40','feature_41','feature_42','feature_43','feature_44','feature_45','feature_46','feature_47','feature_48','feature_49','menus']
data.columns=columnnames
data.head()



menus = data["menus"].str.split(",")

# Yeni sütunları oluşturun
data["menus_0"] = 0
data["menus_1"] = 0
data["menus_2"] = 0
data["menus_3"] = 0
data["menus_4"] = 0
data["menus_5"] = 0
data["menus_6"] = 0
data["menus_7"] = 0
data["menus_8"] = 0
data["menus_9"] = 0


# Verisetini kaydedin
# data.to_csv("train_final2.csv")

data.head()

a=0
for menus in data['menus']:
    a+=1
    print(a)
    for menu in menus :
        gelen_veri = menu
        sayisal_veri = ""
        for karakter in gelen_veri:
                if karakter.isdigit():  # Karakter bir sayı ise
                    sayisal_veri += karakter
                    print(sayisal_veri)
                    data['menus_'+sayisal_veri]=1

df = data.fillna(0)
data.head()

data.to_csv("train_final2.csv")