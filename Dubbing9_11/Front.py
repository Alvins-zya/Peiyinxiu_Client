
import unittest
import warnings


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
        print('===测试结束===')

