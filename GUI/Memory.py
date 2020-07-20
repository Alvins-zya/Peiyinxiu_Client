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
            cmd = r'adb shell dumpsys meminfo com.happyteam.dubbingshow  | findstr "TOTAL"'  # % apk_file
            pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            pr.wait()  # 不会马上返回输出的命令，需要等待
            out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
            str_out = map(str, out)
            number = []
            for i in str_out:
                number.append(int(re.findall('\d+', i)[0]))  # 正则匹配出字符串中的数字列表，按选择列表[0]的数字大写排序
            return (number[0])
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
