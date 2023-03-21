import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
           
data = pd.read_csv("data (2).csv")

film =data.groupby("Director")["Title"].count()

veri1 = pd.DataFrame(film)

sart=veri1.sort_values("Title", ascending=False).head(1)

sart1 = data["Director"] == sart.index.item()


veri1=data[(sart1)]
kisi = veri1.sort_values("Revenue",ascending=False).head(1)