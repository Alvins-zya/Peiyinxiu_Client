
import unittest
import warnings
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from operate.Driver_Operate import BaseOperate


class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()



    @classmethod
    def tearDownClass(self):
        pass

