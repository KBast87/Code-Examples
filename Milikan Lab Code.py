import numpy as np
import LT.box as B
import matplotlib.pyplot as plt

#Constants:

pm = "+/-"
V = 500
dV = 5
d = 0.05
n = 1.84e-5
p = 880
p_press = 1.0345E+05

g = 9.79
e_theory = 1.609e-19
pi = np.pi 

E = V/d
b = 8.2000E-03
b_2p = 3.9631e-8
visc_const = 9.6109e-9

#Part A: Monte Carlo 

rand_factor = 0.1

e_count = [1,7,4,5,5,5,2,4,1,1,3]

rise_time = [14.85,0.96,1.26,0.99,1.15,3.29,1.08,5.15,5.71,1.58]

fall_time = [10.45,10.45,16.45,16.45,13.42,13.42,20.32,20.32,18.42,18.43]

rise_v = [0.000033666, 0.0005227, 0.00039733, 0.00050426, 0.00043550, 0.00015185, 0.0001585, 0.00046253, 0.000097178, 0.00008751, 0.00031680]

fall_v = [0.000047847, 0.000047847, 0.00003039, 0.00003039, 0.00003725, 0.00003725, 0.00002460, 0.00002460, 0.00002713, 0.00002713]

a = [0.0000063965, 0.0000063965, 0.0000050231, 0.0000050231, 0.0000056008, 0.0000056008, 0.0000044828, 0.0000044828, 0.0000047253, 0.0000047253]

e_count = [1,7,4,5,5,2,4,1,1,3]

np_e_count = np.array(e_count)

np_rise_time= np.array(rise_time)
np_fall_time = np.array(fall_time)
np_rise_v = np.array(rise_v)
np_fall_v = np.array(fall_v)
np_a = np.array(a)

Q = e_theory*np_e_count
np_Q = np.array(Q)

rand_rise_time = rand_factor*np_rise_time
rand_fall_time = rand_factor*np_fall_time
rand_rise_v = rand_factor*np_rise_v
rand_fall_v = rand_factor*np_fall_v
rand_a = rand_factor*np_a
rand_Q = rand_factor*np_Q

for i in range(1,11,1):
    
    rise_time_gauss = np.random.normal(np_rise_time,rand_rise_time)
    fall_time_gauss = np.random.normal(np_fall_time, rand_fall_time)
    rise_v_gauss = np.random.normal(np_rise_v, rand_rise_v)
    fall_v_gauss = np.random.normal(np_fall_v, rand_fall_v)
    a_gauss = np.random.normal(np_a,rand_a)
    Q_gauss= np.random.normal(np_Q, rand_Q)
    
    print("Total Charge: Q - Group", str(i))
    print(Q_gauss)
    print("---")
    print("Rise Time", str(i))
    print(rise_time_gauss)
    print("---")
    print("Fall Time", str(i))
    print(fall_time_gauss)
    print("---")
    print ("Rise Velocity", str(i))
    print(rise_v_gauss)
    print("---")
    print("Fall Velocity", str(i))
    print(fall_v_gauss)
    print("---")
    print("Droplet Size", str(i))
    print(a_gauss)
    print("---")
    
    i = i + 1 

#Part B: Experimental Data:

line_dist = 0.0005

uncert_line_dist= 0.00005
uncert_time = 0.05

n_line_rise = [10,9,3,10,10,16,6,9,2,9]
n_line_fall = [2,1,2,1,1,2,0.1,1,0.3,2]

np_n_line_rise = np.array(n_line_rise)
np_n_line_fall = np.array(n_line_fall)


n_dist_rise = line_dist*np_n_line_rise
n_dist_fall = line_dist*np_n_line_fall

time_rise = [3,3,3,3,3,3,3,3,3,3]
time_fall = [3,3,3,3,3,3,3,3,3,3]

np_time_rise = np.array(time_rise)
np_time_fall = np.array(time_fall)

v_rise = n_dist_rise/time_rise
v_fall = n_dist_fall/time_fall

#Calculation a:

a = np.sqrt(b_2p**2 + visc_const*v_fall) - b_2p

#Calculation Q:


const_q1 = 6*pi*d/E
const_q2 = visc_const*n**2
const_q3 = (1 + b/p_press*a)**3
const_q4 = (v_rise + v_fall)*np.sqrt(v_fall)
const_q5 = np.sqrt(const_q2/const_q3)
Q = const_q1*const_q5*const_q4

Q_1 = [6.20783761e-18, 3.65800339e-18, 2.58659901e-18]
Q_2 = [4.02380373e-18, 4.02380373e-18, 9.31175642e-18]
Q_3 = [9.31175642e-18, 3.65800339e-18, 4.60821324e-19, 5.69051781e-18]

np_Q_1 = np.array(Q_1)
np_Q_2 = np.array(Q_2)
np_Q_3 = np.array(Q_3)

n_1 = np_Q_1/2.58659901e-18
n_2 = np_Q_2/4.02380373e-18
n_3 = np_Q_3/3.65800339e-18

int_n1 =[2,1,1]
int_n2 = [1,1,2]
int_n3 = [3,1,0,2]

n_1plot = np.array(int_n1)
n_2plot = np.array(int_n2)
n_3plot = np.array(int_n3)

#Uncertainty Calculation:

dvr_const1 = (uncert_line_dist/np_n_line_rise)**2 + (uncert_time/np_time_rise)**2
v_rise_uncert = v_rise*np.sqrt(dvr_const1)

dvf_const1 = (uncert_line_dist/np_n_line_fall)**2 + (uncert_time/np_time_fall)**2
v_fall_uncert = v_fall*np.sqrt(dvf_const1)

uncert_a = (1/2*a*v_fall_uncert)/v_fall

uncert_Q0 = (dV/V)**2 + np.sqrt(v_rise_uncert**2 + v_fall_uncert**2) + 1/2*(v_fall_uncert)/(v_fall**(3/2))

uncert_Q = Q*np.sqrt(uncert_Q0)

uncert_Q1 = [4.19460747e-18, 2.93923539e-18, 1.74771806e-18]
uncert_Q2 = [3.23316585e-18, 3.23316585e-18, 6.29202464e-18]
uncert_Q3 = [6.29202464e-18, 2.93923539e-18, 5.00299143e-19, 3.84504540e-18]

#Plotting:

#I have no idea why plot_line is plotting multiple lines for a set of data. Maybe it's a visual glitch.

#Monte Carlo was taken from a randomly generated data:

e_count_plot = [1,7,4,5,2,3]
Q_plot = [1.49541119e-19, 1.24256976e-18, 6.10324432e-19, 9.19351689e-19, 2.81508593e-19, 4.94956180e-19]

np_e_count_plot = np.array(e_count_plot)
np_Q_plot = np.array(Q_plot)

print("Monte Carlo calculation for e")
plt.figure(0)
B.plot_exp(np_e_count_plot,np_Q_plot)
B.plot_line(np_e_count_plot, np_Q_plot)
fit = B.linefit(np_e_count_plot,np_Q_plot)
B.pl.title("Q_monte vs n_monte")
B.pl.xlabel("n_monte [number of charges]")
B.pl.ylabel("Q_monte [total charge]")
print("---")

print("Q1")
plt.figure(1)
B.plot_exp(n_1plot,np_Q_1,uncert_Q1)
fit = B.linefit(n_1plot,np_Q_1)
B.pl.title("Q1 vs n1")
B.pl.xlabel("n1 [number of charges]")
B.pl.ylabel("Q1 [total charge]")
B.plot_line(n_1plot,np_Q_1)
print("---")

print("Q2")
plt.figure(2)
B.plot_exp(n_2plot,np_Q_2,uncert_Q2)
fit = B.linefit(n_2plot,np_Q_2)
B.pl.title("Q2 vs n2")
B.pl.xlabel("n2 [number of charges]")
B.pl.ylabel("Q2 [total charge]")
B.plot_line(n_2plot,np_Q_2)
print("---")

print("Q3")
plt.figure(3)
B.plot_exp(n_3plot,np_Q_3,uncert_Q3)
fit = B.linefit(n_3plot,np_Q_3)
B.pl.title("Q3 vs n3")
B.pl.xlabel("n3 [number of charges]")
B.pl.ylabel("Q3 [total charge]")
B.plot_line(n_3plot,np_Q_3)
print("---")

#Experimental Calculation of e:

e_values = [3.085536410000002e-18, 5.287952690000003e-18, 2.8585319708000012e-18]
np_e_values = np.array(e_values)

uncert_e_values = [9.278634108059156e-19, 3.268411497039467e-33, 2.0591607957002244e-19]

average_e = np.mean(e_values)
uncert_avg_e = np.sqrt(9.278634108059156e-19**2 + 3.268411497039467e-33**2 + 2.0591607957002244e-19**2)

#Values:

print("Experimental Rising Velocity")
print(v_rise, pm, v_rise_uncert)
print("---")
print("Experimental Falling Velocity")
print(v_fall, pm, v_fall_uncert)
print("---")
print("Experimental Radius of the Droplets")
print(a, pm, uncert_a)
print("---")
print("Experimental Total Charge")
print(Q, pm, uncert_Q)
print("---")
print("Experimental Value of e")
print(average_e,pm,uncert_avg_e)
