# from PySide2.QtWidgets import QApplication, QMessageBox
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtCore import QFile
# from PySide2 import QtCore,QtGui
# import PySide2.QtWidgets
# from PySide2.QtCore import Slot
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import os
import subprocess
import threading
import re
import time
import sys

class Stats(QWidget):
    textWritten = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        qfile = QFile('Test.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = loadUi('Test.ui',self)
        self.ui.pushButton.clicked.connect(self.click)
        self.textWritten.connect(self.output)

    def excute(self,cmd):
        replay = subprocess.getoutput(cmd)
        self.textWritten.emit(replay)

    def click(self):
        self.textWritten.emit('启动。。。。')
        list = ['79URX18B09001391']
        path_file = 'C:/Users/PYX/Desktop/APK/dubbingshow_v9.13.644_official_release_noad.apk'
        cmd_list = []
        for i in list:
            cmd = 'adb -s %s install -r %s'%(i,path_file)
            cmd_list.append(cmd)
        count = len(cmd_list)
        for i in range(count):
            p = threading.Thread(target=self.excute, args=(cmd_list[i],))
            p.start()
            p.join()
    def output(self,info):
        self.ui.textBrowser.setText(str(info))



if __name__=="__main__":
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec_()
    sys.exit(0)