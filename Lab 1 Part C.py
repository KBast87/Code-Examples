import numpy as np
import LT.box as B
import LT_Fit.parameters as P
import LT_Fit.gen_fit as G
import scipy.misc as ms

file_name = 'histoFitting.data'
f = B.get_file(file_name)

A = B.get_data (f, 'A')

h2 = B.histo(A, (0.5, 10.5), 10)

h2.plot();

hx = h2.bin_center
hy = h2.bin_content
dy = np.sqrt(hy)

print "hy/n" 
print "dy/n" 

mu = P.Parameter(2., 'mu')
norm = P.Parameter(10., 'norm')

def myfun1(x):
    value = norm()*mu()**x*np.exp(-mu())/ms.factorial(x)
    return value

fit10 = G.genfit(myfun1, [mu,norm], x = hx, y = hy)

B.plot_line(fit10.xpl, fit10.ypl, color= 'red')

B.pl.text(2,0,'Kavon Bastian 6161148')

B.pl.title('6161148 Lab Example 3')

h2.plot()
B.pl.show()