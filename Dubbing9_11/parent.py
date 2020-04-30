
import unittest
import warnings
import pytest

from operate.Driver_Operate import BaseOperate

soucred_id = 'com.happyteam.dubbingshow:id/'
class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()



    @classmethod
    def tearDownClass(self):
        print('===测试结束===')

