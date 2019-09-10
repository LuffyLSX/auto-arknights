import sys, multiprocessing
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import Ui_arknight_ui
from PyQt5 import QtWidgets


if __name__ == '__main__':
    multiprocessing.freeze_support() #只要在你的程序的入口中加上这行代码加上就可以了
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_arknight_ui.mywindow()
    w.show()
    sys.exit(app.exec_())
