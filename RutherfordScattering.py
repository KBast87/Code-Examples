import LT.box as B
import numpy as np
import scipy as sp

file0nt = B.get_spectrum("Zero Degrees without Target.Spe")
file0 = B.get_spectrum("Zero Degrees with Target.Spe")
filep5 = B.get_spectrum("Positive 5 Degrees.Spe")
filem5 = B.get_spectrum("Negative 5 Degrees.Spe")
filep10 = B.get_spectrum("Positive 10 Degrees.Spe")
filem10 = B.get_spectrum("Negative 10 Degrees.Spe")
filep15 = B.get_spectrum("Positive 15 Degrees.Spe")
filem15 = B.get_spectrum("Negative 15 Degrees.Spe")
filep20 = B.get_spectrum("Positive 20 Degrees.Spe")
filem20 = B.get_spectrum("Negative 20 Degrees.Spe")
filem30 = B.get_spectrum("Negative 30 Degrees.Spe")
filem40 = B.get_spectrum("Negative 40 [1000.22s] Degrees.Spe")

C0nt, dC0nt = file0nt.sum(30, 60)
C0, dC0 = file0nt.sum(30, 60)
Cp5, dCp5 = filep5.sum(30, 60)
Cm5, dCm5 = filem5.sum(30, 60)
Cp10, dCp10 = filep10.sum(25, 65)
Cm10, dCm10 = filem10.sum(25, 65)
Cp15, dCp15 = filep15.sum(20, 65)
Cm15, dCm15 = filem15.sum(20, 65)
Cp20, dCp20 = filep20.sum(15, 70)
Cm20, dCm20 = filem20.sum(15, 70)
Cm30, dCm30 = filem30.sum(15, 70)
Cm40, dCm40 = filem40.sum(15, 70)

# get the live time from a spectrum
def get_time(sp):
    tt = float(sp.title.split('=')[1].split('s')[0])
    return tt
#

t0nt = get_time(file0nt)
t0 = get_time(file0)
tp5 = get_time(filep5)
tm5 = get_time(filem5)
tp10 = get_time(filep10)
tm10 = get_time(filem10)
tp15 = get_time(filep15)
tm15 = get_time(filem15)
tp20 = get_time(filep20)
tm20 = get_time(filem20)
tm30 = get_time(filem30)
tm40 = get_time(filem40)

C = np.concatenate((Cp5, Cm5, Cp10, Cm10, Cp15, Cm15, Cp20, Cm20, Cm30, Cm40), axis=None)
dC = np.concatenate ((dCp5, dCm5, dCp10, dCm10, dCp15, dCm15, dCp20, dCm20, dCm30, dCm40), axis=None)
t = np.concatenate((tp5, tm5, tp10, tm10, tp15, tm15, tp20, tm20, tm30, tm40), axis=None)
R = C/t
dR = dC/t

deg = [5, -5, 10, -10, 15, -15, 20, -20, -30, -40]
thet = np.asarray(deg) *((np.pi)/180.)

C = B.Parameter(5.2e-5, 'C')       # define the parameter
thet0 = B.Parameter(0.0673, 'theta_0') # define parameter for

def S(x):                       # define the function
    return C()/B.np.sin(0.5*(x - thet0()) )**4

#B.plot_exp(thet, R, dR, logy=True)

B.plot_exp(np.log(abs(np.sin(thet/2.))), np.log(R), dR)

lfit = B.linefit(np.log(abs(np.sin(thet/2.))), np.log(R), dR)
B.plot_line(lfit.xpl, lfit.ypl)


sfit = B.genfit( S, [C, thet0], \
                 x = thet,\
                 y = R,\
                 y_err = dR)
                 
B.plot_line(sfit.xpl, sfit.ypl)


filep20.plot()
B.pl.show()