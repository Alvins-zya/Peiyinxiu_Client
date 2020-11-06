#encoding: utf-8
'''
@author:alvin.zhu
@file:test_single_mate30.py
@time:2020/10/30 15:24
@Description:

'''
import unittest
import time
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Public.Unittest_import import Dubbing

class test_single(Dubbing):
    def test_Source(self):
        self.D.Material_library_dubble()



if __name__ == '__main__':
    unittest.main()