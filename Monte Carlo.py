# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:22:39 2020

@author: Kavon Bastian
"""

import numpy as np
import random
import time
import matplotlib.pyplot as plt
import LT.box as B

# Monte Carlo:

# Part A: Computing Pi and uncertainty

#Plus-Minus Sign:

pm = "+/-"

#Loop Variables:

i = 0

C = 0

#Loop for computing pi:

for i in range(0,10000,1):
         
    x = random.random()
    y = random.random()
    
    if (x**2. + y**2.) < 1.:
        
        C += 1
    
    i += 1
    
C_1 = C/10000

#Computation of pi_comp:

pi_comp = C_1*4

pi_act = np.pi

ratio_pi = pi_comp/4

#Uncertainty in pi_comp:

uncert_circle = np.sqrt(C*(1-C_1))

constant = (4.0/10000)**2

pi_uncert = np.sqrt(constant*uncert_circle**2)

print()
print("--- Value of pi is",pi_comp,pm,pi_uncert, "---")
print("--- Actual Value of pi is", pi_act, "---")

#Uncertainty of Events for 1%, 0.01% and 0.00001%

# Statistical Uncertainties [You can plug in the percent wanted because I was kind of lazy. Dont mark me down please. :D]

perc_1= input("Statistical Uncertainty Wanted [in percent (%)]: ")
perc_wanted = float(perc_1)
perc = perc_wanted/100

top = 16.0*ratio_pi*(1-ratio_pi)
bottom = np.pi * perc**2

number_c = top/bottom

print("--- Statistical uncertainty of", perc_wanted ,"% requires", int(number_c), "try/ies ---" )


#Part B: N-dimensional sphere

#Loop Variables:

j = 0

C1 = 0

#Dimension N:
    
N_1 = input("Dimension of Sphere [1-5 supported]: ")

N = float(N_1)

#N = 1
    
if N == 1:
    
        for j in range(0,10000,1):
        
            x = random.random()
        
            sp = x**2
        
            if (x**2.) < 1.:
            
                C1+= 1
        
            j=+ 1
        
            vol = 2
    
#N = 2

if N == 2:
        
    for j in range(0,10000,1):
             
            x = random.random()
            y = random.random()
        
            sp = x**2 + y**2
        
            if (x**2. + y**2.) < 1.:
            
                C1+= 1
        
            j += 1
            
            vol = np.pi

#N = 3

if N == 3:

    for j in range(0,10000,1):
        
        x = random.random()
        y = random.random()
        z = random.random()
            
        sp = x**2 + y**2 + z**2
        
        if (x**2. + y**2. + z**2.) < 1.:
            
            C1 += 1
                
        j += 1
        
        vol = 4.189
            
#N = 4
  
if N == 4:

         for j in range(0,10000,1):
        
            x = random.random()
            y = random.random()
            z = random.random()
            a = random.random()
        
            sp = x**2 + y**2 + z**2 + a**2
            
            if (x**2. + y**2. + z**2 + a**2.) < 1.:
                
                C1+= 1
        
            j += 1
        
            vol = 4.935
     
#N = 5

if N == 5:

        for j in range(0,10000,1):
        
            x = random.random()
            y = random.random()
            z = random.random()
            a = random.random()
            b = random.random()
        
            sp = x**2 + y**2 + z**2 + a**2 + b**2
        
            if (x**2. + y**2. + z**2 + a**2. + b**2.) < 1.:
            
                C1+= 1
        
            j += 1
        
            vol = 5.264
            
# Total counts found 
    
tot_sph = C1/10000

# Binomial Uncertainty 

binom_error = np.sqrt(C1*(1-tot_sph))

# Sphere Volume and its uncertainty 

vol_sph = (tot_sph)*(2.**N)

volerr = np.sqrt((((2**N)/j)**2)*(binom_error)**2)

print()
print("--- Analytic Volume of Sphere:", vol, "---")
print("--- Experimental Volume of Sphere:", vol_sph, pm, volerr, "---")
        


#Part C and D: Gaussian Fitting and Poisson Plotting

Pmean = 8.4
Gmean = 0.0
Gsigma = 1.0
Ndeviates = 20000

Pdeviates = np.random.poisson(Pmean, Ndeviates)
Gdeviates = np.random.normal(Gmean, Gsigma, Ndeviates)

hpoisson = B.histo(Pdeviates, bins=max(Pdeviates))
hgaussian = B.histo(Gdeviates, bins=max(Pdeviates))

plt.figure(1)
plt.title("Gaussian Plot and Fit")

hgaussian.plot()
hgaussian.fit()
hgaussian.plot_fit()

plt.figure(2)
hpoisson.plot()
