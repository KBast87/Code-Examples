import numpy as np
import LT.box as B


file_name = 'examples.data'
f = B.get_file(file_name)

A = B.get_data(f, 'A')
b = B.get_data(f, 'b')
db = B.get_data(f, 'db')
C = B.get_data(f, 'C')
D = B.get_data(f, 'D')

B.plot_exp(A, C, db)
B.pl.show()

B.pl.xlabel("x (unit)")
B.pl.ylabel("y (unit)")

fit1 = B.linefit(A, C, db)
B.plot_line(fit1.xpl, fit1.ypl)

r1= B.in_window(4.0,10.0, C)
r2= B.in_window(2.0,12.0, C)

fit3= B.linefit(A[r1], C[r1], db[r1])
B.plot_line(fit3.xpl, fit3.ypl)

fit4= B.polyfit(A[r1], C[r1], db[r1])
B.plot_line(fit3.xpl,fit3.ypl)

speed = fit4.parameters[1].value
d_speed = fit4.parameters[1].err

B.pl.text(2,0,'Kavon Bastian 6161148')

B.pl.title('6161148 Lab Example 1')

print "/nspeed is %.3E +/- %.3E m/s\n" % (speed, d_speed)


