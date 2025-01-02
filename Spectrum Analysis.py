import LT.box as B
import numpy as np
import scipy as sp

#Spectrum for Alpha Particle at x degrees with and without target:

spec = B.get_spectrum('Positive 20 Degrees.SPE')
spec.set_window(0,100)
spec.plot()

#Plotting:

B.pl.show()

#B.pl.title("Signal Histogram: Counts [Unitless] vs Channel Number [C]")
B.pl.xlabel("Channel Number [C]")
B.pl.ylabel("Counts [unitless]")

#Counting Rate:

def get_time(spec):
    tt = float(spec.title.split('=')[1].split('s')[0])
    return tt

C, dC = spec.sum(30)
t = get_time(spec)

R = C/t
dR = dC/t

print R, '+/-', dR

