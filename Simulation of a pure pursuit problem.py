import random
import numpy as np
import matplotlib.pyplot as plt

thresh=100
vf= 20
flag=1
escapped_thresh=900
t=0

xf=random.randint(1,1000)
yf=random.randint(1,1000)
bomber_x=[]
bomber_y=[]
fighter_x=[]
fighter_y=[]
fighter_x.append(xf)
fighter_y.append(yf)

while(flag):
    xb=random.randint(1,1000)
    yb=random.randint(1,1000)
    
    bomber_x.append(xb)
    bomber_y.append(yb)
    
    dist=np.sqrt((xb-xf)**2+(yb-yf)**2)
    # dist=np.sqrt((xb-xf)**2)+((yb-yf)**2)
    print(xf,yf,xb,yb)
    print('Distance: ',dist)
    if dist<thresh:
        print("Target Caught")
        flag=0
    elif dist>escapped_thresh:
        flag=0
        print("Escapped")
    
    else:
        sin=(yb-yf)/dist
        cos=(xb-xf)/dist
        xf=xf+vf*cos
        yf=yf+vf*sin
    t=t+1
    
    fighter_x.append(xf)
    fighter_y.append(yf)

print("T:",t)

plt.plot(bomber_x,bomber_y,'r*')
plt.plot(fighter_x,fighter_y,'b*')
plt.show()

