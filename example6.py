import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
 
          
data = pd.read_csv("data (2).csv")

data=data[data["Year"]>2010]

data=data[(data["Genre"]=="Comedy") | (data["Genre"]=="Drama") | (data["Genre"]=="Action")]


grup=data.groupby(["Year","Genre"])["Title"].count()
veri=pd.DataFrame(grup)

veri1=grup.copy().reset_index()


sns.lineplot(veri1.Year, veri1.Title, hue="Genre",data=veri1,linewidth=2.5,
             style="Genre",markers=True,dashes=False)