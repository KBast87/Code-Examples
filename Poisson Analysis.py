import LT.box as B
import numpy as np
import scipy.special as sp


file_name = "PDLC [Poisson].data"
f = B.get_file(file_name)

#Defining Parameters:

V = f.par.get_value('V')
C = B.get_data(f,'C')
N = 205
pi = np.pi

#Define histogram with bin width 1:

def set_range(first_bin = 0, bin_width = 1., Nbins = 10):
     rmin = first_bin - bin_width/2.
     rmax = rmin + Nbins*bin_width
     return (rmin,rmax)

hg_Poisson = B.histo(C, range = set_range(first_bin= 0., bin_width = 1, Nbins = 7), bins = 7)

hg_Poisson.plot()
B.pl.show()

B.pl.title("Low Count [0 < C > 6] Histogram")
B.pl.xlabel("Number of Counts [Unitless]")
B.pl.ylabel("Occurences [Unitless]")
B.pl.ylim(0,70)

#Define Poisson Function:

mu = C.mean()
X = C - mu
std_dev = np.sqrt(sum((X)**2/N))

def P(y):
    P = 200*mu**y*np.exp(-mu)/sp.factorial(y)
    return P

x = np.array([0.,1.,2.,3.,4.,5.,6.])

#Poisson Plot:

B.plot_exp(x,P(x),color = 'b')
B.pl.show()

B.pl.title("Low Count [0 < C > 6] Histogram")
B.pl.xlabel("Number of Counts [Unitless]")
B.pl.ylabel("Occurences [Unitless]")

#Comparing Probabilities:

#Probability from Histogram -

freq_list = [51.,58.,60.,21.,10.,5.]
freq = np.array(freq_list)
p_histo = freq/205

#Probablity from Poisson Function:

freq_poiss_list = [44.84,67.04,50.12,24.98,9.33,2.79]
freq_poiss = np.array(freq_poiss_list)
p_poiss = freq_poiss/205

#Fitting Parameters:

#hg_Poisson.fit()
#hg_Poisson.plot_fit()

print "----------------------------Poisson Distribution------------------------"
print p_poiss
print mu
print std_dev
print "------------------------------------------------------------------------"


