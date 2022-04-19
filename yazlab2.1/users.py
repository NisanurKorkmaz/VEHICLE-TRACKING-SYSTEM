import sqlite3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

time = datetime.datetime.now()
currentTime = time.strftime("%H:%M")
currentTime = currentTime.split(":")
currentSum = int(currentTime[0])*60 + int(currentTime[1])

dictionary = {}
keyList = []
liste = []
liste2 = []
liste3 = []
liste4 = []


#SQLITE BAĞLANTISI
usersData = list()
usersDataList = list()
conection = sqlite3.connect('database.db')
c = conection.cursor()

c.execute("SELECT * FROM users")
usersData=c.fetchall()
for i in range(len(usersData)):
    for j in range(len(usersData[i])):
        u=usersData[i][j]
        usersDataList.append(u)

conection.commit()
conection.close()

#FİRESTORE BAĞLANTISI
cred = credentials.Certificate("firestorekey.json")
firebase_admin.initialize_app(cred)


#VERİLERİ PARÇALAMA
db = firestore.client()

data_25_docu = db.collection(u'ALLCARS').document(str(25))
data_25_doc = data_25_docu.get()._data
data_10_docu = db.collection('ALLCARS').document(str(10))
data_10_doc = data_10_docu.get()._data
data_34_docu = db.collection(u'ALLCARS').document(str(34))
data_34_doc = data_34_docu.get()._data
data_37_docu = db.collection(u'ALLCARS').document(str(37))
data_37_doc = data_37_docu.get()._data


# 10 numaralı araba için
x_list10=[]
y_list10=[]
date_list10=[]
time_point10=[]
doc10 = data_10_doc

for value, date in doc10.items():
    x_list10.append(doc10[value]['x'])
    y_list10.append(doc10[value]['y'])
    date_list10.append(value)
    time = value.split(" ")
    saat = time[1]
    saat_birim = saat.split(":")
    toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
    time_point10.append(toplam)


#25 numaralı araba için

x_list25=[]
y_list25=[]
date_list25=[]
time_point25=[]
doc25 = data_25_doc

for value, date in doc25.items():
    x_list25.append(doc25[value]['x'])
    y_list25.append(doc25[value]['y'])
    date_list25.append(value)
    time = value.split(" ")
    saat = time[1]
    saat_birim = saat.split(":")
    toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
    time_point25.append(toplam)


#34 numaralı araba için

x_list34=[]
y_list34=[]
date_list34=[]
time_point34=[]
doc34 = data_34_doc

for value, date in doc34.items():
    x_list34.append(doc34[value]['x'])
    y_list34.append(doc34[value]['y'])
    date_list34.append(value)
    time = value.split(" ")
    saat = time[1]
    saat_birim = saat.split(":")
    toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
    time_point34.append(toplam)

#37 numaralı araba için

x_list37=[]
y_list37=[]
date_list37=[]
time_point37=[]
doc37 = data_37_doc

for value, date in doc37.items():
    x_list37.append(doc37[value]['x'])
    y_list37.append(doc37[value]['y'])
    date_list37.append(value)
    time = value.split(" ")
    saat = time[1]
    saat_birim = saat.split(":")
    toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
    time_point37.append(toplam)


#SON 30 DK VERİLERİNİ ÇEKME - t=şimdiki zaman ,x=x koordinat ,y=y koordinat ,sumT=araba konum saatleri, son_30= haritada gösterilecek konumlar
def son_30_veriler(t,x,y,sumT):
    son_30_minute = t-30
    son_30 = []
    for i in range(1440):
        
        if sumT[i] <= t and sumT[i] >= son_30_minute:
            son_30_konum = {
                "x":0,
                "y":0
            }
            son_30_konum.update({"x": x[i]})
            son_30_konum.update({"y": y[i]})
            son_30.append(son_30_konum)
            
    return son_30

#Arabaya göre saat sorgusu çekme
liste = son_30_veriler(currentSum,x_list10,y_list10,time_point10)
liste2 = son_30_veriler(currentSum,x_list37,y_list37,time_point37)
liste3 = son_30_veriler(currentSum,x_list25,y_list25,time_point25)
liste4 = son_30_veriler(currentSum,x_list34,y_list34,time_point34)

