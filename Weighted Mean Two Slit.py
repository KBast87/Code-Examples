import numpy as np
import LT.box as B
import LT_Fit.parameters as P
import LT_Fit.gen_fit as G

A = np.array([7.36,6.61,6.85,6.99,6.99])
b = np.array([0.01,0.02,0.05,0.06,0.06])

C = np.array([4.11,4.13,4.13])
D = np.array([0.004,0.009,0.009])
#Defining the weighted Sum:

D_over_dD = (A/(b**2))
S_D_over_dD = sum(D_over_dD)

one_over_D = 1.0/(b**2)
S_one_over_D = sum(one_over_D)

WM_D_over_dD = S_D_over_dD/S_one_over_D
WM_one_over_D = np.sqrt(1/S_one_over_D)

print (WM_D_over_dD),"+/-", (WM_one_over_D)

S_over_dS = (C/(D**2))
S_S_over_dS = sum(S_over_dS)

one_over_dS = 1.0/(D**2)
S_one_over_dS = sum(one_over_dS)

WM_S_over_dS = S_S_over_dS/S_one_over_dS
WM_one_over_dS = np.sqrt(1/S_one_over_dS)

print (WM_S_over_dS),"+/-", (WM_one_over_dS)


