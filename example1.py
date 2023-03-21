import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

veri = pd.read_csv('veri.csv')

veriler = veri.iloc[:,1:7]
g=np.transpose(veriler)

dendrogram = sch.dendrogram(sch.linkage(g, method='complete'),leaf_rotation=90,leaf_font_size=10)

