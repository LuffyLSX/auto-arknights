import os
import time
import cv2
from subprocess import run
import re

def resize_img(img_path):
    img1 = cv2.imread(img_path, 0)
    img2 = cv2.imread('images/test/chapter_pr_d_.png', 0)
    height, width = img1.shape[:2]
    ratio = 2560 / img2.shape[1]
    size = (int(width/ratio), int(height/ratio))
    return cv2.resize(img1, size, interpolation=cv2.INTER_AREA)

def Image_to_position(image, m=0):
    image_path = 'images/' + str(image) + '.png'
    screen = cv2.imread('images/screen.png', 0)
    # template = cv2.imread(image_path, 0)
    template = resize_img(image_path)
    methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED]
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, methods[m])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)

    if max_val > 0.89:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        return center
    else:
        return False

def click(x, y):
    os.popen('adb shell input tap %s %s' % (x, y))
def swipe(x1, x2, y1, t):
    os.popen('adb shell input swipe %s %s %s %s %s' % (x1, y1, x2, y1, t))
    time.sleep(2)


if __name__ == "__main__":
    # name = '[1]5-10 ^ 6'
    # matchObj = re.match(r'(.*)\s\^\s(.*)', name, re.M | re.I)
    # print(matchObj.group(2))
    # path = os.path.abspath('.') + '\images'
    path = os.path.abspath('.') + '\images'
    run('adb shell screencap /data/screen.png', shell=True)
    run('adb pull /data/screen.png %s' % path, shell=True)
    Image_to_position('prts_off')
    # img = cv2.imread('images/screen.png', 0)
    # click(center[0],center[1])
    # swipe(img.shape[1]*0.9, img.shape[1]*0.1, img.shape[0]/2, 2000)
    # time.sleep(1)
    # print('finish')

    