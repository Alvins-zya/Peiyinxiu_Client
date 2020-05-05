import unittest
import pytest
from selenium import webdriver

def test():
    line = ['1','2']
    line2 = ['3','2']
    # print(len(line))
    # check = 10
    assert line == line2,'字符数不相等'

if __name__=="__main__":
    test()