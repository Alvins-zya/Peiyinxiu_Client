#coding=utf-8
'''
create on 2020年2月9日
@author：Alvin_zhu
'''

from selenium.common.exceptions import NoSuchElementException
import time
class KybTest():
    def __init__(self,driver):
        self.driver = driver

    def background(self):
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(3)
        print('check skipBtn')

        try:
            skipBtn = self.driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_more')
            skipBtn.click()
            time.sleep(3)
            try:
                self.driver.find_element_by_id('com.happyteam.dubbingshow:id/boy')
                print('成功')
            except:
                print('失败')
        except NoSuchElementException:
            print('com.happyteam.dubbingshow:id/btn_more')
        # self.driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_more').click()

    def run_start(self):
        self.background()

