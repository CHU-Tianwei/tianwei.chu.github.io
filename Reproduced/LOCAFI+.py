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
list_Q = np.array([503,503,515,515,468,468,442,442,493,493,563,563,575,575,511,607,607,512,512,496,496,468,468,490,472,472,500,
                   500,500,500,500,500,500,500,3000,3000],dtype=float)  #HRR
list_D = np.array([0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,
                   0.7,0.7,0.7,0.7,0.7,0.7,0.7,1.6,1.6],dtype=float)  #Diameter of fuel pan
Hfs = 0 #fuel surface height
xrad = 0.31  #radiation fraction

#Probe position
list_Dt = np.array([1,1,0.5,0.5,1,1,0.5,0.5,1.5,1.5,1,1,0.5,0.5,1.5,1.5,1.5,0.5,0.5,1,1,0.5,0.5,1.5,0.5,0.5,0.5,0.5,1,1,1.5,1.5,
                    1.5,1.5,1.5,1.5],dtype=float) #Target distance
list_Lt = np.array([0,0,0,0,0,0,0,0,0.5,0.5,0,0,0,0,0.5,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0.5,0.5,1,1,0,0],dtype=float) #Target distance
list_Ht = np.array([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2],dtype=float) #Target height

#both nonuniform
Qsum = []
for Q,D,Dt,Lt,Ht in zip(list_Q,list_D,list_Dt,list_Lt,list_Ht):
    Hf = 0.235*(Q**0.4)-1.02*D   #flame height
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


