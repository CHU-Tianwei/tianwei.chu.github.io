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
# =============================================================================

#Fire parameters
Q = 4446.39 #HRR
D = 0.8 #Diameter of fuel pan
Hf = 0.235*(Q**0.4)-1.02*D   #flame height
Hfs = 0.2 #fuel surface height
xrad = 0.31  #radiation fraction

#Probe position
list_Dt = np.array([1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,
                    8.5,8.5,8.5,8.5,1.5,1.5,1.5,1.5],dtype=float)   #Target Distance from the flame axis
list_Lt = np.array([3,3,3,3,3,3,3,3,2.5,3.5,2,4,1.5,4.5,2.5,3.5,2,4,1.5,4.5,0.6,0.6,0.1,0.1,0.6,0.6,
                    0.1,0.1],dtype=float)   #Target horizontal length
list_Ht = np.array([1.35,3,1.8,2.2,2.6,3.5,4,4.5,1.35,1.35,1.35,1.35,1.35,1.35,3,3,3,3,3,3,1.35,3,1.35,
                    3,1.35,3,1.35,3,],dtype=float)   #Target height

#both nonuniform
Qsum = []
for Dt,Lt,Ht in zip(list_Dt,list_Lt,list_Ht):
    Q_ave = Q/Hf
    h = np.linspace(0,Hf,2000)
    h_star = h/Hf
    w = 1.55/(1+(h_star/0.625)**(20/3))
    r_star = 1-3.5*h_star+5.5*(h_star**2)-3*(h_star**3)
    rf = r_star*D/2
    St = ((((Dt**2+Lt**2)**0.5)-rf)**2+(Ht-h-Hfs)**2)**0.5
    costheta = (((Dt**2+Lt**2)**0.5)-rf)/St
    qrad = xrad*w*Q_ave*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qsum.append(Qrad)
print(Qsum)


