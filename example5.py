import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

           
data = pd.read_csv("data (2).csv")

sart=data.sort_values("Score",ascending=False).head(30)
rev=sart["Revenue"]
sc=sart["Score"]

rev=pd.DataFrame(rev)

adet_toplam=rev.size
nan_adet_toplamı=rev.isnull().sum()

toplam=(adet_toplam)-(nan_adet_toplamı)

deger_top=rev.sum()

ortalama=deger_top/toplam


sart2 = rev.fillna(value=ortalama)
sart2["Score"] = sc

grup=sart2.groupby("Score")["Revenue"].sum()

x=grup.index.tolist()
y=grup.values.tolist()

plt.figure(figsize=(10,10))
sns.barplot(x=sart.Revenue,y=sart.Score)

plt.xlabel("Hasılat Bilgileri",size=20)
plt.ylabel("IMDB Puanı",size=20)

plt.xticks(size=15)
plt.yticks(size=15)

plt.title("IMDB Puanı - Hasılat Bilgisi")