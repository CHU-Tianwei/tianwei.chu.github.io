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
Q = 390  #HRR
D = 1 #Diameter of fuel pan
Hf = 0.235*(Q**0.4)-1.02*D   #flame height
Hfs = 0 #fuel surface height
xrad = 0.31  #radiation fraction
Dt = 2
Lt = 0
h = np.linspace(Hfs,Hfs+Hf,2000)
h_star = (h-Hfs)/(Hf-Hfs)
def w(h_star):
    
    return np.piecewise(h_star, [h_star >= 0.34549, h_star < 0.34549], [lambda h_star: -30.85*h_star**4 + 103.4*h_star**3 - 119.4*h_star**2 + 52.67*h_star - 5.78,
                                                                        lambda h_star: -931.6*h_star**4 + 717.6*h_star**3 - 172.2*h_star**2 + 16.78*h_star + 0.4442])
w = w(h_star)

n = 200
i = 1
Qboth = []
while i <= n:
    Ht = i/100
    Q_star = Q/Hf
    r_star = 1-2.8*h_star+3.7*(h_star**2)-1.9*(h_star**3)
    rf = r_star*D/2
    St = ((((Dt**2+Lt**2)**0.5)-rf)**2+(Ht-h)**2)**0.5
    costheta = (((Dt**2+Lt**2)**0.5)-rf)/St
    qrad = xrad*w*Q_star*costheta/(4*np.pi*St**2)
    dh = h[1]-h[0]
    Qrad = np.sum(qrad*dh)
    Qboth.append(Qrad)
    i += 1
H = np.linspace(0,Hf,200) 
plt.plot(H,Qboth,label='formal both nonuniform(D=2m)')
plt.axis([np.min(H),np.max(H),0,np.max(Qboth)]) 
plt.legend() 
plt.show() 

