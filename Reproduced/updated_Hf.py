# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:02:35 2021

@author: Tianwei
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:36:26 2021

@author: Tianwei
"""

import numpy as np
import math
from scipy import integrate
from matplotlib import pyplot as plt

#火源参数
list_Q = np.array([486.7628142,503.678504,568.062841,918.0351863,926.6678773,908.7726923,914.048679,881.4271765,910.6375419,993.0606807,1974.878798,1969.008146,
              1936.25933,1884.740858,1795.795808,1777.560474,1761.623288,3482.441739,3905.152646],dtype=float)   #HRR
print('Q is :\n',list_Q)
list_Lf = np.array([2.06313182,2.101480678,2.240769758,2.694971714,2.7084468,2.680428724,2.688723364,2.636967583,2.68336384,2.809651334,3.68725258,3.681443979,
               3.648849074,3.59689626,3.505156967,3.486013991,3.469186829,4.491719073,4.778869274],dtype=float)   #火焰高度
print('Lf is :\n',list_Lf)
list_Fh = np.array([0.2,0.2,0.2,0.21,0.21,0.21,0.21,0.21,0.21,0.21,0.44,0.44,0.44,0.44,0.44,0.44,0.44,0.25,0.25],dtype=float)   #火焰表面高度
list_FD = np.array([0.71,0.71,0.71,0.88,0.88,0.88,0.88,0.88,0.88,0.88,1.17,1.17,1.17,1.17,1.17,1.17,1.17,1.6,1.6],dtype=float)   #油池直径
xrad = 0.35  #辐射系数

#测点参数
H1 =1.35
H2 =3
S = 0  #heat flux gauge距离火源轴线在墙面投影的水平距离
D = 1.5  #火源中心与墙体的距离
D2 = (D**2)+(S**2)
D_dot = D2**0.5

#isotropic
Q01 = []
Q02 = []
for Q,Lf,Fh in zip(list_Q,list_Lf,list_Fh):
    Q_star = Q/Lf    #单位长度的平均HRR
    L = np.linspace(Fh,Lf+Fh,2000)
    qrad01 = xrad*Q_star*(D2**0.5)/(4*np.pi*(D2+(H1-L)**2)**1.5)
    qrad02 = xrad*Q_star*(D2**0.5)/(4*np.pi*(D2+(H2-L)**2)**1.5)
    dL = L[1]-L[0]
    Qrad01 = np.sum(qrad01*dL)
    Qrad02 = np.sum(qrad02*dL)
    Q01.append(Qrad01)
    Q02.append(Qrad02)
print(Q01)
print(Q02)

#nonuniform energy
Q11 = []
Q12 = []
for Q,Lf,Fh in zip(list_Q,list_Lf,list_Fh):
    Q_star = Q/Lf
    L = np.linspace(Fh,Lf+Fh,2000)
    L_star = (L-Fh)/Lf
    def w(L_star):

        return np.piecewise(L_star, [L_star >= 0.34549, L_star < 0.34549], [lambda L_star: -30.85*L_star**4 + 103.4*L_star**3 - 119.4*L_star**2 + 52.67*L_star - 5.78, 
                                                                            lambda L_star: -931.6*L_star**4 + 717.6*L_star**3 - 172.2*L_star**2 + 16.78*L_star + 0.4442])
    w = w(L_star)
    qrad11 = xrad*w*Q_star*(D2**0.5)/(4*np.pi*(D2+(H1-L)**2)**1.5)
    qrad12 = xrad*w*Q_star*(D2**0.5)/(4*np.pi*(D2+(H2-L)**2)**1.5)
    dL = L[1]-L[0]
    Qrad11 = np.sum(qrad11*dL)
    Qrad12 = np.sum(qrad12*dL)
    Q11.append(Qrad11)
    Q12.append(Qrad12)
print(Q11)
print(Q12)

#nonuniform diameter
Q21 = []
Q22 = []
for Q,Lf,Fh,FD in zip(list_Q,list_Lf,list_Fh,list_FD):
    Q_star = Q/Lf
    L = np.linspace(Fh,Lf+Fh,2000)
    L_star = (L-Fh)/Lf
    A = 0.659*L_star**2 - 1.659*L_star + 1
    D1 = D_dot-A*FD/2
    qrad21 = xrad*Q_star*(D1)/(4*np.pi*(D1**2+(H1-L)**2)**1.5)
    qrad22 = xrad*Q_star*(D1)/(4*np.pi*(D1**2+(H2-L)**2)**1.5)
    dL = L[1]-L[0]
    Qrad21 = np.sum(qrad21*dL)
    Qrad22 = np.sum(qrad22*dL)
    Q21.append(Qrad21)
    Q22.append(Qrad22)
print(Q21)
print(Q22)

#both nonuniform
Q31 = []
Q32 = []
for Q,Lf,Fh,FD in zip(list_Q,list_Lf,list_Fh,list_FD):
    Q_star = Q/Lf
    L = np.linspace(Fh,Lf+Fh,2000)
    L_star = (L-Fh)/Lf
    def w(L_star):
        return np.piecewise(L_star, [L_star >= 0.34549, L_star < 0.34549], [lambda L_star: -30.85*L_star**4 + 103.4*L_star**3 - 119.4*L_star**2 + 52.67*L_star - 5.78, 
                                                                             lambda L_star: -931.6*L_star**4 + 717.6*L_star**3 - 172.2*L_star**2 + 16.78*L_star + 0.4442])
    w = w(L_star)
    A = 0.659*L_star**2 - 1.659*L_star + 1
    D1 = D_dot-A*FD/2
    qrad31 = xrad*w*Q_star*(D1)/(4*np.pi*(D1**2+(H1-L)**2)**1.5)
    qrad32 = xrad*w*Q_star*(D1)/(4*np.pi*(D1**2+(H2-L)**2)**1.5)
    dL = L[1]-L[0]
    Qrad31 = np.sum(qrad31*dL)
    Qrad32 = np.sum(qrad32*dL)
    Q31.append(Qrad31)
    Q32.append(Qrad32)
print(Q31)
print(Q32)

