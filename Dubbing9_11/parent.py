
import unittest
import warnings

from operate.Driver_Operate import BaseOperate

soucred_id = 'com.happyteam.dubbingshow:id/'
class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = BaseOperate()

    @classmethod
    def tearDownClass(self):
        print('===测试结束===')


