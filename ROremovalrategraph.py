#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:35:22 2021

@author: suee
"""
## reverse osmosis membrane filtration
import numpy as np
import math
import matplotlib.pyplot as plt
# return q_e*(1-math.exp(k*V))

V=[10,20,30,40,50,60,70,80,90,100,150,200,300,400,500]
n=len(V)
C20=np.zeros(n)
C50=np.zeros(n)
C100=np.zeros(n)
C200=np.zeros(n)
r20=np.zeros(n)
r50=np.zeros(n)
r100=np.zeros(n)
r200=np.zeros(n)
for i in range(n):
    C20[i]= 15*(1-math.exp(-0.002*V[i]))
    C50[i]= 30*(1-math.exp(-0.004*V[i]))
    C100[i]=75*(1-math.exp(-0.018*V[i]))
    C200[i]=150*(1-math.exp(-0.04*V[i]))
    r20[i]= (20-15*(1-math.exp(-0.002*V[i])))/20
    r50[i]= (50-35*(1-math.exp(-0.004*V[i])))/50
    r100[i]= (100-75*(1-math.exp(-0.018*V[i])))/100
    r200[i]= (200-150*(1-math.exp(-0.036*V[i])))/200
    
plt.plot(V,C20,linestyle='-',label='concentration 20ug/L')
plt.plot(V,C50,linestyle='dashdot',label='concentration 50ug/L')
plt.plot(V,C100,linestyle=':',label='concentration 100ug/L')
plt.plot(V,C200,linestyle='-',label='concentration 200ug/L')
plt.legend(loc='center', bbox_to_anchor=(0.7, 0.7))
plt.xlabel("filtered water/L")
plt.ylabel("ratio of C_t to C_O")

#plt.plot(V,r20,linestyle='-',label='concentration 20ug/L')
#plt.plot(V,r50,linestyle='dashdot',label='concentration 50ug/L')
##plt.plot(V,r100,linestyle=':',label='concentration 100ug/L')
#plt.plot(V,r200,linestyle='-',label='concentration 200ug/L')
#plt.legend(loc="upper right")
#plt.xlabel("filtered water/L")
#plt.ylabel("removal rate of lead from tap water")
