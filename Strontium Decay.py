import LT.box as B
import scipy as sp
import numpy as np

file_name = 'SDRA [Strontium Decay].data'
f = B.get_file(file_name)

#Define Constants:
Ci_A = 3.7*10**10
pi = np.pi

#Define Parameters:

#Radius [Distance] away from the detector:
r =B.get_data(f, 'd')

#Number of Counts [unitless]:
C =B.get_data(f, 'C')

#Time interval for ~200 counts:
t = B.get_data(f, 't')

#Diameter of the electron Detector:
d = 0.01

#Count Rate:

C_t_total = C/t
C_br = 1
C_t= C_t_total-C_br

R= r/100
R2 = R**2

#Uncertainties in Values:
dD = 0.005
dC = np.sqrt(C)
dt = 0.5

#Uncertainty in C/t:

dC_t_dC = (1.0)*(1/t)
dC_t_dt = (-1.0)*C/t**2

X = dC_t_dC*dC
Y = dC_t_dt*dt

d_C_t = np.sqrt(X**2+Y**2)

#Plot Count Rate vs 1/R2

B.plot_exp(1/R2, C_t,d_C_t)
B.pl.show()

B.pl.title("C/T vs 1/R**2")
B.pl.xlabel("1/R**2 [1/m**2]")
B.pl.ylabel("C/T [Number of Counts/s]")

fit1 = B.linefit(1/R2,C_t)
B.plot_line(fit1.xpl, fit1.ypl)

#Calculating the Decay rate of Strontium:

m = 0.0112196589202
dm = 0.000608499676089

m1 = (Ci_A)*(d**2)/16

S_t = m/m1

dS_t_dm = 1/m1
Z = dS_t_dm*dm

dS_t = np.sqrt(Z**2)

print "---------------------------Strontium Decay-----------------------------"

print S_t ,"+/-", dS_t

print "-----------------------------------------------------------------------"













