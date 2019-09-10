# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Luffy\Desktop\auto-arknights\arknight_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from auto_game import*


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(600, 650)
        Form.setMinimumSize(QtCore.QSize(600, 650))
        Form.setMaximumSize(QtCore.QSize(600, 650))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        Form.setToolTip("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 480, 131, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arknights.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 600, 200))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setMidLineWidth(0)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 480, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(300, 370, 40, 20))
        self.spinBox.setObjectName("spinBox")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setGeometry(QtCore.QRect(230, 280, 130, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setLineWidth(3)
        self.lcdNumber.setMidLineWidth(1)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 370, 54, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 250, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.spinBox.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.connect_to_sim)
        self.pushButton_2.clicked.connect(self.start_script)
        self.spinBox.valueChanged['int'].connect(self.lcdNumber.display)

        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.spinBox)
        Form.setTabOrder(self.spinBox, self.textBrowser)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "明日方舟小助手"))
        self.pushButton.setText(_translate("Form", "连接模拟器"))
        self.pushButton_2.setText(_translate("Form", "启动脚本"))
        self.label.setText(_translate("Form", "刷图次数"))
        self.label_2.setText(_translate("Form", "剩余次数"))

class mywindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.work = connectThread()
        self.work.connect_signal.connect(self.addText)
        self.work1 = disconnectThread()
        self.work1.disconnect_signal.connect(self.addText)
        self.job = start_scriptThread()
        self.job.script_str.connect(self.addText)
        self.job.script_int.connect(self.lcdchange)
        self.job.script_signal.connect(self.func)
    
    def connect_to_sim(self):
        sender = self.sender()
        # print(sender.text())
        if (sender.text() == '连接模拟器') | (sender.text() == '重新连接'): 
            self.pushButton.setEnabled(False)
            self.textBrowser.append('正在连接...')
            self.work.start()
        else:
            self.pushButton.setEnabled(False)
            self.work1.start()

    def addText(self, str):
        if str == '连接失败':
            self.textBrowser.append(str)
            self.pushButton.setText('重新连接')
            self.pushButton.setEnabled(True)
        elif str == '已断开连接':
            self.textBrowser.append(str)
            self.pushButton.setText('连接模拟器') 
            self.pushButton.setEnabled(True)
        elif str == 'end':
            self.textBrowser.append('刷完啦！')
        else:
            self.pushButton.setText('断开连接')
            self.pushButton.setEnabled(True)
            self.textBrowser.append(str)

    def lcdchange(self, int):
        self.lcdNumber.display(int)
    
    def start_script(self):
        sender = self.sender()
        if sender.text() == '启动脚本':
            self.pushButton_2.setText('中止脚本')
            self.job.start()
            self.spinBox.setEnabled(False)
            self.spinBox.valueChanged.disconnect
            global t
            t = self.spinBox.value()
        elif sender.text() == '中止脚本':
            self.pushButton_2.setText('启动脚本')
            self.textBrowser.append('已中止脚本')
            self.job.terminate()
            self.func('end')

    def func(self, str):
        if str == 'end':
            self.spinBox.valueChanged['int'].connect(self.lcdNumber.display)
            self.spinBox.setEnabled(True)
            self.spinBox.setValue(0)
               

      
class connectThread(QThread):
    # 定义一个信号
    connect_signal = pyqtSignal(str)
    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        f = os.popen(r"adb connect 127.0.0.1:7555", "r")
        console = f.readlines()
        f.close()
        for i in console:
            self.connect_signal.emit(i.replace("\n", ""))

        if console[-1].find('unable') == -1:
            self.connect_signal.emit('连接成功')
        else:
            self.connect_signal.emit('连接失败')
       

class disconnectThread(QThread):
    # 定义一个信号
    disconnect_signal = pyqtSignal(str)
    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        f = os.popen(r"adb kill-server", "r")
        console = f.readlines()
        f.close()
        for i in console:
            self.disconnect_signal.emit(i.replace("\n", ""))
        self.disconnect_signal.emit('已断开连接')

class start_scriptThread(QThread):
    # 定义一个信号
    script_str = pyqtSignal(str)
    script_int = pyqtSignal(int)
    script_signal = pyqtSignal(str)
    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        images = ['start-go1', 'start-go2', 'end', 'report', 'level up']
        round = 0
        now = ''
        while True:
            screenshot()
            for image in images:
                center = Image_to_position(image, m = 0)
                if center != False:
                    now = image
                    time.sleep(0.5)
                    click(center[0], center[1])
            self.script_str.emit('脚本正在运行中...')
            if now == 'end':
                time.sleep(1)
                round = round + 1
                self.script_int.emit(t - round)   
                if round == t:
                    self.script_signal.emit(now)
                    self.script_str.emit(now)
                    break



