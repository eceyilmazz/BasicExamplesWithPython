import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
          
data = pd.read_csv("data (2).csv")

def hacker_bul (x):
    if "hacker" in  x.lower():
        return True
    return False

gecici= data[data["Description"].apply(hacker_bul)]

sıralı=gecici.sort_values("Score",ascending=False)