import LT.box as B
import numpy as np

#constants
nm2m = 10**9
mm2m = 0.001                      
sin = np.sin
cos = np.cos
deg2rad = np.pi/180
D_mm = (1./1200)        #in mm
D = (D_mm)*mm2m
hc = 1240            #in eV*nm
RH = 10973731.568508 #in 1/m
dRH = 0.000065       #in 1/m
h = 3.6456e-7        #in meters; not planck constant

                    #Angles in arcminutes
thetasorder1 = np.array([(90.5+(1./60)), (102.5+(15./60)), (106.5+(14./60)), (108.5+(10./60))])  
uncer_thetasorder1 = ((np.array([0.05, 0.05, 0.05, 0.05]))*(1./60))*deg2rad

thetasorder2 = (np.array([(43.0+(1./60)), (68.5+(5./60)), (75.5+(17./60)),(79.0+(10./60))]))      
uncer_thetasorder2 = ((np.array([0.05, 0.05, 0.05, 0.05]))*(1./60)) #*deg2rad

thetasorder3 = (np.array([(43.5+(20./60))]))
uncer_thetasorder3 = ((np.array([0.05]))*(1./60))*deg2rad


                    #Angles for experimental setup
thetaA = 179.5+(19./60)
uncer_thetaA = 0.0006

theta0 = 158.5+(5./60)
uncer_theta0 = 0.0006

theta_in = (((179.5+19./60)-(158.5+5./60))/2)*deg2rad

theta_g = ((179.5+19./60)+(158.5+5./60))/2

thetaout1 = (theta_g-thetasorder1)*deg2rad
thetaout2 = (theta_g-thetasorder2)*deg2rad
thetaout3 = (theta_g-thetasorder3)*deg2rad

#Lambda calculations in nm
lambdaa1 = (D*(cos(theta_in)-cos(thetaout1)))*nm2m
lambdaa2 = ((D*(cos(theta_in)-cos(thetaout2)))/2)*nm2m
lambdaa3 = ((D*(cos(theta_in)-cos(thetaout3)))/3)*nm2m

#print lambdaa1
#print lambdaa2
#print lambdaa3 

#______________________________________________________________________________________________________
#Uncertainty calculation lambda 1

uncer_thetain = ((1./4.)*(uncer_theta0**2+uncer_thetaA**2))**(1./2.)
uncer_thetaout = ((uncer_thetasorder1**2+(uncer_theta0*(1./2.))**2+(uncer_thetaA*(1./2.))**2))**(1./2.)

delta1 = D*sin(theta_in)
delta2 = D*sin(thetaout1)
uncerdelta1 = ((D*sin(theta_in)*uncer_thetain)**2)**(1./2.)
uncerdelta2 = ((D*sin(thetaout1)*uncer_thetaout)**2)**(1./2.)

uncerpathtot = ((uncerdelta1**2)+(uncerdelta2**2))**(1./2.)

uncerlambda1 = (1. * uncerpathtot)*nm2m

lambda1 = lambdaa1/nm2m
u_lambda1 = uncerlambda1/nm2m

n_1 = 4
n_2 = np.array(([9.,16., 25., 36.]))

X_x= 1/n_1 - 1/n_2
Y_1 = 1/lambda1

#B.plot_exp(X_x,Y_1,u_lambda1)

#fit1 = B.linefit(X_x, Y_1)
#B.plot_line(fit1.xpl, fit1.ypl)
#B.pl.show()

#B.pl.title("1/lambda [1/m] vs 1/n1**2 - 1/n2**2 [unitless] 1st Order")
#B.pl.xlabel("1/n1**2 - 1/n2**2 [unitless]")
#B.pl.ylabel("1/lambda [1/m]")

#______________________________________________________________________________________________________

#Uncertainty calculation lambda 2
d_thetain = ((1./4.)*(uncer_theta0**2+uncer_thetaA**2))**(1./2.)
d_thetaout = (((uncer_thetasorder2)**2+(uncer_theta0*(1./2.))**2+(uncer_thetaA*(1./2.))**2))**(1./2.)

d_delta1 = ((D*sin(theta_in)*d_thetain)**2)**(1./2.)
d_delta2 = ((D*sin(thetaout2)*d_thetaout)**2)**(1./2.)

delta2_1 = D*sin(thetaout2)

#print delta2_1, "+/-", d_delta2

uncerpathtot_1 = ((d_delta1**2)+(d_delta2**2))**(1./2.)

uncerlambda2 = ((1./2.) * uncerpathtot_1)*nm2m

lambda2 = lambdaa2/nm2m
u_lambda2 = uncerlambda2/nm2m

n_1 = 4
n_2 = np.array(([9.,16., 25., 36.]))

X_x1= 1/n_1 - 1/n_2
Y_2 = 1/lambda2

#B.plot_exp(X_x1,Y_2,u_lambda2)

#fit2 = B.linefit(X_x1, Y_2)
#B.plot_line(fit2.xpl, fit2.ypl)
#B.pl.show()

#B.pl.title("1/lambda [1/m] vs 1/n1**2 - 1/n2**2 [unitless] 2nd Order")
#B.pl.xlabel("1/n1**2 - 1/n2**2 [unitless]")
#B.pl.ylabel("1/lambda [1/m]")

#______________________________________________________________________________________________________

#Uncertainty calculation lambda 3
uncer_thetain = ((1./4.)*(uncer_theta0**2+uncer_thetaA**2))**(1./2.)
uncer_thetaout = ((uncer_thetasorder3**2+(uncer_theta0*(1./2.))**2+(uncer_thetaA*(1./2.))**2))**(1./2.)

uncerdelta1 = ((D*sin(theta_in)*uncer_thetain)**2)**(1./2.)
uncerdelta2 = ((D*sin(thetaout3)*uncer_thetaout)**2)**(1./2.)

uncerpathtot3 = ((uncerdelta1**2)+(uncerdelta2**2))**(1./2.)

uncerlambda3 = (1./3. * uncerpathtot3)*nm2m

lambda3 = lambdaa3/nm2m
u_lambda3 = uncerlambda3/nm2m

n_1 = 4
n_2 = np.array(([36.]))

X_x3 = 1/n_1 - 1/n_2
Y_3 = 1/lambda3

B.plot_exp(X_x3,Y_3,u_lambda3)
B.pl.show()

B.pl.title("1/lambda [1/m] vs 1/n1**2 - 1/n2**2 [unitless] 3rd Order")
B.pl.xlabel("1/n1**2 - 1/n2**2 [unitless]")
B.pl.ylabel("1/lambda [1/m]")
#______________________________________________________________________________________________________

#Energy of the Photons:

E_1 = hc/lambdaa1
E_2 = hc/lambdaa2
E_3 = hc/lambdaa3

d_E_1_dlambda = -hc/(lambdaa1)**2
d_E_2_dlambda = -hc/(lambdaa2)**2
d_E_3_dlambda = -hc/(lambdaa3)**2

X_1 = d_E_1_dlambda*uncerlambda1
X_2 = d_E_2_dlambda*uncerlambda2
X_3 = d_E_3_dlambda*uncerlambda3

sigma_E1 = np.sqrt(X_1**2)
sigma_E2 = np.sqrt(X_2**2)
sigma_E3 = np.sqrt(X_3**2)

#print E_1, "+/-", sigma_E1
#print E_2, "+/-", sigma_E2
#print E_3, "+/-", sigma_E3


