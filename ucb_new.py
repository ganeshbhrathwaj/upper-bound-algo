#UCB

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#importing dataset
ds=pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing UCB

N=10000
d=10
ads_selected=[]
no_of_selection=[0]*d
sum_of_reward=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_ub=0
    for i in range(0,d):
        if(no_of_selection[i]>0):
            avg_reward=sum_of_reward[i]/no_of_selection[i]
            delta=math.sqrt(3/2 * math.log(n+1) / no_of_selection[i])
            ub=avg_reward+delta
        else:
            ub=1e400
        if(ub >max_ub):
            max_ub=ub
            ad=i
    ads_selected.append(ad)
    no_of_selection[ad]=no_of_selection[ad]+1
    reward=ds.values[n,ad]
    sum_of_reward[ad]= sum_of_reward[ad]+reward
    total_reward=total_reward+reward
        
#visualization
plt.hist(ads_selected)
plt.title("ads_selected")
plt.xlabel("ads")
plt.ylabel("no of times each ad was selected")
plt.show()
