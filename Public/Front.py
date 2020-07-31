
import unittest
import warnings
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Package_module.Dubbing_funcation import Dubb_funcation
from Package_module.Live_funcation import Live_funcation

class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.Dub = Dubb_funcation()
        self.Live = Live_funcation()


    @classmethod
    def tearDownClass(self):
        pass

