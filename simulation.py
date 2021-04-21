#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:15:23 2021

@author: suee
"""
from pprint import pprint
from dataclasses import dataclass, field 
from typing import Callable
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



#counter initialization code at the top instead of the bottom
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(t=0)
def now():
    return now.t 

# print("The current simulation time is", now(), "o'clock.")

def set_time(t_new=0):
    now.t = t_new
    return now()

#set_time(5)
#print("Now it's", now(), "o'clock.")
@dataclass(order=True)
class Event:
    t: float
    f: Callable=field(compare=False)
    
#e1 = Event(3, lambda _1=None, _2=None: "me first")
#e2 = Event(7, lambda _1=None, _2=None: "me second")
# print(e.t, e.f())


class FutureEventList:
    def __init__(self):
        self.events = []
        
    def __iter__(self):
        return self
    
    def __next__(self) -> Event:
        from heapq import heappop
        if self.events:
            return heappop(self.events)
        raise StopIteration
    
    def __repr__(self) -> str:
        from pprint import pformat
        return pformat(self.events)    
    
event_list=FutureEventList()

def schedule(e: Event, fev: FutureEventList):
    from heapq import heappush
    heappush(fev.events, e)

#schedule(e2, event_list)
#schedule(e1, event_list)
# print(event_list)

def simulate(state, event_list, verbose=True):
    for e in event_list:
        set_time(e.t)
        state = e.f(state, event_list)
        if verbose: print(f"[t={e.t}] {state}")


def initial_stateGAC4():
    return{'used water': 0,         # Volume of water usage
            'efficiency': 1,      # efficiency of filter
            'Ci': 50 ,       # 1 is GAC, 0 is RO membrane
            'Mass': 0,
            'filter_type': 1,
            'filter_free': True,
            'no.inline': 0}

def initial_stateGAC1():
    return{'used water': 0,         # Volume of water usage
            'efficiency': 1,      # efficiency of filter
            'Ci': 50  ,      # 1 is GAC, 0 is RO membrane
            'Mass': 0    ,  # family member count
            'filter_free': True,
            'filter_type': 1,
            'no.inline': 0}


def initial_stateRO4():
    return{'used water': 0,         # Volume of water usage
            'efficiency': 1,      # efficiency of filter
            'Ci': 50     ,  # 1 is GAC, 0 is RO membrane
            'Mass': 0     , # family member count
            'filter_free': True,
            'filter_type': 0,
            'no.inline': 0}


def initial_stateRO1():
    return{'used water': 0,         # Volume of water usage
            'efficiency': 1,      # efficiency of filter
            'Ci': 50     ,   # 1 is GAC, 0 is RO membrane
            'Mass': 0    ,  # family member count
            'filter_free': True,
            'filter_type': 0,
            'no.inline':  0}

timef = 0.03  # Time using the runway
timep = 0.01 

def used(s,fev):
    s['no.inline']+=1
    if s['filter_free']:
        s['filter_free'] = False
        schedule(Event(now() + timef, filter), fev)
#    s['no.people'] -=1 
    return s

def usedeventa(s,fev):
    s['no.inline']+=1
    if s['filter_free']:
        s['filter_free'] = False
        schedule(Event(now() + timef, filtereventa), fev)
    return s

def filtereventa(s,fev): 
    n=random.uniform(0,0.1)
    s['Mass']=n*s['Ci']
    s['used water'] += np.round(n,2)
    s['used water'] =np.round(s['used water'],2)
    V1=s['used water']
    efficiency1=(50-35*(1-math.exp(-0.004*V1)))/50
    efficiency0=1.7-1/(1+math.exp(0.00033*(200.85-56*V1)))
    if s['filter_type']== 0: 
        s['efficiency'] = efficiency0                             
    if s['filter_type']== 1: 
        s['efficiency'] = efficiency1   
    if s['efficiency'] >=1:
        s['efficiency']=1
    assert not s['filter_free']
    s['no.inline']-=1
    if s['no.inline']:
        schedule(Event(now()+ timef, filtereventa),fev)
    else:
        s['filter_free']=True
    return s 

def usedeventb(s,fev):
    s['no.inline']+=1
    if s['filter_free']:
        s['filter_free'] = False
        schedule(Event(now() + timef, filtereventb), fev)
    return s

def filtereventb(s,fev): 
    n=random.uniform(1.5,2.5)
    s['Mass']=n*s['Ci']
    s['used water'] += np.round(n,2)
    s['used water'] += np.round(n,2)
    s['used water'] =np.round(s['used water'],2)
    V1=s['used water']
    efficiency1=(50-35*(1-math.exp(-0.004*V1)))/50
    efficiency0=1.7-1/(1+math.exp(0.00033*(200.85-56*V1)))
    if s['filter_type']== 0: 
        s['efficiency'] = efficiency0                             
    if s['filter_type']== 1: 
        s['efficiency'] = efficiency1 
    if s['efficiency'] >=1:
        s['efficiency']=1
    assert not s['filter_free']
    s['no.inline']-=1
    if s['no.inline']:
        schedule(Event(now()+ timef, filtereventb),fev)
    else:
        s['filter_free']=True
    return s 

def usedeventc(s,fev):
    s['no.inline']+=1
    if s['filter_free']:
        s['filter_free'] = False
        schedule(Event(now() + timef, filtereventc), fev)
    return s

def filtereventc(s,fev): 
    s['Ci']=200
    n=random.uniform(1.5,2.5)
    s['Mass']=n*s['Ci']
    s['used water'] += np.round(n,2)
    s['used water'] += np.round(n,2)
    s['used water'] =np.round(s['used water'],2)
    V1=s['used water']
    efficiency1=(200-150*(1-math.exp(-0.004*V1)))/200
    efficiency0=1.7-1/(1+math.exp(0.00033*(500.85-56*V1)))
    if s['filter_type']== 0: 
        s['efficiency'] = efficiency0                             
    if s['filter_type']== 1: 
        s['efficiency'] = efficiency1
    if s['efficiency'] >=1:
        s['efficiency']=1
    assert not s['filter_free']
    s['no.inline']-=1
    if s['no.inline']:
        schedule(Event(now()+ timef, filtereventc),fev)
    else:
        s['filter_free']=True
    return s 

def filter(s,fev): 
    n=random.uniform(1.5,2.5)
    s['Mass']=n*s['Ci']
    s['used water'] += np.round(n,2)
    s['used water'] =np.round(s['used water'],2)
    V1=s['used water']
    efficiency1=(50-35*(1-math.exp(-0.004*V1)))/50
    efficiency0=1.65-1/(1+math.exp(0.00033*(200.85-56*V1)))
    if s['filter_type']== 0: 
        s['efficiency'] = efficiency0                             
    if s['filter_type']== 1: 
        s['efficiency'] = efficiency1   
    assert not s['filter_free']
    s['no.inline']-=1
    if s['no.inline']:
        schedule(Event(now()+ timef, filter),fev)
    else:
        s['filter_free']=True
    if s['efficiency'] >=1:
        s['efficiency']=1
    ###### reset family number 
#    if s['no.people'] <= 0:
#        s['no.peple']=4
    return s 

def usedeventd(s,fev):
    s['no.inline']+=1
    if s['filter_free']:
        s['filter_free'] = False
        schedule(Event(now() + timef, filtereventd), fev)
    return s

def filtereventd(s,fev): 
    s['Ci']=50
    n=random.uniform(0.1,0.2)
    s['Mass']=n*s['Ci']
    s['used water'] += np.round(n,2)
    s['used water'] += np.round(n,2)
    s['used water'] =np.round(s['used water'],2)
    V1=s['used water']
    efficiency1=(50-35*(1-math.exp(-0.004*V1)))/50
    efficiency0=1.7-1/(1+math.exp(0.00033*(200.85-56*V1)))
    if s['filter_type']== 0: 
        s['efficiency'] = efficiency0                             
    if s['filter_type']== 1: 
        s['efficiency'] = efficiency1
    if s['efficiency'] >=1:
        s['efficiency']=1
    assert not s['filter_free']
    s['no.inline']-=1
    if s['no.inline']:
        schedule(Event(now()+ timef, filtereventd),fev)
    else:
        s['filter_free']=True
    return s 
def changefilter(s,fev):
     if s['filter_type']== 1:
         s['used water']=2
         s['efficiency']== 1
     elif s['filter_type']== 0:
         s['used water']=s['used water']*0.2
     return s
 


event_list = FutureEventList()

###################################################################

#simulation
time=1

m_V_RO1=[]
m_efficiency_RO1=[]
m_Mass_RO1=[]

#m_V_RO4=[]
#m_efficiency_RO4=[]
#m_Mass_RO4=[]
#m_V_GAC1=[]
#m_efficiency_GAC1=[]
#m_Mass_GAC1=[]
#m_V_GAC4=[]
#m_efficiency_GAC4=[]
#m_Mass_GAC4=[]
# =============================================================================
m_time=[]
#state = initial_stateGAC4()
#state = initial_stateGAC1()
#state = initial_stateRO4()
state = initial_stateRO1()

while time <= 360:
    if time ==28 or time ==29 or time ==30 or time ==87 or time ==88 or time ==89 or time ==100 or time ==101 or time ==102 or time ==103 or time ==104 or time ==105:
        schedule(Event(random.uniform(8.5,9.5), usedeventa), event_list)

#         schedule(Event(random.uniform(8.7,9.7), usedeventa), event_list)
#         schedule(Event(random.uniform(8.8,9.8), usedeventa), event_list)
#         schedule(Event(random.uniform(8.9,9.9), usedeventa), event_list)
#         schedule(Event(random.uniform(18.5,19.5), usedeventa), event_list)
#         schedule(Event(random.uniform(18.7,19.7), usedeventa), event_list)
#         schedule(Event(random.uniform(18.8,19.8), usedeventa), event_list)
        schedule(Event(random.uniform(18.9,19.9), usedeventa), event_list)
    elif time==55 or time ==188 or time ==189 or time ==200 or time ==201 or time ==202 or time ==203 or time ==204 or time ==205:
        schedule(Event(random.uniform(8.5,9.5), usedeventb), event_list)
#         schedule(Event(random.uniform(8.7,9.7), usedeventb), event_list)
#         schedule(Event(random.uniform(8.8,9.8), usedeventb), event_list)
#         schedule(Event(random.uniform(8.9,9.9), usedeventb), event_list)
#         schedule(Event(random.uniform(18.5,19.5), usedeventb), event_list)
#         schedule(Event(random.uniform(18.7,19.7), usedeventb), event_list)
#         schedule(Event(random.uniform(18.8,19.8), usedeventb), event_list)
        schedule(Event(random.uniform(18.9,19.9), usedeventb), event_list)
    elif time==31 or time==32 or time==33 or time==55 or time ==288 or time ==289 or time ==300 or time ==301 or time ==302 or time ==303 or time ==304 or time ==305: 
        schedule(Event(random.uniform(8.5,9.5), usedeventc), event_list)
#        schedule(Event(random.uniform(8.7,9.7), usedeventc), event_list)
#        schedule(Event(random.uniform(8.8,9.8), usedeventc), event_list)
#        schedule(Event(random.uniform(8.9,9.9), usedeventc), event_list)
#        schedule(Event(random.uniform(18.5,19.5), usedeventc), event_list)
#        schedule(Event(random.uniform(18.7,19.7), usedeventc), event_list)
#        schedule(Event(random.uniform(18.8,19.8), usedeventc), event_list)
        schedule(Event(random.uniform(18.9,19.9), usedeventc), event_list)
    elif time==150 or time==151 or time==152 or time==153 or time==154 or time ==155 or time ==156 or time ==157 or time ==158 or time ==159 or time ==160 or time ==161 or time ==162: 
#        schedule(Event(random.uniform(8.5,9.5), usedeventd), event_list)
#        schedule(Event(random.uniform(8.7,9.7), usedeventd), event_list)
#        schedule(Event(random.uniform(8.8,9.8), usedeventd), event_list)
        schedule(Event(random.uniform(8.9,9.9), usedeventd), event_list)
#        schedule(Event(random.uniform(18.5,19.5), usedeventd), event_list)
#        schedule(Event(random.uniform(18.7,19.7), usedeventd), event_list)
#        schedule(Event(random.uniform(18.8,19.8), usedeventd), event_list)
        schedule(Event(random.uniform(18.9,19.9), usedeventd), event_list)
    else:
        schedule(Event(random.uniform(8.5,9.5), used), event_list)
#        schedule(Event(random.uniform(8.7,9.7), used), event_list)
#        schedule(Event(random.uniform(8.8,9.8), used), event_list)
#        schedule(Event(random.uniform(8.9,9.9), used), event_list)
        schedule(Event(random.uniform(18.5,19.5), used), event_list)
#        schedule(Event(random.uniform(18.7,19.7), used), event_list)
#        schedule(Event(random.uniform(18.8,19.8), used), event_list)
#        schedule(Event(random.uniform(18.9,19.9), used), event_list)
    if time==30 or time==60 or time==90 or time==120 or time==150 or time==180 or time==210 or time==240 or time==270 or time==300 or time==330 or time==360:
        schedule(Event(23, changefilter), event_list)

    simulate(state, event_list)
    m_efficiency_RO1.append(state.get('efficiency'))
    m_V_RO1.append(state.get('used water'))
    m_Mass_RO1.append(state.get('Mass'))

#    m_efficiency_RO4.append(state.get('efficiency'))
#    m_V_RO4.append(state.get('used water'))
#    m_Mass_RO4.append(state.get('Mass'))

#    m_efficiency_GAC1.append(state.get('efficiency'))
#    m_V_GAC1.append(state.get('used water'))
#    m_Mass_GAC1.append(state.get('Mass'))

#    m_efficiency_GAC4.append(state.get('efficiency'))
#    m_V_GAC4.append(state.get('used water'))
#    m_Mass_GAC4.append(state.get('Mass'))
# =============================================================================
    time +=1
    m_time.append(time-1)
    
#m_Mass_RO1=np.cumsum(m_Mass_RO1)/1000
#m_Mass_GAC1=np.cumsum(m_Mass_GAC1)/1000
#m_Mass_RO4=np.cumsum(m_Mass_RO4)/1000
#plt.plot(m_time,m_Mass_RO1)
#plt.plot(m_time,m_efficiency_RO1)
#plt.plot(m_time,m_efficiency_GAC1)
# =============================================================================
# Plot graph for four cases
# m_Mass_GAC4=np.cumsum(m_Mass_GAC4)/1000
# 
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('Filter:GAC membrane, Family size:4')
# ax1.plot(m_time,m_efficiency_GAC4, color="chocolate",linestyle='dashed')
# ax1.set_xlabel('simulation time,day')
# ax1.set_ylabel('efficiency, 100%')
# ax2.plot(m_time ,m_Mass_GAC4,color="slategrey",linestyle='-')
# ax2.set_xlabel('simulation time,day')
# ax2.set_ylabel('Total lead treated, mg')
# ax2.plot(m_V, m_efficiency_RO4)
# ax2.plot(m_V, m_efficiency_GAC4)
# =============================================================================fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)



#plot safety level graph
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
# fig.set_figheight(12)
# fig.set_figwidth(4)
# fig.suptitle('Verification: volume of treated water vs. efficiency')
# ax1.scatter(m_V_RO1,m_efficiency_RO1,color='chocolate',s=1.5)
# ax1.set_title('RO membrane filter, family of 1')
# ax1.set_yticks(np.arange(0.5, 1.1, 0.1))
# ax2.scatter(m_V_RO4,m_efficiency_RO4,color='grey',s=1.5)
# ax2.set_title('RO membrane filter, family of 4')
# ax2.set_yticks(np.arange(0.5, 1.1, 0.1))
# ax3.scatter(m_V_GAC1,m_efficiency_GAC1,color='red',s=1.5)
# ax3.set_title('GAC activated carbon filter, family of 1')
# ax3.set_yticks(np.arange(0.5, 1.1, 0.1))
# ax4.scatter(m_V_GAC4,m_efficiency_GAC4,color='green',s=1.5)
# ax4.set_title('GAC activated carbon filter, family of 4')
# ax4.set_yticks(np.arange(0.3, 1.1, 0.1))
# ax4.set_xlabel('Volume of treated water,L')

def safetylevel(array):
    num=len(array)
    count=0
    for i in range(num):
        if array[i]<=0.6:
            count+=1
    safetylevel=1-count/num
    return safetylevel
    
    
    
    
    
    
    
    
    
    