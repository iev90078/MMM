import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin


def f(x):
    return np.tan(x)

def df(x):
    return np.cos(x)**(-2)

def fch(x):
    global h
    return (f(x+h)-f(x-h))/(2*h)

def d2f(x):
    return 2*(cos(x)**(-3))*sin(x)
print("!!!")

h=0.0000001

""" 
x=np.arange(-1.5, 1.5, h)
print("!!!")

y=f(x)
print("!!!")
plt.plot(x, y)
print("!!!")
plt.show()


dy=df(x)
plt.plot(x, dy)
plt.show()

ych=fch(x)
plt.plot(x, ych)
plt.show()

plt.plot(x, abs(dy-ych))
plt.show()

print("!!!")

"""
e_mash=2**-53
a=1
e=np.linspace(a-h, a+h, 10000000)
Ml=max(d2f(e))
Mo=max(f(e))

h_opt=2*(Mo*e_mash/Ml)**0.5

print(h_opt)


E=[]
h_mass=np.arange(h_opt/10, 10*h_opt, h_opt/1000)
for h in h_mass:
    e=np.linspace(a-h, a+h, 10000)
    Ml=max(d2f(e))
    Mo=max(f(e))
    err_met=Ml*h/2
    err_round=(Mo*2)*e_mash/h
    #err_min=2*(Mo*Ml*e_mash)**0.5
    E+=[err_met+err_round]
    #E+=[err_min]


plt.plot(h_mass, np.array(E))
#plt.plot(h_opt, )
plt.show()
print(min(E), h_opt, abs(min(E)-h_opt))