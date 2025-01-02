import numpy as np
import matplotlib.pyplot as plt
import LT.box as B

#Extracting data from files:

file0 = B.get_file('T1counts.data')
file1 = B.get_file('T2counts.data')
file2 = B.get_file('T1counts1.data')

V1 = file0['V']
T1 = file0['T']

V2 = file1['V']
T2 = file1['T']

V3 = file2['V']
T3 = file2['T']

#Errors associated with the data:

V1_err = []
T1_err = []

V2_err = []
T2_err = []

for i in V1:
    V1_err.append(0.005)
    
for i in T1:
    T1_err.append(0.0005)
    
for i in V2:
    V2_err.append(0.005)
    
for i in T2:
    T2_err.append(0.0005)
    
#Converting to np arrays for plotting.

V1_np = np.array(V1)
V2_np = np.array(V2)
V3_np = np.array(V3)

V1_err_np = np.array(V1_err)
V2_err_np = np.array(V2_err)
V3_err_np = np.array(V1_err)

T1_np = np.array(T1)
T2_np = np.array(T2)
T3_np = np.array(T1)

T1_err_np = np.array(T1_err)
T2_err_np = np.array(T2_err)
T3_err_np = np.array(T1_err)

V3_np1 = [6.32,  6.  ,  5.52,  5.2 ,  4.96,  4.86,  4.16,  3.68,  2.9 , 2.24]
V3_np2 = np.array(V3_np1)
log_V3_np2 = np.log(V3_np2)
T3_np1 = [0.1  , 0.094, 0.088, 0.076, 0.07 , 0.064, 0.058, 0.052, 0.046, 0.04]
T3_np2 = np.array(T3_np1)
V3_err_np1 = [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005]

#Plotting:

plt.figure(0)
B.plot_exp(T1_np,V1_np,V1_err_np,T1_err_np)
B.pl.xlabel("Tau [s]")
B.pl.ylabel("Voltage [V]")
B.pl.title("T1 measurements - not corrected")

plt.figure(1)
B.plot_exp(T3_np,V3_np,V3_err_np,T3_err_np)
B.pl.xlabel("Tau [s]")
B.pl.ylabel("Voltage [V]")
B.pl.title("T1 measurements")

plt.figure(2)
B.plot_exp(T2_np,V2_np,V2_err_np,T2_err_np)
B.pl.xlabel("Tau [s]")
B.pl.ylabel("Voltage [V]")
B.pl.title("T2 measurements")

plt.figure(3)
B.plot_exp(T3_np1,log_V3_np2, V3_err_np1)
B.linefit(T3_np2,log_V3_np2)
R0 = B.linefit(T3_np2,np.log(V3_np2))
B.plot_line(R0.xpl,R0.ypl)
B.pl.xlabel("Tau [s]")
B.pl.ylabel("Natural Log of Voltage ln([V])")
B.pl.title("T1 measurements - linearized")

plt.figure(4)
B.plot_exp(T2_np,np.log(V2_np),V2_err_np)
R = B.linefit(T2_np,np.log(V2_np))
B.plot_line(R.xpl,R.ypl)
B.pl.xlabel("Tau [s]")
B.pl.ylabel("Natural Log of Voltage ln([V])")
B.pl.title("T2 measurements - linearized")

#Uncertainty Calculations:

ln_M0 = 0.4478124134905279
ln_M01 = -0.18827518784621455

d_ln_M0 = 0.1978521980367789
d_ln_M01 = 0.007307673379433058

k = 14.965769820233334
dk = 2.1755108220704065

k1 = -49.88959801292191
dk1 = 1.1227967641855734

T1 = ln_M0/k
T2 = ln_M01/k1

const = (dk/k)**2 + (d_ln_M0/ln_M0)**2
const2 = (dk1/k1)**2 + (d_ln_M01/ln_M01)**2

uncert_T1 = T1*np.sqrt(const)
uncert_T2 = T2*np.sqrt(const2)

print('T1:',T1, '+/-', uncert_T1)
print('T2:',T2, '+/-',uncert_T2)


