import LT.box as B
import numpy as np
import scipy as sp
import LT.plotting as P

file_name = "Data Set for 405nm.data"

f = B.get_file(file_name)

V = B.get_data(f,'V')
I = B.get_data(f,'I')
dI = 0.005

#Plotting:

B.plot_exp(V,I,dI)
B.pl.show()

B.pl.title("I vs V [Current vs Voltage] for 405nm")
B.pl.xlabel("Voltage [Volts]")
B.pl.ylabel("Current [milli-Amps]")

print "------------------------------------------------------------------------"
ir = B.in_window(1.6,2.5,V)
l1 = B.linefit(V[ir],I[ir])
B.plot_line(l1.xpl,l1.ypl)
print "------------------------------------------------------------------------"
ir1 = B.in_window(1.1,1.3,V)
l2 = B.linefit(V[ir1],I[ir1])
B.plot_line(l2.xpl,l2.ypl)
print "------------------------------------------------------------------------"
ir2= B.in_window(1.2,1.6,V)
l3= B.linefit(V[ir2],I[ir2])
B.plot_line(l3.xpl,l3.ypl)
print "------------------------------------------------------------------------"

m1 = -0.0257967005473
m2 = -0.91656308266
m3 = -0.296838442308
b1 = -0.10197767006
b2 = 1.10152234307
b3 = 0.329595626197
#Uncertainties:
dm1 = 0.0112891910753
db1 = 0.0217089324479
dm2 = 0.0910626061607
db2 = 0.10820045901
dm3 = 0.0623727286265
db3 = 0.0840008123919

print "------------------------------------------------------------------------"
x1 = (b2-b1)/(m1-m2)

#Uncertainties in Voltage 1:
dx1_db2 = -b1/(m1-m2)
dx1_db1 = b2/(m1-m2)
dx1_dm1 = (b2-b1)/((m1-m2)**2)
dx1_dm2 = (-1.0)*(b2-b1)/((m1-m2)**2)

A = dx1_db2*db2
b = dx1_db1*db1
C = dx1_dm1*dm1
D = dx1_dm2*dm2

dx1 = np.sqrt(A**2+b**2+C**2+D**2)

print x1 ,"+/-", dx1

print "------------------------------------------------------------------------"
x2 = (b3-b1)/(m1-m3)

#Uncertainties in Voltage 2:
dx2_db3= -b1/(m1-m3)
dx2_db1 = b3/(m1-m3)
dx2_dm1 = (b3-b1)/((m1-m3)**2)
dx2_dm3 = (-1.0)*(b3-b1)/((m1-m3)**2)

A1 = dx2_db3*db2
b1 = dx2_db1*db1
C1 = dx2_dm1*dm1
D1 = dx2_dm3*dm2

dx2 = np.sqrt(A1**2+b1**2+C1**2+D1**2)

print x2, "+/-", dx2

print "------------------------------------------------------------------------"
x = (x1+x2)/2

#Uncertainty in Stopping Voltage:
dx_dx1 = x2/2
dx_dx2 = x1/2

A2 = dx_dx1*dx1
b2 = dx_dx2*dx2

dx = np.sqrt(A2**2+b2**2)

print x, "+/-", dx

print "------------------------------------------------------------------------"