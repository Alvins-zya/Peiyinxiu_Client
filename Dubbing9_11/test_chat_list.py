import unittest
import pytest
'''
语聊主界面功能测试用例
'''
soucred_id = 'com.happyteam.dubbingshow:id/'

@pytest.mark.usefixtures('driver')
def test1(self,driver):
    driver.lanuch_app()
    driver.wait_id(soucred_id + 'task_box')
    driver.find_id(soucred_id + 'btn_more').click()








if __name__ == '__main__':
    pytest.main(["-s", "test_chat_list.py"])
