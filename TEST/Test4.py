import unittest
import re
import random
from selenium import webdriver

class Test(unittest.TestCase):

    def test(self):
        list = ['念白/旁白', '情感语录', '抖音', 'Pia戏', '影视混剪', '古风/仙侠', '萌新', '情感网文', '古风', '萌萌哒', '朗诵', '动漫', '王者荣耀', '桀儿自制', '兔子温柔馆', '朗读', '优酱自制', '声优', '星子自制']
        list.remove('Pia戏')
        print(list)


if __name__ == '__main__':
    unittest.main()
