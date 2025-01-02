import numpy as np
import matplotlib.pyplot as plt
import LT.box as B

#Part A: Monte Carlo Simulation of Cosmic Ray Flux

#Poisson Plotting:

Pmean_1 = 1
Ndeviates = 20000

Pdeviates = np.random.poisson(Pmean_1, Ndeviates)
hpoisson = B.histo(Pdeviates, bins=max(Pdeviates))

plt.figure(1)
hpoisson.plot()
B.pl.xlabel('Counts')
B.pl.ylabel('Frequency')
B.pl.title('Monte Carlo: Mean 1')


Pmean_2 = 5
Pdeviates1 = np.random.poisson(Pmean_2, Ndeviates)
hpoisson1 = B.histo(Pdeviates1, bins = max(Pdeviates1))

plt.figure(2)
hpoisson1.plot()
B.pl.xlabel('Counts')
B.pl.ylabel('Frequency')
B.pl.title('Monte Carlo: Mean 5')

Pmean_3 = 100
Pdeviates2= np.random.poisson(Pmean_3, Ndeviates)
hpoisson2 = B.histo(Pdeviates2, bins = max(Pdeviates2))

plt.figure(3)
hpoisson2.plot()
B.pl.xlabel('Counts')
B.pl.ylabel('Frequency')
B.pl.title('Monte Carlo: Mean 100')

#Cosmic Ray Plotting

background_rate = 2
flux_guess = 60

theta = [-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90]
theta_rad = np.radians(theta)

flux = flux_guess*(np.cos(theta_rad))**2

flux_np = np.array(flux)

counts = []
error = []

for i in flux_np:
    j = np.random.poisson(i,1)
    counts.append(j)
    
for i in counts:
    if i == 0:
        j = 1
    else:
        j = np.sqrt(i)
    error.append(j)

counts_np = np.array(counts)
error_np = np.array(error)
theta_rad_np = np.array(theta_rad)

#Plotting

plt.figure(4)
B.plot_exp(theta_rad_np,counts_np,error_np)

B.pl.title("Monte Carlo Cosmic Ray Flux")
B.pl.xlabel('Theta [Radians]')
B.pl.ylabel('Counts')

#Experimental Poisson Data:

file0 = B.get_file('Ave1-1.data')
file1 = B.get_file('Ave10-1.data')
file2 = B.get_file('Ave100-1.data')

C0 = file0['C']
C1 = file1['C']
C2 = file2['C']

plt.figure(5)
c0 = B.histo(C0, bins = 4)
c0.plot(filled = False)
B.pl.title("Experimental: Mean 1")
B.pl.xlabel('Count')
B.pl.ylabel('Frequency')

plt.figure(6)
c1 = B.histo(C1, bins = 9)
c1.plot(filled = False)
B.pl.title("Experimental: Mean 10")
B.pl.xlabel('Count')
B.pl.ylabel('Frequency')

plt.figure(7)
c2 = B.histo(C2,bins = 99)
c2.plot(filled = False)
B.pl.title("Experimental: Mean 100")
B.pl.xlabel('Count')
B.pl.ylabel('Frequency')

#Experimental Cosmic Ray Flux:

file3 = B.get_file("cosmic_Phase2_DataB.py")

#Experimental Flux Guess
flux_guess_exp = B.Parameter(29.068391793677385,'flux parameter')

theta_exp = file3['theta']
theta_exp_rad = np.radians(theta_exp)
C_exp = file3['C']
C_exp_err = np.sqrt(C_exp)

def S(x):
    return flux_guess_exp() * (B.np.cos(x))**2

plt.figure(8)
sfit = B.genfit(S,[flux_guess_exp], x = theta_exp_rad, y = C_exp, y_err = C_exp_err)
B.plot_exp(theta_exp_rad,C_exp,C_exp_err)
B.plot_line(sfit.xpl,sfit.ypl)
B.pl.xlabel("Angle [Radians]")
B.pl.ylabel("Counts")
B.pl.title("Experimental Cosmic Ray Flux")