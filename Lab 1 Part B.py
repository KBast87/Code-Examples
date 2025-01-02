import numpy as np
import LT.box as B

import LT_Fit.parameters as P
import LT_Fit.gen_fit as G

import scipy.misc as ms

file_name = 'examples.data'

f = B.get_file(file_name)

A = B.get_data(f, 'A')

b = B.get_data(f, 'b')

db = B.get_data(f, 'db')

C = B.get_data(f, 'C')

D = B.get_data(f, 'D')

B.plot_exp(C,D,db)
B.pl.show()

c1 = P.Parameter(1.,'pol0')
c2 = P.Parameter(1., 'pol1')
c3 = P.Parameter(1., 'pol2')

height = P.Parameter(8., 'height')
mean = P.Parameter(6.,'mean')
sigma = P.Parameter(1., 'sigma')

def myfun(x):
    value = c1()+c2()*x+c3()*x**2+height()*np.exp(-((x-mean())/(2*sigma()))**2)    
    return value

fit5= G.genfit(myfun,[c1,c2,c3,height,mean,sigma], x = C, y = D, y_err = db)

B.plot_line(fit5.xpl,fit5.ypl, color = 'blue')

r3 = B.in_window(2.0, 12.0, C)

fit6 = G.genfit(myfun, [c1,c2,c3,height,mean, sigma], x= C[r3], y = D[r3], y_err = db[r3])

B.plot_line(fit6.xpl,fit6.ypl, color = 'magenta')

mu = P.Parameter(6., 'mu')
norm = P.Parameter(10.,'norm')

def myfun1(x):
    value = norm()*mu()**(x)*np.exp(-mu())/ms.factorial(x)
    return value

fit7 = G.genfit(myfun1, [mu,norm], x = C[r3], y = D[r3], y_err = db[r3])
B.plot_line(fit7.xpl,fit7.ypl, color = 'red')

c1 = P.Parameter(1, 'pol0')
c2 = P.Parameter(1., 'pol1')
c3 = P.Parameter(1., 'pol2')

mu = P.Parameter(7., 'mu')
norm = P.Parameter(20., 'norm')

def myfun2(x):
    pol2 = c1()+c2()*x+c3()*x**2
    value = pol2*norm()*mu()**(x)*np.exp(-mu())/ms.factorial(x)
    return value

r4 = B.in_window(4.0,16.0,C)

fit8 = G.genfit(myfun2, [c1,c2,c3,mu,norm], x = C[r4], y = D[r4], y_err = db[r4])
B.plot_line(fit8.xpl, fit8.ypl, color = 'brown')

c1 = P.Parameter(1., 'pol0')
c2 = P.Parameter(1., 'pol1')
c3 = P.Parameter(1., 'pol2')

mu = P.Parameter(7., 'mu')
norm = P.Parameter(20., 'norm')

c2.set(0.)

fit9 = G.genfit(myfun2, [c1,c3,mu,norm], x = C[r4], y = D[r4], y_err = db[r4])
B.plot_line(fit9.xpl, fit9.ypl, color = 'green')

muvalue = mu.value
muerr = mu.err

B.pl.text(10,5,'Kavon Bastian 6161148')

B.pl.title('6161148 Lab Example 2')

B.pl.xlabel("x (unit)")
B.pl.ylabel("y (unit)")

print "mu has the value of %.3f +- %.3f\n" %(muvalue, muerr)

    
    