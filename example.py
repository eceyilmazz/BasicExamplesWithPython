from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

veri = pd.read_csv("data2.csv")

çıktı = pd.DataFrame(veri.K)

a= veri.iloc[:,0:5]
b = veri.iloc[:,6:9]

girdiler = pd.concat([a,b], axis=1)


 # Çoklu doğrusal regresyon 
 # eğitim ve test kümesine bölmediğimiz için modeli eğitirken girdiler ve çıktıyı kullanıyoruz

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(girdiler,çıktı)


#       için çapraz doğrulama
from sklearn.model_selection import cross_val_score
kfold=cross_val_score(lr,girdiler,çıktı,cv=5) 
print(kfold) 
print(np.mean(kfold))


# Random Forest
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=10, random_state=0) 
rf_reg.fit(girdiler,çıktı)


#      içiçe çapraz doğrulama
from sklearn.model_selection import cross_val_score
kfold2=cross_val_score(rf_reg,girdiler,çıktı,cv=5) 
print(kfold2) 
print(np.mean(kfold2))


# Çoklu doğrusal regresyon daha başarılı çıktı

# # # #

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(girdiler,çıktı,test_size=30, random_state=0)


from sklearn.linear_model import LinearRegression
lr2=LinearRegression()
lr2.fit(x_train,y_train)


tahmin=lr2.predict(x_test)


print("Çoklu Linear R2 Değeri: ")
print(r2_score(y_test,tahmin))

# # # # 

# Manuel R2 Score
x2= x_test.values
y2=y_test.values

RSS=sum((y2-tahmin)**2)
TSS=sum((y2-np.mean(y2))**2)
R2=1-(RSS/TSS)
print("R2",R2)

# düzeltilmiş R2
n = len(y2)  
d = x2.shape[1]  

adj_R2 = 1-(RSS/(n-d-1))/(TSS/(n-1))

print("Düzeltilmiş R2" ,adj_R2)

# # # # 

n2=len(veri)

s=np.ones((n2,1))

X = np.concatenate([s,girdiler], axis=1) 

A = np.dot(X.transpose(), X)    

A2 = np.linalg.inv(A) 

A3=np.dot(X.transpose(),çıktı) 

B = np.dot(A2,A3)


b2 = pd.DataFrame(B)

beta0 = b2.iloc[0:1,:]
beta1 = b2.iloc[1:2,:]
beta2 = b2.iloc[2:3,:]

Beta0= np.array(beta0)
Beta1= np.array(beta1)
Beta2= np.array(beta2)


x1 = veri.iloc[:,0:1]
x2 = veri.iloc[:,1:2]


tahmin3 = Beta0 + (Beta1 * x1) + (Beta2 * x2) 