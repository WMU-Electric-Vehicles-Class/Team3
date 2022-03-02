# This is a model for the longitudinal Dynamics of
# the Electric Vehicle
 
 
 
ng=0.70 #gearbox efficiency                   assumed
nd=.7 #differential efficiency                 assumed
Pm=150000 #constant motor power
density=1.2 #density of air
Cd=0.29 #drag coefficient
A=2.799 #cross-sectional area
Crr=0.02 #rolling resistance coefficient     assumed
m=1685 #mass
g=9.81 #gravitational acceleration
Bg=1 #gear box ratio                          assumed
Bd=7.981 #Final drive ratio
Tm=395 #maximum torque
Rwheel=0.33 #wheel radius
 
from sympy import Eq, Symbol, solve
 
umax = Symbol('umax')
eq1 = Eq((ng*nd*Pm/umax)-0.5*density*Cd*A*umax**2-Crr*m*g,0)
sol = solve(eq1)
print('Maximum Speed in m/s= ',sol[0])  #sol[0] is the real value solution
print('Maximum Speed in mph= ',sol[0]*2.23694)
 
import math
maxgrade=math.asin((nd*ng*Bg*Bd*Tm)/(Rwheel*m*g)-Crr)
maxgradedegree=maxgrade*180/math.pi
print('Maximum Gradability =',format(maxgradedegree,".2f"))