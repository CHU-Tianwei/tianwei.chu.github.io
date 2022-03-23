# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:16:19 2021

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
list_Q = np.array([87,141,87,121,373,372,776,750,752,769,776,1272,1281,1229,1236,1901,1911,1858,1871],dtype=float)  #HRR
list_D = np.array([0.6,0.6,0.6,0.6,1,1,1.4,1.4,1.4,1.4,1.4,1.8,1.8,1.8,1.8,2.2,2.2,2.2,2.2],dtype=float) #Diameter of fuel pan

Hfs = 0 #fuel surface height
xrad = 0.35  #radiation fraction

#Probe position
Dt = 3.75   #Target distance
Ht = 1.86   #Target height

#both nonuniform
Qsum = []
for Q,D in zip(list_Q,list_D):
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


