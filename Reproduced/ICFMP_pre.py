# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:01:43 2021

@author: Tianwei
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:36:26 2021

@author: Tianwei
"""

import numpy as np
# =============================================================================
# import math
# from scipy import integrate
# from matplotlib import pyplot as plt
# 
# =============================================================================

#Fire parameters
list_Q = np.array([1190,1190,1200],dtype=float)   #HRR
list_Hfs = np.array([0.1,0.1,0.1],dtype=float)   #火焰表面高度
list_D = np.array([1.13,1.13,1.13],dtype=float)   #油池直径
xrad = 0.31  #辐射系数

#Probe position
# =============================================================================
# Dt = 2.33  #Target distance
# Ht = 2.54  #Target height
# =============================================================================
Dt = 3.38  #Target distance
Ht = 1.75  #Target height 

#both nonuniform
Qsum = []
for Q,D,Hfs in zip(list_Q,list_D,list_Hfs):
    Hf = 0.235*(Q**0.4)-1.02*D   #flame height
    Q_ave = Q/Hf
    h = np.linspace(0,Hf,2000)
    h_star = h/Hf
    w = 1.55/(1+(h_star/0.625)**(20/3))
    r_star = 1-3.5*h_star+5.5*(h_star**2)-3*(h_star**3)
    rf = r_star*D/2
    St = ((Dt-rf)**2+(Ht-h-Hfs)**2)**0.5
    costheta = (Dt-rf)/St
    qrad = xrad*w*Q_ave*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qsum.append(Qrad)
print(Qsum)
