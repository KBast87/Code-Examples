import LT.box as B
import numpy as np

file_name = "PPDT [Plateau].data"

f = B.get_file(file_name)

#V is the Voltage, C is the number of counts.

V = B.get_data(f,'V')
C = B.get_data(f, 'C')

#Uncertainty in V [Volts]
dV = 1

#Uncertainty in C [Counts - unitless]
dC = np.sqrt(C)

#Plotting:

B.plot_exp(V,C,dC)
B.pl.show()

B.pl.title("Number of Counts vs Voltage")
B.pl.xlabel("Voltage [Volt]")
B.pl.ylabel("Number of Counts [unitless]")