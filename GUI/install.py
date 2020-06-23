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
class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        qfile = QFile('service.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile)

        self.ui.pushButton.clicked.connect(self.devices)
        self.ui.pushButton_2.clicked.connect(self.main)
        self.ui.pushButton_3.clicked.connect(self.single_install)

    def get_conn_dev(self):
        p = os.popen('adb devices')
        outstr = p.read()
        print(outstr)
        connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
        return connectdeviceid
    def devices(self):
        devices = Stats().get_conn_dev()
        for dev in devices:
            self.ui.textEdit.setText(dev+',')

    def excute(self,cmd):
        subprocess.Popen(cmd, shell=True)

    def main(self):
        connectdevice = Stats().get_conn_dev()
        commands = []
        path_file = self.ui.textEdit_2.toPlainText()
        Re_file = re.findall(r'file:///(.*)',path_file)
        str_file = ''.join(Re_file)
        for device in connectdevice:
            cmd = "adb -s %s install -r %s" % (device, str_file)
            commands.append(cmd)
        # self.ui.textEdit_3.setText(cmd)

        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=Stats().excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()


    def single_install(self):
        dev = self.ui.textEdit_4.toPlainText()
        print(dev)
        commands = []
        path_file = self.ui.textEdit_2.toPlainText()
        Re_file = re.findall(r'file:///(.*)', path_file)
        str_file = ''.join(Re_file)
        cmd = "adb -s %s install -r %s" % (dev, str_file)
        commands.append(cmd)
        # self.ui.textEdit_3.setText(cmd)

        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=Stats().excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()