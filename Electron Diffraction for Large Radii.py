import numpy as np
import scipy as sp
import LT.box as B

#Define Constants:
pi = np.pi
n = 1
rad_deg = 180/pi

R = 0.0625
dR = 0.00005

L = 0.137
dL = 0.0005

l1 = L-R
dl1 = np.sqrt(dR**2+dL**2)

#Start Program:

#file_name = 'Large Radii Photshop.data'
file_name = 'Large Radii.data'

f = B.get_file(file_name)

kV = B.get_data(f, 'V')
dkV = 0.005

D2_cm = B.get_data(f,'D2')
dD2_cm = 0.05

V = kV*10**3
dV = dkV*10**3

D2 = D2_cm/10**2
dD2 = dD2_cm/10**2

#Wavelength

wave1 = 1.228/(np.sqrt(V))
wave = wave1/10**9

dwave1_dV = -0.644/((V)**(3.0/2.0))
X = dwave1_dV*dV

dwave1 = np.sqrt(X**2)

dwave = dwave1/10**9

#l2

l2 = np.sqrt(R**2-(D2/2)**2)

dl2_dR = R/np.sqrt(((R)**2-(D2/2)**2))
dl2_dD1 = D2/4*np.sqrt(((R)**2-(D2/2)**2))

Y = dl2_dR*dR
Z = dl2_dD1*dD2

dl2 = np.sqrt(Y**2+Z**2)

#New Parameter: L_star

L_star= l1 + l2

d_L_star = np.sqrt(dl1**2+dl2**2)

#Two Theta:

tan_2theta = (D2/2)/L_star

A = (D2/2)/L_star

two_theta = np.arctan(A)
two_theta_deg = two_theta*rad_deg

#Uncertainty in 2Theta

b = (1/A**2 + 1)

dtwo_theta_dD1 = b/2*L_star
dtwo_theta_dL_star = ((-1)*b*D2)/(2*L_star)**2

C = dtwo_theta_dD1*dD2
D = dtwo_theta_dL_star*d_L_star

dtwo_theta = np.sqrt(C**2+D**2)

dtwo_theta_deg = dtwo_theta*rad_deg

#Theta

theta = two_theta/2
theta_deg = two_theta_deg/2

d_theta = dtwo_theta/2
d_theta_deg = dtwo_theta_deg/2

#Sin Theta

sin_theta = np.sin(theta)

dsin_theta_d_theta = np.cos(theta)

E = dsin_theta_d_theta*d_theta

d_sin_theta = np.sqrt(E**2)

#Finding Distance 2:

n_wave = (n*wave)
dn_wave = (n*dwave)

B.plot_exp(n_wave,sin_theta,d_sin_theta)
B.pl.show()

m = 3287168426.69
dm = 151269904.806

fit1 = B.linefit(n_wave,sin_theta)
B.plot_line(fit1.xpl, fit1.ypl)

B.pl.title("sin(theta) vs n*lambda [Large Diameter]")
B.pl.xlabel("n*lambda [m]")
B.pl.ylabel("sin(theta) [unitless]")

d2 =1/(2*m)

d_d2_dm = -1/(2*(m)**2)

F = d_d2_dm*dm

d_d2 = np.sqrt(F**2)

print d2, '+/-', d_d2

#Distance s [s]:

s = d2/(1+np.sin(pi/6))
ds = d_d2/(np.sin(pi/6))

print s, '+/-', ds

#Weighted mean for d2

d2_1 = (n_wave)/(2*sin_theta)
#print d2_1

dd2_1_dwave = n/(2*sin_theta)
dd2_1_dsin_theta = ((-1.0)*n_wave*np.cos(theta))/2*((np.sin(theta)**2))

G = dd2_1_dwave*dwave
H = dd2_1_dsin_theta*d_sin_theta

dd2_1 = np.sqrt(G**2+H**2)

#print d2_1, '+/-', dd2_1

one_over_d_2 = d2_1/(dd2_1**2)
one_over_dd_2 = 1/(dd2_1**2)

S_one_over_d_2 = sum(one_over_d_2)
S_one_over_dd_2 = sum(one_over_dd_2)

WM_one_over_d_2 = S_one_over_d_2/S_one_over_dd_2
WM_one_over_dd_2 = np.sqrt(1/S_one_over_dd_2)

print WM_one_over_d_2, '+/-', WM_one_over_dd_2

#Weighted mean for s:

s_1 = d2_1/(1 + np.sin(pi/6))

#print s_1

d_s_1_d1_1 = 1/(1 + np.sin(pi/6))

I = d_s_1_d1_1*dd2_1

ds_1 = np.sqrt(I**2)

one_over_s_1 = s_1/(ds_1**2)
one_over_ds_1 = 1/(ds_1**2)

S_one_over_s_1 = sum(one_over_s_1)
S_one_over_ds_1 = sum(one_over_ds_1)

WM_one_over_s_1 = S_one_over_s_1/S_one_over_ds_1
WM_one_over_ds_1 = np.sqrt(1/S_one_over_ds_1)

print WM_one_over_s_1, '+/-', WM_one_over_ds_1

