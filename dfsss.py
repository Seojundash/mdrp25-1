import numpy as np

def checkImage(x,y,image, buffer):
    H,W= image.shape
    if 0<=y<H and 0<=x<W and not buffer[y][x] and not image[y][x]: return True
    return False

def dfs(x,y,image, buffer):
    stack = []
    line = []
    stack.append((x,y))
    def search(x,y):
        buffer[y][x]=1;
        for i in range(-1,2):
            for j in range(-1,2):
                x_=x+i
                y_=y+j
                if checkImage(x_,y_,image, buffer):
                    stack.append((x_,y_))
                    search(x_,y_,image, buffer)
    search(x,y)
    print(stack)
    line=stack
    
    return line


#no need to change fit_line
def fit_line(points_list):
    num_a, den_a, x_bar, y_bar = 0, 0, 0, 0
    n = len(points_list)

    for i in range(n):   # x_bar & y_bar 계산하기
        x,y = points_list[i]
        x_bar += x
        y_bar += y

    x_bar = x_bar /n
    y_bar = y_bar /n

    for i in range(n):    # num_a & den_a 계산하기
        x,y = points_list[i]
        num_a += (x - x_bar) * (y - y_bar)
        den_a += (x - x_bar) ** 2

    a = num_a / den_a
    b = y_bar - a * x_bar
    return a, b


def find_max_line(image):
    buffer = np.zeros_like(image)
    max_line = []
    H,W= image.shape
    for i in range(H):
        for j in range(W):
            print(i,j)
            line=dfs(j,i,image, buffer)
            if len(line)>=len(max_line):
                max_line=line
    
    a, b = fit_line(max_line)

    return a,b
    
    

#no need to change below code
if __name__ == '__main__':
    image = np.loadtxt("line.csv", delimiter=",")
    a,b = find_max_line(image)
    print(a,b)