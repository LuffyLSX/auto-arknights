# -*- coding:utf-8 -*-
# @author：LuffyLSX、DSK
# @version：1.2
# @update time：2019年9月3日

import os,time
import cv2
import chapter_list #字典

a=[]

def connect():
    try:
        os.system('adb connect 127.0.0.1:7555')
    except:
        print('连接失败')

def click(x, y):
    os.system('adb shell input tap %s %s' % (x, y))
    time.sleep(0.5)

def swipe(x1, x2, y1,t):
    os.system('adb shell input swipe %s %s %s %s %s' % (x1, y1, x2, y1, t))


def screenshot():
    path = os.path.abspath('.') + '\images'
    os.system('adb shell screencap /data/screen.png')
    os.system('adb pull /data/screen.png %s' % path)

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

def chapter_selet():#没有GUI暂时没什么乱用的自定义刷图线路模块
    
    Chinese_note =('没有GUI凑合用，活动511/3、524，以任意字符结尾')

    
    chapter = ['chapter_start']
    n = 1
    print ('输入你要刷的关卡路线（回车进行下一步）\n ')
    while True:#路线输入模块
        print(Chinese_note)#未完成，用GUI代替
        
        
        get_input=input()
        get_the_chapter=eval('chapter_list.'+str(chapter[n-1])+ "('%s')"  %get_input )
        print(get_the_chapter)
        chapter.append (get_the_chapter)
        print(chapter)
        print(n)
        if chapter[n]=='end':
            chapter.pop()
            print('去掉了end',chapter)
            break 
        n=n+1

    global a
    a =(int(input('输入刷图次数:')))

    #点击模块
    before_end=True 
    while before_end:
        screenshot()
        for image in chapter:
            if Image_to_position(image) != False:
                print(image)
                click(center[0], center[1])
                if image==chapter[-2]:
                    before_end=False

    screenshot()
    if Image_to_position(chapter[-1]) == False:#移动屏幕找最终目标关
        print('如果屏幕有目标关就不应该出现这句话')
        img = cv2.imread('images/screen.png', 0)
        swipe(10,img.shape[1]-10,img.shape[0]/2,200)#屏幕移动至最左
        time.sleep(2)
        while Image_to_position(chapter[-1]) == False:
            swipe(img.shape[1]/2,img.shape[1]/4,img.shape[0]/2, 500)
            time.sleep(2)
            
        
    print('find the level successfully')
    click(center[0], center[1])
    #确认点上了代理
    
    screenshot()
    if Image_to_position('prts_off') == True:#移动屏幕找最终目标关
        click(center[0], center[1])


def run(n):
    images = ['start-go1', 'start-go2', 'end', 'level up']
    round = 0
    # Image_to_position('start-go1')
    # time.sleep(2)
    # Image_to_position('start-go2')
    # while not Image_to_position('end'):
    #     time.sleep(5)
    while True:
        screenshot()
        now = ''
        for image in images:
            if Image_to_position(image, m = 0) != False:
                print(image)
                now = image
                time.sleep(0.5)
                click(center[0], center[1])
                
        if now == 'end':
            time.sleep(0.8)
            round = round + 1
            if round == n:
                break
        

if __name__ == '__main__':
    connect()
    '''for i in range(int(input('输入刷图次数' + '\n'))):
        run()
        time.sleep(3)'''
    print('正在启动中……')
    time.sleep(5)
    chapter_selet()
    run(a)
    os.system('adb kill-server')

