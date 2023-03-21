import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import math 


x=np.array([1,2,4,5,6,8])
y=np.array([2,2.4,5.1,7.3,9.4,18.3])

a1=math.exp(sum((x-np.mean(x))*((math.log(y))-(math.log(np.mean(y))))))

a2=sum((x-np.mean(x))**2)

beta=a1/a2

a=math.exp((math.log(np.mean(y)))-(math.log(x)))