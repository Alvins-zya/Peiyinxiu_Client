from itertools import chain
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,time
import threading,subprocess
from PyQt5.uic import loadUi
import subprocess
import threading
import re


class Stats(QWidget):
    signal = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        qfile = QFile('service.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = loadUi('service.ui',self)

        self.ui.devices_list.clicked.connect(self.show_dev)
        self.ui.install_apps.clicked.connect(self.install_Apps)
        self.ui.install_app.clicked.connect(self.single_install)
        self.ui.uninstall_apps.clicked.connect(self.uninstalls)
        self.ui.uninstall_app.clicked.connect(self.uninstall)
        self.ui.close_apps.clicked.connect(self.closes)
        self.ui.start_apps.clicked.connect(self.starts)
        self.ui.shutdow.clicked.connect(self.close_dev)
        self.ui.clear_devices.clicked.connect(self.clears)
        self.ui.single_clear.clicked.connect(self.Single_clear)
        self.signal.connect(self.outputs)

    def get_conn_dev(self):
        p = os.popen('adb devices')
        outstr = p.read()
        # print(outstr)
        connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
        return connectdeviceid

    def get_dev_name(self):
        devs = self.get_conn_dev()
        dev_name = []
        for d in devs:
            dev = os.popen('adb -s %s shell getprop ro.product.model'%d)
            dev_name.append(dev.read())
        return dev_name

    #设备列表
    def devices(self):
        devices = self.get_conn_dev()
        for dev in devices:
            self.ui.listWidget.addItem(dev)
        self.ui.listWidget.addItem(str(len(devices)))
        self.signal.emit(object)

    #将设备名称显示在窗口中
    def show_dev(self):
        devs = self.get_dev_name()
        dev_info = self.get_conn_dev()
        lists = list(chain.from_iterable(zip(devs,dev_info)))
        for info in lists:
            self.ui.listWidget.addItem(info)
        self.signal.emit(object)



    def excute(self,cmd):
        replay =subprocess.getoutput(cmd)
        self.signal.emit(replay)

    #批量安装app
    def install_Apps(self):
        connectdevice = self.get_conn_dev()
        cmd_list = []
        path_file = self.ui.file_path.toPlainText()
        Re_file = re.findall(r'file:///(.*)',path_file)
        str_file = ''.join(Re_file)
        for device in connectdevice:
            cmd = "adb -s %s install -r %s" % (device, str_file)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错se
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

    #单设备安装app
    def single_install(self):
        dev = self.ui.put_device.toPlainText()
        path_file = self.ui.file_path.toPlainText()
        Re_file = re.findall(r'file:///(.*)', path_file)
        str_file = ''.join(Re_file)
        dev_list = []
        cmd_list = []
        dev_list.append(dev)
        for i in dev_list:
            cmd = "adb -s %s install -r %s" % (i, str_file)
            cmd_list.append(cmd)
        threads_count = len(cmd_list)
        for i in range(threads_count):
            T = threading.Thread(target=self.excute, args=(cmd_list[i],))
            T.start()
            # T.join()

    #批量卸载APP
    def uninstalls(self):
        connectdevice = self.get_conn_dev()
        cmd_list = []
        for device in connectdevice:
            cmd = "adb -s %s uninstall com.happyteam.dubbingshow" % (device)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

    #单设备卸载APP
    def uninstall(self):
        dev = self.ui.put_device.toPlainText()
        dev_list = []
        cmd_list = []
        dev_list.append(dev)
        for i in dev_list:
            cmd = "adb -s %s uninstall com.happyteam.dubbingshow" % (i)
            cmd_list.append(cmd)

        threads_count = len(cmd_list)
        for i in range(threads_count):
            T = threading.Thread(target=self.excute, args=(cmd_list[i],))
            T.start()
            # T.join()

    #批量启动APP
    def starts(self):
        connectdevice = self.get_conn_dev()
        cmd_list = []
        for device in connectdevice:
            cmd = "adb -s %s shell am start -W -n com.happyteam.dubbingshow/.ui.StartActivity" % (device)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

    #批量关闭APP
    def closes(self):
        connectdevice = self.get_conn_dev()
        cmd_list = []
        for device in connectdevice:
            cmd = "adb -s %s shell am force-stop com.happyteam.dubbingshow" % (device)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

    #批量关机
    def close_dev(self):
        connectdevice = self.get_conn_dev()
        cmd_list = []
        for device in connectdevice:
            cmd = "adb -s %s shell reboot -p" % (device)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

    #清空设备列表
    def clears(self):
        self.listWidget.clear()

    #清空单个设备号输入框
    def Single_clear(self):
        self.put_device.clear()

    #输出结果至GUI界面
    def outputs(self,info):
        self.ui.output.append(str(info))





if __name__=="__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('show.ico'))
    stats = Stats()
    stats.show()
    app.exec_()
    sys.exit(0)