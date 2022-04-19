import pandas as pd

import firebase_admin
from firebase_admin import credentials ,firestore

col_Names=["date", "x", "y", "carid"]
data= pd.read_csv("cars.csv",names=col_Names)


kimlik= credentials.Certificate('./key.json')
app=firebase_admin.initialize_app(kimlik)
db=firestore.client()

#Her arabanın ID'sine göre csv dosyasından verileri çekiliyor
id =10

car =data

print(data['carid'][2000])

for i in range(len(data)):
        if data['carid'][i] == 37:            
            
            document=db.collection("ALLCARS").document(str(data['carid'][i]))
            document.update({

            data['date'][i]:
                
                {"x": data['x'][i],
                "y": data['y'][i],
                
                }})
