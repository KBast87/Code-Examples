import LT.box as B
import numpy as np
import scipy as sp

#Analysis of Conversion Factor:

file_name = 'Calibration Linear Analysis.data'
f = B.get_file(file_name)

E = B.get_data(f,'E')
C = B.get_data(f,'C')
dC = B.get_data(f,'dC')

B.plot_exp(E,C,dC)
B.pl.show()

B.pl.title("Channels [C] vs Energy [MeV]")
B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Channels [C]")

l1 = B.linefit(E,C)
B.plot_line(l1.xpl,l1.ypl)

#The Unit of the slope is Channels/MeV:

m = 403.87595071
dm = 19.1980565025
intercept = 28.005325231
d_intercept = 21.3147465364

#Calibration Setup and Value:

cal = B.linefit(C,E)

cal_r = 0.0024704257829
d_cal_r = 0.000117430546884
intercept_cal = -0.0667747824023
d_intercept_cal = 0.0558344943137

#The unit of the calibration is MeV/C
