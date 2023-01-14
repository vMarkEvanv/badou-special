import cv2
import numpy as np

def RGB2Gray(img):
    height,width,channels = img.shape
    img_R = img[:,:,2]
    img_B = img[:,:,1]
    img_G = img[:,:,0]
    gray = (img_R*0.3+img_B*0.11+img_G*0.59)
    gray = gray.astype(np.uint8)
    return gray
def Binarization(img,threshold):
    height,width = img.shape
    for i in range(height):
        for j in range(width):
            if(img[i,j] >= threshold):
                img[i,j] = 255
            else:
                img[i,j] = 0
    return img
test = cv2.imread('lenna.png',1)
cv2.imshow('1',RGB2Gray(test))
cv2.imshow('2',Binarization(RGB2Gray(test),100))
cv2.waitKey(0)
