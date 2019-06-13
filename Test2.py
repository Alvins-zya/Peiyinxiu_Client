#coding = utf-8
#防止中文显示乱码
#coding = gb18030

# import random
import os

from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


dev = 'b490dce3'


desired_caps = {}
desired_caps['platformName'] ='Android'
desired_caps['deviceName'] = dev
desired_caps['udid'] = dev
desired_caps['platformVersion'] = '7.1.2'
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


driver = webdriver.Remote('http://localhost:4740/wd/hub', desired_caps)


time.sleep(2)

def toast(x):

    el = '%s'%x
    WebDriverWait(driver,10,0.01).until(lambda driver:driver.find_element_by_xpath(el))
    toast = driver.find_element_by_xpath(el).text
    return toast

def test():
    try:
        get_tost = toast('//android.widget.Toast')
        print(get_tost,'1')
    except:
        try:
            driver.find_element_by_xpath('大家')
        except:
            try:
                driver.find_element_by_xpath('我们')
            except:
                try:
                    driver.find_element_by_xpath('hello')
                except:
                    print("2")


if __name__=="__main__":
    test()