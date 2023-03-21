import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
           
data = pd.read_csv("data (2).csv")

sart=data.sort_values("Score",ascending=False).head(10)

rev=sart["Revenue"]
sc=sart["Score"]

rev=pd.DataFrame(rev)

# nan temizleme
adet_toplam=rev.size
nan_adet_toplamı=rev.isnull().sum().sum()

toplam=(adet_toplam)-(nan_adet_toplamı)

deger_top=rev.sum()

ortalama=deger_top/toplam


sart2 = rev.fillna(value=ortalama)
sart2["Score"] = sc

# plt.pie(sart2.Revenue,labels=sart2.Score,autopct='%1.1f%%',shadow=True,
#            startangle=90,pctdistance=0.7,textprops={'fontsize':10})

grup=sart2.groupby("Score")["Revenue"].mean()

x=grup.index.tolist()  # Score
y=grup.values.tolist()  # Revenue

plt.pie(y,labels=x,autopct='%1.1f%%',shadow=True,
            startangle=90,pctdistance=0.7,textprops={'fontsize':10})

# plt.figure()
# plt.pie(x, labels=y,autopct='%1.1f%%',shadow=True,
#            startangle=90,pctdistance=0.7,textprops={'fontsize':10})