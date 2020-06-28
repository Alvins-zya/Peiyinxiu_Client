import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot,QObject,Signal
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2 import QtCore,QtGui
import PySide2.QtWidgets
import os
import subprocess
import threading
import re
import time
import sys
class Ui_Main(QObject):
    # 定义你的信号
    output_str = QtCore.Signal(str)
    def __init__(self):
        super(Ui_Main, self).__init__()
        # 从文件中加载UI定义
        qfile = QFile('Test.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile)
        self.ui.pushButton.clicked.connect(self.start_thread)


    # 按钮点击触发的函数
    def start_thread(self):
        # 创建线程执行函数
        t1 = threading.Thread(target=self.output)
        print("start")
        t1.start()

    # 执行shell指令
    def output(self):
        T = os.system('adb devices')
        self.ui.textEdit.insertPlainText(T)


    # 用于接受信号数据的槽函数
    @Slot(str)
    def update(self, str):
        print(str)
        # 在文本输入框末尾添加新收到的字符数据
        self.textEdit.insertPlainText(str)
app = QApplication([])
stats = Ui_Main()
stats.ui.show()
app.exec_()