#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:47:25 2021

@author: suee
"""
#plot distribution for wate usage and time for usage

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import math
# 
# # water usa
# # =============================================================================
# mu, sigma, num_bins = 8, 0.5, 50
# mu1, sigma1 , num_bins1 = 10, 0.5, 50
# mu2, sigma2 , num_bins2 = 12, 0.5, 50
# mu3, sigma3 , num_bins3 = 3, 0.5, 50
# x = mu + sigma * np.random.randn(1000)
# x1 = mu1 + sigma1 * np.random.randn(1000)
# x2 = mu2 + sigma2 * np.random.randn(1000)
# x3 = mu3 + sigma3 * np.random.randn(1000)
# # 
# n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor = 'blue', alpha = 0.5)
# n1, bins1, patches = plt.hist(x1, num_bins1, normed=True, facecolor = 'blue', alpha = 0.5)
# n2, bins2, patches = plt.hist(x2, num_bins2, normed=True, facecolor = 'blue', alpha = 0.5)
# n3, bins3, patches = plt.hist(x3, num_bins3, normed=True, facecolor = 'blue', alpha = 0.5)
# # 
# y = norm.pdf(bins, mu, sigma)
# y1 = norm.pdf(bins1, mu1, sigma1)
# y2 = norm.pdf(bins2, mu2, sigma2)
# y3 = norm.pdf(bins3, mu3, sigma3)
# plt.xlabel('water usage L/person*day')
# plt.ylabel('frequency of every X')
# plt.title('normal distribution of water usage: $\mu = 2$, $\sigma=0.5$')
# plt.plot(bins, y, 'r--')
# plt.plot(bins1, y1, 'r--')
# plt.plot(bins2, y2, 'r--')
# plt.plot(bins3, y3, 'r--')
# =============================================================================
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm

 

 

# 根据均值、标准差,求指定范围的正态分布概率值

def normfun(x, mu, sigma):

    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))

    return pdf

 
left,width=0.14,0.77
bottom,height=0.11,0.5
bottom_h=bottom+height+0.04

rect_line1=[left,bottom,width,height]

axbelow=plt.axes(rect_line1)

# result = np.random.randint(-65, 80, size=100) # 最小值,最大值,数量

result = np.random.normal(8, 0.5, 100) # 均值为0.5,方差为1
result1 = np.random.normal(8.2, 0.5, 100)
result2 = np.random.normal(8.3, 0.5, 100)
result3 = np.random.normal(8.4, 0.5, 100)

 
x = np.arange(min(result), max(result), 0.1)
x1 = np.arange(min(result1), max(result1), 0.1)
x2 = np.arange(min(result2), max(result2), 0.1)
x3 = np.arange(min(result3), max(result3), 0.1)
# 设定 y 轴，载入刚才的正态分布函数

y = normfun(x, result.mean(), result.std())
y1 = normfun(x1, result1.mean(), result1.std())
y2 = normfun(x2, result2.mean(), result2.std())
y3 = normfun(x3, result3.mean(), result3.std())
# axbelow.plot(x, y,label='person A at 8:00am') # 这里画出理论的正态分布概率曲线
# plt.plot(x1, y1,label='person B at 8:12am')
# plt.plot(x2, y2,label='person C at 8:18am')
# plt.plot(x3, y3,label='person D at 8:24am')

result7 = np.random.normal(18, 0.5, 100) # 均值为0.5,方差为1
result4 = np.random.normal(18.2, 0.5, 100)
result5 = np.random.normal(18.3, 0.5, 100)
result6 = np.random.normal(18.4, 0.5, 100)

 
x7 = np.arange(min(result7), max(result7), 0.1)
x4 = np.arange(min(result4), max(result4), 0.1)
x5 = np.arange(min(result5), max(result5), 0.1)
x6 = np.arange(min(result6), max(result6), 0.1)
# 设定 y 轴，载入刚才的正态分布函数

y7 = normfun(x7, result7.mean(), result7.std())
y4 = normfun(x4, result4.mean(), result4.std())
y5 = normfun(x5, result5.mean(), result5.std())
y6 = normfun(x6, result6.mean(), result6.std())
plt.plot(x7, y7,label='person A at 6:00pm') # 
plt.plot(x4, y4,label='person B at 6:12pm')
plt.plot(x5, y5,label='person C at 6:18pm')
plt.plot(x6, y6,label='person D at 6:24pm')
 

  

# 这里画出实际的参数概率与取值关系

plt.hist(result, bins=10, rwidth=0.8, density=True) # bins个柱状图,宽度是rwidth(0~1),=1没有缝隙
plt.hist(result1, bins=10, rwidth=0.8, density=True)
plt.hist(result2, bins=10, rwidth=0.8, density=True)
plt.hist(result3, bins=10, rwidth=0.8, density=True)
plt.hist(result4, bins=10, rwidth=0.8, density=True) # bins个柱状图,宽度是rwidth(0~1),=1没有缝隙
plt.hist(result5, bins=10, rwidth=0.8, density=True)
plt.hist(result6, bins=10, rwidth=0.8, density=True)
plt.hist(result7, bins=10, rwidth=0.8, density=True)
plt.title('Probablity of water usage from one family during one day')

plt.xlabel('time in one day')

plt.ylabel('probability of using the filter')
plt.legend(loc='upper center', numpoints=1)

leg = plt.gca().get_legend()

ltext = leg.get_texts()

plt.setp(ltext, fontsize='small')


# 输出

plt.show()

# =============================================================
# ====================== Plots ================================
# =============================================================
colorIdx = np.linspace(0, 256, num = 20).astype('int')
xTick = np.arange(6, 20 + 1, step = 1)
xTickLabel = [str(item) + ':00' for item in xTick]

fig, ax = plt.subplots(dpi = 150)

ax.set_title('Probability of Water Usage\nfrom One Family during One Day', fontsize = 18, weight = 'bold')
ax.set_xlabel('Time of the Day', fontsize = 14, weight = 'normal')
ax.set_ylabel('Probability of Using Filter', fontsize = 14, weight = 'normal')
ax.set_xticks(xTick)
ax.set_xticklabels(xTickLabel, rotation = 30)

ax.plot(x, y, linestyle = '-', color = cm.turbo(colorIdx[3]))
ax.plot(x1, y1, linestyle = '-', color = cm.turbo(colorIdx[5]))
ax.plot(x2, y2, linestyle = '-', color = cm.turbo(colorIdx[7]))
ax.plot(x3, y3, linestyle = '-', color = cm.turbo(colorIdx[9]))

ax.plot(x4, y4, linestyle = '-', color = cm.turbo(colorIdx[11]))
ax.plot(x5, y5, linestyle = '-', color = cm.turbo(colorIdx[13]))
ax.plot(x6, y6, linestyle = '-', color = cm.turbo(colorIdx[15]))
ax.plot(x7, y7, linestyle = '-', color = cm.turbo(colorIdx[17]))
legend = ['person A at 8:00am', 'person B at 8:12am', 'person C at 8:18am', 'person D at 8:24am',
          'person B at 6:12pm', 'person C at 6:18pm', 'person D at 6:24pm', 'person A at 6:00pm']
ax.legend(legend, loc = 'best', frameon = False)

ax.hist(result, bins=10, rwidth=0.8, density=True) 
ax.hist(result1, bins=10, rwidth=0.8, density=True)
ax.hist(result2, bins=10, rwidth=0.8, density=True)
ax.hist(result3, bins=10, rwidth=0.8, density=True)
ax.hist(result4, bins=10, rwidth=0.8, density=True) 
ax.hist(result5, bins=10, rwidth=0.8, density=True)
ax.hist(result6, bins=10, rwidth=0.8, density=True)
ax.hist(result7, bins=10, rwidth=0.8, density=True)
