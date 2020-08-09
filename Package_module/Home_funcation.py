#coding=utf-8
'''
首页功能列表
'''
from Public.Driver_Operate import BaseOperate,resource_id
import time

class Home():
    def __init__(self):
        self.driver = BaseOperate()
        self.id = resource_id
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()

    def tips(self):
        self.driver.find_id(self.id + 'img_hot').click()
        time.sleep(2)
        self.driver.tap(self.x * 0.5,self.y * 0.5)
        time.sleep(2)

    def task_list(self):
        self.driver.find_id(self.id + 'task_box').click()
        self.driver.wait_id(self.id + 'desc')
        tasks = self.driver.find_ids(self.id + 'desc')
        assert len(tasks) == 5
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    def Home_search(self):
        self.driver.find_id(self.id + 'iv_search').click()
        self.driver.wait_id(self.id + 'txtKeyword')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    def Source_search(self):
        self.driver.find_id(self.id + 'tv_source').click()
        time.sleep(2)
        hot_sources = self.driver.find_ids(self.id + 'tv')
        for i in range(len(hot_sources)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    def Workes_search(self):
        self.driver.find_id(self.id + 'tv_work').click()
        time.sleep(2)
        hot_workes = self.driver.find_ids(self.id + 'tv')
        for i in range(len(hot_workes)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    def User_search(self):
        self.driver.find_id(self.id + 'tv_user').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').click()
        user_list = ['148207791','152726825','159420264','141130466']
        for i in user_list:
            self.driver.find_id(self.id +'txtKeyword').send_keys(i)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSearch').click()
            time.sleep(2)
            self.driver.wait_id(self.id +'userhead')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    def User_recommend(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(2)

    def Work_list_load(self):
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    def touch_into_video(self):
        #点击作品封面进入视频详情
        imgs = self.driver.find_ids(self.id + 'film_img2')
        for i in range(len(imgs)):
            self.driver.find_ids(self.id + 'film_img2')[i].click()
            self.driver.wait_id(self.id + 'btnBack')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        #点击用户头像进入视频详情
        self.driver.find_id(self.id + 'user_head').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        #点击作品标题进入视频详情
        self.driver.find_id(self.id + 'title2').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        #点击作品标签
        self.driver.find_id(self.id + 'film2_channel1').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film2_channel2').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)











