import cv2
import numpy as np
def bilinear_interp(img,out_dim):
    height, width, channels = img.shape
    goal_height = out_dim[0]
    goal_width = out_dim[1]
    goal_img = np.zeros((goal_height, goal_width, channels), dtype = np.uint8)
    Pro_h = float(goal_height)/height
    Pro_w = float(goal_width)/width
    for channel in range(3):
        for i in range(goal_height):
            for j in range(goal_width):
                result_x = (j + 1 / 2) / float(Pro_w) - 1 / 2
                result_y = (i + 1 / 2) / float(Pro_h) - 1 / 2
                src_x0 = int(np.floor(result_x))
                src_x1 = min(src_x0 + 1, width - 1)
                src_y0 = int(np.floor(result_y))
                src_y1 = min(src_y0 + 1, height - 1)

                r0 = img[src_y0, src_x0, channel] * ((src_x1 - result_x) ) + img[src_y0, src_x1, channel] * ((result_x - src_x0) )
                r1 = img[src_y1, src_x0, channel] * ((src_x1 - result_x) ) + img[src_y1, src_x1, channel] * ((result_x - src_x0) )

                goal_img[i,j,channel] = int(r0*(src_y1 - result_y)  + r1*(result_y - src_y0) )

if __name__ == '__main__':
    test = cv2.imread('lenna.png', 1)
    bilinear_interp(test, (600, 600))
    cv2.imshow('', goal_img)
    cv2.waitKey(0)