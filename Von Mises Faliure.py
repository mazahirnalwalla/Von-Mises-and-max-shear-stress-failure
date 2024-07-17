import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,pi

Syt = float(input("Enter the tensile yield stress in MPa = "))
Sx = float(input("Enter stress in x-direction in MPa = "))
Sy = float(input("Enter stress in y-direction in MPa = "))

Sv = np.sqrt((Sx**2)+(Sy**2)-(Sx*Sy)) #Von-Mises Stress

a = 2**0.5*Syt #Semi-major axis of ellipse
b = (2/3)**0.5*Syt #Semi-minor axis of ellipse

theta = np.linspace(0,360*pi/180,1000)

x0 = a*cos(theta)
y0 = b*sin(theta)

x = x0*cos(pi/4)-y0*sin(pi/4)
y = x0*sin(pi/4)+y0*cos(pi/4)

xp = [Syt,Syt,0,-Syt,-Syt,0,Syt]
yp = [0,Syt,Syt,0,-Syt,-Syt,0]

sp1 = []
sp2 = []

pts = int(input("Enter the number of points you wish to plot: "))
pts1 = pts+1
i = 1

while i<pts1:
    xi = float(input(f"Enter value of point {i} in x-direction in MPa: "))
    yi = float(input(f"Enter value of point {i} in y-direction in MPa: "))
    sp1.append(xi)
    sp2.append(yi)
    i = i+1


ax = plt.axes()
ax.set_facecolor("black")
plt.plot(x,y,color="orange",label="Von-Mises Regoin")
plt.plot(xp,yp,color="red",linestyle="--",marker="o",label="Max Shear Region")
plt.scatter(sp1,sp2,color="pink",label="Plotted points")
plt.grid(color="cyan")
plt.legend()
plt.show()
