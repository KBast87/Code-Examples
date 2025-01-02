import LT.box as B
import numpy as np
import scipy as sp
import LT.plotting as P

c = 299792458
q = 1.6021765/10**19

file_name = "Planck's Constant.data"

f = B.get_file(file_name)
V = B.get_data(f,'V')
dV = B.get_data(f, 'dV')

q_V = q*V
q_dV = q*dV

lamba = B.get_data(f,'lamba')
lamba_m = lamba/10**9
freq = c/lamba_m

#Plotting:

print "------------------------------------------------------------------------"
B.plot_exp(freq,q_V,q_dV)
B.pl.show()
print "------------------------------------------------------------------------"

B.pl.title("Kinetic Energy [Joules] vs Frequency [Hz]")
B.pl.xlabel("Frequency [Hz]")
B.pl.ylabel("Kinetic Energy [Joules]")
#Fitting Line:

l1 = B.linefit(freq,q_V)
print "------------------------------------------------------------------------"
B.plot_line(l1.xpl,l1.ypl)
print "------------------------------------------------------------------------"

print "------------------------------------------------------------------------------"
print "The Value of Planck's Constant is 5.90015616416e-34  +/-  1.94889898016e-35"
print "------------------------------------------------------------------------------"

print "------------------------------------------------------------------------------"
print "The Value of the Work Function is 2.07813609912e-19  +/-  1.31195549898e-20"
print "------------------------------------------------------------------------------"

h = 5.90015616416e-34
dh = 1.94889898016e-35
phi = 2.07813609912e-19
d_phi = 1.31195549898e-20 

#Minimum Photon Energy:

min_eng = phi/h

d_min_eng_dh = -phi/(h**2)
d_min_eng_d_phi = 1/h

A = d_min_eng_dh*dh
b = d_min_eng_d_phi*d_phi

d_min_eng = np.sqrt(A**2+b**2)

print "------------------------------------------------------------------------"
print min_eng ,"+/-", d_min_eng
print "------------------------------------------------------------------------"