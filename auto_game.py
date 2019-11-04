# -*- coding:utf-8 -*-
# @author：LuffyLSX、DSK
# @version：1.2
# @update time：2019年9月3日

import os
import time
import cv2
import chapter_list  # 字典
import random
import threading
from subprocess import run

random_time = random.uniform(1.0, 3.0)
a = []
run_state = 'standby'
__running = threading.Event()


def click(x, y):
    os.popen('adb shell input tap %s %s' % (x, y))
    time.sleep(1.5)


def swipe(x1, x2, y1, t):
    os.popen('adb shell input swipe %s %s %s %s %s' % (x1, y1, x2, y1, t))
    time.sleep(2)


def screenshot():
    if __running.is_set() == False:
        __running.wait()
    path = os.path.abspath('.') + '\images'
    run('adb shell screencap /data/screen.png', shell=True)
    time.sleep(0.5)
    run('adb pull /data/screen.png %s' % path, shell=True)
    time.sleep(0.7)


def resize_img(img_path):
    img1 = cv2.imread(img_path, 0)
    img2 = cv2.imread('images/screen.png', 0)
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
    # print(max_val)

    if max_val > 0.89:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        return center
    else:
        return False


def find_back():
    chapter = ['back_2', 'back_1']
    while True:
        screenshot()
        if Image_to_position('chapter_start'):
            return
        for image in chapter:
            print(image)
            if Image_to_position(image):
                click(center[0], center[1])
                if image == 'back_2':
                    break


def chapter_selet(chapter_name):  # 刷图线路模块

    eval('chapter_list.chapter_'+str(chapter_name)+'()')
    chapter = chapter_list.chapter_list
    print(chapter)

    before_end = True
    while before_end:
        screenshot()
        for image in chapter:
            if Image_to_position(image):
                print(image)
                click(center[0], center[1])
                if image == chapter[-2]:
                    before_end = False
                if Image_to_position(chapter[-1]):
                    click(center[0], center[1])
                    return
            elif image == 'chapter_zx':
                screenshot()
                if Image_to_position(chapter[2]) == False:
                    print('如果屏幕有目标章节就不应该出现这句话')
                    img = cv2.imread('images/screen.png', 0)
                    swipe(10, img.shape[1]-10, img.shape[0]/2, 200)  # 屏幕移动至最左

                    screenshot()
                    while Image_to_position(chapter[2]) == False:
                        swipe(img.shape[1]/2, img.shape[1] /
                              5, img.shape[0]/2, 1000)
                        time.sleep(2)
                        screenshot()

    screenshot()
    if Image_to_position(chapter[-1]) == False:  # 移动屏幕找最终目标关
        print('如果屏幕有目标关就不应该出现这句话')
        img = cv2.imread('images/screen.png', 0)
        swipe(10, img.shape[1]-10, img.shape[0]/2, 200)  # 屏幕移动至最左
        screenshot()
        while Image_to_position(chapter[-1]) == False:
            swipe(img.shape[1]*0.9, img.shape[1]*0.1, img.shape[0]/2, 2000)
            time.sleep(1)
            screenshot()

    print('find the level successfully')
    click(center[0], center[1])
    chapter_list.chapter_list = []


def chapter_run(n):
    screenshot()
    if Image_to_position('prts_off'):  # 确认点上了代理
        click(center[0], center[1])
    images_ = ['start-go1', 'start-go2']
    images = ['end', 'level up', 'report']
    round = 0
    while True:
        while True:
            screenshot()
            now = ''
            for image in images_:
                if Image_to_position(image, m=0):
                    print(image)
                    now = image
                    click(center[0], center[1])
            if now == 'start-go2':
                print('进入完成')
                break

        if round == 0:
            time_start = time.perf_counter()
            print('第一次循环')
            while True:
                time.sleep(random_time+8)
                screenshot()
                for image in images:
                    if Image_to_position(image, m=0):
                        print(image)
                        now = image
                        time.sleep(1)
                        click(center[0], center[1])
                if now == 'end':
                    round += 1
                    time.sleep(3)
                    break
            time_end = time.perf_counter()
            time_wait = (time_end-time_start)
            print(time_wait)
        else:
            print('待机开始')
            time.sleep(time_wait)
            while True:
                screenshot()
                for image in images:
                    if Image_to_position(image, m=0):
                        print(image)
                        now = image
                        time.sleep(2)
                        click(center[0], center[1])
                if now == 'end':
                    round += 1
                    time.sleep(1)
                    break
        if round == n:
            break


if __name__ == "__main__":
    __running.set()
    chapter_run(3)
