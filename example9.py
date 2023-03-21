import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
          
data = pd.read_csv("data (2).csv")

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

data["Year"]=le.fit_transform(data["Year"]) 

buyuk=data["Year"].max()

for j,i in enumerate(range(96,99)):
    j=j+2013
    sonuc=data[(data["Year"]==i)]
    sonuc1=sonuc[sonuc["Score"]==sonuc["Score"].max()]["Title"].iloc[0]
    yil=str(j)
    print(yil + ":" +sonuc1)