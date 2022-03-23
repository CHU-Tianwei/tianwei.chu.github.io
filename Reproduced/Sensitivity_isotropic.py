# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:39:48 2021

@author: Tianwei
"""
import numpy as np
import math
from scipy import integrate
from matplotlib import pyplot as plt

#Fire parameters
Q = 500 #HRR
D = 1 #Diameter of fuel pan
Hf = 0.235*(Q**0.4)-1.02*D   #flame height
Hfs = 0 #fuel surface height
xrad = 0.31  #radiation fraction
Dt = 2
Lt = 0

n = 300
i = 1
Qiso = []
while i <= n:
    Ht = i/100
    Q_star = Q/Hf
    h = np.linspace(Hfs,Hfs+Hf,2000)
    St = (Dt**2+Lt**2+(Ht-h)**2)**0.5
    costheta = (((Dt**2+Lt**2)**0.5))/St
    qrad = xrad*Q_star*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qiso.append(Qrad)
    i += 1
H = np.linspace(0,3,300)
plt.plot(H,Qiso,label='isotropic')
plt.axis([np.min(H),np.max(H),0,np.max(Qiso)]) 
plt.legend() 
plt.show()
