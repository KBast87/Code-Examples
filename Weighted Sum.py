#Defining the weighted Sum:

em_over_dem2 = (e_over_m/(de_over_m**2))
S_em_over_dem2 = sum(em_over_dem2)

one_over_dem2 = 1.0/(de_over_m**2)
S_one_over_dem2 = sum(one_over_dem2)

WM_e_over_m = S_em_over_dem2/S_one_over_dem2
WM_de_over_m = np.sqrt(1/S_one_over_dem2)

print (WM_e_over_m/10**11),"+/-", (WM_de_over_m/10**11)



