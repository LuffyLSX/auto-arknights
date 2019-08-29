import os,time
import cv2


def connect():
    try:
        os.system('adb connect 127.0.0.1:7555')
    except:
        print('连接失败')

def click(x, y):
    os.system('adb shell input tap %s %s' % (x, y))

def screenshot():
    path = os.path.abspath('.') + '\images'
    os.system('adb shell screencap /data/screen.png')
    os.system('adb pull /data/screen.png %s' % path)

def Image_to_position(image):
    image_path = 'images/' + str(image) + '.png'
    screenshot()
    screen = cv2.imread('images/screen.png', 0)
    template = cv2.imread(image_path, 0)
    methods = cv2.TM_CCOEFF_NORMED
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, methods)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val > 0.8:
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        click(center[0], center[1])
        return True
    else:
        return False

def run():
    Image_to_position('start-go1')
    time.sleep(1)
    Image_to_position('start-go2')
    while not Image_to_position('end'):
        time.sleep(5)


if __name__ == '__main__':
    connect()
    for i in range(1):
        run()
        time.sleep(3)
        
