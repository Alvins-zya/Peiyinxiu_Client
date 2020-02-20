import os,re
import threading
import multiprocessing
from appium import webdriver
from Peiyinxiu_Client import get_conn_dev
from selenium.webdriver.support.ui import WebDriverWait

D = get_conn_dev()


def get_version():
    version = []
    for i in range(len(D)):
        platformVersion = os.popen('adb -s %s shell getprop ro.build.version.release'%D[i]).read()
        PV = re.sub('\r|\n','',platformVersion)
        version.append(PV)
    return version

P = get_version()
class ConcurrentExecution:

    def __init__(self):
        self.driver_device = D
        self.driver_Platversion = P
        self.driver_port = [4723,4725,4727,4729,4781,4783]

    def android_driver(self, i,k):
        driver_list = []
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = self.driver_device[i]
        desired_caps['udid'] = self.driver_device[i]
        desired_caps['platformVersion'] = self.driver_Platversion[i]
        desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
        desired_caps['appActivity'] = 'ui.StartActivity'
        desired_caps['appWaitPackage'] = 'com.happyteam.dubbingshow'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['ignoreUnimportantViews'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['newCommandTimeout'] = 10000
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['systemPort'] = 8200
        driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub"%(self.driver_port[i]), desired_caps)
        driver_list.append(driver)
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/film_img2'))
        driver.find_element_by_id('com.happyteam.dubbingshow:id/film_img2').click()
        # return driver_list


    def start_appium_server(self, j):
        """
         启动appium服务器
         :return:
        """
        os.system("appium -p {0}".format(self.driver_port[j]))
    # def run(self,k):
    #     self.driver = k
    #     print(self.driver)
    #     WebDriverWait(self.driver, 20).until(lambda driver: self.driver.find_element_by_id('com.happyteam.dubbingshow:id/film_img2'))
    #     self.driver.find_element_by_id('com.happyteam.dubbingshow:id/film_img2').click()





if __name__ == '__main__':

    obj = ConcurrentExecution()
    counts = len(D)
    for j in range(counts): #启动服务
        th = threading.Thread(target=obj.start_appium_server,args=(j,))
        th.start()


    for i in range(counts):#运行
        t = multiprocessing.Process(target=obj.android_driver, args=(i,))
        t.start()





