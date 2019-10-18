import os
import time
import cv2
from subprocess import run
import re

# def resize_img(img_path):
#     img1 = cv2.imread(img_path, 0)
#     img2 = cv2.imread('images/screen.png', 0)
#     height, width = img1.shape[:2]
#     ratio = 2560 / img2.shape[1]
#     size = (int(width/ratio), int(height/ratio))
#     return cv2.resize(img1, size, interpolation=cv2.INTER_AREA)

# def Image_to_position(image, m=0):
#     image_path = 'D:/study/wait/finish/images/' + str(image) + '.png'
#     screen = cv2.imread('images/screen.png', 0)
#     # template = cv2.imread(image_path, 0)
#     template = resize_img(image_path)
#     methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED]
#     image_x, image_y = template.shape[:2]
#     result = cv2.matchTemplate(screen, template, methods[m])
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     print(max_val)

#     if max_val > 0.92:
#         global center
#         center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
#         print(center)
#         return center
#     else:
#         return False
# def click(x, y):
#     os.popen('adb shell input tap %s %s' % (x, y))

if __name__ == "__main__":
    name = '[1]5-10 ^ 6'
    matchObj = re.match(r'(.*)\s\^\s(.*)', name, re.M | re.I)
    print(matchObj.group(2))

    