# -*- coding:utf-8 -*-
# @author：LuffyLSX
# @version：1.0
# @update time：2019/8/31

import os,time
import cv2
import numpy as np
from subprocess import run

def connect():
    try:
        os.popen('adb connect 127.0.0.1:7555')
    except:
        print('连接失败')

def click(x, y):
    os.popen('adb shell input tap %s %s' % (x, y))
    time.sleep(1)

def screenshot():
    path = os.path.abspath('.') + "\images"
    run('adb shell screencap /data/screen.png', shell=True)
    run('adb pull /data/screen.png %s' % path, shell=True)
    # os.popen('adb shell screencap /data/screen.png ; adb pull /data/screen.png %s' % path)
    # os.system('adb pull /data/screen.png %s' % path)

def resize_img(img_path):
    img1 = cv2.imread(img_path, 0)
    img2 = cv2.imread('images/screen.png', 0)
    height, width = img1.shape[:2]
    ratio = 2560 / img2.shape[1]
    size = (int(width/ratio), int(height/ratio))
    return cv2.resize(img1, size, interpolation = cv2.INTER_AREA)

def Image_to_position(image, m = 0):
    image_path = 'images/' + str(image) + '.png'
    screen = cv2.imread('images/screen.png', 0)
    # template = cv2.imread(image_path, 0)
    template = resize_img(image_path)
    methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED]
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, methods[m])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(max_val)
    if max_val > 0.9:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        return center
    else:
        return False
    
def Images_to_position(image):
    L1 = []
    image_path = 'images/' + str(image) + '.png'
    screen = cv2.imread('images/screen.png', 0)
    # img_gray = cv2.cvtColor(img_tem, cv2.COLOR_BGR2GRAY)
    img_tem = resize_img(image_path)
    w, h = img_tem.shape[::-1]
    result = cv2.matchTemplate(screen, img_tem, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where(result >= threshold)
    list_p = []
    # print(res)
    for pt in zip(*loc[::-1]):    
        pos = (pt[0] + w / 2, pt[1] + h / 2)
        list_p.append(pos)
    
    for p1 in filter(list_p):
        for p2 in list_p:
            if distance(p1, p2) < 5:
                L1.append(p1)
                break
    return L1

def distance(p1, p2):
    d = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)** 1/2
    return d

def filter(list):
    x = sorted(list, key = lambda x : x[0])
    y = sorted(list, key = lambda y : y[1])
    a = x[0]
    b = y[0]
    list_x = [a[0]]
    list_y = [b[1]]
    L = []

    for i in x:
        if (abs(i[0] - a[0]) > 211):
            list_x.append(i[0])
            a = i
    for i in y:
        if (abs(i[1] - b[1]) > 206):
            list_y.append(i[1])
            b = i
    for x in list_x:
        for y in list_y:
            L.append((x, y))
    return L
    
def script_run(n):
    images = ['start-go1', 'start-go2', 'end', 'report', 'level up']
    round = 0
    now = ''
    # Image_to_position('start-go1')
    # time.sleep(2)
    # Image_to_position('start-go2')
    # while not Image_to_position('end'):
    #     time.sleep(5)
    while True:
        screenshot()
        for image in images:
            if Image_to_position(image, m = 0) != False:
                print(image)
                now = image
                time.sleep(0.5)
                click(center[0], center[1])
        if now == 'start-go2':
            print('进度：%s/%s' % (round + 1, n))      
        if now == 'end':
            time.sleep(1)
            round = round + 1
            if round == n:
                break
        
'''
if __name__ == '__main__':
    connect()
    
    script_run(int(input('输入刷图次数' + '\n')))
    os.popen('adb kill-server')
    input('按回车键退出脚本')

    
    screenshot()
    l = Images_to_position('text/text7')
    for (x, y) in l:
        click(x, y)
        time.sleep(0.5)
        
    
'''
