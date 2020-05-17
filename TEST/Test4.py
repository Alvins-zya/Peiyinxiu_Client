import unittest
# import re
# import random
# from selenium import webdriver

class Test(unittest.TestCase):

    def test(self):
        list = '34'
        list1 = '35.0'
        assert list in list1


if __name__ == '__main__':
    unittest.main()
