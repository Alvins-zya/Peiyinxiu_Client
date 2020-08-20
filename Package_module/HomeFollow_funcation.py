#coding=utf-8
'''
首页发现界面功能封装
'''
from Public.Driver_Operate import BaseOperate,resource_id
from Package_module.Video_detail_funcation import Video_detail_functions
import time

class Follow():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入首页关注界面
    def into_follow(self):
        self.driver.find_id(sourced_id + 'ivCirclesTab').click()
        self.driver.wait_id(sourced_id + 'musicPlayView')
        time.sleep(2)

    #语聊通知动画
    def chat_notice(self):
        self.driver.find_id(sourced_id + 'ivCirclesTab').click()
        self.driver.wait_id(sourced_id + 'musicPlayView')
        self.driver.find_id(sourced_id + 'musicPlayView').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'musicPlayView').click()
        time.sleep(2)

    #关注界面点击播放视频
    def Play_video(self):
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.wait_download(sourced_id + 'play')

    #关注界面进入视频详情
    def into_video_detail(self):
        self.driver.find_id(sourced_id + 'content').click()
        self.driver.wait_id(sourced_id + 'tv_video_detail_title')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)


