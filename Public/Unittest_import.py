
import unittest
import warnings
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Public.Driver_Operate import BaseOperate,resource_id
from Package_module.happyteam_dubbingshow import Home
# ,Home_Function,Dub,Follow,Live,Material,Person,Video_detail,Circle,Society

class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.ID = resource_id
        # self.D = Dub()
        self.H = Home(Dubbing)
        # self.Home_enter = Home_Function()
        # self.L = Live()
        # self.F = Follow()
        # self.M = Material()
        # self.P = Person()
        # self.V = Video_detail()
        # self.C = Circle()
        # self.S = Society()
        # self.driver = BaseOperate()

    @classmethod
    def tearDownClass(self):
        pass

    def test_a(self):
        self.H.Task_list()
        # self.driver.wait_id_click('task_box')
        # self.driver.wait_id('rl1')
