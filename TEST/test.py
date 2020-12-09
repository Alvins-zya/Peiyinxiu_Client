#coding = utf-8
import time
import os,sys,re
import threading
import warnings
import subprocess
from Public.Driver_Operate import BaseOperate
import unittest

file = open('D:\Git_pyhthon\Package_module\Elemets.txt','r',encoding='UTF-8')

class test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = BaseOperate()
    @classmethod
    def tearDownClass(self):
        pass

    def test_a(self):
        el_list = self.driver.page_sources()
        el = 'userhead'
        if el in el_list:
            print(file)
            self.driver.find_id_click('userhead')
            self.driver.wait_id('ll_fan')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)





