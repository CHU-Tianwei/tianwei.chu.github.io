# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:51:20 2021

@author: Tianwei
"""

import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import integrate

#Fire parameters
Q = 1000  #HRR
D = 1.5 #Diameter of fuel pan
Hf = 0.235*(Q**0.4)-1.02*D   #flame height
Hfs = 0 #fuel surface height
xrad = 0.31  #radiation fraction
Dt = 2
Lt = 0

n = 200
i = 1
Qenergy = []
while i <= n:
    Ht = i/100
    Q_star = Q/Hf
    h = np.linspace(Hfs,Hfs+Hf,2000)
    h_star = (h-Hfs)/(Hf-Hfs)
    w = 1.55/(1+(h_star/0.625)**(20/3))
    St = ((Dt**2+Lt**2)+(Ht-h)**2)**0.5
    costheta = (((Dt**2+Lt**2)**0.5))/St
    qrad = xrad*w*Q_star*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qenergy.append(Qrad)
    i += 1
H = np.linspace(0,Hf,200) 
plt.plot(H,Qenergy,label='energy nonuniform')
plt.axis([np.min(H),np.max(H),0,np.max(Qenergy)]) 
plt.legend() 
plt.show() 

