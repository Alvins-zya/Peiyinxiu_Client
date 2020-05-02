import unittest
import pytest
from selenium import webdriver

class TestFixture(unittest.TestCase):

    @pytest.fixture()
    def init_driver(self):
        driver = webdriver.Chrome()
        driver.get("http://baidu.com")
        yield driver
        driver.quit()
    @pytest.mark.usefixtures('init_driver')
    def test_fixture(self):    #fixture 函数名作为参数传入
        init_driver.find_element_by_id("kw").send_keys("selenium 配置")
        init_driver.find_element_by_id("su").submit()
        #函数名代表了fixture 的返回值，即driver
        print("我在测试用例中直接调用fixture")


if __name__ == "__main__":
    pytest.main(["-s", "Test4.py"])