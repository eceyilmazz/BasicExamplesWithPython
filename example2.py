import pandas as pd
import math 

risk = [["Var","Yok"]]

girdi = pd.DataFrame(risk)
Hastalık = [[35,16],[25,61],[60,77]]

cıktı = pd.DataFrame(Hastalık)

p = 2/60  #p(x)

t = p/(1-p) #(p(x)/1p(x))

h = math.log(t) #ln(p(x)/1p(x))   h->m

gecici = math.exp(h)
o = gecici/1+gecici  # hastalığın var olma olasılığı
print("Hastalığın var olma olasılığı")
print(o)


hastalık_yok = 1-p
print("Hastalığın yok olma olasılığı (1-p(x)) ")
print(hastalık_yok)

