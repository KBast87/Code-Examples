import numpy as np
import LT.box as B
import LT_Fit.parameters as P
import LT_Fit.gen_fit as G

#Start Program:

f = B.get_file('Double Slit Interference.data')
D = B.get_data(f,'x') #micro
Vn = B.get_data(f,'V') #v

dV = 0.0005
V = Vn - 0.007
dVn = (1/1.836)*dV

#B.plot_exp(D,V,dV)

#B.pl.title('Voltage [V] vs Position [mm] [Double Slit]')
#B.pl.xlabel('Position [mm]')
#B.pl.ylabel('Voltage [V]')

#Constants:

DS = 0.50 #m
DConv = D *1e-3 #m
DC = 4.45 * 1e-3 # meters

#Theta:

theta1 = (np.arctan(DConv/DS)) #rad
thetaC = (np.arctan(DC/DS)) # radians

theta = theta1 - thetaC
Vn = (V - V.min()) / (V.max() - V.min())

#Define wavenumber - k:

Ix = theta
Iy = Vn
lam = 670.e-9
k = 2.*np.pi/lam

#Define Intensity Function:

S = P.Parameter(0.4e-3,'S') #slit separation
I0 = P.Parameter(1.,'I0') #maximum intensity
D = P.Parameter(0.15e-3,'D') #slit width
x = DConv
x0 = P.Parameter(DC,'x0') 

def I(x):
    th = ((x-x0())/DS) + 1.e-10
    A1 = k*D()*np.sin(th)/2.
    A2 = k*S()*np.sin(th)/2.
    Atot = (np.sin(A1)*np.cos(A2))/A1
    intensity = I0()*Atot**2.
    return intensity

fit = G.genfit(I, [D,S,I0,x0], x, y=Vn)
B.plot_exp(x,Vn,dVn)
B.plot_line(x,I(x))

B.pl.show()

B.pl.title('Relative Intensity [V] vs Viewing Angle [rad]')
B.pl.xlabel('Viewing Angle [rad]')
B.pl.ylabel('Intensity [V]')