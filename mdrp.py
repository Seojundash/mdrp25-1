import cv2
import numpy as np

pre = cv2.imread("public_22.PNG", cv2.IMREAD_COLOR)
img = cv2.cvtColor(pre, cv2.COLOR_BGR2HSV)
H,W= len(img), len(img[0])
monit = []
for i in range(H):
    l=[0]*W
    monit.append(l)

def color(t):
    h,s,v=t[0],t[1],t[2]
    if v<50:
        return 1
    if s>50 and v>50:
        if h>160 or h<20: return 2
        elif 40<h<80: return 3
        elif 100<h<140: return 4
    return 0

def check(x,y,image):
    if 0<=x<H and 0<=y<W:
        if image[x][y]==1: return True
    return False

def dfs(x, y, image, buffer):
    stack = []
    group = []
    stack.append((x,y))
    while len(stack):
        X, Y = stack.pop(0)
        if buffer[X][Y]==1: continue
        group.append((X, Y))
        buffer[X][Y]=1;
        for i in range(-1,2):
            for j in range(-1,2):
                x_=X+i; y_=Y+j
                if check(x_,y_,image):
                    stack.append((x_,y_))
    return group

for i in range(H):
    for j in range(W):
        t=img[i][j]
        monit[i][j]=color(t)

buf=np.zeros_like(monit)

f=0
for i in range(H):
    for j in range(W):
        if monit[i][j]==1:
            frame = dfs(i,j,monit,buf)
            if len(frame)>=2000:
                f=1
                break
    if f==1: break

x_max, x_min, y_max, y_min = 0,H,0,W
for i in frame:
    if x_max<i[0]: x_max=i[0]
    if x_min>i[0]: x_min=i[0]
    if y_max<i[1]: y_max=i[1]
    if y_min>i[1]: y_min=i[1]

R,G,B=0,0,0
for i in range(x_min, x_max+1):
    for j in range(y_min, y_max+1):
        if monit[i][j]==2: R+=1
        elif monit[i][j]==3: G+=1
        elif monit[i][j]==4: B+=1
m=max(R,G,B)
if m==R: print('R')
elif m==G: print('G')
elif m==B: print('B')