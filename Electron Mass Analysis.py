import LT.box as B
import numpy as np
import scipy as sp

#Start Program:

file_name = 'Energy and Theta.data'
f = B.get_file(file_name)

E_f = B.get_data(f,'E')
dE_f = B.get_data(f,'dE')
theta = B.get_data(f,'theta')
dtheta = B.get_data(f,'dtheta')

E_0 = 0.6617
dE_0 = 0.00005

c = 3.00*10**8
c_2 = c**2

E_yplot = (E_0/E_f) 
cos_xplot = 1-np.cos(theta)

#Uncertainty in the Y Plots:
dE_yplot_dE_0 = 1/E_f
dE_yplot_dE_f = (-1.0)*E_0/(E_f)**2

A = dE_yplot_dE_0*dE_0
b = dE_yplot_dE_f*dE_f

dE_yplot = np.sqrt(A**2 + b**2)

#Uncertainty in the X plots:
dcos_xplot_dtheta = np.sin(theta)
dcos_xplot = np.sin(theta)*dtheta

#print E_yplot, "+/-", dE_yplot
print cos_xplot, "+/-", dcos_xplot

#Plotting:

B.plot_exp(cos_xplot,E_yplot, dE_yplot)
B.pl.show()

l1 = B.linefit(cos_xplot,E_yplot)
B.plot_line(l1.xpl,l1.ypl)

B.pl.title("E0/Ef [MeV] vs 1 - cos(theta) [unitless]")
B.pl.xlabel("1 - cos(theta) [Unitless]")
B.pl.ylabel("E0/Ef [MeV]")

m = 1.57399988411
dm = 0.0403792823858

#Electron Mass:

e_mass_exp = (E_0)/m

d_e_mass_exp_dE_0 = 1/m
d_e_mass_exp_dm = -E_0/m**2

C = d_e_mass_exp_dE_0*dE_0
D = d_e_mass_exp_dm*dm

d_e_mass = np.sqrt(C**2 + D**2)

print "------------------------------------------------------------------------"
print "The experimental value for the mass of an electron is:"
print e_mass_exp, '+/-', d_e_mass, "[MeV/c^2]"
print "------------------------------------------------------------------------"
print "The percent difference between the theoretical value and the experimental value is:"
print "19.54%"
print "------------------------------------------------------------------------"


