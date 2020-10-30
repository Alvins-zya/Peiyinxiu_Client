#coding=utf-8
from Public.Unittest_import import Dubbing
import unittest

class Test_Live(Dubbing):
    def test_a_into_out(self):
        while True:
            self.Live.Into_live_detail()



if __name__=="__main__":
    unittest.main()