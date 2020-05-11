import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test1(self):
        print('1')
        self.skipTest('跳过')
        print(3)

    def test2(self):
        print('4')

if __name__ == '__main__':
    unittest.main()
