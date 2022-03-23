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
list_Q = np.array([6000,6000,6000,4000,4000,4000,17000,17000,17000,12000,12000,12000,31000,31000,31000,23000,23000,23000],dtype=float)  #HRR
list_D = np.array([1.56,1.56,1.56,1.56,1.56,1.56,2.7,2.7,2.7,2.7,2.7,2.7,3.83,3.83,3.83,3.83,3.83,3.83],dtype=float) #Diameter of fuel pan
list_Hfs = np.array([1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.7,1.5,1.5,1.5,1.5,1.5,1.5],dtype=float) #fuel surface height

xrad = 0.31  #radiation fraction

#Probe position
list_Dt = np.array([2,4,6,2,4,6,3,6,9,3,6,9,4,8,12,4,8,12]) #Target distance
Ht = 1  #Target height

#both nonuniform
Qsum = []
for Q,D,Hfs,Dt in zip(list_Q,list_D,list_Hfs,list_Dt):
    Hf = 0.235*(Q**0.4)-1.02*D   #flame height
    Q_ave = Q/Hf
    h = np.linspace(0,Hf,2000)
    h_star = h/Hf
    w = 1.55/(1+(h_star/0.625)**(20/3))
    r_star = 1-2.5*h_star+3.5*(h_star**2)-2*(h_star**3)
    rf = r_star*D/2
    St = ((Dt-rf)**2+(Ht-h-Hfs)**2)**0.5
    costheta = (Dt-rf)/St
    qrad = xrad*w*Q_ave*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qsum.append(Qrad)
print(Qsum)


