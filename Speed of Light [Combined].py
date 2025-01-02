import LT.box as B
import numpy as np
import scipy as sp

#Define Constants:

pi = np.pi
c_theoretical = 3.00 * 10*8

file_name = "Delta_x vs Frequency [Combined].data"
f = B.get_file(file_name)

delta_x = B.get_data(f, 'x')

x = delta_x/1000
d_x = 0.00001

disp1 = (0.00398+0.00390)/2

disp = x - disp1
d_disp = d_x

freq = B.get_data(f, 'fr')
d_freq = 5

ang_freq = 2*np.pi*freq
d_ang_freq = 2*np.pi*d_freq

D1= f.par.get_value('D1')
D2 = f.par.get_value('D2')
f2 = f.par.get_value('f2')

d_D1 = 0.5
d_D2 = d_D1
d_f2 = 0.003

L = D1 + D2
dL = np.sqrt((d_D1**2)+(d_D2**2))

#Plot Delta-X vs Angular Frequency

B.plot_exp(ang_freq, disp,d_disp)
B.pl.show()

B.pl.title("Delta X vs Angular Frequency")
B.pl.xlabel("Angular Frequency [rad/s]")
B.pl.ylabel("Displacement [m]")

fit1 = B.linefit(ang_freq,disp)
B.plot_line(fit1.xpl, fit1.ypl)

#Uncertainty Calculations:

m =  5.28185346038e-8
dm = 1.49969038195e-9

c_exp = (4*f2*(D1+D2))/m

#Uncertainty Calculations:

dc_df2 = (4*L)/m
dc_dL = 4*f2/m
dc_dm = -1*(4*f2*L)/m**2

X = dc_df2*d_f2
Y = dc_dL*dL
Z = dc_dm*dm

d_c = np.sqrt(X**2+Y**2+Z**2)

print "-----------------------Speed of Light Values----------------------------"
print c_exp/10**8 ,"+/-", d_c/10**8
print "------------------------------------------------------------------------"

#Uncertainty Ratio:

c_exp_per = (d_c/c_exp)*100

print "-----------------------Speed of Light Uncertainty Ratio-----------------"
print c_exp_per 
print "------------------------------------------------------------------------"

#Weighted c value calculation:

c_exp_2 = (4*ang_freq*f2*L)/disp
#print c_exp_2

dc2_dx = (-1.0*f2*4*ang_freq*L)/disp**2
dc2_df2 = (4*ang_freq*L)/disp 
dc2_dw = (4*L*f2)/disp
dc2_dL = (4*f2*ang_freq)/disp

A = dc2_dx*d_x
b = dc2_df2*d_f2
C = dc2_dw*d_ang_freq
D = dc2_dL*dL

d_c_exp_2 = np.sqrt(A**2+b**2+C**2+D**2)
#print d_c_exp_2

#Weighted Mean

c_exp_2_d_c_exp_2= (c_exp_2/(d_c_exp_2**2))
S_c_exp_2_d_c_exp_2= sum(c_exp_2_d_c_exp_2)

one_over_d_c_exp_2 = 1.0/(d_c_exp_2**2)
S_one_over_d_c_exp_2= sum(one_over_d_c_exp_2)

WM_c_exp_2= S_c_exp_2_d_c_exp_2/S_one_over_d_c_exp_2
WM_d_c_exp_2= np.sqrt(1/S_one_over_d_c_exp_2)

print "-------------------------Weighted c Values------------------------------"
print (WM_c_exp_2/10**8),"+/-", (WM_d_c_exp_2/10**8)
print "------------------------------------------------------------------------"



