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
        time.sleep(10)
        self.driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_more').click()


