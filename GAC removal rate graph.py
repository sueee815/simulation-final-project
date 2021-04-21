#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:29:31 2021

@author: suee
"""
import numpy as np
import math 
import matplotlib.pyplot as plt

## C_e/C_0 =1/(1+exp[K/Q(q_0M-C_0V)])
# have a volumetric flow rate 
#return 1/(1+math.exp(0.00023*(401.85-C_0*V))
# return q_e*(1-math.exp(k*V))
V=[10,20,30,40,50,60,70,80,90,100,150,200,300,400,500]
n=len(V)
C20=np.zeros(n)
C56=np.zeros(n)
C80=np.zeros(n)
C100=np.zeros(n)
r20=np.zeros(n)
r56=np.zeros(n)
r80=np.zeros(n)
r100=np.zeros(n)
for i in range(n):
    C20[i]=1/(1+math.exp(0.00023*(401.85-20*V[i]))) 
    C56[i]=1/(1+math.exp(0.00023*(401.85-56*V[i]))) 
    C80[i]=1/(1+math.exp(0.00023*(401.85-80*V[i]))) 
    C100[i]=1/(1+math.exp(0.00023*(401.85-100*V[i]))) 
    r20[i]=1-C20[i]
    r56[i]=1-C56[i]
    r80[i]=1-C80[i]
    r100[i]=1-C100[i]

#plt.plot(V,C20,linestyle='-',label='concentration 20ug/L')
#plt.plot(V,C56,linestyle='--',label='concentration 56ug/L')
#plt.plot(V,C80,linestyle='dashdot',label='concentration 80ug/L')
#plt.plot(V,C100,linestyle='-',label='concentration 100ug/L')
#plt.legend(loc="lower right")
#plt.xlabel("filtered water/L")
#plt.ylabel("ratio of C_t to C_O")

plt.plot(V,r20,linestyle='-',label='concentration 20ug/L')
plt.plot(V,r56,linestyle='--',label='concentration 56ug/L')
plt.plot(V,r80,linestyle='dashdot',label='concentration 80ug/L')
plt.plot(V,r100,linestyle='-',label='concentration 100ug/L')
plt.legend(loc="upper right")
plt.xlabel("filtered water/L")
plt.ylabel("removal rate of lead from tap water")

plt.plot(m_time,m_efficiency_RO4,linestyle='-',linewidth=1.5,label='RO, 4')
plt.plot(m_time,m_efficiency_GAC4,linestyle='-',linewidth=1.5,label='GAC, 4')
#plt.plot(m_time,m_efficiency_RO1,linestyle='-',linewidth=1,label='RO, 1')
#plt.plot(m_time,m_efficiency_GAC1,linestyle='-',linewidth=1,label='GAC, 1')
plt.legend(loc="best")
plt.xlabel("time,day")
plt.ylabel("efficiency,100%")
plt.title("Filters performance within 90 days, change/clean filter every 45days")