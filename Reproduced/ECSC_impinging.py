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
list_Q = np.array([3482.441739,3905.152646],dtype=float)  #HRR
list_D = np.array([1.6,1.6],dtype=float) #Diameter of fuel pan
list_Hfs = np.array([0.25,0.25],dtype=float) #fuel surface height

xrad = 0.31  #radiation fraction

#Probe position
Dt = 1.5   #Target distance
Ht = 3     #Target height

#both nonuniform
Qsum = []
for Q,D,Hfs in zip(list_Q,list_D,list_Hfs):
    Hf = 0.235*(Q**0.4)-1.02*D   #flame height
    Q_ave = Q/4.75
    h = np.linspace(0,4.75,2000)
    h_star = h/4.75
    w = 1.55/(1+(h_star/0.625)**(20/3))
    r_star = 1-1.3*h_star-2*(h_star**2)+3.5*(h_star**3)
    rf = r_star*D/2
    St = ((Dt-rf)**2+(Ht-h-Hfs)**2)**0.5
    costheta = (Dt-rf)/St
    qrad = xrad*w*Q_ave*costheta/(4*np.pi*(St**2))
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qsum.append(Qrad)
print(Qsum)
     

