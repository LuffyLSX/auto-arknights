# auto-arknights
明日方舟自动刷图脚本

利用adb控制mumu模拟器，并通过截图进行图像识别来点击，已经实现了基本的刷图功能

由于我的模拟器和显示器都是2k分辨率，可能在其他分辨率下会无法准确识别图像，可以根据自己的情况修改

之后我也会尽量适配1080p的分辨率，并添加其他的功能

# 安装python并添加opencv模块

https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624

打开cmd输入 pip install opencv-python
![Image text](https://github.com/LuffyLSX/auto-arknights/blob/master/readme/demo2.png)
如图显示表示安装成功

# 如何使用

*使用之前要先安装python-opencv*

1.将adb压缩包解压后的三个文件复制到C:\Windows 目录下

2.打开模拟器并选择要刷的地图，注意要将代理指挥勾上√
![Image text](https://github.com/LuffyLSX/auto-arknights/blob/master/readme/demo.png)

3.运行auto-game.py文件，输入要刷的次数即可

# 更新日志

2019-8-31

1.0 增加了对2k以下分辨率的支持（仅限16:9）~~应该没有大佬用4k来玩吧~~

2.0 向分支里加了一个巨丑的gui
