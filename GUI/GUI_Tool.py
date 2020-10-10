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
    signal_Mem_max = pyqtSignal(int)
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
        self.flag = 0
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
        self.ui.file_path_clear.clicked.connect(self.File_path_clear)
        self.ui.output_clear.clicked.connect(self.Output_clear)
        self.ui.clear_apps_data.clicked.connect(self.Clear_apps_data)
        self.ui.clear_app_data.clicked.connect(self.Clear_app_data)
        self.ui.delete_dubbing.clicked.connect(self.Delete_dub)
        self.ui.deletes_dubbing.clicked.connect(self.Delete_batch_dub)
        self.ui.Memory_start.clicked.connect(self.Run_Thread)
        self.ui.Memory_stop.clicked.connect(self.Stop_Mem)
        self.signal_Mem_max.connect(self.Show_Mem_Max)
        self.ui.Flow.clicked.connect(self.Get_send_recv)
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
            dev_name.append(dev.read().rstrip('\n'))
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
            T.join()

    #应用内存获取
    def Memory_info(self):
        Dev = self.ui.put_device.toPlainText()
        if len(Dev) !=0:
            cmd = r'adb -s %s shell dumpsys meminfo com.happyteam.dubbingshow | findstr "TOTAL"'%(Dev)
            run_cmd = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
            run_cmd.wait()
            result_out = run_cmd.stdout.readlines()
            str_out = map(str,result_out)
            num = []
            for i in str_out:
                num.append(int(re.findall('\d+',i)[0]))
            return (num[0])
        else:
            return 0

    #内存筛选
    def Memory_filter(self):
        self.flag = 1
        Men_list = []
        while True:
            if self.flag == 1:
                Mem = self.Memory_info()
                Mem_Mb = int(int(Mem)/1024)
                if Mem == 0:
                    pass
                else:
                    self.signal.emit(Mem_Mb)
                Men_list.append(Mem_Mb)
                self.signal_Mem_max.emit(max(Men_list))
                time.sleep(5)
            else:
                break

    #显示内存
    def Show_Mem(self,Mem):
        self.ui.output.append(str(Mem))

    #显示内存最大值
    def Show_Mem_Max(self,max):
        self.ui.Mem_show_max.setPlainText(str(max))

    def Run_Thread(self):
        self.ui.output.append(str('===开始显示内存==='))
        T = threading.Thread(target=self.Memory_filter)
        T.start()

    #停止获取内存
    def Stop_Mem(self):
        self.flag=0
        self.ui.output.append(str('===已停止==='))

    #批量启动APP
    def starts(self):
        self.ui.output.append(str('===开始批量启动APP==='))
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
        self.ui.output.append(str('===开始批量关闭APP==='))
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
        self.ui.output.append(str('===批量关机==='))
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

    #批量清空应用数据
    def Clear_apps_data(self):
        self.ui.output.append(str('===开始批量清除dubbing文件==='))
        dev = self.get_conn_dev()
        cmd_list =  []
        for d in dev:
            cmd = "adb -s %s shell pm clear com.happyteam.dubbingshow"%(d)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)
        for i in range(threads_count):
            t = threading.Thread(target=self.excute,args=(cmd_list[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()
        self.ui.output.append(str('===批量清除成功==='))

    #单设备清空应用数据
    def Clear_app_data(self):
        dev = self.ui.put_device.toPlainText()
        dev_list = []
        cmd_list = []
        dev_list.append(dev)
        for i in dev_list:
            cmd = "adb -s %s shell pm clear com.happyteam.dubbingshow " % (i)
            cmd_list.append(cmd)
        threads_count = len(cmd_list)
        for i in range(threads_count):
            T = threading.Thread(target=self.excute, args=(cmd_list[i],))
            T.start()
            T.join()
        time.sleep(1)

    #批量删除手机dubbing文件夹
    def Delete_batch_dub(self):
        self.ui.output.append(str('===开始批量删除dubbing文件==='))
        dev = self.get_conn_dev()
        cmd_list = []
        for d in dev:
            cmd = "adb -s %s shell rm -r /sdcard/dubbing"%(d)
            cmd_list.append(cmd)

        threads = []
        threads_count = len(cmd_list)
        for i in range(threads_count):
            T = threading.Thread(target=self.excute,args=(cmd_list[i],))
            threads.append(T)

        for x in range(threads_count):
            time.sleep(1)
            threads[i].start()

        for y in range(threads_count):
            threads[i].join()
        self.ui.output.append(str('===已完成批量删除dubbing文件==='))
    #单设备删除手机dubbing文件夹
    def Delete_dub(self):
        self.ui.output.append(str('===开始==='))
        dev = self.ui.put_device.toPlainText()
        dev_list = []
        cmd_list = []
        dev_list.append(dev)
        for d in dev_list:
            cmd = "adb -s %s shell rm -r /sdcard/dubbing"%(d)
            cmd_list.append(cmd)

        thread_list = len(cmd_list)
        for i in range(thread_list):
            T = threading.Thread(target=self.excute,args=(cmd_list[i],))
            T.start()
        time.sleep(1)
        self.ui.output.append(str('===结束==='))

    #获取应用pid
    def Get_app_pid(self):
        Dev = self.ui.put_device.toPlainText()
        p = os.popen('adb -s %s shell ps | findstr "com.happyteam.dubbingshow"'%(Dev))
        outstr = p.readline()
        pid = re.findall(r'      (.*?) ', outstr)
        return pid
    #获取应用uid
    def Get_app_uid(self):
        p = self.Get_app_pid()
        Dev = self.ui.put_device.toPlainText()
        U = os.popen('adb -s %s shell cat /proc/%s/status'%(Dev,p[0]))
        out = U.read()
        uid = re.findall(r'Uid:\t(.*?)\t',out)
        return uid

    #获取应用上传、下载流量
    def Get_send_recv(self):
        self.ui.output.append(str("应用上传流量"))
        U = self.Get_app_uid()
        Dev = self.ui.put_device.toPlainText()
        send = os.popen('adb -s %s shell cat /proc/uid_stat/%s/tcp_snd'%(Dev,U[0]))
        send_out = send.read()
        send_Mb = int(int(send_out)/1024/1024)
        self.ui.output.append(str('%s\Mb'%send_Mb))
        self.ui.output.append(str("应用下载流量"))
        recv = os.popen('adb -s %s shell cat /proc/uid_stat/%s/tcp_rcv'%(Dev,U[0]))
        recv_out = recv.read()
        recv_Mb = int(int(recv_out)/1024/1024)
        self.ui.output.append(str('%s\Mb'%recv_Mb))

    #清空设备列表
    def clears(self):
        self.listWidget.clear()

    #清空单个设备号输入框
    def Single_clear(self):
        self.put_device.clear()

    #清空文件路径输入框
    def File_path_clear(self):
        self.file_path.clear()

    #输出结果至GUI界面
    def outputs(self,info):
        self.ui.output.append(str(info))

    #清空输出结果
    def Output_clear(self):
        self.output.clear()




if __name__=="__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('show.ico'))
    stats = Stats()
    stats.show()
    app.exec_()
    sys.exit(0)