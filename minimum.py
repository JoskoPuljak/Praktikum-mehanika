import math as mt
import csv
import matplotlib.pyplot as plt
import numpy as np
def method_newtonraphson(f,x0,h,epsilon):
    xn=x0
    while abs(f(xn))>epsilon:
        derivacija=(f(xn+h)-f(xn-h))/(2*h)
        xn=xn-f(xn)/derivacija
    return xn, abs(f(xn))

def f1(U):
    Iks=0.0035+0.0003*(np.exp(4.404))*((60/100)**(-1.903))
    return Iks+0.0014-U*0.0014*np.exp(2.008*U)*(1+2.008*U)
def f2(U):    
    Iks=0.0035+0.0003*(np.exp(4.404))*((75/100)**(-1.903))
    return Iks+0.001-0.001*np.exp(2.096*U)*(1+2.096*U)
def f3(U):
    Iks=0.0035+0.0003*(np.exp(4.404))*((90/100)**(-1.903))
    return Iks+0.0008-0.0008*np.exp(2.193*U)*(1+2.193*U)

U1, f1_U1=method_newtonraphson(f1,0.5,0.00001,0.000001)
print("U1=",U1)
def P1(U):
    Iks=0.0035+0.0003*(np.exp(4.404))*((60/100)**(-1.903))
    return U*Iks-U*0.0014*(np.exp(2.008*U)-1)
print("P(U1)=",P1(U1))
U2, f2_U2=method_newtonraphson(f2,0.5,0.00001,0.000001)
print("U2=",U2)
def P2(U):
    Iks=0.0035+0.0003*(np.exp(4.404))*((75/100)**(-1.903))
    return U*Iks-U*0.001*(np.exp(2.096*U)-1)
print("P(U2)=",P2(U2))
U3, f3_U3=method_newtonraphson(f3,0.5,0.00001,0.000001)
print("U3=",U3)
def P3(U):
    Iks=0.0035+0.0003*(np.exp(4.404))*((90/100)**(-1.903))
    return U*Iks-U*0.0008*(np.exp(2.193*U)-1)
print("P(U3)=",P3(U3))

Pin1=0.005*(np.exp(4.404))*((60/100)**(-1.903))
Pin2=0.005*(np.exp(4.404))*((75/100)**(-1.903))
Pin3=0.005*(np.exp(4.404))*((90/100)**(-1.903))
print("Pin1=",Pin1)
print("Pin2=",Pin2)
print("Pin3=",Pin3)
print(P1(U1)/Pin1)
print(P2(U2)/Pin2)
print(P3(U3)/Pin3)
