# This python code will be used to determine the electric vehicle's
# Power and Torque with respect to motor speed.
 
import numpy as np
import matplotlib.pyplot as plt
 
Xm=np.array([1,0.75,0.5,0.25]) #motor control signal * 100%
constantmotorpower=150000  #W
basemotorspeed=160 #rad/s    assumed from lecture's use
Tmstar=constantmotorpower/basemotorspeed   #N-m
Wmax=350 #rad/s  I have no idea
 
 
def piecewise (Wm):
    if 0 <= Wm <= basemotorspeed:
        return Xm*Tmstar
    elif Wm >= basemotorspeed and Wm <= Wmax:
        return Xm*constantmotorpower/Wm
 
Wm=np.arange(0,Wmax,1)
y=[]
for i in range(len(Wm)):
    y.append(piecewise(Wm[i]))
 
plt.plot(Wm,y)
#plt.plot(Wm,y[1],label="100%")
 
plt.title("EM Power and Torque")
plt.xlabel('Angular Velocity of Motor (rad/s)')
plt.ylabel('Torque (N-m)')
plt.text(100,900,'100%')
plt.text(100,630,'75%')
plt.text(100,400,'50%')
plt.text(100,200,'25%')
plt.show()
