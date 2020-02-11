import os
import threading
import multiprocessing
from appium import webdriver

class ConcurrentExecution:
      """
      多进程并发安装本地apk
      """
    def __init__(self):
        self.driver_port = [[4700,"127.0.0.1:21503"],[4701,"127.0.0.1:21513"]]

    def android_driver(self,i):
         driver_list = []
         capabilities = {
                "platformName"  : "Android",
                "udid"                   : self.driver_port[i][1],
                "deviceName"      : self.driver_port[i][1],
                "noReset"             : "True"
                 }
         driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(self.driver_port[i][0]),capabilities)
         driver_list.append(driver)
       　return driver_list

     def kill_server(self):
         """
     　    清理appium环境,杀node.exe的进程
           :return:
     　　 """
         server_list = os.popen('tasklist | find "node.exe"').readlines()
         print(server_list)
         if len(server_list)>0:
            os.system("taskkill -F -PID node.exe")

     def start_appium_server(self,j):
         """
           启动appium服务器
           :return:
         """
         li_port = [4700,4701]
         os.system("appium -p {0}".format(li_port[j]))

if __name__ == '__main__':
     obj = ConcurrentExecution()
     obj.kill_server()
     for j in range(2):  #启动服务
           th = threading.Thread(target=obj.start_appium_server,args=(j,))
        　　th.start()
     for i in range(2): #运行
            t = multiprocessing.Process(target=obj.android_driver,args=(i,))
            t.start()