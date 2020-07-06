from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os,sys,re,time
import threading,subprocess


class Performance(QWidget):
    Signal = pyqtSignal(int)
    Signal1 =pyqtSignal(int)
    def __init__(self):
        super(Performance,self).__init__()
        file = QFile('tools.ui')
        file.open(QFile.ReadOnly)
        file.close()
        self.flag = 0
        self.ui = loadUi('tools.ui',self)
        self.ui.Memory.clicked.connect(self.Thread)
        self.ui.stop_run.clicked.connect(self.stop)
        self.Signal.connect(self.Text_show)
        self.Signal1.connect(self.show_Max)



    def getTotalPss(self):
        p = os.popen('adb devices')
        outstr = p.read()
        connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
        if len(connectdeviceid) != 0:
            lines = os.popen("adb shell dumpsys meminfo com.happyteam.dubbingshow").readlines() #逐行读取
            total = "TOTAL"
            mem_list = []
            for line in lines:
                if re.findall(total, line): # 找到TOTAL 这一行
                    lis = line.split(" ")  #将这一行，按空格分割成一个list
                    while '' in lis:       # 将list中的空元素删除
                        lis.remove('')
            return (lis[1]) #返回总共内存使用
        else:
            return 0

    def run(self):
        self.flag =1
        mem_list = []
        while True:
            if self.flag == 1:
                mem = self.getTotalPss()
                Men_Mb = int(int(mem) / 1024)
                time.sleep(1)
                if mem == '0':
                    self.Signal.emit(mem)
                else:
                    self.Signal.emit(Men_Mb)
                mem_list.append(Men_Mb)
                if len(mem_list) > 500:
                    mem_list.clear()
                # print(mem_list)
                # print(len(mem_list))
                self.Signal1.emit(max(mem_list))
                # if len(mem_list) > 1:
                #     if mem_list[-1] > mem_list[-2]:
                #         print(mem_list[-1],mem_list[-2])
                #         list_max = mem_list[-1]
                #         self.Signal1.emit(list_max)
                #     else:
                #         print('test')

            else:
                break



    def Text_show(self,Mem):
        # print(Mem)
        self.ui.Mem_list.append(str(Mem))

    def show_Max(self,info):
        self.ui.Max_mem.setPlainText(str(info))

    def Thread(self):
        T = threading.Thread(target=self.run)
        T.start()



    def stop(self):
        self.flag = 0

if __name__=="__main__":
    Gui = QApplication(sys.argv)
    P = Performance()
    P.show()
    sys.exit(Gui.exec_())
