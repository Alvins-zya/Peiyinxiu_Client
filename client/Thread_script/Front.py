
import unittest
import warnings
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from client.Package_module import Dubb_funcation
from client.Package_module import Live_funcation
from client.Public.Driver_Operate import BaseOperate
class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.Dub = Dubb_funcation()
        self.Live = Live_funcation()
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()



    @classmethod
    def tearDownClass(self):
        pass

