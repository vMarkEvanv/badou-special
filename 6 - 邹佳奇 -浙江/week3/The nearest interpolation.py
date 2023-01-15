import cv2
import numpy as np
def nearest_inter(img, goal_height, goal_width):
    height, width, channels = img.shape
    goal_img = np.zeros((goal_height,goal_width),np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    proportion_h = goal_height/height
    proportion_w = goal_width/width
    for i in range(goal_height):
        for j in range(goal_width):
            x = int(i/proportion_h - 0.5)
            y = int(j/proportion_w - 0.5)
            goal_img[i,j] = gray[x,y]
    return goal_img
if __name__=='__main__':
    test = cv2.imread('lenna.png',1)

    cv2.imshow('',nearest_inter(test,512,512))
    cv2.waitKey(0)