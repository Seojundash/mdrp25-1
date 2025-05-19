import cv2
import numpy as np

def apply_filter(a, b):

    # TODO 2: Get the dimensions of the image and filter
    ih, iw = len(a), len(a[0])
    fh, fw = len(b), len(b[0])

    # TODO 3: Define the output image as a zero array with the appropriate size
    oh = ih - fh + 1
    ow = iw - fw + 1
    c = np.zeros((oh, ow))

    # TODO 4: Apply the filter to the image using nested for loops
    for i in range(oh):
        for j in range(ow):
            c[i, j] = np.sum(a[i:i+fh, j:j+fw]*b)

    return c

img = cv2.imread("xxiong.png")
img2 = cv2.imread("xxiong.png", cv2.IMREAD_GRAYSCALE)
img_b=np.zeros_like(img)
img_g=np.zeros_like(img)
img_r=np.zeros_like(img)
H=len(img)
W=len(img[0])
for i in range(H):
    for j in range(W):
        img_b[i][j][0]=img[i][j][0]
        img_g[i][j][1]=img[i][j][1]
        img_r[i][j][2]=img[i][j][2]

filt=np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
img3= apply_filter(img2, filt)
print(img2)
cv2.imshow("image", img2)
cv2.waitKey(0)
cv2.imshow("image", img3)
cv2.waitKey(0)
print(img3)