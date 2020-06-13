import numpy as np
import cv2
import os
height,width,c=200,200,3
front_path='rainy/front/'
left_path='rainy/left/'
right_path='rainy/right/'
steer_path='rainy/steer/'
speed_path='rainy/speed/'
acc_path='rainy/acc/'
comm_path='rainy/comm/'
files=os.listdir(front_path)
frontx=np.empty((0,height,width,c),dtype='float32')
leftx=np.empty((0,height,width,c),dtype='float32')
rightx=np.empty((0,height,width,c),dtype='float32')
steery=np.empty((0,1),dtype='float32')
speedx=np.empty((0,1),dtype='float32')
accy=np.empty((0,1),dtype='float32')
comm_x=np.empty((0,1),dtype='float32')

for j in files:
    name=''
    for i in range(5,len(j)):
        if(j[i]!='.'):
            name+=j[i]
        else:
            break
    frontx=np.append(frontx,np.load(front_path+'front'+name+'.npy'),axis=0)
    leftx=np.append(leftx,np.load(left_path+'left'+name+'.npy'),axis=0)
    rightx=np.append(rightx,np.load(right_path+'right'+name+'.npy'),axis=0)
    steery=np.append(steery,np.load(steer_path+'steer'+name+'.npy'),axis=0)
    speedx=np.append(speedx,np.load(speed_path+'speed'+name+'.npy'),axis=0)
    accy=np.append(accy,np.load(acc_path+'acc'+name+'.npy'),axis=0)
    comm_x=np.append(comm_x,np.load(comm_path+'comm'+name+'.npy'),axis=0)
