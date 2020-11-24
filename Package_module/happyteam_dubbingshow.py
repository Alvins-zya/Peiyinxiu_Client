#encoding: utf-8

'''
@author:alvin.zhu
@file:happyteam_dubbingshow.py
@time:2020/11/6 10:27
@Description:
'''

import datetime
import re
import time, random
from typing import Counter

file = open('D:/Git_pyhthon/Package_module/topic_words.txt', 'r', encoding='UTF-8')
from Public.Driver_Operate import BaseOperate, resource_id


class Home:
    def __init__(self):
        self.driver = BaseOperate()
        self.id = resource_id
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()

    def Tips(self):
        try:
            self.driver.find_id(self.id + 'img_hot')
            self.driver.find_id(self.id + 'img_hot').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'img_hot').click()
            time.sleep(2)
        except:
            pass

    #每日任务列表加载
    def Task_list(self):
        self.driver.find_id(self.id + 'task_box').click()
        self.driver.wait_id(self.id + 'rl1')

    #每日签到
    def Task_daily_attendance(self):
        #奖池
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

        #签到
        self.driver.find_id(self.id + 'rl1').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'img_double')
            self.driver.find_id(self.id + 'img_double').click()
            self.driver.wait_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'img_one').click()
            self.driver.wait_toast('//android.widget.Toast')
        except:
            self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_count1')
        except:
            print('每日签到错误')

    #日常任务
    def Task_Daily_tasks(self):
        check = ['上传一个带频道的作品', '分享作品至朋友圈', '收听语聊10分钟', '用钻石曝光1个作品', '评论5个曝光区作品', '看完5个作品']
        task_list = []
        tasks = self.driver.find_ids(self.id + 'title')
        for i in range(len(tasks)):
            task = self.driver.find_ids(self.id + 'title')[i].text
            task_list.append(task)
        time.sleep(2)
        if sorted(check) != sorted(task_list):
            print('日常任务列表校验错误')
        time.sleep(2)
        for i in range(len(task_list)):
            result = ('{0}, {1}', format(i, task_list[i]))
            num = int(result[1])
            if task_list[num] == '上传一个带频道的作品':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'rl_coor')
                time.sleep(1)
                self.driver.find_id(self.id + 'ivDubbingTab').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'task_box').click()
                time.sleep(2)

            elif task_list[num] == '分享作品至朋友圈':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'll_follow')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)

            elif task_list[num] == '收听语聊10分钟':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'create')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)

            elif task_list[num] == '用钻石曝光1个作品':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'll_follow')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)

            elif task_list[num] == '评论5个曝光区作品':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'filmBg')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)

            elif task_list[num] == '看完5个作品':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'iv_search')
                time.sleep(2)
                self.driver.find_id(self.id + 'task_box').click()
                time.sleep(2)

        time.sleep(2)


#首页搜索
    def Home_search(self):
        self.driver.find_id(self.id + 'iv_search').click()
        self.driver.wait_id(self.id + 'txtKeyword')

    #首页素材搜索
    def Source_search(self):
        self.driver.find_id(self.id + 'tv_source').click()
        time.sleep(2)
        hot_sources = self.driver.find_ids(self.id + 'tv')
        for i in range(len(hot_sources)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'iv_source').click()
            self.driver.wait_id(self.id + 'dubbing_fake')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    # 首页作品搜索
    def Work_search(self):
        self.driver.find_id(self.id + 'tv_work').click()
        time.sleep(2)
        hot_works = self.driver.find_ids(self.id + 'tv')
        for i in range(len(hot_works)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'filmBg')
            self.driver.find_id(self.id + 'filmBg').click()
            self.driver.wait_id(self.id + 'tv_good')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    #首页用户搜索
    def User_search(self):
        self.driver.find_id(self.id + 'tv_user').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').click()
        user_list = ['148207791', '152726825', '159420264', '141130466']
        for i in user_list:
            self.driver.find_id(self.id + 'txtKeyword').send_keys(i)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSearch').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

    #推荐用户
    def User_recommend(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(2)

    #列表上、下滑动
    def Work_list_load(self):
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    #作品列表界面点击进入视频详情
    def Touch_into_video(self):
        #点击作品封面进入视频详情
        self.driver.find_id(self.id + 'film_img2').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #列表界面点击用户头像进入视频详情
        self.driver.find_id(self.id + 'user_head').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #列表界面点击作品标题进入视频详情
        self.driver.find_id(self.id + 'title2').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #列表界面点击作品标签
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

class Home_Function:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    # 进入首页频道列表界面
    def Function_Channel(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(self.id + 'task_box')
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.197, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >= 2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)

        time.sleep(2)
        self.driver.find_xpath('频道').click()
        while True:
            try:
                self.driver.wait_id(self.id + 'tv')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    # 频道界面标签列表
    def Function_Channel_Tvs(self):
        labels = self.driver.find_ids(self.id + 'tv')
        time.sleep(2)
        for i in range(len(labels) - 4):
            name = self.driver.find_ids(self.id + 'tv')[i].text
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_xpath('排行榜')
            channel_name = self.driver.find_id(self.id + 'txtTitle').text
            assert name == channel_name, '频道列表界面标签名称与标签详情界面标签名称校验不一致'
            time.sleep(1)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 热门频道
    def Function_Channel_Hot(self):
        title = self.driver.find_id(self.id + 'tv2').text
        self.driver.find_id(self.id + 'tv2').click()
        self.driver.wait_id(self.id + 'follow_ta')
        self.driver.Background()
        time.sleep(2)
        video_title = self.driver.find_id(self.id + 'tv_video_detail_title').text
        assert title in video_title, '频道主界面点击的视频标题与视频详情的标题校验失败'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'count').click()
        self.driver.wait_id(self.id + 'txtTitle')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)

    # 附近
    def Function_Channel_Nearby(self):
        while True:
            try:
                self.driver.find_xpath('附近')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >= 2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('附近').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                try:
                    self.driver.wait_sys('允许')
                except:
                    pass
        except:
            pass
        while True:
            try:
                self.driver.wait_id(self.id + 'distance')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    # 附近列表
    def Function_Channel_Nearby_work_list(self):
        distance = self.driver.find_ids(self.id + 'distance')
        count = self.driver.find_ids(self.id + 'userHead')
        if len(distance) != len(count):
            print('附近当前界面有个别作品未显示距离信息')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'channel1')
        except:
            print('当前列表界面作品未显示频道标签')
        time.sleep(2)

    # 视频详情切换-列表作品名称与视频详情作品名称校验
    def Function_Channel_Nearby_work_detail(self):
        name = self.driver.find_ids(self.id + 'title')
        title_list = []
        for title in range(len(name)):
            title_name = self.driver.find_ids(self.id + 'title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'title').click()
        for i in range(len(name)):
            self.driver.wait_id(self.id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            name = self.driver.find_id(self.id + 'tv_video_detail_title').text
            # label1 = 'ch'
            label2 = 'lr'
            if label2 in name:
                new_Name = re.findall(r"lr (.*)", name)  # 获取list类型的字符串['xxxx']
                str_name = ''.join(new_Name)  #转换成纯字符串'xxxx'
                assert str_name in title_list, '视频详情标题不在标题列表中'
                time.sleep(2)
            else:
                new_Name1 = re.findall(r"ch (.*)", name)
                str_name1 = ''.join(new_Name1)
                assert str_name1 in title_list, u'视频详情标题不在标题列表中'
                time.sleep(2)
            self.driver.swip_up()
        time.sleep(2)


    #进入曝光区
    def Function_Exposure(self):
        while True:
            # noinspection PyBroadException
            try:
                self.driver.find_xpath('曝光区')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >= 2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('曝光区').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id(self.id + 'filmBg')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #曝光作品评论
    def Function_Exposure_Comment(self):
        progress_before = self.driver.find_id(self.id + 'progress_bar').text
        self.driver.find_id(self.id + 'filmBg').click()
        while True:
            self.driver.wait_id(self.id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_comment').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('^.^')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        try:
            self.driver.wait_xpath('^.^')
        except:
            print('未检测到发送的评论')
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        progress_after = self.driver.find_id(self.id + 'progress_bar').text
        if progress_after == progress_before:
            value = '100.0'
            if progress_after != value:
                print('曝光评论进度显示错误')
        time.sleep(2)

    #进入排行榜
    def Function_Rank(self):
        while True:
            try:
                self.driver.find_xpath('排行榜')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >= 2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('排行榜').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id(self.id + 'iv_source')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #获赞榜-列表加载
    def Function_Rank_Good_Rank(self):
        self.driver.find_id(self.id + 'tv_rich_rank').click()
        while True:
            try:
                self.driver.wait_id(self.id + 'userHead1')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'tv_rich_rank').click()
            time.sleep(2)

    #获赞榜-点赞数排序检查
    def Function_Rank_Good_Rank_Sort(self):
        count = self.driver.find_ids(self.id + 'desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            goods = re.findall(r'获赞(.*)', limit)
            str_good_count = ''.join(goods)
            int_num = int(str_good_count)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=True)
        assert lists == list_set, '获赞榜点赞排序验证错误'
        time.sleep(2)

    #获赞榜-用户信息
    def Function_Rank_Good_Rank_UserInfo(self):
        No1_name = self.driver.find_id(self.id + 'username1').text
        self.driver.find_id(self.id + 'userHead1').click()
        self.driver.wait_id(self.id + 'll_follow')
        No1_zoom_name = self.driver.find_id(self.id + 'username').text
        assert No1_name == No1_zoom_name, '获赞榜第一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    #获赞榜-周榜，月榜查看
    def Function_Rank_Good_Rank_table(self):
        self.driver.find_id(self.id + 'rl_tag2').click()
        time.sleep(2)
        No1_name = self.driver.find_id(self.id + 'username1').text
        self.driver.find_id(self.id + 'userHead1').click()
        self.driver.wait_id(self.id + 'll_follow')
        No1_zoom_name = self.driver.find_id(self.id + 'username').text
        assert No1_name == No1_zoom_name, '榜一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(self.id + 'rl_tag3').click()
        time.sleep(2)
        No1_name = self.driver.find_id(self.id + 'username1').text
        self.driver.find_id(self.id + 'userHead1').click()
        self.driver.wait_id(self.id + 'll_follow')
        No1_zoom_name = self.driver.find_id(self.id + 'username').text
        assert No1_name == No1_zoom_name, '榜一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)


    #主播榜
    def Function_Rank_Anchor(self):
        self.driver.find_id(self.id + 'tv_live_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(self.id + 'userHead1')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'tv_live_rank').click()
        time.sleep(2)

    #主播榜-参与人排序检查
    def Function_Rank_Anchor_Sort(self):
        count = self.driver.find_ids(self.id + 'desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'直播总参与(.*)人', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=True)
        assert lists == list_set, '=主播榜人数排序验证错误'
        time.sleep(2)

    #社团榜
    def Function_Rank_Societies(self):
        self.driver.find_id(self.id + 'tv_society_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(self.id + 'userHead1')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'tv_society_rank').click()
        time.sleep(2)

    #社团榜-作品数排序检查
    def Function_Rank_Societies_Sort(self):
        count = self.driver.find_ids(self.id + 'desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'(.*)作品', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=True)
        assert lists == list_set, '=社团榜作品数排序验证错误'
        time.sleep(2)

    #素材榜
    def Function_Rank_Sources(self):
        self.driver.find_id(self.id + 'tv_source_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(self.id + 'userHead1')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'tv_source_rank').click()
        time.sleep(2)

    #素材榜-素材数排序检查
    def Function_Rank_Sources_sort(self):
        count = self.driver.find_ids(self.id + 'desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'(.*)收录', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        assert lists == list_set, '素材榜素材收录数排序验证错误'
        time.sleep(2)

    #作品榜-列表标题是视频详情标题校验
    def Function_Rank_Works_title_check(self):
        self.driver.find_id(self.id + 'film').click()
        time.sleep(2)
        list_title = self.driver.find_ids(self.id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(self.id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_source_title').click()
        for i in range(len(list_title)):
            self.driver.wait_id(self.id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            Name = self.driver.find_id(self.id + 'tv_video_detail_title').text
            # label1 = 'ch'
            label2 = 'lr'
            if label2 in Name:
                new_Name = re.findall(r"lr (.*)", Name)  # 获取list类型的字符串['xxxx']
                str_name = ''.join(new_Name)  # 转换成纯字符串'xxxx'
                assert str_name in title_list, u'视频详情标题不在标题列表中'
                time.sleep(2)
            else:
                new_Name1 = re.findall(r"ch (.*)", Name)
                str_name1 = ''.join(new_Name1)
                assert str_name1 in title_list, u'视频详情标题不在标题列表中'
                time.sleep(2)
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #热门标签tab-列表切换数据检查
    def Function_Rank_Hot_Label(self):
        self.driver.find_id(self.id + 'commentary').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top')
            self.driver.find_id(self.id + 'close').click()
        except:
            pass
        time.sleep(2)
        list_title = self.driver.find_ids(self.id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(self.id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'film').click()
        time.sleep(2)
        list_title1 = self.driver.find_ids(self.id + 'tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids(self.id + 'tv_source_title')[title].text
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        assert list_title != list_title1, '排行榜与热门标签榜作品标题校验错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'commentary').click()
        time.sleep(2)

    #切换热门标签
    def Function_Rank_Hot_Label_change(self):
        label_name = self.driver.find_id(self.id + 'commentary').text
        list_title = self.driver.find_ids(self.id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(self.id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'commentary').click()
        time.sleep(2)
        label_tv = self.driver.find_ids(self.id + 'tv')
        tv_list = []
        for i in range(len(label_tv)):
            tv_name = self.driver.find_ids(self.id + 'tv')[i].text
            tv_list.append(tv_name)
            time.sleep(1)
        tv_list.remove(label_name)
        select = random.randint(0, len(tv_list))
        self.driver.find_ids(self.id + 'tv')[select].click()
        self.driver.wait_id(self.id + 'iv_source')
        list_title1 = self.driver.find_ids(self.id + 'tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids(self.id + 'tv_source_title')[title].text
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        assert title_list != title_list1, '切换不同的热门标签后，列表中的作品未刷新'
        time.sleep(2)

    #潜力榜
    def Function_Rank_Potential_list(self):
        self.driver.find_id(self.id + 'potential').click()
        time.sleep(2)
        name = self.driver.find_id(self.id + 'tv_source_title').text
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        name1 = self.driver.find_id(self.id + 'tv_video_detail_title').text
        self.driver.find_id(self.id + 'btnBack').click()
        assert name in name1, '列表标题与视频详情标题不一致'
        time.sleep(2)
        for i in range(3):
            self.driver.swip_up()
            time.sleep(2)

    # 社作榜
    def Function_Rank_society_works(self):
        self.driver.find_id(self.id + 'society_film').click()
        time.sleep(2)
        titles = self.driver.find_ids(self.id + 'tv_source_title')
        for i in range(len(titles)):
            self.driver.find_ids(self.id + 'iv_source')[i].click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)

            try:
                self.driver.find_id(self.id + 'dubbing')
                print('社团作品显示有配音按钮')
            except:
                pass
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    # 榜单列表加载
    def Function_Rank_Works_list_load(self):
        while True:
            ranking = self.driver.find_ids(self.id + 'rank')[-1].text
            if ranking == '300':
                break
            else:
                pass
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    # 进入在线pia戏
    def Function_Pia(self):
        while True:
            try:
                self.driver.find_xpath('在线pia戏')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('在线pia戏').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id(self.id + 'start')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    # 勋章列表
    def Function_Pia_Medal_list(self):
        self.driver.find_id(self.id + 'goXun').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userHead')
            time.sleep(2)
        except:
            print('未加载显示勋章列表')
        time.sleep(2)


    # 道具商城
    def Function_Pia_Prop_Mall(self):
        self.driver.find_xpath('道具商城').click()
        time.sleep(2)
        num = self.driver.find_id(self.id + 'diamond').text
        self.driver.find_id(self.id + 'diamond').click()
        time.sleep(2)
        num1 = self.driver.find_id(self.id + 'diamond_count_tv').text
        time.sleep(2)
        assert num in num1, '钻石额度校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    # 幸运宝箱
    def Function_Pia_Prop_Mall_Lucky_Box(self):
        self.driver.find_id(self.id + 'diamond').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'diamond_count_tv')
        except:
            print('幸运夺宝界面跳转至钻石充值界面失败')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        num = self.driver.find_id(self.id + 'diamond').text
        if num < 49:
            self.driver.find_id(self.id + 'smoke_ten').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'back').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)


    # Pia戏装扮
    def Function_Pia_Prop_Mall_Dress_up(self):
        num = self.driver.find_ids(self.id + 'img')
        for i in range(len(num)):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(1)


    # 创建pia戏房间
    def Function_Pia_Create_room(self):
        self.driver.find_id(self.id + 'create_room').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'check_normal').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'crate_room').click()
        try:
            self.driver.wait_id(self.id + 'chat')
        except:
            print('pia戏房间创建失败')
        time.sleep(2)

    # 评论
    def Function_Pia_Room_comment(self):
        self.driver.find_id(self.id + 'show_comment').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('哈哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'rl')
        time.sleep(2)

    # 用户头像
    def Function_Pia_Room_Userhead(self):
        self.driver.find_id(self.id + 'head').click()
        self.driver.wait_id(self.id + 'user_id')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'username')
            try:
                self.driver.find_id(self.id + 'gender')
                try:
                    self.driver.find_id(self.id + 'user_id')
                    try:
                        self.driver.find_id(self.id + 'user_detail')
                    except:
                        print('未显示用户简介')
                except:
                    print('未显示用户ID')

            except:
                print('未显示性别')
        except:
            print('未显示用户名')
        time.sleep(2)
        self.driver.find_id(self.id + 'icon_close').click()
        time.sleep(2)

    # 房间私密
    def Function_Pia_Room_Private(self):
        self.driver.find_id(self.id + 'private_btn').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert tip == check, '普通房间设置私密，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 邀请好友
    def Function_Pia_Room_invite_friend(self):
        self.driver.find_ids(self.id + 'head')[-1].click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert tip == check, '普通房间邀请好友，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 剧本列表
    def Function_Pia_Room_Script_list(self):
        self.driver.find_id(self.id + 'script').click()
        time.sleep(2)
        source = self.driver.find_ids(self.id + 'sourcename')
        source_list = []
        for i in range(len(source)):
            name = self.driver.find_ids(self.id + 'sourcename')[i].text
            source_list.append(name)

        No1 = source_list[0]
        No2 = source_list[1]
        assert No1 == No2, '剧本列表校验失败'
        time.sleep(2)

        # 添加剧本
        self.driver.find_id(self.id + 'add_drama').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert tip == check, '添加剧本，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 退出在线pia戏房间
    def Function_Pia_Room_exit(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'create_room')
        time.sleep(2)

    # 在线匹配
    def Function_Pia_Match_online(self):
        while True:
            self.driver.find_id(self.id + 'start')
            try:
                self.driver.find_id(self.id + 'script')
                break
            except:
                pass
        time.sleep(2)
        self.driver.wait_id(self.id + 'home_close')
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'create_room')
        time.sleep(2)

    # 跟随进入
    def Function_Pia_Follow(self):
        self.driver.find_id(self.id + 'follow').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'refresh').click()
        try:
            self.driver.wait_toast(self.id + '//android.widget.Toast')
        except:
            print('未检测到刷新toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 作品列表
    def Function_Pia_Draft(self):
        self.driver.find_id(self.id + 'draft').click()
        time.sleep(2)

    # 有声漫画
    def Function_Cartoon(self):
        while True:
            try:
                self.driver.find_xpath('有声漫画')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        while True:
            self.driver.find_xpath('有声漫画').click()
            time.sleep(2)
            try:
                self.driver.wait_id(self.id + 'collect')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    # 推荐列表-声漫名称校验
    def Function_Cartoon_title_check(self):
        name = self.driver.find_id(self.id + 'title').text
        self.driver.find_id(self.id + 'title').click()
        self.driver.wait_id(self.id + 'start_play')
        detail_name = self.driver.find_id(self.id + 'tvTitle').text
        assert name == detail_name, '推荐列表中声漫名称与声漫详情界面名称不一致'
        time.sleep(2)

    # #声漫更新集数校验
    # def test_b_a(self):
    #     update = self.driver.find_id(self.id + 'update').text
    #     num = re.findall(r'更新至(.*)话',update)
    #     self.driver.find_id(self.id + 'update').click()
    #     self.driver.wait_id(self.id + 'start_play')
    #     while True:
    #         number = self.driver.find_ids(self.id + 'name')[-1].text
    #         self.driver.swip_up()
    #         time.sleep(2)
    #         number1 = self.driver.find_ids(self.id + 'name')[-1].text
    #         if number == number1:
    #             break
    #         else:
    #             pass
    #     time.sleep(2)
    #     new = re.findall(r'第 (.*) 话',number1)
    #     assert (num,new,msg='列表更新集数与声漫详情界面更新集数不一致')
    #     time.sleep(2)
    #     self.driver.find_id(self.id + 'btnBack').click()
    #     time.sleep(2)

    # 推荐列表加载
    def Function_Cartoon_list_load(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        for i in range(4):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)

    # 声漫剧集详情
    def Function_Cartoon_Episodes_detail(self):
        i = 0
        while i <= 10:
            self.driver.find_id(self.id + 'imgHead').click()
            try:
                self.driver.wait_id(self.id + 'start_play')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            if i == 10:
                break
            else:
                pass
            i = i + 1
            time.sleep(2)

    # 剧集列表界面点击声漫收藏
    def Function_Cartoon_collection(self):
        self.driver.find_id(self.id + 'collect').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        check = '收藏成功'
        assert toast == check, '收藏toast校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'collect').click()
        cancel_toast = self.driver.wait_toast('//android.widget.Toast')
        cancel_check = '取消收藏成功'
        assert cancel_check == cancel_toast, '声漫取消收藏toast校验不一致'
        time.sleep(2)

    # 声漫制作相关社团列表
    def Function_Cartoon_Make_society(self):
        self.driver.find_id(self.id + 'right_rl').click()
        try:
            self.driver.wait_id(self.id + 'count')
        except:
            print('声漫制作社团列表加载失败')
        time.sleep(2)
        self.driver.find_ids(self.id + 'name')[1].click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 连载漫画集数查看
    def Function_Cartoon_Episode_check(self):
        num = self.driver.find_id(self.id + 'name').text
        self.driver.find_id(self.id + 'name').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        Re_num = re.findall(r'第 (.*) 话', num)
        new_num = ''.join(Re_num)
        title_name = self.driver.find_id(self.id + 'tv_video_detail_title').text
        assert new_num == title_name, '声漫切换集数校验不一致'
        time.sleep(2)


    #最新列表-话集更新检查
    def Function_Cartoon_Update_check(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        # update = self.driver.find_id(self.id + 'update').text
        union = self.driver.find_id(self.id + 'union_name').text
        # new_update = re.findall(r'更新至(.*)', update)
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        detail_name = self.driver.find_id(self.id + 'user_name').text
        assert union == detail_name, '社团名称校验不一致'
        time.sleep(2)


    # 声漫分类列表
    def Function_Cartoon_Classification_list(self):
        self.driver.find_id(self.id + 'tab3').click()
        time.sleep(2)
        title = self.driver.find_ids(self.id + 'title')
        for i in range(len(title) - 1, -1, -1):
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(1)

    # 声漫制作
    def Function_Cartoon_Make(self):
        self.driver.find_id(self.id + 'sm').click()
        time.sleep(2)
        title = self.driver.find_ids(self.id + 'title')
        for i in range(len(title) - 1, -1, -1):
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(1)

    # 漫画详情
    def Function_Cartoon_detail(self):
        self.driver.find_id(self.id + 'btn_add').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('你听说过女大学生吗')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_pic1').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    # 制作声漫
    def Function_Cartoon_Making(self):
        self.driver.find_id(self.id + 'tv_make').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_make').click()
            time.sleep(2)
        except:
            pass
        while True:
            try:
                self.driver.find_xpath('添加配音者')
                self.driver.find_xpath('添加配音者').click()
                time.sleep(2)
                self.driver.wait_id(self.id + 'socialstatus')
                self.driver.find_id(self.id + 'socialstatus').click()
                time.sleep(2)
            except:
                break
            time.sleep(1)
        self.driver.find_id(self.id + 'tv_sure').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)


    # 我的漫画
    def Function_Cartoon_My(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.wait_xpath('你听说过女大学生吗')
        time.sleep(2)

    # 声漫统筹界面-更新配音者
    def Function_Cartoon_change_Voiceover(self):
        self.driver.find_id(self.id + 'iv_pic1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'socialstatus')
        time.sleep(1)
        self.driver.find_ids(self.id + 'socialstatus')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'socialstatus')
        time.sleep(1)
        self.driver.find_id(self.id + 'socialstatus').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    # 进入统筹界面-添加音效
    def Function_Cartoon_Making_insert_Sound(self):
        self.driver.find_id(self.id + 'make').click()
        self.driver.wait_id(self.id + 'upload')
        self.driver.find_xpath('添加音效').click()
        time.sleep(2)

    # 点击录音
    def Function_Cartoon_Record(self):
        self.driver.find_id(self.id + 'transcribe').click()
        time.sleep(5)
        self.driver.find_id(self.id + 'transcribe').click()
        time.sleep(4)

    # 点击试听音效
    def Function_Cartoon_Making_listening_test(self):
        Sounds = self.driver.find_ids(self.id + 'effect_types_img')
        for i in range(len(Sounds)):
            self.driver.find_ids(self.id + 'effect_types_img')[i].click()
            time.sleep(3)
            Sounds_Classification = self.driver.find_ids(self.id + 'effect_sound_name')
            for y in range(len(Sounds_Classification)):
                self.driver.find_ids(self.id + 'effect_sound_name')[y].click()
                time.sleep(2)

        # 播放整体动漫音效
        self.driver.find_id(self.id + 'preview').click()
        time.sleep(10)

    # 进入添加背景音界面
    def Function_Cartoon_Making_background_music(self):
        self.driver.find_id(self.id + 'upload').click()
        self.driver.wait_id(self.id + 'comic_sound_class_name')
        time.sleep(2)
        self.driver.find_xpath('舒缓').click()
        time.sleep(2)
        self.driver.find_id(self.id + "add").click()
        self.driver.find_id(self.id + 'tv_preview')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.045, self.y * 0.718, self.x * 0.891, self.y * 0.683)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.934, self.y * 0.785, self.x * 0.066, self.y * 0.785)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_preview').click()
        time.sleep(5)
        self.driver.find_xpath('完成').click()
        time.sleep(5)
        self.driver.wait_xpath('保存')
        time.sleep(2)
        self.driver.find_xpath('保存').click()
        self.driver.wait_xpath('下一步')
        self.driver.find_id(self.id + 'preview').click()
        self.driver.wait_id(self.id + 'preview')
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        self.driver.wait_id(self.id + 'upload')
        time.sleep(2)

    # 声漫上传界面-保存并退出
    def Function_Cartoon_Making_Save(self):
        self.driver.find_id(self.id + 'preview').click()
        self.driver.wait_id(self.id + 'preview')
        time.sleep(2)
        self.driver.find_id(self.id + 'savebtn').click()
        self.driver.wait_id(self.id + 'make')
        time.sleep(2)

    # 声漫上传
    def Function_Cartoon_Making_Upload(self):
        self.driver.find_id(self.id + 'make').click()
        self.driver.wait_id(self.id + 'upload')
        time.sleep(2)
        self.driver.find_id(self.id + 'upload').click()
        self.driver.wait_id(self.id + 'comic_sound_class_name')
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        self.driver.wait_id(self.id + 'upload')
        time.sleep(2)
        self.driver.find_id(self.id + 'upload').click()
        try:
            self.driver.wait_id(self.id + 'imgurl')
        except:
            print('声漫上传失败')
        time.sleep(2)

    # 声漫删除
    def Function_Cartoon_Delete(self):
        try:
            self.driver.find_id(self.id + 'imgurl')
            self.driver.find_id(self.id + 'imgurl').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_good').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'setting').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(0.5 * self.x, 0.867 * self.y)
            elif self.y >= 2280:
                self.driver.tap(0.5 * self.x, 0.883 * self.y)
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
                try:
                    self.driver.wait_toast('//android.widget.Toast')
                except:
                    print('未检测到声漫删除toast')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(3)
                self.driver.find_id(self.id + 'close1').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
        except:
            print('未位于声漫剧集列表界面')

class Dub:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #合作素材
    def Material_library_dubble(self):
        self.driver.wait_id(self.id + 'task_box')
        self.driver.find_id(self.id + 'btn_more').click()
        self.driver.wait_id(self.id + 'coor')
        self.driver.find_id(self.id + 'coor').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)

    # 双配素材-进入配音界面
    def Into_Dubbing_double(self):
        self.driver.find_id(self.id + 'dubbing_fake').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'close').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'dubbing_fake')
                self.driver.find_id(self.id + 'dubbing_fake').click()
                time.sleep(3)
                self.driver.find_id(self.id + 'next')
                self.driver.find_id(self.id + 'next').click()
                time.sleep(2)
                try:
                    self.driver.wait_sys('始终允许')
                except:
                    self.driver.wait_sys('允许')
            except:
                print('未返回到素材预览界面')
                self.driver.Quit()
        except:
            pass
        self.driver.wait_id(self.id + 'roleall')
        self.driver.find_id(self.id + 'roleall').click()
        time.sleep(2)

    #首次进入配音节目引导界面(9.19版本移除）
    def Dub_Guidance(self):
        try:
            self.driver.find_id(self.id + 'subtitleView').click()
        except:
            pass
        time.sleep(2)

    #退出配音界面
    def Dub_Exit_dubbing(self):
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(3)

    # 双配素材配音界面配音角色切换
    def Dub_Exchange_roles(self):
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'role1_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'role2_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'roleall').click()
        time.sleep(2)

    # 配音界面背景音开关
    def Dub_Background_sound(self):
        self.driver.find_id(self.id + 'headset').click()
        time.sleep(2)
        try:
            tips = self.driver.find_id(self.id + 'txtContent').text
            check = '开启背景音需要插上耳机！'
            assert tips == check, '耳机提示文案不一致'
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
        except:
            pass

    # 开启实况
    def Dub_Start_Camera(self):
        # 开启实况权限检查
        self.driver.find_id(self.id + 'living').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys("始终允许")
            except:
                self.driver.wait_sys("允许")
        except:
            try:
                self.driver.wait_sys("始终允许")
            except:
                try:
                    self.driver.wait_sys("允许")
                except:
                    pass
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'cameraView2')
        except:
            self.driver.find_id(self.id + 'living').click()
            time.sleep(4)

    #关闭实况开关
    def Dub_Close_Camera(self):
        self.driver.find_id(self.id + 'living').click()
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'cameraView2')
            self.driver.find_id(self.id + 'living').click()
        except:
            pass
        time.sleep(2)

    #配音界面台词列表
    def Dub_Script_list_swip(self):
        self.driver.find_id(self.id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'titleTextView')
        count = self.driver.find_ids(self.id + 'titleTextView')
        num = len(count)
        if num > 4:
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'cancelBn').click()
        self.driver.wait_id(self.id + 'scirpt')
        time.sleep(2)

    # 台词列表切换台词
    def Dub_Script_change(self):
        script_cout = int(self.driver.find_id(self.id + 'scirpt_count').text)
        if script_cout > 1:
            self.driver.find_id(self.id + 'scirpt').click()
            self.driver.wait_id(self.id + 'titleTextView')
            count = self.driver.find_ids(self.id + 'titleTextView')
            for i in range((count)-1, -1, -1):
                self.driver.find_ids(self.id + 'titleTextView')[i].click()
                self.driver.wait_id(self.id + 'edit_subtitle')
                self.driver.find_id(self.id + 'scirpt').click()
                self.driver.wait_id(self.id + 'titleTextView')
                time.sleep(2)
            self.driver.find_id(self.id + 'cancelBn').click()
        time.sleep(2)

    # 修改台词后点击完成，再次进入编辑界面查看修改后的台词
    def Dub_Script_edit(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_ids(self.id + 'content_editor')[0].clear()
        time.sleep(2)
        self.driver.find_ids(self.id + 'content_editor')[0].send_keys("台词修改")
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        assert tip == tip_check
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        content = self.driver.find_ids(self.id + 'content_editor')[0].text
        content_check = '台词修改'
        assert content == content_check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

    # 修改首句台词后不保存返回配音界面再进，查看台词首句显示
    def Dub_Script_edit_nosave(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_ids(self.id + 'content_editor')[0].send_keys('台词修改')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '真的要放弃本次台词编辑吗？'
        assert tip_check == tip
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(3)

    # 切换系统默认台词
    def Dub_Script_default(self):
        self.driver.find_id(self.id + 'scirpt').click()
        self.driver.wait_id(self.id + 'titleTextView')
        self.driver.find_id(self.id + 'titleTextView').click()
        time.sleep(3)
        try:
            self.driver.find_id(self.id + 'roleall')
            self.driver.find_id(self.id + 'roleall').click()
        except:
            pass
        time.sleep(2)

    # 清空字幕所有内容
    def Dub_Script_clearall(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.driver.hide_keyboard()
        time.sleep(2)
        for i in range(2):
            Subtitles = self.driver.find_ids(self.id + 'content_editor')
            for y in range(len(Subtitles)):
                self.driver.find_ids(self.id + 'content_editor')[y].clear()
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        toast_check = '台词不能为空，请输入至少一句台词'
        assert toast == toast_check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

    # 编辑台词输入特殊符号后保存
    def Dub_Script_special_char(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_id(self.id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content_editor').send_keys('∯∰∱∲∳')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'edit_subtitle')
        except:
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'edit_subtitle')

    #单行台词输入超过30个字符
    def Dub_Script_char_lenth(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_id(self.id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content_editor').send_keys('123456789012345678901234567890123456789')
        tip = self.driver.wait_toast('//android.widget.Toast')
        check = '单行台词不能超过30个字符'
        assert tip == check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'edit_subtitle')

    # 配音界面点击预览原声视频
    def Dub_Video_play(self):
        self.driver.find_id(self.id + 'play').click()
        try:
            self.driver.find_id(self.id + 'video_time')
        except:
            print('未发现配音视频播放时间进度')
        self.driver.wait_download(self.id + 'play')

    # 播放过程中暂停
    def Dub_Video_pause(self):
        self.driver.find_id(self.id + 'play').click()
        self.driver.find_id(self.id + 'fl_video').click()
        # self.driver.Background()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

    # 播放过程中推到后台
    def Dub_Video_background(self):
        self.driver.find_id(self.id + 'play').click()
        time.sleep(2)
        self.driver.Background()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)

    # 录音权限
    def Dub_Record_permissions(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            self.driver.wait_download(self.id + 'title')
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
        time.sleep(2)

    # 手动点击提交进入配音预览界面
    def Dub_Manual_into_preview(self):
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)

    # 在完整录制后的基础上点击原声试听，查看视频播放是否从头开始播放
    def Dub_Video_play_time(self):
        time1 = datetime.datetime.now()
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_download(self.id + 'play')
        time2 = datetime.datetime.now()
        time_result = time2 - time1
        time_video = self.driver.find_id(self.id + 'video_time').text
        print('视频时间：', time_video, '实际播放时间：', time_result)
        time.sleep(2)

    # 配音试听
    def Dub_Video_review(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

    # 试听过程中点击提交进入预览界面
    def Dub_review_into_preview(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    # 试听过程中，点击退出配音界面
    def Dub_Video_review_quit(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '确定放弃吗？'
        assert tip == tip_check, "退出配音界面弹窗提示文案错误"
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)

    # 点击回撤按钮
    def Dub_Video_withdraw(self):
        while True:
            try:
                self.driver.find_id(self.id + 'withdraw')
                self.driver.find_id(self.id + 'withdraw').click()
            except:
                break
        time.sleep(2)

    # 录制过程中暂停
    def Dub_Record_pause(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'dubbingWaveform')
        except Exception as e:
            print(e, '没有显示音轨，未录制进人声')
        time.sleep(2)

    # 录制完成后自动跳转再返回配音界面
    def Preview_back_dubbing(self):
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    # 手动拖音轨
    def Dub_Audio_track_move(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.185, self.y * 0.65, self.x * 0.787, self.y * 0.65)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.24, self.y * 0.71, self.x * 0.81, self.y * 0.71)
        else:
            pass
        time.sleep(2)

    # 重新录制
    def Dub_Restart_record_dubbing(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.wait_id(self.id + 'play')
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(4)

    # 长按回撤按钮
    def Dub_Long_withdraw(self):
        el = self.driver.find_id(self.id + 'withdraw')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)

    # 播放完整的视频
    def Preview_video_play(self):
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)

    # 字幕开关
    def Preview_subtitle_onoff(self):
        el = self.driver.find_id(self.id + 'add_subtitle_cb').get_attribute('checked')
        check = 'true'
        if el == check:
            print('字幕默认开启')
        else:
            print('字幕默认关闭')
        time.sleep(2)
        self.driver.find_id(self.id + 'add_subtitle_cb').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id(self.id + 'add_subtitle_cb').get_attribute('checked')
        assert el != el1
        self.driver.find_id(self.id + 'add_subtitle_cb').click()
        time.sleep(2)

    #降噪开关
    def Preview_voice_onoff(self):
        el = self.driver.find_id(self.id + 'clear_voice').get_attribute('checked')
        self.driver.find_id(self.id + 'clear_voice').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id(self.id + 'clear_voice').get_attribute('checked')
        assert el != el1
        self.driver.find_id(self.id + 'clear_voice').click()
        time.sleep(2)

    # 预览界面人声
    def Preview_voice_volume(self):
        #调节人声音量
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37, self.y * 0.718)  #调大音量
            time.sleep(4)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718, self.x * 0.115, self.y * 0.628)  # 调小音量
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.245, self.y*0.535, self.x*0.376, self.y*0.633)  #调大音量
            time.sleep(4)
            self.driver.swip_move(self.x*0.364, self.y*0.627, self.x*0.107, self.y*0.627)  #调小音量
        else:
            pass
        time.sleep(4)

    # 声音校准
    def Preview_voice_calibration(self):
        self.driver.find_id(self.id + 'trim').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37, self.y * 0.718)  # 提前播放人声进度
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718, self.x * 0.115, self.y * 0.628)  # 延后播放人声进度
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.245, self.y * 0.535, self.x * 0.376, self.y * 0.633)  # 提前播放人声进度
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107, self.y * 0.627)  # 延后播放人声进度
        time.sleep(2)

    # 人声变声调节
    def Preview_Voice_Changer(self):
        self.driver.find_id(self.id + 'pitch').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37, self.y * 0.718)  # #人声声线加粗
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718, self.x * 0.115, self.y * 0.628)  #人声声线变细
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.245, self.y * 0.535, self.x * 0.376, self.y * 0.633)  #人声声线加粗
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107, self.y * 0.627)  #人声声线变细
        else:
            pass
        time.sleep(2)

    #人声混响调节
    def Preview_reverberation(self):
        self.driver.find_id(self.id + 'fx').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.093, self.y * 0.8, self.x * 0.093, self.y * 0.59)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.8, self.x * 0.254, self.y * 0.59)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.8, self.x * 0.419, self.y * 0.59)  # 增加回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.093, self.y * 0.59, self.x * 0.093, self.y * 0.8)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.59, self.x * 0.254, self.y * 0.8)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.59, self.x * 0.419, self.y * 0.8)  # 减小回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.098, self.y * 0.7, self.x * 0.098, self.y * 0.553)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.7, self.x * 0.252, self.y * 0.553)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.7, self.x * 0.413, self.y * 0.553)  # 增加回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.098, self.y * 0.553, self.x * 0.098, self.y * 0.7)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.553, self.x * 0.252, self.y * 0.7)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.553, self.x * 0.413, self.y * 0.7)  # 减小回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
        # try:
        #     self.driver.find_xpath('确定')
        #     self.driver.find_xpath('确定').click()
        #     print("服务端关闭人声混响功能，不做混响调节测试")
        # except:

    # 背景音音量调节
    def Preview_background_music(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.632, self.y * 0.62, self.x * 0.893, self.y * 0.67)#增大背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.893, self.y * 0.67, self.x * 0.632, self.y * 0.62)#减小背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.632, self.y * 0.62, self.x * 0.893, self.y * 0.67)  # 增大背景音音量
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.607, self.y * 0.591, self.x * 0.884, self.y * 0.571)#增大背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.884, self.y * 0.571, self.x * 0.607, self.y * 0.591)#减小背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.607, self.y * 0.591, self.x * 0.884, self.y * 0.571)#增大背景音音量
        time.sleep(2)

    #关闭背景音音量
    def Preview_close_background_music(self):
        self.driver.find_id(self.id + 'voice_open').click()
        el = self.driver.find_id(self.id + 'voice_open').get_attribute('checked')
        if el != 'true':
            print ('状态点击背景音关闭按钮后，状态没有显示关闭')
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)

    # 背景音音乐列表中选择其它音乐
    def Preview_chage_music(self):
        count = self.driver.find_id(self.id + 'tvBgCount').text
        if int(count) > 1:
            self.driver.find_id(self.id + 'imgBgCount').click()
            time.sleep(4)
            if self.y == 1920:
                self.driver.tap(self.x*0.5,self.y*0.469)
            elif self.y > 2250:
                self.driver.tap(self.x*0.5,self.y*0.464)
            else:
                pass
        time.sleep(4)

    # 背景音混响调节
    def Preview_background_reverberation(self):
        self.driver.find_id(self.id + 'bgfx').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('确定')
            self.driver.find_xpath('确定').click()
            print("服务端关闭人声混响功能，不做混响调节测试")
        except:
            el = self.driver.find_id(self.id + 'bgfx').get_attribute('checked')
            if el != 'true':
                print('状态点击背景音混响按钮后，状态没有显示选中')
            time.sleep(2)
        if self.y == 1920:
            #增加混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.8, self.x*0.588, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.8, self.x*0.75, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.8, self.x*0.91, self.y*0.59)
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            #减小背景音混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.59, self.x*0.588, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.59, self.x*0.75, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.59, self.x*0.91, self.y*0.8)
            time.sleep(2)
        elif self.y > 2250:
            #增加混响效果
            self.driver.swip_move(self.x * 0.593, self.y * 0.699,self.x*0.595, self.y*0.539)
            time.sleep(2)
            self.driver.swip_move(self.x*0.748, self.y*0.704,self.x*0.755, self.y*0.536)
            time.sleep(2)
            self.driver.swip_move(self.x*0.913, self.y*0.702,self.x*0.907, self.y*0.538)
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            #减小混响效果
            self.driver.swip_move(self.x*0.595, self.y*0.539,self.x * 0.593, self.y * 0.699)
            time.sleep(2)
            self.driver.swip_move(self.x*0.755, self.y*0.536,self.x*0.748, self.y*0.704)
            time.sleep(2)
            self.driver.swip_move(self.x*0.907, self.y*0.538,self.x*0.913, self.y*0.702,)
            time.sleep(2)


    # 下载系统推荐背景音音乐
    def Preview_download_music(self):
        self.driver.find_id(self.id + 'bgvol').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'imgBgCount').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.955)
        elif self.y > 2250:
            self.driver.tap(self.x*0.5, self.y*0.96)
        self.driver.wait_id(self.id + 'btnRight')
        while True:
            try:
                self.driver.find_id(self.id + 'btnDownload')
                self.driver.find_id(self.id + 'btnDownload').click()
            except:
                break

    # 随机选中背景音音乐
    def Preview_select_music(self):
        count = self.driver.find_ids(self.id + 'title')
        select = random.randint(0,len(count)-1)
        self.driver.find_ids(self.id + 'title')[select].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)
        #选中音乐后进入音乐试听界面，拖动视频进度条
        if self.y == 1920:
            self.driver.swip_move(self.x*0.052,self.y*0.487,self.x*0.704,self.y*0.487)
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.052,self.y*0.448,self.x*0.633,self.y*0.448)
        time.sleep(2)
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'clear_voice')
        time.sleep(2)

    # 上滑加载背景音音乐列表并点击下载按钮
    def Preview_load_music_list(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    #预览界面点击完成
    def Preview_into_upload(self):
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)

    # 修改作品封面-视频截图
    def Upload_work_Cover_Screenshots(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.708)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.422, self.x * 0.74, self.y * 0.422)
        elif self.y == 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.752)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.033, self.y * 0.361, self.x * 0.441, self.y * 0.361)
        elif self.y == 2340:
            self.driver.tap(self.x * 0.5, self.y * 0.752)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.066, self.y * 0.351, self.x * 0.5, self.y * 0.351)
        time.sleep(4)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    #修改作品封面-拍照
    def Dubbing_work_Cover_Photo(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.755)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.82)
        time.sleep(5)
        try:
            # 米5
            self.driver.find_id('com.android.camera:id/v9_camera_picker')
            self.driver.find_id('com.android.camera:id/v9_camera_picker').click()
            time.sleep(5)
            self.driver.find_id('com.android.camera:id/inten_done_apply').click()
            time.sleep(4)
        except:
            try:
                # vivoX21、vivoX9
                self.driver.find_id('com.android.camera:id/shutter_button')
                self.driver.find_id('com.android.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.android.camera:id/done_button').click()
                time.sleep(4)
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                    time.sleep(4)
                except:
                    pass
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(3)

    # 修改作品封面——相册
    def Dubbing_work_Cover_Album(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
        time.sleep(3)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.856)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.875)
        else:
            pass
        time.sleep(2)
        photo_count = self.driver.find_ids(self.id + 'photo_wall_item_photo')
        select = random.randint(0, len(photo_count) - 1)
        self.driver.find_ids(self.id + 'photo_wall_item_photo')[select].click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
            select = random.randint(0, len(photo_count) - 1)
            self.driver.find_ids(self.id + 'photo_wall_item_photo')[select].click()
        except:
            pass
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(4)

    # 标题名称-输入30个字符
    def Upload_title(self):
        self.driver.find_id(self.id + 'title').send_keys('123456789012345678901234567890')
        time.sleep(2)
        char = self.driver.find_id(self.id + 'title').text
        char_check = '123456789012345678901234567890'
        assert char == char_check
        time.sleep(2)

    # 标题名称-清空标题
    def Upload_title_clear(self):
        self.driver.find_id(self.id + 'title').clear()
        num = self.driver.find_id(self.id + 'title_count').text
        check = '0/30'
        assert num == check
        time.sleep(2)

    # 上传界面标签显示检查
    def Upload_channel_select(self):
        try:
            self.driver.find_xpath('添加')
        except:
            self.driver.find_id(self.id + 'tv1').click()
        time.sleep(2)
        self.driver.find_xpath('添加').click()
        self.driver.wait_id(self.id + 'edit_text')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv')
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_xpath('添加').click()
            self.driver.wait_id(self.id + 'edit_text')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv1')
            self.driver.find_id(self.id + 'tv1').click()
            time.sleep(2)
            hot_lable = self.driver.find_ids(self.id + 'tv')
            select = random.randint(0, len(hot_lable))
            self.driver.find_ids(self.id + 'tv')[select].click()
            time.sleep(2)
            label_name = self.driver.find_id(self.id + 'tv1').text
            self.driver.find_id(self.id + 'tv_right').click()
            time.sleep(2)
            label_check = self.driver.find_id(self.id + 'tv1').text
            assert label_name == label_check,'标签对比不一致，%s,%s' % (label_name, label_check)
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #上传界面设置私密
    def Upload_privacy(self):
        try:
            self.driver.find_id(self.id + 'tv1')
            self.driver.find_id(self.id + 'pri_switch_tv').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'private_top_tv2')
            except:
                print('点击私密后未显示私密提示文案')
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 上传界面-求合作开关
    def Dubbing_Coor_switch(self):
        try:
            self.driver.find_id(self.id + 'check_box_add_square')
            state = self.driver.find_id(self.id + 'check_box_add_square').get_attribute('checked')
            if state:
                self.driver.find_id(self.id + 'check_box_add_square').click()
                time.sleep(2)
            else:
                pass
        except:
            pass
        time.sleep(2)

    # 作品上传按钮
    def Upload(self):
        self.driver.find_id(self.id + 'uploadbtn').click()
        self.driver.wait_id(self.id + 'close')
        time.sleep(2)

    #上传成功后点击查看视频详情
    def Upload_video_detial(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #点击查看视频详情
            self.driver.find_id(self.id + 'img_url').click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            print('视频上传失败，不执行视频查看用例')

    #上传成功后下载视频到本地
    def Video_download(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #视频下载
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.922, self.y * 0.232, self.x * 0.57, self.y * 0.232)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.786, self.y * 0.186, self.x * 0.54, self.y * 0.186)
            time.sleep(2)
            self.driver.find_id(self.id + 'down').click()
            time.sleep(2)
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.507, self.y * 0.24, self.x * 0.897, self.y * 0.24)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.509, self.y * 0.186, self.x * 0.753, self.y * 0.186)
        except:
            pass
        time.sleep(2)

    #上传成功后视频站外分享
    def Upload_video_share(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #微信分享
            self.driver.find_id(self.id + 'wx').click()
            time.sleep(4)
            self.driver.wait_id('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            self.driver.wait_id(self.id + 'wx')
            time.sleep(2)

            #朋友圈分享
            self.driver.find_id(self.id + 'wxf').click()
            self.driver.wait_id('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            self.driver.wait_id(self.id + 'wx')
            time.sleep(2)

            #QQ分享
            self.driver.find_id(self.id + 'qq').click()
            self.driver.wait_id('com.tencent.mobileqq:id/ivTitleBtnRightText')
            time.sleep(2)
            self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
            time.sleep(2)

            #QQ空间分享
            self.driver.find_id(self.id + 'qqz').click()
            self.driver.wait_id('com.tencent.mobileqq:id/ivTitleBtnRightText')
            self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
            time.sleep(2)

            #微博分享
            self.driver.find_id(self.id + 'wb').click()
            self.driver.wait_id('com.sina.weibo:id/titleSave')
            self.driver.find_id('com.sina.weibo:id/titleBack').click()
            time.sleep(2)
            self.driver.find_xpath('不保存').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.507, self.y * 0.24, self.x * 0.897, self.y * 0.24)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.786, self.y * 0.186, self.x * 0.54, self.y * 0.186)
            time.sleep(2)
        except Exception as e:
            print(e)

    #上传成功进入视频详情删除视频
    def Upload_video_delete(self):
        try:
            self.driver.find_id(self.id + 'wx')
            self.driver.find_id(self.id + 'img_url').click()
            self.driver.wait_id(self.id + 'btnBack')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'setting').click()
            time.sleep(2)
            self.driver.tap(self.x * 0.5,self.y * 0.854)
            time.sleep(2)
            tip = self.driver.find_id(self.id + 'txtContent').text
            check = '删除作品'
            assert check in tip,'作品删除提示内容校验不一致'
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except Exception as e:
            print(e)

    #上传失败保存草稿箱
    def Upload_fail_save(self):
        try:
            self.driver.find_id(self.id + 're_update')
            self.driver.find_id(self.id + 'saveToDraft').click()
            time.sleep(3)
            self.driver.find_xpath('保存草稿').click()
            self.driver.wait_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except Exception as e:
            print(e)

    # 上传失败查看失败原因
    def Upload_fail_reason(self):
        try:
            self.driver.find_id(self.id + 're_update')
            self.driver.find_id(self.id + 'rl_bg').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                print('上传失败的情况下，点击作品封面：', toast)
            except:
                pass
            time.sleep(2)
            reason = self.driver.find_id(self.id + 're_update').text
            reason_state1 = '修改标题'
            reason_state2 = '重新上传'
            if reason == reason_state1:
                self.driver.find_id(self.id + 're_update').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'edit').clear()
                time.sleep(2)
                self.driver.find_id(self.id + 'edit').send_keys('标题修改')
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
                try:
                    self.driver.wait_id(self.id + 'wx')
                except:
                    print('修改标题后重新上传失败')
            elif reason_state2 == reason_state2:
                self.driver.find_id(self.id + 're_update').click()
                try:
                    self.driver.wait_id(self.id + 'wx')
                except:
                    print('点击重新上传按钮后，作品依然上传失败')
            else:
                print('未知错误')
            time.sleep(2)
        except:
            pass

class Follow:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #首页关注主界面
    def Follow_jump(self):
        self.driver.find_id(self.id + 'ivCirclesTab').click()
        self.driver.wait_id(self.id + 'musicPlayView')
        time.sleep(2)

    #语聊推荐列表
    def Follow_chat_list(self):
        self.driver.find_id(self.id + 'musicPlayView').click()
        self.driver.wait_id(self.id + 'item_theme_image')
        self.driver.find_id(self.id + 'item_theme_image').click()
        self.driver.wait_download(self.id + 'user_list')
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'item_theme_image').click()
        time.sleep(2)


    #首页关注列表进入个人空间
    def Follow_person_zoom(self):
        name = self.driver.find_id(self.id + 'textView').text
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        Name = self.driver.find_id(self.id + 'username').text
        assert name == Name

    #切换分类
    def Follow_Switch_Classification(self):
        #作品tab
        self.driver.find_id(self.id + 'tv_film').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
        except:
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)

        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)

        # QQ空间
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)

        # 点击新浪
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.682, self.y * 0.712)
        self.driver.wait_xpath('发送')
        time.sleep(2)
        self.driver.find_id('com.sina.weibo:id/titleBack').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('不保存')
            self.driver.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        # 点击私信
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.846)
        self.driver.wait_id(self.id + 'filter_edit')
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys("15697802")
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_id(self.id + 'userhead')
            name = self.driver.find_id(self.id + 'name').text
            name2 = '米爱'
            if name == name2:
                self.driver.find_id(self.id + 'name').click()
                self.driver.wait_id(self.id + 'right_icon1')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            else:
                print("未搜索到指定用户")
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 点击下载视频到本地
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.807)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.311, self.y * 0.846)
        # 先判断点击是否为下载按钮，若是复制按钮则会toast提示，不是复制按钮则判断是否有非会员弹窗，不是则直接等待作品下载完成
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '存在'
            if check in toast:
                print(toast)
        except:
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                try:
                    self.driver.wait_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                except:
                    pass

        # 点击复制链接
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.846)
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.wait_id(self.id + 'txtContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                pass
        time.sleep(2)

        # 点击转发
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.88, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.87, self.y * 0.846)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'reprint')
            self.driver.find_id(self.id + 'content').send_keys("不错，转发了！")
            time.sleep(2)
            self.driver.find_id(self.id + 'reprint').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                try:
                    self.driver.find_id(self.id + 'reprint')
                    self.driver.find_id(self.id + 'reprint').click()
                    self.driver.wait_toast('//android.widget.Toast')
                except Exception as e:
                    print(e)
        except:
            # 点击取消分享弹窗按钮
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.937)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.947)
        time.sleep(2)
        # 关注界面点赞
        while True:
            try:
                self.driver.find_id(self.id + 'item_attention_pprint()')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        num = self.driver.find_id(self.id + 'item_attention_pprint()').text
        self.driver.find_id(self.id + 'item_attention_pprint()').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            pass
        new_num = self.driver.find_id(self.id + 'item_attention_pprint()').text
        assert num == new_num
        time.sleep(2)

        # 关注界面评论作品
        while True:
            try:
                self.driver.find_id(self.id + 'item_attention_comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'item_attention_comment_count').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('日常评论下！^.^')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast,'关注界面发送评论提示校验不一致'
        except:
            print('未检测到评论发送toast提示')
        time.sleep(2)

        #帖子tab
        self.driver.find_id(self.id + 'tv_tiezi').click()
        time.sleep(3)
        # 设置关注区权限
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.794)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.7)
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 特别关注
        for i in range(2):
            self.driver.find_id(self.id + 'more').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.864)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.77)
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败'+toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)

        #转发私信
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        self.driver.find_id(self.id + 'group_chat').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'editContent')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #帖子举报
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('举报功能测试！')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '举报成功'
            if toast != check:
                print(toast)
                self.driver.find_id(self.id + 'btnBack').click()
        except:
            print('未检测到举报toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'tag').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').click()
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'img1')
            self.driver.find_id(self.id + 'img1').click()
            time.sleep(2)
            self.driver.back()
        except:
            try:
                self.driver.find_id(self.id + 'play')
                self.driver.find_id(self.id + 'play').click()
                time.sleep(2)
            except:
                try:
                    self.driver.find_id(self.id + 'playBtn')
                    self.driver.find_id(self.id + 'playBtn').click()
                    self.driver.wait_id(self.id + 'tv_video_detail_title')
                    self.driver.back()
                except:
                    pass
        time.sleep(2)

        #素材tab
        self.driver.find_id(self.id + 'tv_source').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        #设置关注区权限
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        #设置特别关注
        for i in range(2):
            self.driver.find_id(self.id + 'more').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.864)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.89)
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败' + toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)


        self.driver.find_id(self.id + 'content').click()
        self.driver.wait_id(self.id + 'right_icon1')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #点击素材标签
        self.driver.find_id(self.id + 'tv_source_from').click()
        self.driver.wait_id(self.id + 'right_icon1')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_source_right')
            self.driver.find_id(self.id + 'tv_source_right').click()
            self.driver.wait_id(self.id + 'right_icon1')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        #点击素材配音按钮
        self.driver.find_id(self.id + 'action').click()
        while True:
            try:
                self.driver.find_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
                try:
                    self.driver.find_id(self.id + 'roleall')
                    self.driver.find_id(self.id + 'roleall').click()
                except:
                    pass
                break
            except:
                try:
                    self.driver.find_id(self.id + 'roleall')
                    self.driver.find_id(self.id + 'roleall').click()
                    break
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

        #特别关注
        self.driver.find_id(self.id + 'tv_attention').click()
        time.sleep(2)
        for i in range(2):
            self.driver.find_id(self.id + 'more').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.864)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.89)
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败' + toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)

    #关注界面送礼9.12版本不再支持送礼
    # def test_h(self):
    #     while True:
    #         try:
    #             self.driver.find_id(self.id + 'item_attention_pprint')
    #             self.driver.find_id(self.id + 'item_attention_pprint').click()
    #             break
    #         except:
    #             self.driver.swip_up()
    #             time.sleep(2)
    #     time.sleep(4)
    #     self.driver.find_id(self.id + 'confirm').click()
    #     self.driver.wait_toast('//android.widget.Toast')
    #     time.sleep(2)
    #     self.driver.swip_up()
    #     time.sleep(2)


    def Follow_Up_refresh(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)

class Live:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id
    def Live_list(self):
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.197, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >= 2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)

        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        self.driver.find_id(self.id + 'create')

    #进入语聊间
    def Live_Into_live_detail(self):
        self.driver.find_id(self.id + 'fram').click()
        self.driver.wait_id(self.id + 'gift_value')

    #切换语聊间
    def Live_Switch_live(self):
        for i in range(3):
            self.driver.swip_left()
            self.driver.wait_id(self.id + 'gift_value')
            time.sleep(2)

    #语聊间创建界面编辑
    def LiveCreate_live_edit(self):
        self.driver.find_id(self.id + 'create').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'title').send_keys('空')
        time.sleep(2)
        self.driver.find_id(self.id + 'tag_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv').click()
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #创建进入语聊间
    def LiveCreate_Room(self):
        self.driver.find_id(self.id + 'create').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'check_box').click()
        self.driver.find_id(self.id + 'start_live').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        self.driver.wait_id(self.id + 'name')

    #闭麦
    def Live_Close_mic(self):
        try:
            self.driver.find_id(self.id + 'mic_tag')
        except:
            self.driver.find_id(self.id + 'home_microphone1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'mic_own_control').click()
            self.driver.wait_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'mic_tag').click()
        time.sleep(2)

    #开麦
    def Live_Open_mic(self):
        try:
            self.driver.find_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'home_microphone1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'mic_own_control').click()
            self.driver.wait_not_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'name').click()
        except:
            pass
        time.sleep(2)

    #查看头像简介
    def Live_Head_Introduction(self):
        el = self.driver.find_id(self.id + 'userhead')
        self.driver.Long_Touche(el,3000)
        try:
            self.driver.find_id(self.id + 'user_id')
            self.driver.find_id(self.id + 'icon_close').click()
        except:
            print('长按麦位用户头像未显示简介弹窗')
        time.sleep(2)

    #送礼
    def Live_gift(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'gift_img')
        time.sleep(2)
        self.driver.find_xpath(self.id + '鲜花').click()
        self.driver.find_id(self.id + 'right_view').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_view').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(2)
        self.driver.tap(self.x * 0.5,self.y * 0.5)
        time.sleep(2)

    #点赞
    def Live_good(self):
        self.driver.find_id(self.id + 'periscope_view').click()
        time.sleep(2)

    #语聊间发送评论
    def Live_comments(self):
        self.driver.find_id(self.id + 'function_comment_layout').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('这是一个语聊间！')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'home_comment_comments')
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #长按用户名@用户
    def Live_at(self):
        el = self.driver.find_id(self.id + 'username')
        self.driver.Long_Touche(el,3000)
        try:
            self.driver.find_id(self.id + 'editContent')
            content = self.driver.find_id(self.id + 'editContent').text
            check = '@'
            assert check in content
            time.sleep(1)
            self.driver.find_id(self.id + 'btn_send')
            self.driver.wait_id(self.id + 'home_comment_comments')
            self.driver.find_id(self.id + 'name').click()
        except:
            print('长按用户名未出现@')
        time.sleep(2)

    #发红包
    def Live_red(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.097, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'cash_num').send_keys('0.1')
        time.sleep(1)
        self.driver.find_id(self.id + 'people_num').send_keys('1')
        time.sleep(2)
        self.driver.find_id(self.id + 'generate_red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'rl_red')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_more').click()
        self.driver.wait_id(self.id + 'open_red_packet_btn')
        self.driver.find_id(self.id + 'open_red_packet_btn').click()
        self.driver.wait_id(self.id + 'diamond')
        self.driver.back()
        time.sleep(2)

    #语聊间分享
    def Live_share(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.301, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.295, self.y * 0.812)
            time.sleep(2)
        #私信
        self.driver.tap(self.x * 0.122, self.y * 0.912)
        self.driver.wait_id(self.id + 'group_chat')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(3)

    #语聊间私信
    def Live_persion_notice(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.499, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)



    #语聊间黑名单
    def Live_blacklist(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.698, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    #设置房管
    def Live_Manager(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.894, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    #随机抽选游戏
    def Live_Games(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_turntable').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'customize_back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_random').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'random_close').click()
        time.sleep(2)

    #麦位数量
    def Live_Mic_count(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.295, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'check2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    #pia戏
    def Live_Pia(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.496, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_close').click()
        time.sleep(2)

    #组Cp
    def Live_Cp(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.704, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_check').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #公告
    def Live_Notice(self):
        self.driver.find_id(self.id + 'marquee').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_sure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_title').send_keys('哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'et_content').send_keys('哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_save').click()
        time.sleep(2)

    #房间成员列表
    def Live_Members(self):
        try:
            self.driver.find_id(self.id + 'pack_up').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'count').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'room_user').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'fast_room_check').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        self.driver.wait_xpath('移除')
        self.driver.find_xpath('申请').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'fast_room_check').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #房间详情
    def Live_Room_detail(self):
        self.driver.find_id(self.id + 'user_list').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

    #房间背景音音乐
    def Live_Music(self):
        self.driver.find_id(self.id + 'function_joke_articles').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'title')
        except:
            self.driver.find_id(self.id + 'add_music').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'rl').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'previous').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'modify').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'music_list').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #语聊任务
    def Live_Tasks(self):
        self.driver.find_id(self.id + 'img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)


    #退出语聊间
    def Live_Room_Exit(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'outLive')
            self.driver.find_id(self.id + 'outLive').click()
        except:
            pass
        time.sleep(2)

class Material:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入素材库
    def Source_into_List(self):
        self.driver.find_id(self.id + 'btn_more').click()
        self.driver.wait_id(self.id + 'coor')

    # 素材库搜索素材
    def Source_searchs(self):
        self.driver.wait_id(self.id + 'tv_search')
        self.driver.find_id(self.id + 'tv_search').click()
        time.sleep(4)

        #点击热门素材标签
        tv_name = self.driver.find_ids(self.id + 'tv')
        time.sleep(2)
        for i in range(len(tv_name)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'rl_left2')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)

        # 历史搜索记录
        try:
            self.driver.find_id(self.id + 'item').click()
            self.driver.wait_id(self.id + 'iv_source')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        except:
            print('未显示有历史搜索记录')
        time.sleep(2)
        # 清空搜索记录
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

        # 推荐搜索-更多热点
        self.driver.find_id(self.id + 'tv1').click()
        self.driver.wait_id(self.id + 'rank_name')
        time.sleep(2)
        self.driver.find_id(self.id + 'rank_name').click()
        try:
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            print('素材标签详情界面未显示素材信息')

        # 上滑加载标签列表
        while True:
            self.driver.swip_up()
            time.sleep(2)
            label_name = self.driver.find_ids(self.id + 'rank_name')[-1].text
            self.driver.swip_up()
            label_name1 = self.driver.find_ids(self.id + 'rank_name')[-1].text
            if label_name == label_name1:
                self.driver.find_id(self.id + 'btnBack').click()
                break
            else:
                pass
        time.sleep(2)

    # 进入标签详情界面
    def Source_tv_detail(self):
        self.driver.find_id(self.id + 'tv1').click()
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)
        # 依次点击切换标签，且点击标签后进入素材预览界面再返回
        label_touche = self.driver.find_ids(self.id + 'types_name')
        for i in range(len(label_touche) - 1, -1, -1):
            self.driver.find_ids(self.id + 'types_name')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            try:
                self.driver.find_id(self.id + 'iv_source').click()
                self.driver.wait_id(self.id + 'userhead')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

        # 上滑加载素材搜索结果列表
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnClear').click()
        time.sleep(2)

    # 搜索素材
    def Source_search(self):
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'iv_source')
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        el = self.driver.find_ids(self.id + 'types_name')
        for i in reversed(el):
            i.click()
            time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 素材库主界面8个大分类
    def Source_Classification(self):
        tv_main = self.driver.find_ids(self.id + 'tv')
        for i in range(len(tv_main)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            # 热门推荐标签
            tv_Branch = self.driver.find_ids(self.id + 'tv')
            for x in range(len(tv_Branch)):
                self.driver.find_ids(self.id + 'tv')[x].click()
                self.driver.wait_id(self.id + 'img_url')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            # 更多热门标签
            self.driver.find_id(self.id + 'tv1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            Screening = self.driver.find_ids(self.id + 'types_name')
            for j in range(len(Screening) - 1, -1, -1):
                self.driver.find_ids(self.id + 'types_name')[j].click()
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(self.id + 'iv_source').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 合作广场-广场列表
    def Source_Coor(self):
        self.driver.find_id(self.id + 'rl_coor').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

        # 点击视频预览界面的合作按钮进入配音界面
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')

        # 点击广场列表中的配音按钮进入配音界面
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        time.sleep(2)

        # 获取广场中的求合作剩余时间
        try:
            self.driver.find_id(self.id + 'item_sh_clock_time')
        except:
            print('未显示时间')
        time.sleep(2)

        # 加载列表
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)

    # 合作广场角色tab筛选项切换
    def Source_role_change(self):
        self.driver.find_id(self.id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'dp_female').click()
        time.sleep(2)

    # 合作广场-热门列表
    def Source_coor_hot(self):
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        # 显示合作次数
        try:
            self.driver.find_id(self.id + 'count')
        except:
            print('合作广场热门列表未显示合作次数')
        time.sleep(2)
        # 加载列表
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)


    # 合作广场-我的
    def test_i(self):
        time.sleep(2)
        self.driver.find_xpath('我的').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 合作广场-搜索
    def Source_coor_search(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_search_keyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.find_id(self.id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(self.id + 'play')
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        # 滑动加载列表
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_search_keyword').send_keys('槛花笼鹤')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(5)
        try:
            self.driver.find_xpath('没有搜索到任何内容')
        except:
            print('检查搜索无结果显示失败')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # # 声音鉴定
    # def test_a(self):
    #     self.driver.find_id(self.id + 'sj').click()
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id(self.id + 'reIndetify')
    #         self.driver.find_id(self.id + 'reIndetify').click()
    #         time.sleep(2)
    #     except:
    #         pass
    #     self.driver.find_id(self.id + 'boy').click()
    #     time.sleep(2)
    #     self.driver.find_id(self.id + 'girl').click()
    #     time.sleep(2)
    #     conten = self.driver.find_id(self.id + 'text').text
    #     self.driver.find_id(self.id + 'change').click()
    #     time.sleep(2)
    #     conten_new = self.driver.find_id(self.id + 'text').text
    #     assert conten != conten_new,'切换朗读的前后内容对比一致，切换失败'
    #     time.sleep(2)
    #
    # # 录音
    # def test_b(self):
    #     i = 1
    #     while True:
    #         i = i + 1
    #         try:
    #             self.driver.find_id(self.id + 'dubbing').click()
    #             time.sleep(15)
    #             self.driver.find_id(self.id + 'dubbing').click()
    #             self.driver.wait_id(self.id + 'preview')
    #             break
    #         except:
    #             pass
    #         if i == 10:
    #             break
    #         else:
    #             pass
    #     time.sleep(2)
    #
    # def test_b_a(self):
    #     try:
    #         self.driver.find_id(self.id + 'play')
    #         return True
    #     except:
    #         return False
    #
    # # 声鉴报告界面
    # def test_c(self):
    #     state = Test_c_Voicetest().test_b_a()
    #     print(state)
    #     if state == True:
    #         voice_style = self.driver.find_id(self.id + 'voice_type').text
    #         print(voice_style)
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'play').click()
    #         self.driver.wait_download(self.id + 'play')
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'title').click()
    #         self.driver.wait_id(self.id + 'userhead')
    #         self.driver.find_id(self.id + 'btnBack').click()
    #         time.sleep(2)
    #         for i in range(3):
    #             self.driver.swip_up()
    #             time.sleep(2)
    #         time.sleep(2)
    #     else:
    #         print('声鉴结果界面跳转失败，跳过此测试步骤')
    #
    # # 点击配音，保存草稿箱
    # def test_d(self):
    #     state = Test_c_Voicetest().test_b_a()
    #     if state == True:
    #         self.driver.find_id(self.id + 'action').click()
    #         time.sleep(2)
    #         self.driver.wait_download(self.id + 'action')
    #         self.driver.find_id(self.id + 'action').click()
    #         self.driver.wait_download(self.id + 'title')
    #         self.driver.Background()
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'complete').click()
    #         self.driver.wait_id(self.id + 'txtTitle')
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'pri_switch_tv').click()
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'saveToDraft').click()
    #         time.sleep(2)
    #         self.driver.find_id(self.id + 'btnSubmit').click()
    #         time.sleep(2)
    #         self.driver.wait_xpath('退出配音')
    #         self.driver.find_xpath('退出配音').click()
    #         time.sleep(2)
    #         for i in range(6):
    #             self.driver.swip_down()
    #             time.sleep(2)
    #         self.driver.find_id(self.id + 'reIndetify').click()
    #         time.sleep(2)
    #         # 返回素材库
    #         self.driver.find_id(self.id + 'back').click()
    #         time.sleep(2)
    #     else:
    #         print('声鉴结果界面跳转失败，跳过此测试步骤')
    #         self.driver.back()

    '''素材列表'''
    def Source_list(self):
        self.driver.find_id(self.id + 'unlimited').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        for i in range(15):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
        except:
            pass
        time.sleep(4)

    #素材列表预览模式
    def Source_preview(self):
        try:
            self.driver.find_id(self.id + 'tv_title')
        except:
            self.driver.find_id(self.id + 'change_type').click()
        time.sleep(2)
        self.driver.swip_up()
        self.driver.find_id(self.id + 'bg_view').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'subtitleView').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change_type').click()
        time.sleep(2)

        # 点击进入素材预览界面
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 切换角色筛选项
        self.driver.find_id(self.id + 'boy').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_girl')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'coor').click()
        time.sleep(2)
        num = self.driver.find_ids(self.id + 'tv_source_from')
        for i in range(len(num)):
            try:
                self.driver.find_ids(self.id + 'tv_boy')[i]
            except:
                name = self.driver.find_ids(self.id + 'tv_source_title')[i].text
                print("合作素材列表中未显示双人角色:%s" % name)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'unlimited').click()
        time.sleep(4)

    # 素材预览详情界面查看视频是否循环播放
    def Source_detail(self):
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')

        # 进入素材作者个人空间
        name1 = self.driver.find_id(self.id + 'user_name').text
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        name2 = self.driver.find_id(self.id + 'username').text
        assert name1 in name2,'素材视频详情界面的用户名称与空间中的用户名称校验不一致'
        time.sleep(2)

    # 关注按钮
    def Source_detail_follow(self):
        self.driver.find_id(self.id + 'btn_video_detail_follow').click()
        try:
            follow_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '关注成功'
            assert check in follow_toast, '关注toast内容校验不一致'
        except:
            try:
                self.driver.find_id(self.id + 'editContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
            except:
                pass
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        self.driver.find_id(self.id + 'follow_status').click()
        time.sleep(4)

    # 素材预览界面点击素材标签
    def Source_detail_types(self):
        lable_name = self.driver.find_ids(self.id + 'types_name')
        for i in range(len(lable_name)):
            name = self.driver.find_ids(self.id + 'types_name')[i].text
            self.driver.find_ids(self.id + 'types_name')[i].click()
            self.driver.wait_id(self.id + 'tag_name')
            name1 = self.driver.find_id(self.id + 'tag_name').text
            assert name1 in name,'素材预览界面点击的标签与标签详情界面的标签校验不一致'
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 退出素材预览界面
    def Source_detail_exit(self):
        try:
            self.driver.find_id(self.id + 'tag_name')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)


    # 素材库界面素材上传按钮
    def Source_upload(self):
        self.driver.find_id(self.id + 'upload').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'tv_upload')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

class Person:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    # 退出当前界面
    def Bcak(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 首页进入“我的”界面
    def Person_My(self):
        self.driver.wait_id(self.id + 'ivMineTab')
        self.driver.find_id(self.id + 'ivMineTab').click()
        self.driver.wait_id(self.id + 'username')
        time.sleep(2)

    # 我的界面点击头像进入个人空间
    def Person_into_my_zoom(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        time.sleep(2)

    # 我的界面点击关注进入关注列表
    def Person_home_into_follow(self):
        follow_count = self.driver.find_id(self.id + 'followed_count').text
        time.sleep(1)
        self.driver.find_id(self.id + 'followed_count').click()
        self.driver.wait_id(self.id + 'filter_edit')
        time.sleep(2)
        if int(follow_count) > 9:
            self.driver.back()
        else:
            follow_count1 = self.driver.find_ids(self.id + 'username')
            assert int(len(follow_count1)) == int(follow_count)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 我的界面点击粉丝进入粉丝列表
    def Person_home_into_fans(self):
        fan_count = self.driver.find_id(self.id + 'fans_count').text
        time.sleep(1)
        self.driver.find_id(self.id + 'fans_count').click()
        self.driver.wait_id(self.id + 'vip_tag')
        time.sleep(2)
        if int(fan_count) > 8:
            pass
        else:
            fan_count1 = self.driver.find_ids(self.id + 'username')
            assert int(len(fan_count1)) == int(fan_count)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 用户ID
    def Person_copy_ID(self):
        self.driver.find_id(self.id + 'tv_uid').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    # 个人空间搜索-作品
    def Person_Zoom_works_search(self):
        search_title = self.driver.find_id(self.id + 'title').text
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys(search_title)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'photo').click()
        self.driver.wait_id(self.id + 'txtKeyword')
        try:
            self.driver.find_id(self.id + 'clear')
            time.sleep(2)
            self.driver.find_id(self.id + 'clear').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'clear')
                print('个人空间搜索作品后，点击清空搜索记录，依然显示有搜索记录')
            except:
                pass
        except:
            print('个人空间搜索作品后退出再进，未显示作品搜索历史记录')
        time.sleep(2)

        # 个人空间搜索——作品搜索无结果显示
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_xpath(self.id + 'll_noSearchResult')
        except:
            print('作品搜索无结果时未显示任何提示信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 个人空间—搜索-搜索个人素材
    def Person_Zoom_source_search(self):
        self.driver.find_id(self.id + 'source_text').click()
        time.sleep(2)
        search_title = self.driver.find_id(self.id + 'source_text').text
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_xpath('没有搜到任何内容')
        except:
            print('素材搜索无结果时未显示任何提示信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys(search_title)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'iv_source')
            name = self.driver.find_id(self.id + 'tv_source_title').text
            assert search_title in name
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_source_title').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 编辑资料
    def Person_Zoom_edit_info(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.719)
        elif self.y > 2279:
            self.driver.tap(self.x * 0.5, self.y * 0.76)
        time.sleep(4)
        try:
            self.driver.find_xpath('个人资料')
        except:
            print('未跳转到个人资料界面')
        time.sleep(2)

    # 更换头像
    def Person_Zoom_change_head(self):
        # 点击头像-拍照
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.793)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            try:
                self.driver.wait_sys('始终允许')
            except:
                try:
                    self.driver.wait_sys('允许')
                except:
                    pass
            self.driver.find_id(self.id + 'userhead').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.793)
            elif self.y == 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(2)
        except:
            pass
        time.sleep(3)
        try:
            '''
            以下操作只适用VIVOx9
            '''
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                '''
                oppo r11
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.oppo.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        time.sleep(6)
        self.driver.find_id(self.id + 'confirm').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            assert toast == check
        except:
            print('拍照更换头像未检测到toast提示')
        time.sleep(2)
        # 更换相册图片
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.869)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        time.sleep(2)
        self.driver.find_id('com.android.gallery3d:id/ic_public_arrow_right').click()
        time.sleep(2)
        self.driver.find_id('com.android.gallery3d:id/top_frame').click()
        time.sleep(2)
        self.driver.find_id('com.android.gallery3d:id/head_select_right').click()
        try:
            toast1 = self.driver.wait_toast('//android.widget.Toast')
            check1 = '视频'
            assert check1 in toast1, toast1
        except:
            self.driver.find_id(self.id + 'confirm').click()
            try:
                toast1 = self.driver.wait_toast('//android.widget.Toast')
                check1 = '修改成功'
                assert check1 in toast1,'相册替换头像toast提示内容校验不一致'
            except:
                print('相册更换头像未检测到toast提示')
            time.sleep(2)

    # 输入个人简介
    def Person_Zoom_Introduction(self):
        self.driver.find_id(self.id + 'tv_sign').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_sign').send_keys('空空空')
        time.sleep(2)

    # 修改性别
    def Person_Zoom_change_gender(self):
        gender = self.driver.find_id(self.id + 'tv_gender').text
        if gender == '女':
            self.driver.find_id(self.id + 'tv_gender').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.872)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(2)
        else:
            self.driver.find_id(self.id + 'tv_gender').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.872)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.89)
            time.sleep(2)

    # 修改地区
    def Person_Zoom_change_area(self):
        area = self.driver.find_id(self.id + 'tv_area').text
        self.driver.find_id(self.id + 'tv_area').click()
        self.driver.wait_id(self.id + 'name')
        areas = self.driver.find_ids(self.id + 'name')
        select = random.randint(0, len(areas))
        self.driver.find_ids(self.id + 'name')[select].click()
        time.sleep(2)
        area1 = self.driver.find_id(self.id + 'tv_area').text
        assert area != area1, '地区修改前后显示未刷新,%s' %area1
        time.sleep(2)

    # 修改生日
    def Person_Zoom_change_birthday(self):
        self.driver.find_id(self.id + 'tv_time').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_ensure').click()
        time.sleep(2)

    # 用户名敏感词检测
    def Person_Zoom_username_check(self):
        self.driver.find_id(self.id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_nickname').send_keys('政府')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '敏感词'
            assert check in toast
        except:
            print('用户名包含有敏感词，点击保存未弹出敏感词toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id('android:id/button1').click()
        time.sleep(2)

    # 会员头像挂件
    def Person_Zoom_Vip_headwear(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.792)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.823)
        self.driver.wait_id(self.id + 'txtTitle')
        count = self.driver.find_ids(self.id + 'img')
        for i in range(len(count) - 1, -1, -1):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'txtContent')
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'renew')
                self.driver.find_id(self.id + 'btnBack').click()
            except:
                pass
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnCancel').click()
            time.sleep(2)
        except:
            pass

    # 会员空间装扮
    def Person_Zoom_Vip_Dress(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.867)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        count = self.driver.find_ids(self.id + 'img')
        for i in range(len(count) - 1, -1, -1):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 用户演绎等级
    def Person_Zoom_user_level(self):
        self.driver.find_id(self.id + 'source_level').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'img_vip').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'guize1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    # 身份认证
    def Person_Zoom_Authentication(self):
        self.driver.find_id(self.id + 'vip_description').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 粉丝列表
    def Person_Zoom_fans(self):
        self.driver.find_id(self.id + 'll_fan').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'vip_tag')
        self.driver.find_id(self.id + 'iwant').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)

    # 关注列表
    def Person_Zoom_follows(self):
        self.driver.find_id(self.id + 'll_follow').click()
        self.driver.wait_id(self.id + 'status_icon')
        self.driver.find_id(self.id + 'username').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)

    # 社团列表
    def Person_Zoom_Societies(self):
        self.driver.find_id(self.id + 'll_society').click()
        self.driver.wait_id(self.id + 'status_icon')
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'user_image').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 作品上榜列表
    def Person_Zoom_Crunchies_list(self):
        self.driver.find_id(self.id + 'll_rank').click()
        self.driver.wait_id(self.id + 'middle_img')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_vip')
            self.driver.find_id(self.id + 'tv_vip').click()
            time.sleep(2)
            self.driver.wait_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'img_url').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)


    # 作品列表
    def Person_Zoom_work_list(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)

    # 切换作品列表tab
    def Person_Zoom_work_switch_label(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        count = self.driver.find_ids(self.id + 'title')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        for i in range(len(count) - 1, -1, -1):
            self.driver.find_id(self.id + 'film_all_count').click()
            time.sleep(2)
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(2)

    # 置顶作品
    def Person_Zoom_work_top(self):
        el = self.driver.find_id(self.id + 'filmBg1')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.789)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'img')
        except:
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.943)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.952)
            time.sleep(2)
            self.driver.find_id(self.id + 'filmBg1').click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'setting').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.703)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.75)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(3)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(4)
            el = self.driver.find_id(self.id + 'filmBg1')
            self.driver.Long_Touche(el, 3000)
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.789)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(4)
            try:
                self.driver.find_id(self.id + 'img')
            except:
                print('未显示置顶标签')
        time.sleep(2)

    # 作品列表界面长按删除作品
    def Person_Zoom_work_delete(self):
        el = self.driver.find_id(self.id + 'filmBg1')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.868)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(4)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(4)

    # 个人空间-求合作
    def Person_Zoom_coors(self):
        self.driver.find_id(self.id + 'coor_text').click()
        self.driver.wait_id(self.id + 'btnCooperate')
        self.driver.find_id(self.id + 'islook').click()
        self.driver.wait_download(self.id + 'video_play_btn')
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    # 求合作-邀请好友
    def Person_Zoom_coor_invite(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'invitation_count').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        time.sleep(2)
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.629)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.688)
        self.driver.wait_id(self.id + 'socialstatus')
        self.driver.find_id(self.id + 'socialstatus').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('给自己的合作！')
        time.sleep(2)
        self.driver.find_id(self.id + 'reprint').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            success_check = '邀请成功'
            Not_accept_check = '该用户暂不接受合作'
            if toast == success_check:
                pass
            elif toast == Not_accept_check:
                self.driver.find_id(self.id + 'cancel').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
        except:
            print('发送邀请后未检测到toast提示')
        time.sleep(2)

    # 求合作-私密（公开）
    def Person_Zoom_coor_Private_public(self):
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.703)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.746)
        time.sleep(2)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = "公开成功"
            assert check in toast,'求合作私密转公开toast校验不一致'
        except:
            try:
                self.driver.find_id(self.id + 'renew')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.back()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    # 求合作删除
    def Person_Zoom_coor_delete(self):
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.857)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.877)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast,'求合作删除失败'
        except:
            pass
        time.sleep(2)

    # 素材-视频预览
    def Person_Zoom_source_preview(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'source_text')
        time.sleep(2)
        self.driver.find_id(self.id + 'source_text').click()
        self.driver.wait_id(self.id + 'imgSource')
        self.driver.find_id(self.id + 'imgSource').click()
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 素材配音
    def Person_Zoom_Source_dubbing(self):
        self.driver.find_id(self.id + 'imgSource').click()
        self.driver.wait_id(self.id + 'right_icon1')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'yinpin')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'roleall')
                    break
                except:
                    self.driver.find_id(self.id + 'btnSubmit')
                    time.sleep(1)
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    break
            self.driver.wait_id(self.id + 'roleall')
            self.driver.find_id(self.id + 'roleall').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'action')
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'btnSubmit')
                        time.sleep(1)
                        self.driver.find_id(self.id + 'btnSubmit').click()
                        break
                    except:
                        pass
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        time.sleep(2)

    # 更多-点赞
    def Person_Zoom_goods_record(self):
        self.driver.find_id(self.id + 'more_text').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        num = self.driver.find_id(self.id + 'look').text
        if num == '0':
            el = self.driver.find_id(self.id + 'filmBg')
            self.driver.Long_Touche(el, 3000)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_good').click()
        good1 = self.driver.find_id(self.id + 'tv_good').text
        self.driver.find_id(self.id + 'tv_good').click()
        time.sleep(1)
        good2 = self.driver.find_id(self.id + 'tv_good').text
        assert good1 != good2
        time.sleep(2)

    # 更多-转发
    def Person_Zoom_forward(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('转发').click()
        self.driver.wait_id(self.id + 'filmBg')
        name = self.driver.find_id(self.id + 'userName').text
        self.driver.find_id(self.id + 'filmBg').click()
        try:
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '不存在'
            assert check in tip, '转发作品点击进入失败，提示信息错误'
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            detail_name = self.driver.find_id(self.id + 'user_name').text
            assert name == detail_name,'转发列表界面用户名与视频详情界面用户名不一致'
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 作品转发列表——删除作品
        title = self.driver.find_id(self.id + 'title').text
        count = self.driver.find_id(self.id + 'film_all_count').text
        el = self.driver.find_id(self.id + 'filmBg')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_xpath(title)
            print('转发作品删除失败')
        except:
            pass
        time.sleep(2)
        count1 = self.driver.find_id(self.id + 'film_all_count').text
        assert count != count1,'转发作品删除失败'
        time.sleep(2)

    # 帖子列表
    def Person_Zoom_post_list(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('帖子').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'good').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'tag').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'comment').click()
        self.driver.wait_id(self.id + 'editContent')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    # 帖子-转发私信-删除
    def Person_Zoom_forword_and_delete(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.793)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.829)
        time.sleep(2)
        self.driver.find_id(self.id + 'group_chat').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            print('帖子删除未检测到toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'username').click()
        self.driver.wait_id(self.id + 'film_all_count')
        time.sleep(2)
        self.driver.find_id(self.id + 'more_text').click()
        time.sleep(2)

    # 语聊列表
    def Person_chat_list(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        time.sleep(4)

    # 创建合辑
    def Person_Zoom_create_compilation(self):
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('合辑')
        time.sleep(2)
        self.driver.find_id(self.id + 'ok').click()
        time.sleep(3)
        try:
            self.driver.find_id(self.id + 'choice')
            self.driver.find_id(self.id + 'choice').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_right').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '创建成功'
                assert toast == check
                time.sleep(2)
            except:
                pass
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)

    # 合辑删除
    def Person_Zoom_delete_compilation(self):
        self.driver.find_id(self.id + 'single_text').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('合辑').click()
        self.driver.wait_id(self.id + 'filmBg')
        el = self.driver.find_id(self.id + 'filmBg')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            pass
        time.sleep(2)

    # 退出个人空间
    def Person_Zoom_quit(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 我的界面VIP入口
    def Person_Vip_enter(self):
        # 会员首次购买优惠入口
        try:
            self.driver.find_id(self.id + 'right_huiyuan').click()
            self.driver.wait_id(self.id + 'renew')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'img_vip').click()
        self.driver.wait_id(self.id + 'renew')
        time.sleep(2)

    # 会员权益计算
    def Person_Vip_Equity(self):
        self.driver.find_id(self.id + 'img_right').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'price')
        except:
            print('会员权益计算弹窗中未检测到相关控件')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    # 会员价格
    def Person_Vip_Price(self):
        price = self.driver.find_ids(self.id + 'tv_now_money')
        for i in range(len(price)):
            Price = self.driver.find_ids(self.id + 'tv_now_money')[i].text
            self.driver.find_ids(self.id + 'rl_all')[i].click()
            time.sleep(1)
            self.driver.find_id(self.id + 'renew').click()
            time.sleep(2)
            Price_buy = self.driver.find_id(self.id + 'tv_money').text
            assert Price in Price_buy
            time.sleep(2)
            self.driver.find_id(self.id + 'close_icon').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'cancel').click()
            time.sleep(2)

    # 会员赠送
    def Person_Vip_Give(self):
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'user_head')
        self.driver.find_id(self.id + 'user_head').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'renew')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 会员特权
    def Person_Vip_Privileges(self):
        try:
            self.driver.find_xpath('作品编辑')
        except:
            if self.y <= 2280:
                self.driver.swip_move(self.x * 0.5, self.y * 0.818, self.x * 0.5, self.y * 0.585)
        time.sleep(2)
        Member_privileges_page1 = self.driver.find_ids(self.id + 'name')
        privileges_list = []
        for i in range(len(Member_privileges_page1)):
            Name = self.driver.find_ids(self.id + 'name')[i].text
            privileges_list.append(Name)
        time.sleep(2)
        Start_Locat = self.driver.find_ids(self.id + 'name')[-1].location
        End_Locat = self.driver.find_ids(self.id + 'name')[-4].location
        start_swip_x = Start_Locat['x']
        start_swip_y = Start_Locat['y']
        end_swip_x = End_Locat['x']
        end_swip_y = End_Locat['y']
        if self.y >= 2280:
            self.driver.swip_move(start_swip_x, start_swip_y, end_swip_x, end_swip_y)
        time.sleep(2)
        Member_privileges_page2 = self.driver.find_ids(self.id + 'name')
        for i in range(len(Member_privileges_page2)):
            Name1 = self.driver.find_ids(self.id + 'name')[i].text
            privileges_list.append(Name1)
        privileges_chck_list = ['双倍金币', '免费曝光', '推荐涨粉', '升级加速', '上榜历史', '作品下载', '评论置顶',
                                '作品编辑', '云端存储', '语聊麦位', '专属挂件', '空间装扮']
        assert sorted(privileges_list) == sorted(privileges_chck_list)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #CP邀请
    def Person_Cp_invite(self):
        self.driver.find_id(self.id + 'img_cp').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'invite')
            self.driver.find_id(self.id + 'invite').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'filter_edit').send_keys('1247792')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSearch').click()
            time.sleep(2)
            self.driver.wait_xpath('逍遥剑仙')
            time.sleep(2)
            self.driver.find_id(self.id + 'userhead').click()
            self.driver.wait_id(self.id + 'right_icon1')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'cancel_invite').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'invite')
            time.sleep(2)
            self.driver.find_id(self.id + 'invite').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'filter_edit').send_keys('1247792')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSearch').click()
            time.sleep(2)
            self.driver.wait_xpath('逍遥剑仙')
            time.sleep(2)
            self.driver.find_id(self.id + 'userhead').click()
            self.driver.wait_id(self.id + 'right_icon1')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # #CP空间
    # def Person_Cp_Zoom(self):
    #
    # #达人
    # def Person_Daren(self):
    #     self.driver.find_id(self.id + 'img_daren').click()


    # 系统消息
    def Person_System_Notices(self):
        self.driver.find_id(self.id + 'system_notice').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'agree')
            self.driver.find_id(self.id + 'agree').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 点赞消息
    def Person_Good_Notices(self):
        try:
            self.driver.find_id(self.id + 'gift_point')
            self.driver.find_id(self.id + 'gift').click()
            self.driver.wait_id(self.id + 'userhead')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'gift_point')
                print('点赞红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'gift').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
            time.sleep(2)
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

        # 回赞
        self.driver.find_id(self.id + 'guanzhu').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 合作消息
    def Person_Coor_Notices(self):
        try:
            self.driver.find_id(self.id + 'cooper_count')
            self.driver.find_id(self.id + 'textView15').click()
            self.driver.wait_id(self.id + 'userhead')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'cooper_count')
                print('合作消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'textView15').click()
        self.driver.wait_id(self.id + 'more')
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 合作配音
    def Person_Coor_Dubbing(self):
        try:
            self.driver.find_xpaths('合作配音')[1].click()
            self.driver.wait_download(self.id + 'action')
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'play').click()
            time.sleep(3)
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 删除合作消息
    def Person_Coor_delete(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.882)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.903)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除合作消息成功'
            assert check in toast, '合作消息删除失败'
        except:
            print('未检测到合作消息删除toast提示')
        time.sleep(2)

    # 生成作品
    def Person_Coor_Generate_works(self):
        self.driver.find_id(self.id + 'rl_tag2').click()
        time.sleep(2)
        self.driver.find_xpaths('生成作品')[1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'head_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_take_photo').click()
        time.sleep(5)
        try:
            '''
            以下操作只适用VIVOx9
            '''
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                '''
                oppo r11/r15
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.oppo.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        time.sleep(4)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'head_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'title').send_keys('功能测试')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv')
            self.driver.find_id(self.id + 'tv').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    # 生成作品tab界面预览视频
    def Person_Coor_video_play(self):
        self.driver.find_id(self.id + 'play').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast,'视频详情界面进入失败'
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    # 合作消息设置
    def Person_Coor_Notice_setting(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(4)
        # 获取当前界面所有resourceId,但部分ID不可用，因此无法区分筛选出真正可以点击的ID
        # count = self.driver.search_id()
        # print(count)
        # self.id = re.findall(r'resource-id="com.happyteam.dubbingshow:id/(.*?)"',count)
        # print(self.id)
        self.driver.find_id(self.id + 'acceptAll').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'acceptFirends').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'acceptNone').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'clearAllInviter').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 评论消息-跳转个人空间
    def Person_Comment_Notices(self):
        try:
            self.driver.find_id(self.id + 'comment_count')
            self.driver.find_id(self.id + 'textView16').click()
            self.driver.wait_id(self.id + 'reply')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'comment_count')
                print('评论消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'textView16').click()
        self.driver.wait_id(self.id + 'reply')
        time.sleep(2)
        name = self.driver.find_id(self.id + 'textView').text
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        Zoom_name = self.driver.find_id(self.id + 'username').text
        assert name == Zoom_name
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 评论消息-关注
    def Person_Comment_follows(self):
        self.driver.find_id(self.id + 'guanzhu').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'editContent')
            time.sleep(2)
            self.driver.find_id(self.id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.877)
            self.driver.wait_id(self.id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(self.id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        except:
            self.driver.find_id(self.id + 'guanzhu').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.877)
            self.driver.wait_id(self.id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(self.id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(self.id + 'guanzhu').click()
        time.sleep(2)

    # 评论消息-进入作品详情
    def Person_Comment_video_detail(self):
        self.driver.find_id(self.id + 'content').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 评论消息-回复评论
    def Person_Comment_Reply(self):
        self.driver.find_id(self.id + 'reply_btn').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('哈哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_toast('//android.widget.Toast')
        try:
            self.driver.find_id(self.id + 'editContent')
            self.driver.back()
        except:
            pass

    # 评论消息-帖子消息
    def Person_Comment_Post_Notices(self):
        self.driver.find_id(self.id + 'tab2').click()
        self.driver.wait_id(self.id + 'content')
        time.sleep(2)
        self.driver.find_id(self.id + 'content').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check == toast, '帖子跳转失败'
        except:
            self.driver.wait_id(self.id + 'editContent')
            time.sleep(2)
            self.driver.find_id(self.id + 'editContent').send_keys('hhh')
            time.sleep(2)
            self.driver.find_id(self.id + 'btn_send').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '帖子发布评论失败'
            except:
                pass
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    # 聊天消息
    def Person_Chat_Notices(self):
        try:
            self.driver.find_id(self.id + 'chat_count')
            self.driver.find_id(self.id + 'chat').click()
            self.driver.wait_id(self.id + 'right_icon1')
            time.sleep(2)
            while True:
                try:
                    self.driver.find_id(self.id + 'txtCount')
                    self.driver.find_id(self.id + 'txtCount').click()
                    self.driver.wait_id(self.id + 'editContent')
                    time.sleep(2)
                    self.driver.find_id(self.id + 'btnBack').click()
                    time.sleep(2)
                except:
                    break
                time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'chat_count')
                print('私信消息红点未消失')
            except:
                pass
        except:
            pass
        self.driver.find_id(self.id + 'chat').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(2)

    # 聊天列表界面用户
    def Person_chat_user_list(self):
        try:
            self.driver.find_id(self.id + 'userhead')
            count = self.driver.find_ids(self.id + 'userhead')
            for i in range(len(count)):
                self.driver.find_ids(self.id + 'userhead')[i].click()
                self.driver.wait_id(self.id + 'editContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 用户聊天
    def Person_User_Chat(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys('1247792')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_xpath('逍遥剑仙')
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_xpath('逍遥剑仙').click()
        time.sleep(2)

        # 清除聊天记录
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送文字
        self.driver.find_id(self.id + 'editContent').send_keys('功能测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'content')
        time.sleep(2)
        try:
            self.driver.find_xpath('功能测试')
        except:
            print('聊天内容区域未找到发送的文案')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送表情
        self.driver.find_id(self.id + 'btn_send_smile').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'emojicon_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'content')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'content')
        except:
            print('聊天内容区域未找到发送的表情')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送语音
        self.driver.find_id(self.id + 'btn_change_input_mode').click()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'btn_record_voice')
        self.driver.Long_Touche(el, 3000)
        self.driver.wait_id(self.id + 'btn_play_sound_content_layout')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_play_sound_content_layout').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送图片
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'cb_select_tag').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next_step_tv').click()
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 拍照发送私信信息
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'camera').click()
        time.sleep(4)
        try:
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(3)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                self.driver.find_id('com.huawei.camera:id/shutter_button')
                self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                time.sleep(3)
                self.driver.find_id('com.huawei.camera:id/done_button').click()
            except:
                pass
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送作品
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film').click()
        time.sleep(4)
        self.driver.find_id('filmBg').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'btnSelect').click()
        self.driver.wait_id(self.id + 'chat_film_title')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送红包
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'redpacket').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'cash_num').send_keys('0.1')
        time.sleep(3)
        self.driver.find_id(self.id + 'generate_red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'red_packet')
        time.sleep(2)
        self.driver.find_id(self.id + 'red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'open_red_packet_btn').click()
        self.driver.wait_id(self.id + 'diamond')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        # 发送社团邀请
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'union_inviter').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'userName').click()
        self.driver.wait_id(self.id + 'union_inviter_apply')
        time.sleep(2)
        self.driver.find_id(self.id + 'union_inviter_apply').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

    # 私信聊天界面举报用户-其它原因
    def Person_Chat_Report(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.619)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.689)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('功能测试，可忽略此举报信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '举报成功'
            assert check == toast, '私信聊天用户举报toast校验不一致'
        except:
            print('未检测到举报成功toast')
        time.sleep(2)

    # 私信聊天界面-进入对方空间
    def Person_Chat_User_Zoom(self):
        try:
            self.driver.find_id(self.id + 'txtKeyword')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.859)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.877)
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 私信列表界面长按删除
    def Person_Chat_list_delete(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        el = self.driver.find_xpath('逍遥剑仙')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'delete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('撸串')
            print('列表中长按用户删除失败')
        except:
            pass
        time.sleep(2)

    # 私信消息-未关注
    def Person_Chat_Not_follow(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'userhead').click()
            time.sleep(3)
            try:
                self.driver.find_id(self.id + 'tishi')
            except:
                print('私信未关注界面，私信详情界面未显示谨防诈骗信息')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            el = self.driver.find_id(self.id + 'userhead')
            self.driver.Long_Touche(el, 3000)
            time.sleep(2)
            self.driver.find_id(self.id + 'delete').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 草稿箱-会员同步
    def Person_Vip_Draft_synchronous(self):
        self.driver.find_id(self.id + 'draft').click()
        time.sleep(2)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.wait_load('同步')
        time.sleep(2)

    # 草稿箱作品断网后删除再重新同步下载
    def Person_Draft_reload(self):
        date_before = self.driver.find_id(self.id + 'date').text
        self.driver.Disconnect_network()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'date')
        self.driver.Long_Touche(el, 3000)
        if self.y == 1920:
            self.driver.tap(self.x * 0.656, self.y * 0.552)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.657, self.y * 0.546)
        else:
            pass
        time.sleep(2)
        self.driver.Only_wifi()
        time.sleep(15)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        self.driver.wait_xpath('同步')
        date_after = self.driver.find_id(self.id + 'date').text
        assert date_before == date_after, '草稿箱断网情况删除以后联网再同步，作品时间校验不一致'
        time.sleep(2)

    # 草稿箱-草稿箱作品视频预览
    def Person_Draft_Video_Preview(self):
        self.driver.find_id(self.id + 'imgSource').click()
        time.sleep(10)
        try:
            self.driver.find_id(self.id + 'imgSource')
            self.driver.find_id(self.id + 'imgSource').click()
        except:
            pass
        self.driver.wait_download(self.id + 'video_play_btn')
        time.sleep(2)
        self.driver.back()
        time.sleep(3)

    # 草稿箱作品时间重复性检查
    def Person_Draft_Repeat(self):
        date = self.driver.find_ids(self.id + 'date')
        lists = []
        for i in range(len(date)):
            times = self.driver.find_ids(self.id + 'date')[i].text
            lists.append(times)
            time.sleep(1)
        set_list = set(lists)  # set会生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
        if len(lists) == len(set_list):
            pass
        else:
            Dic = dict(Counter(lists))
            print([key for key, value in Dic.items() if value > 1])  # 展示重复元素
        time.sleep(2)

    # 草稿箱作品重配
    def Person_Draft_Reassignment(self):
        count = self.driver.find_ids(self.id + 'imgSource')
        for i in range(len(count)):
            self.driver.find_ids(self.id + 'upload')[i].click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'reDubbing')
                self.driver.find_id(self.id + 'reDubbing').click()
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        while True:
            try:
                self.driver.find_id(self.id + 'roleall')
                self.driver.find_id(self.id + 'roleall').click()
                break
            except:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        pass
                    break
                except:
                    break
        time.sleep(2)
        self.driver.wait_id(self.id + 'action')
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(self.id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        self.Bcak()

    # 已配素材列表
    def Person_Already_source_list(self):
        self.driver.find_id(self.id + 'source').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)

    # 已配素材列表界面点击配音
    def Person_Already_source_dubbing(self):
        self.driver.find_id(self.id + 'iv_dub').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '素材不存在'
            assert check in toast,'素材配音下载失败'
        except:
            while True:
                try:
                    self.driver.find_id(self.id + 'roleall')
                    self.driver.find_id(self.id + 'roleall').click()
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'btnSubmit')
                        self.driver.find_id(self.id + 'btnSubmit').click()
                        try:
                            self.driver.find_id(self.id + 'roleall')
                            self.driver.find_id(self.id + 'roleall').click()
                            break
                        except:
                            pass
                        break
                    except:
                        break
            time.sleep(2)
            self.driver.wait_id(self.id + 'action')
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)

    # 已配素材列表界面删除已配素材
    def Person_Alread_Source_delete(self):
        source = self.driver.find_id(self.id + 'iv_source')
        self.driver.Long_Touche(source, 3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除成功'
            assert check in toast, '已配素材长按删除toast提示检验不一致'
            time.sleep(2)
        except:
            print('未检测到素材删除toast提示')
        time.sleep(2)

    # 断网环境下删除已配素材，联网后再刷新
    def Person_Alread_Source_delete_network(self):
        delete_before = self.driver.find_id(self.id + 'tv_source_title').text
        self.driver.Disconnect_network()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'tv_source_title')
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            pass
        self.driver.Only_wifi()
        time.sleep(10)
        self.driver.swip_down()
        time.sleep(2)
        Refresh_after = self.driver.find_id(self.id + 'tv_source_title').text
        assert delete_before == Refresh_after, '断网情况下删除已配素材再联网刷新列表，未显示之前删除的素材'
        time.sleep(2)

    # 已配素材批量删除
    def Person_Alread_Source_Bulk_deletion(self):
        self.driver.find_id(self.id + 'delete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'choice').click()
        time.sleep(2)
        delete = self.driver.find_id(self.id + 'tv_source_title').text
        time.sleep(2)
        self.driver.find_id(self.id + 'toDelete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_toast('//android.widget.Toast')
        delete_after = self.driver.find_id(self.id + 'tv_source_title').text
        assert delete != delete_after, '批量删除未成功删除'
        time.sleep(2)
        self.driver.find_id(self.id + 'cancel').click()
        time.sleep(2)
        self.Bcak()

    # 素材收藏
    def Person_Source_collection(self):
        self.driver.find_id(self.id + 'collect').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('您还没有收藏任何素材哦~')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btn_more').click()
            self.driver.wait_id(self.id + 'iv_source')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            count = self.driver.find_ids(self.id + 'iv_source')
            for i in range(len(count)):
                self.driver.find_ids(self.id + 'iv_source')[i].click()
                self.driver.wait_id(self.id + 'btn_video_detail_follow')
                self.driver.Background()
                time.sleep(2)
                self.driver.find_id(self.id + 'shouchang_tv_fake').click()
                self.driver.wait_toast('//android.widget.Toast')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            time.sleep(2)
            self.driver.find_id(self.id + 'ivMineTab').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'collect').click()
            self.driver.wait_id(self.id + 'iv_source')
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 素材预览界面取消收藏后刷新收藏列表
    def Person_Source_collection_refresh(self):
        self.driver.find_id(self.id + 'iv_source').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '素材不存在'
            assert check in toast, '进入素材详情失败'
        except:
            self.driver.wait_id(self.id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            cancel_before = self.driver.find_id(self.id + 'source_title').text
            self.driver.find_id(self.id + 'shouchang_tv_fake').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '取消收藏成功'
                assert check in toast, '素材取消收藏失败'
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                print("未检测到取消收藏的toast提示")
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'source_title')
                cancel_after = self.driver.find_id(self.id + 'source_title').text
                assert cancel_before != cancel_after, '素材取消收藏，收藏列表刷新依然显示有该素材'
                time.sleep(2)
            except:
                pass
            time.sleep(2)

    # 自制素材列表
    def Person_Self_control_source(self):
        self.driver.find_id(self.id + 'upload_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'middle').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'titlebar')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            print('未加载出素材收录标准文案')
        time.sleep(2)

    # 上传自制素材
    def Person_Self_Control_Video_Select(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_upload').click()
        time.sleep(2)
        self.driver.find_ids('android:id/title')[1].click()
        self.driver.wait_id(self.id + 'next')
        time.sleep(2)

    # 视频剪辑
    def Person_Self_Control_Video_Clip(self):
        self.driver.find_id(self.id + 'play_button').click()
        time.sleep(5)
        self.driver.Background()
        time.sleep(2)
        self.driver.wait_id(self.id + 'play_button')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'cant_clip_tip')
        except:
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.124, self.y * 0.385, self.x * 0.688, self.y * 0.385)
            elif self.y >= 2280:
                self.driver.swip_move(self.x * 0.903, self.y * 0.472, self.x * 0.5, self.y * 0.472)
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        self.driver.wait_id(self.id + 'et_content')
        time.sleep(2)

        # 素材添加角色名称
        self.driver.find_id(self.id + 'et_content').send_keys('角色1')
        time.sleep(2)
        self.driver.find_id(self.id + 'rl_role2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'add_role_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_content2').send_keys('角色2')
        self.driver.find_id(self.id + 'rl_role3').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)

        # 添加字幕
        self.driver.find_id(self.id + 'tv_add_zimu').click()
        self.driver.wait_id(self.id + 'et')
        time.sleep(2)
        self.driver.find_id(self.id + 'close_zimu').click()
        time.sleep(2)
        roles = ['tv_role1', 'tv_role2']
        words = ['角色1的台词', '角色2的台词']
        for i in range(len(roles)):
            self.driver.find_id(self.id + 'tv_add_zimu').click()
            self.driver.wait_id(self.id + 'et')
            time.sleep(2)
            self.driver.find_id(self.id + roles[i]).click()
            self.driver.find_id(self.id + 'et').send_keys(words[i])
            time.sleep(2)
            self.driver.find_id(self.id + 'complete_zimu').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'rl_bottom').click()
            time.sleep(2)
        content = ['tv_content2', 'tv_content2']
        for i in range(len(content)):
            try:
                self.driver.find_id(self.id + content[i])
            except:
                print('字幕显示错误')
        time.sleep(2)

        # 编辑字幕
        self.driver.find_id(self.id + 'linear_view2').click()
        time.sleep(2)
        # 无效
        # left_el = self.driver.find_id(self.id + 'left_view_bottom')
        # right_el = self.driver.find_id(self.id + 'right_view_bottom')
        # el = right_el.rect
        # el_x = int(el['x'] + el['width'] / 2.0)
        # el_y = int(el['y'] + el['height'] / 2.0)
        # self.driver.Long_press_move(left_el,el_x,el_y)
        # time.sleep(2)
        self.driver.find_id(self.id + 'tv_delete_zimu').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

        # 裁剪视频预览
        self.driver.find_id(self.id + 'play_button').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'stop_button')
            #视频无法正常播放
        except:
            self.driver.wait_id(self.id + 'play_button')
        time.sleep(2)

        # 存草稿
        self.driver.find_id(self.id + 'save').click()
        time.sleep(2)

        # 退出素材制作再进
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_upload').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

        # 进入上传素材界面
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)

        # 素材上传封面中添加文字
        self.driver.find_id(self.id + 'add_text').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('素材封面图')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        time.sleep(2)

        # 素材封面更换
        self.driver.find_xpath('更换封面').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)

        # 素材名称
        self.driver.find_id(self.id + 'et_title').send_keys('素材上传测试')
        time.sleep(2)

        # 添加素材音乐
        self.driver.find_id(self.id + 'addMusic').click()
        self.driver.wait_id(self.id + 'title')
        time.sleep(2)
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'local_music').click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'local_video_music').click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnDownload').click()
        self.driver.wait_id(self.id + 'tv_use')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_use').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

        # 添加素材标签
        self.driver.find_id(self.id + 'tv1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit_text').send_keys('测试')
        self.driver.find_id(self.id + 'btn_search').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)

        # 上传素材
        self.driver.find_id(self.id + 'next').click()
        while True:
            try:
                self.driver.find_id(self.id + 'iv_dub')
                break
            except:
                self.driver.find_id(self.id + 'linear_biaoqian').click()
            time.sleep(10)
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'video_play_btn')
        except:
            print('新上传的素材未显示播放按钮，素材播放有问题')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    #素材信息编辑/删除
    def Person_Self_Control_Source_delete(self):
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)

        #素材信息编辑
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.789)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(4)
        self.driver.find_id(self.id + 'et_title').send_keys('素材信息修改测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        while True:
            try:
                self.driver.find_id(self.id + 'iv_dub')
                break
            except:
                self.driver.find_id(self.id + 'music_text').click()
            time.sleep(10)
        time.sleep(2)

        #素材删除
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.868)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(4)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(4)

    # 个人中心-我的财富
    def Person_My_Wealth(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'money').click()
        self.driver.wait_id(self.id + 'diamond_count_tv')
        time.sleep(2)

        # 个人中心-我的账单
        self.driver.find_id(self.id + 'toBill').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        # ids = self.driver.search_id()
        # print(ids)
        # list = re.findall('content-desc="(.*?)"', ids)
        # print(list)
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        # 点击购买钻石
        for i in range(6):
            # price = self.driver.find_ids(self.id + 'price_tv')[i].text
            time.sleep(1)
            self.driver.find_ids(self.id + 'price_tv')[i].click()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_pay').click()
            self.driver.wait_id('android:id/text1')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dm3').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'close_icon').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    # 个人中心-我的收益
    def Person_My_earnings(self):
        self.driver.find_id(self.id + 'gold').click()
        self.driver.wait_id(self.id + 'gold_count')
        time.sleep(2)

        # 常见问题
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        # ids = self.driver.search_id()
        # print(ids)
        # list = re.findall('content-desc="(.*?)"', ids)
        # print(list)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 绑定支付宝
        self.driver.find_id(self.id + 'right').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.868)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(4)
        self.driver.find_id(self.id + 'send_code').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast, '验证码发送失败'
        except:
            print('未检测到验证码发送toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'userhead').click()
            self.driver.wait_id(self.id + 'll_fan')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 我的成就
    def Person_My_achievements(self):
        self.driver.find_id(self.id + 'achievement').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 邀请好友
    def Person_Invite_friend(self):
        self.driver.find_id(self.id + 'addfriend').click()
        time.sleep(2)

        # 规则
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        # 邀请好友
        self.driver.find_id(self.id + 'tv_invite').click()
        time.sleep(2)

        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        time.sleep(2)
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)

        # QQ空间
        self.driver.find_id(self.id + 'tv_invite').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.712)
        self.driver.wait_xpath('发表')
        time.sleep(2)
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)

        # 点击复制链接（QQ取消分享返回应用，分享弹窗还会显示）
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.833)
        try:
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in tip,'邀请好友链接复制失败'
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        #好友召回
        self.driver.find_id(self.id + 'tv_recall').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
            self.driver.find_id(self.id + 're_update').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.12, self.y * 0.83)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.126, self.y * 0.833)
            try:
                tip = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in tip, '召回好友链接复制失败'
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 积分商城
    def Person_Points_Mall(self):
        self.driver.find_id(self.id + 'exchange').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 夜间模式
    def Person_Mode_switch(self):
        self.driver.find_id(self.id + 'tvChange').click()
        time.sleep(5)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'tvChange').click()
        time.sleep(5)

class Video_detail:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    def Btnback(self):
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 首页点击作品封面进入视频详情
    def Into_video(self):
        self.driver.find_id(self.id + 'film_img2').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)

    # 点击用户头像进入个人空间
    def Head_into_zoom_back(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.Btnback()

    # 视频详情点击关注
    def Video_follow(self):
        self.driver.find_id(self.id + 'follow_ta').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.find_id(self.id + 'right_icon1')
                time.sleep(2)
                self.Btnback()
            except:
                pass
        time.sleep(2)

    # 视频-弹幕开关
    def Video_danmu(self):
        try:
            self.driver.find_id(self.id + 'play').click()
        except:
            pass
        self.driver.find_id(self.id + 'media_danmu_img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(20)
        self.driver.Background()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)

    # 全屏播放
    def Video_fullscreen(self):
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_fullscreen_open').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)


    # 点赞
    def Video_good(self):
        num = self.driver.find_id(self.id + 'tv_good').text
        try:
            self.driver.find_id(self.id + 'good_svga').click()
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '恭喜你获得300金币'
            assert tip == check
        except:
            self.driver.find_id(self.id + 'tv_good').click()
        num1 = self.driver.find_id(self.id + 'tv_good').text
        try:
            assert num != num1
        except Exception as e:
            print(e)
        time.sleep(2)

    # 曝光界面功能按钮点击
    def Video_exposure_touch(self):
        tv_title = self.driver.find_id(self.id + 'tv_video_detail_title').text
        self.driver.find_id(self.id + 'tv_exposure').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        tv_title1 = self.driver.find_id(self.id + 'tv_source_title').text
        try:
            assert tv_title1 == tv_title
        except Exception as e:
            print(e)
        time.sleep(2)

        #曝光券
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(1)
        self.driver.find_id(self.id + 'tab1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        self.Btnback()
        time.sleep(2)
        self.Btnback()
        time.sleep(2)

        #评论推荐人简介预览
        self.driver.find_id(self.id + 'tv_preview').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)

        #充值界面跳转
        self.driver.find_id(self.id + 'img_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'price_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

        #曝光价格列表
        prices = self.driver.find_ids(self.id + 'rl')
        for i in range(len(prices) - 1):
            self.driver.find_ids(self.id + 'rl')[i].click()
        time.sleep(2)

        #曝光服务协议
        self.driver.find_id(self.id + 'tv_xieyi').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        #作品曝光要求
        self.driver.find_id(self.id + 'tv_yaoqiu').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        #自定义钻石价格
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('20000')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        self.Btnback()

    # 金币曝光
    def Video_exposure_gold(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'rl').click()
        golds = self.driver.find_id(self.id + 'tv_gold').text
        if int(golds) >= 5000:
            self.driver.find_id(self.id + 'gold_count').click()
        else:
            self.driver.find_id(self.id + 'gold_count').click()
            gold_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '金币余额不足'
            assert check == gold_toast
        self.driver.wait_id(self.id + 'btnBack')
        self.Btnback()

    # 会员曝光
    def Video_exposure_freevip(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        count = self.driver.find_id(self.id + 'free_count').text
        if count == '当前剩余0次':
            self.driver.find_id(self.id + 'free_count').click()
            exp_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '曝光机会用完'
            assert check in exp_toast
        self.driver.find_id(self.id + 'free_count').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('会员中心')
            self.Btnback()  # 返回曝光界面
        except:
            pass
        self.Btnback()#返回视频详情

    # 自定义钻石曝光
    def Video_exposure_diamond(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('20000')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'free_count').click()
        time.sleep(2)
        self.driver.find_xpath('确定').click()
        time.sleep(2)
        self.driver.wait_xpath('钻石余额不足')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'price_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.Btnback()


    # 视频评论
    def Video_comments(self):
        while True:
            try:
                self.driver.find_id(self.id + 'comment_count')
                break
            except:
                self.driver.swip_up()
                self.driver.Background()
            time.sleep(2)

    # 发送评论
    def Video_comment_send(self):
        self.driver.find_id(self.id + 'comment_count').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('暖一个！')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'item_comment_video_more')
        except:
            self.driver.find_id(self.id + 'tv_comment').click()
        self.driver.wait_id(self.id + 'item_comment_video_more')
        time.sleep(2)
        self.driver.find_id(self.id + 'shunxu').click()
        time.sleep(2)

    # 评论举报
    def Video_comment_report(self):
        self.driver.find_ids(self.id + 'item_comment_video_more')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_one').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        check_toast = '举报'
        assert check_toast in toast,toast
        time.sleep(2)
        self.driver.find_id(self.id + 'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('举报功能测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        toast1 = self.driver.wait_toast('//android.widget.Toast')
        assert check_toast in toast1
        time.sleep(2)

    # 评论列表上滑加载
    def Video_comments_load(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'follow_ta').click()
        time.sleep(2)

    # 点击合作配音
    def Video_Coor_dubbing(self):
        while True:
            try:
                self.driver.find_xpath('配音/合作')
                break
            except:
                self.Btnback()
                self.driver.swip_down()
                time.sleep(2)
                self.driver.find_id(self.id + 'film_img2').click()
                self.driver.Background()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('配音/合作').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'coor')
            self.driver.find_id(self.id + 'coor').click()
            while True:
                try:
                    #素材下载失败/素材已被删除
                    self.driver.wait_toast('//android.widget.Toast')
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'action')
                        break
                    except:
                        #限制素材进入配音界面显示限制弹窗
                        try:
                            self.driver.find_id(self.id + 'btnSubmit')
                            self.driver.find_id(self.id + 'btnSubmit').click()
                            break
                        except:
                            pass
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(3)
        except:
            print('未显示合作按钮')
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 视频详情界面进入素材预览界面
    def Video_source(self):
        self.driver.find_id(self.id + 'tvSource').click()
        self.driver.wait_id(self.id + 'source_title')
        self.driver.Background()
        time.sleep(2)
        self.Btnback()

    # 作品分享
    def Video_share(self):
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)

        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)

        # QQ空间
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)

        # 点击新浪
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.682, self.y * 0.712)
        self.driver.wait_xpath('发送')
        time.sleep(2)
        self.driver.find_id('com.sina.weibo:id/titleBack').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('不保存')
            self.driver.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        # 点击私信
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.846)
        self.driver.wait_id(self.id + 'filter_edit')
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys("15697802")
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.wait_id(self.id + 'userhead')
            name = self.driver.find_id(self.id + 'name').text
            name2 = '米爱'
            if name == name2:
                self.driver.find_id(self.id + 'name').click()
                self.driver.wait_id(self.id + 'right_icon1')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            else:
                print("未搜索到指定用户")
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 点击下载视频到本地
        self.driver.find_id(self.id + 'tv_share').click()
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.807)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.311, self.y * 0.846)
        # 先判断点击是否为下载按钮，若是复制按钮则会toast提示，不是复制按钮则判断是否有非会员弹窗，不是则直接等待作品下载完成
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '存在'
            if check in toast:
                print(toast)
        except:
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                try:
                    self.driver.wait_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                except:
                    pass

        # 点击复制链接
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.846)
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.find_id(self.id + 'tv_action_one')
                self.driver.find_id(self.id + 'tv_action_one').click()
                self.driver.wait_id(self.id + 'txtContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                pass
        time.sleep(2)

        # 点击转发
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.88, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.87, self.y * 0.846)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'reprint')
            self.driver.find_id(self.id + 'content').send_keys("不错，转发了！")
            time.sleep(2)
            self.driver.find_id(self.id + 'reprint').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                try:
                    self.driver.find_id(self.id + 'reprint')
                    self.driver.find_id(self.id + 'reprint').click()
                    self.driver.wait_toast('//android.widget.Toast')
                except Exception as e:
                    print(e)
        except:
            # 点击取消分享弹窗按钮
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.937)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.947)
        time.sleep(2)

    # 切换视频
    def Video_switch(self):
        for i in range(10):
            self.driver.swip_up()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.swip_left()
            self.driver.wait_id(self.id + 'll_fan')
            self.Btnback()
        self.Btnback()

    #热门作品标签
    def Video_Hot_work(self):
        while True:
            title = self.driver.find_id(self.id + 'tv_video_detail_title').text
            hot_tv = 'ch'
            if hot_tv in title:
                self.driver.find_xpath('ch')
                try:
                    self.driver.find_id(self.id + 'txtTitle')
                    self.driver.find_id(self.id + 'btnBack').click()
                    time.sleep(2)
                except:
                    try:
                        self.driver.find_id(self.id + 'close')
                        self.driver.find_id(self.id + 'close').click()
                        break
                    except:
                        pass
            self.driver.swip_up()
            time.sleep(2)

class Circle:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id
    #进入圈子界面
    def Circle_into(self):
        self.driver.find_id(self.id + 'ivNewsTab').click()
        time.sleep(2)

    #帖子浏览历史
    def Circle_post_history(self):
        self.driver.find_id(self.id + 'history').click()
        time.sleep(2)

    #进入帖子详情
    def Circle_post_detail(self):
        try:
            self.driver.find_id(self.id + 'title').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.wait_id(self.id + 'userhead')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        except Exception as e:
            print(e)

    #历史记录帖子删除
    def Circle_post_history_delete(self):
        delete_before = self.driver.find_id(self.id + 'title').text
        el = self.driver.find_id(self.id + 'title')
        self.driver.Long_Touche(el, 3000)
        time.sleep(1)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_xpath(delete_before)
            print('帖子长按删除失败')
        except:
            pass
        time.sleep(2)

    #清空帖子浏览记录
    def Circle_history_clear(self):
        try:
            self.driver.find_id(self.id + 'empty_text')
        except:
            self.driver.find_id(self.id + 'tv_right').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
                try:
                    self.driver.find_id(self.id + 'title')
                    print('帖子清空失败')
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 圈子主界面帖子转发
    def Circle_Post_forward(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.802)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        self.driver.wait_id(self.id + 'group_chat')
        self.driver.find_id(self.id + 'group_chat').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'name')
        self.driver.find_id(self.id + 'name').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子列表界面点击圈子标签
    def Circle_tag(self):
        tag_name = self.driver.find_id(self.id + 'tag').text
        self.driver.find_id(self.id + 'tag').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        tag_detail_name = self.driver.find_id(self.id + 'topic_name').text
        assert tag_detail_name == tag_name
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #圈子热门帖子列表界面点击评论按钮进入帖子详情
    def Circle_comment_detail(self):
        self.driver.find_id(self.id + 'comment').click()
        self.driver.wait_id(self.id + 'guanzhu')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子热门帖子列表界面点赞
    def Circle_good(self):
        self.driver.swip_up()
        time.sleep(1)
        touche_good_before = self.driver.find_id(self.id + 'good').text
        self.driver.find_id(self.id + 'good').click()
        time.sleep(2)
        touche_good_later = self.driver.find_id(self.id + 'good').text
        if int(touche_good_later) > int(touche_good_before):
            pass
        else:
            print('点赞数量未变化',touche_good_before,touche_good_later)
        time.sleep(2)

    # 点击帖子内容进入帖子详情
    def Circle_content(self):
        self.driver.find_id(self.id + 'content').click()
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子热门列表刷新
    def Circle_refresh(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(1)
        #一键返回列表顶部
        self.driver.find_id(self.id + 'ivNewsTab').click()
        self.driver.wait_id(self.id + 'tv_key_word_help')
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)

    #圈子搜索界面显示
    def Circle_search(self):
        i = 0
        while True:
            self.driver.find_id(self.id + 'tv_key_word_help').click()
            try:
                self.driver.wait_id(self.id + 'tv')
                break
            except:
                #界面显示失败时返回上一界面再进
                self.driver.find_id(self.id + 'btnBack').click()
            #尝试10次后停止以上操作
            if i == 10:
                break
            else:
                pass
            time.sleep(2)

    #帖子搜索界面热门话题点击跳转
    def Circle_hot_tv_jump(self):
        tvs = self.driver.find_ids(self.id + 'tv')
        for i in range(len(tvs)):
            tv_name = self.driver.find_ids(self.id + 'tv')[i].text
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
            assert tv_detail_name in tv_name, '标签名称校验不一致'
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)

    #已订阅的话题
    def Circle_topic_Subscribes(self):
        try:
            self.driver.find_id(self.id + 'title')
            name = self.driver.find_id(self.id + 'title').text
            self.driver.find_id(self.id + 'title').click()
            self.driver.wait_id(self.id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
            assert tv_detail_name in name, '标签名称校验不一致'
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
        except:
            pass

    #话题搜索
    def Circle_topic_search(self):
        self.driver.find_id(self.id + 'et_key_word').clear()
        time.sleep(1)
        self.driver.find_id(self.id + 'et_key_word').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'title')
        self.driver.find_id(self.id + 'title').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        check = '测试'
        tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
        assert check in tv_detail_name, '标签名称校验不一致'
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子主界面发帖-图文贴
    def Circle_Home_word_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'image_tie').click()
        time.sleep(4)

    #图文贴内容
    def Circle_word_topic_content(self):
        topic_read = file.read()
        self.driver.find_id(self.id + 'content').send_keys(topic_read,'\n')
        time.sleep(2)
        self.driver.find_id(self.id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys(topic_read,'\n')
        time.sleep(2)

    #添加图片
    def Circle_word_topic_add_image(self):
        self.driver.find_id(self.id + 'add_img').click()
        time.sleep(2)

    #选择图片
    def Circle_word_topic_select_image(self):
        self.driver.find_id(self.id + 'tv_photo').click()
        self.driver.wait_id(self.id + 'imgQueue')
        num = self.driver.find_ids(self.id + 'cb_select_tag')
        for i in range(len(num)):
            self.driver.find_ids(self.id + 'cb_select_tag')[i].click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
                break
            except:
                pass
            time.sleep(1)
        self.driver.find_id(self.id + 'next_step_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'del').click()
        time.sleep(2)

    # 拍照
    def Circle_word_topic_photo(self):
        self.driver.find_id(self.id + 'tv_take_photo').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
        except:
            pass
        time.sleep(2)
        try:
            self.driver.wait_sys('始终允许')
        except:
            pass
        time.sleep(5)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id('com.oppo.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.oppo.camera:id/done_button').click()
            self.driver.wait_id(self.id + 'right_icon1')
        except:
            try:
                self.driver.find_id('com.huawei.camera:id/shutter_button')
                self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.huawei.camera:id/done_button').click()
            except:
                self.driver.back()
        time.sleep(2)

    #添加话题
    def Circle_word_topic_insert_topic(self):
        self.driver.find_id(self.id + 'add_topic').click()
        self.driver.wait_id(self.id + 'tv')
        self.driver.find_id(self.id + 'et_key_word').send_keys('一个人的话题')
        time.sleep(1)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'title')
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)

    #添加好友
    def Circle_word_topic_at(self):
        self.driver.find_id(self.id + 'at').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys('16461675')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'no_data_msg')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #发布图文帖
    def Circle_word_topic_release(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            self.driver.wait_id(self.id + 'img_subscribe')
            self.driver.swip_down()
            time.sleep(2)
            self.driver.find_id(self.id + 'content').click()
            self.driver.wait_id(self.id + 'editContent')
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            print('帖子发布失败')
        time.sleep(2)

    #删除图文帖
    def Circle_word_topic_delete(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.885)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.87)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        assert del_toast == check
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #发布语音帖
    def Circle_Home_Voice_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'voice_tie').click()
        time.sleep(2)


    #录制语音
    def Circle_voice_topic_record(self):
        self.driver.find_id(self.id + 'dubbing').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #试听
        self.driver.find_id(self.id + 'review').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #重录
        self.driver.find_id(self.id + 'reDo').click()
        time.sleep(2)
        date_check = '00:00'
        el = self.driver.find_id(self.id + 'time').text
        if el != date_check:
            print('点击重录按钮音轨没有恢复默认状态')
        time.sleep(2)
        self.driver.find_id(self.id + 'dubbing').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(4)

    #语音帖发布界面
    def Circle_voice_topic_next(self):
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('有什么好说的呢？么有哦~')
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'change_cover').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        self.driver.wait_id(self.id + 'photo_wall_item_photo')
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)


    #圈子主页发布听评帖
    def Circle_Home_listen_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film_tie').click()
        time.sleep(2)

    #听评帖添加作品
    def Circle_listen_insert_work(self):
        self.driver.find_id(self.id + 'add_img').click()
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id(self.id + 'myLike').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'playbtn')
        self.driver.find_id(self.id + 'btnSelect').click()
        time.sleep(2)

class Society:
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #点击进入社团主界面
    def Society_Home(self):
        self.driver.find_id(self.id + 'society').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)

    #我的社团-检查是否拥有社团
    def Society_My_society(self):
        self.driver.find_id(self.id + 'ivMineTab').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        num = self.driver.find_id(self.id + 'societyCount').text
        check = '0'
        if num == check:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'ivNewsTab').click()
            time.sleep(2)
        else:
            self.driver.find_id(self.id + 'll_society').click()
            time.sleep(2)
            self.driver.wait_id(self.id + 'status_icon')
            societys = self.driver.find_ids(self.id + 'userName')
            list_society = []
            for i in range(len(societys)):
                title = self.driver.find_ids(self.id + 'userName')[i].text
                list_society.append(title)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'ivNewsTab').click()
            time.sleep(2)
            print(list_society)
    #
    # '''我的社团点击查看'''
    # def test_b_a(self):
    #     state = Test_Society().test_b()
    #     if state == False:
    #         pass
    #     else:
    #         try:
    #             self.driver.find_id(self.id + 'more_img')
    #             self.driver.find_id(self.id + 'more_img').click()
    #         except:
    #             pass
    #         time.sleep(2)
    #         for item in state:
    #             self.driver.find_xpath(item).click()
    #             self.driver.wait_id(self.id + 'btn_change_input_mode')
    #             self.driver.find_id(self.id + 'btnBack').click()
    #             time.sleep(2)

    '''我的社团聊天-文字'''
    def Society_Group_chat(self):
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        select = random.choice('社团聊天文字测试')
        self.driver.find_id(self.id + 'editContent').send_keys(select)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            self.driver.wait_id(self.id + 'content')
            check = self.driver.find_ids(self.id + 'content')[-1].text
            assert select == check,'发送文字校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #我的社团聊天-语音
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_id(self.id + 'btn_change_input_mode').click()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'btn_record_voice')
        #发送60s语音
        self.driver.Long_Touche(el, 60000)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            self.driver.wait_id(self.id + 'btn_play_sound_content_layout')
            self.driver.find_ids(self.id + 'btn_play_sound_content_layout')[-1].click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                pass
        time.sleep(2)
        #录制语音过程中上滑取消
        self.driver.Long_press_move(el, self.x * 0.5, self.y * 0.5)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #我的社团聊天-发送表情
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_id(self.id + 'btn_send_smile').click()
        time.sleep(2)
        emoji = self.driver.find_ids(self.id + 'emojicon_icon')
        for i in range(len(emoji)):
            self.driver.find_ids(self.id + 'emojicon_icon')[i].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'content')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #我的社团聊天-其它按钮
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'cb_select_tag').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next_step_tv').click()
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)

        # 拍照发送私信信息
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'camera').click()
        time.sleep(4)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id('com.oppo.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.oppo.camera:id/done_button').click()
        except:
            try:
                self.driver.find_id('com.android.camera:id/shutter_button').click()
                time.sleep(3)
                self.driver.find_id('com.android.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)

        # 发送作品
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film').click()
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id(self.id + 'myLike').click()
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id('filmBg').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'btnSelect').click()
        self.driver.wait_id(self.id + 'chat_film_title')
        time.sleep(2)

        # 发送红包
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'redpacket').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'cash_num').send_keys('0.1')
        time.sleep(2)
        self.driver.find_id(self.id + 'people_num').send_keys('1')
        time.sleep(3)
        self.driver.find_id(self.id + 'generate_red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'red_packet')
        time.sleep(2)
        self.driver.find_id(self.id + 'red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'open_red_packet_btn').click()
        self.driver.wait_id(self.id + 'diamond')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的社团-活动-每日活动
    def Society_Activity_day(self):
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_xpath('活动').click()
        time.sleep(2)
        title = self.driver.find_id(self.id + 'desc').text
        if title == '给社团成员作品点赞2次':
            # 点赞两次
            self.driver.find_id(self.id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'btn_close')
                self.driver.find_id(self.id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('给社团成员作品点赞2次')
            except:
                self.driver.wait_id(self.id + 'filmBg')
                self.driver.find_ids(self.id + 'filmBg')[0].click()
                self.driver.wait_id(self.id + 'tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id(self.id + 'tv_good1').click()
                except:
                    self.driver.find_id(self.id + 'tv_good').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_ids(self.id + 'filmBg')[1].click()
                self.driver.wait_id(self.id + 'tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id(self.id + 'tv_good1').click()
                except:
                    self.driver.find_id(self.id + 'tv_good').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '评论社团成员的作品2次':
            # 社团作品评论两次
            self.driver.find_id(self.id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'btn_close')
                self.driver.find_id(self.id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('评论社团成员的作品2次')
            except:
                self.driver.wait_id(self.id + 'filmBg')
                self.driver.find_ids(self.id + 'filmBg')[0].click()
                self.driver.wait_id(self.id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(self.id + 'tv_comment').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'editContent').send_keys('作品评论')
                time.sleep(2)
                self.driver.find_id(self.id + 'btn_send').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    assert check_toast in toast, '评论发送失败'
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_ids(self.id + 'filmBg')[1].click()
                self.driver.wait_id(self.id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(self.id + 'tv_comment').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'editContent').send_keys('作品评论')
                time.sleep(2)
                self.driver.find_id(self.id + 'btn_send').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    assert check_toast in toast, '评论发送失败'
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '与社团成员完成合作作品':
            # 完成社团合作
            self.driver.find_id(self.id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'btn_close')
                self.driver.find_id(self.id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('与社团成员完成合作作品')
            except:
                self.driver.wait_id(self.id + 'filmBg')
                self.driver.find_xpath('求合作').click()
                self.driver.wait_id(self.id + 'btnCooperate')
                self.driver.find_id(self.id + 'btnCooperate').click()
                while True:
                    try:
                        self.driver.find_id(self.id + 'btnSubmit')
                        self.driver.find_id(self.id + 'btnSubmit').click()
                        break
                    except:
                        try:
                            self.driver.find_id(self.id + 'action')
                            break
                        except:
                            pass
                self.driver.find_id(self.id + 'action').click()
                self.driver.wait_download(self.id + 'title')
                self.driver.Background()
                self.driver.find_id(self.id + 'complete').click()
                self.driver.wait_id(self.id + 'pri_switch_tv')
                self.driver.swip_up()
                self.driver.find_id(self.id + 'check_box_add_square').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'uploadbtn').click()
                self.driver.wait_download(self.id + 'down')
                self.driver.find_id(self.id + 'ivNewsTab').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'society').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'time').click()
                self.driver.wait_id(self.id + 'btn_change_input_mode')
                self.driver.find_xpath('活动').click()
                time.sleep(2)

    #我的社团-活动-历时活动
    def Society_Activity_week(self):
        self.driver.swip_up()
        time.sleep(2)

        # 社团活动查看历时素材
        try:
            self.driver.find_id(self.id + 'film_look')
            self.driver.find_id(self.id + 'film_look').click()
            self.driver.wait_id(self.id + 'userhead')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'playBtn').click()
            self.driver.wait_download(self.id + 'playbtn')
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        # 社团活动社长添加活动素材
        try:
            self.driver.find_id(self.id + 'choice_source')
            self.driver.find_id(self.id + 'choice_source').click()
            self.driver.wait_id(self.id + 'txtKeyword')
            self.driver.find_id(self.id + 'txtKeyword').send_keys('配音')
            self.driver.find_id(self.id + 'btnSearch').click()
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'iv_source').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '创建成功'
            check1 = '配音秀:创建成功'
            if toast != check and toast != check1:
                self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        time.sleep(2)

        # 社团活动素材配音
        self.driver.find_id(self.id + 'dubbing')
        self.driver.find_id(self.id + 'dubbing').click()
        try:
            self.driver.find_id(self.id + 'btn_close')
            self.driver.find_id(self.id + 'btn_close').click()
        except:
            pass
        while True:
            try:
                self.driver.find_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
                try:
                    self.driver.find_id(self.id + 'roleall')
                    self.driver.find_id(self.id + 'roleall').click()
                except:
                    pass
                break
            except:
                try:
                    self.driver.find_id(self.id + 'action')
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        pass
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'pri_switch_tv')
        self.driver.swip_up()
        try:
            self.driver.find_id(self.id + 'check_box_add_square')
            self.driver.find_id(self.id + 'check_box_add_square').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'uploadbtn').click()
        self.driver.wait_download(self.id + 'exposure')
        self.driver.find_id(self.id + 'ivNewsTab').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'society').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'time').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_xpath('活动').click()
        time.sleep(2)


    #我的社团-榜单
    def Society_Rank(self):
        self.driver.find_xpath('榜单').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'username')
            self.driver.find_id(self.id + 'username').click()
            self.driver.wait_id(self.id + 'll_fan')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'look_rank').click()
        self.driver.wait_id(self.id + 'tv_right')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'username1')
            self.driver.find_id(self.id + 'userHead1').click()
            self.driver.wait_id(self.id + 'll_fan')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        ranks = self.driver.find_ids(self.id + 'img_rank')
        for i in range(len(ranks)):
            self.driver.find_ids(self.id + 'img_rank')[i].click()
            self.driver.wait_id(self.id + 'tv_right')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(1)
        time.sleep(2)

    #我的社团-社团空间
    def Society_Space(self):
        self.driver.find_id(self.id + 'btn_space_jump').click()
        self.driver.wait_id(self.id + 'll_fan')
        #社团空间-头像
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_id')
        except:
            print ('社团id信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_nickname')
        except:
            print('社团昵称信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_sign')
        except:
            print ('社团简介信息未显示')
        time.sleep(2)
        #举报
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            Report_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in Report_toast, '举报失败'
        except:
            pass
        time.sleep(2)

        #社团空间-社团财富
        self.driver.find_id(self.id + 'gold_match').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_gold')
            try:
                self.driver.find_id(self.id + 'tv_diamond')
            except:
                print ('社团财富界面未显示余额信息')
        except:
            print ('社团财富界面未显示余额信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #社团空间-聊天
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'editContent')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 设置关注区权限
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.573)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.64)
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print ('动态开关设置后没有toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #特别关注
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.685)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.71)
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print ('特别关注没有toast提示')
        time.sleep(2)

        #消息免打扰
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.729)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.77)
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print('消息免打扰没有toast提示')

        time.sleep(2)

        #添加社团素材
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.802)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_source').click()
        time.sleep(2)
        self.driver.Background()
        self.driver.find_id(self.id + 'btnSelect').click()
        insert_toast = self.driver.wait_toast('//android.widget.Toast')
        if insert_toast == '该素材存在':
            self.driver.find_id(self.id + 'btnCancelSelect').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #管理/退出社团
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.875)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.87)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnCancel').click()
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #社团空间-粉丝
        self.driver.find_id(self.id + 'll_fan').click()
        self.driver.wait_id(self.id + 'status_icon')
        status = self.driver.find_ids(self.id + 'status_icon')
        for i in range(len(status)):
            self.driver.find_ids(self.id + 'status_icon')[i].click()
            time.sleep(1)
        user_name = self.driver.find_ids(self.id + 'username')[-1].text
        self.driver.find_ids(self.id + 'username')[-1].click()
        self.driver.wait_id(self.id + 'll_fan')
        user_name1 = self.driver.find_id(self.id + 'username').text
        self.driver.find_id(self.id + 'btnBack').click()
        assert user_name == user_name1,'粉丝列表用户名与空间用户名校验失败'
        time.sleep(2)
        user_list = self.driver.find_ids(self.id + 'username')
        new_user_list = []
        for i in range(len(user_list)):
            name = self.driver.find_ids(self.id + 'username')[i].text
            new_user_list.append(name)
        time.sleep(1)
        D_user_list = dict(Counter(new_user_list))
        for key,value in D_user_list.items():
            if value > 1:
                print(key,'粉丝列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #社团空间-成员
        self.driver.find_id(self.id + 'll_member').click()
        self.driver.wait_id(self.id + 'manager')
        user_name = self.driver.find_ids(self.id + 'name')[-1].text
        self.driver.find_ids(self.id + 'userhead')[-1].click()
        self.driver.wait_id(self.id + 'll_fan')
        user_name1 = self.driver.find_id(self.id + 'username').text
        self.driver.find_id(self.id + 'btnBack').click()
        assert user_name == user_name1,'成员列表用户名与空间用户名校验失败'
        time.sleep(2)
        user_list = self.driver.find_ids(self.id + 'username')
        new_user_list = []
        for i in range(len(user_list)):
            name = self.driver.find_ids(self.id + 'name')[i].text
            new_user_list.append(name)
        time.sleep(1)
        D_user_list = dict(Counter(new_user_list))
        for key, value in D_user_list.items():
            if value > 1:
                print(key, '成员列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #社团空间-社团作品
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #社团空间-社团素材
        self.driver.find_id(self.id + 'btnMember').click()
        time.sleep(2)
        count = self.driver.find_id(self.id + 'film_all_count').text
        num = re.findall(r'素材(.*)',count)
        new = "".join(num)
        if new != '0':
            time.sleep(2)
            self.driver.find_id(self.id + 'imgSource').click()
            self.driver.wait_id(self.id + 'shouchang_tv_fake')
            self.driver.Background()
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                    except:
                        pass
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        try:
                            self.driver.find_id(self.id + 'action')
                            break
                        except:
                            pass
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)

        #社团空间-合辑
        self.driver.find_id(self.id + 'btnCollect').click()
        time.sleep(2)
        count = self.driver.find_id(self.id + 'film_all_count').text
        num = re.findall(r'合辑(.*)', count)
        new = ''.join(num)
        if new != '0':
            self.driver.find_id(self.id + 'filmBg').click()
            try:
                self.driver.wait_id(self.id + 'userName')
                self.driver.find_id(self.id + 'filmBg').click()
                self.driver.wait_id(self.id + 'tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id(self.id + 'follow_ta')
                    self.driver.find_id(self.id + 'follow_ta').click()
                    try:
                        follow_toast = self.driver.wait_toast('//android.widget.Toast')
                        check = '社团成员不可取消关注'
                        assert check in follow_toast
                    except:
                        pass
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
            except Exception as e:
                print(e)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #社团管理
    def Society_Manager(self):
        self.driver.find_id(self.id + 'tv_key_word_help').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('141095541')
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.796)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5,self.y * 0.89)
        self.driver.wait_id(self.id + 'userHead')
        time.sleep(2)

    #社团管理-编辑资料
    def Society_Edit_info(self):
        self.driver.find_id(self.id + 'edit_profile').click()
        time.sleep(2)
        # 点击头像-拍照
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.793)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            try:
                self.driver.wait_sys('始终允许')
            except:
                try:
                    self.driver.wait_sys('允许')
                except:
                    pass
            self.driver.find_id(self.id + 'userhead').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.793)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(2)
        except:
            pass
        time.sleep(3)
        try:
            '''
            以下操作只适用VIVOx9
            '''
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                '''
                oppo r11
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.oppo.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        time.sleep(6)
        self.driver.find_id(self.id + 'confirm').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            assert toast == check
        except:
            print('拍照更换头像未检测到toast提示')
        time.sleep(2)

        #修改社团名称
        before_name = self.driver.find_id(self.id + 'society_name').text
        time.sleep(2)
        self.driver.find_id(self.id + 'society_name').send_keys('属于我自己的社团哦~')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        try:
            fail_toast = self.driver.wait_toast('//android.widget.Toast')
            fail_check = '社团名称只支持空格、中英文、数字'
            assert fail_check in fail_toast
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'society_name').send_keys(before_name)
        time.sleep(2)

        #社团简介
        self.driver.find_id(self.id + 'brief_content').send_keys('这是一个严肃的社团简介~')
        time.sleep(2)

        #社团频道
        self.driver.find_ids(self.id + 'tv')[-1].click()
        self.driver.wait_id(self.id + 'edit_text')
        try:
            self.driver.find_id(self.id + 'tv1')
            self.driver.find_id(self.id + 'tv1').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'edit_text').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_search').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)

        #完成社团资料修改
        self.driver.find_id(self.id + 'tv_right').click()
        try:
            edit_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            assert check in edit_toast
            time.sleep(2)
        except:
            pass

    #社团管理-社团成员
    def Society_Members(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'shezhang')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        #添加成员
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'isCheck')
        #搜索用户
        self.driver.find_id(self.id + 'filter_edit').send_keys('15697799')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_xpath('大黑')
        self.driver.find_id(self.id + 'isCheck').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        Invited_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        try:
            self.driver.find_id(self.id + 'isCheck')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        assert check in Invited_toast, '社团成员邀请发送失败'
        time.sleep(2)

        #社团管理-成员权限
        try:
            self.driver.find_id(self.id + 'more')
            self.driver.find_id(self.id + 'more').click()
            time.sleep(2)
            # 社团管理权限
            self.driver.find_id(self.id + 'check_box1').click()
            time.sleep(1)
            state1 = self.driver.find_id(self.id + 'check_box1').get_attribute('checked')
            time.sleep(1)
            self.driver.find_id(self.id + 'check_box2').click()
            time.sleep(1)
            state2 = self.driver.find_id(self.id + 'check_box2').get_attribute('checked')
            time.sleep(2)
            self.driver.find_id(self.id + 'save').click()
            save_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '保存成功'
            assert check in save_toast
            time.sleep(2)
            if state1 == 'true':
                try:
                    self.driver.find_id(self.id + 'power')
                except:
                    print('开启社团管理权限后，成员一栏中未显示管理图标')
            elif state1 == 'false':
                try:
                    self.driver.find_id(self.id + 'power')
                    print('关闭社团管理权限后，成员一栏中依然显示管理图标')
                except:
                    pass
            time.sleep(2)
            if state2 == 'true':
                try:
                    self.driver.find_id(self.id + 'power')
                except:
                    print('开启社团声漫权限后，成员一栏中未显示声漫制作图标')
            elif state2 == 'false':
                try:
                    self.driver.find_id(self.id + 'power')
                    print('关闭社团声漫权限后，成员一栏中依然显示声漫制作图标')
                except:
                    pass
            time.sleep(2)
        except Exception as e:
            print(e)

        #社团管理-移除成员
        members = self.driver.find_ids(self.id + 'username')[-1]
        self.driver.Long_Touche(members, 2000)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'txtContent')
            content = self.driver.find_id(self.id + 'txtContent').text
            check = '移出属于'
            assert check in content
            time.sleep(2)
            self.driver.find_id(self.id + 'btnCancel').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            print('非社长身份，无法移除社团成员')
            try:
                self.driver.find_id(self.id + 'll_fan')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass

    #社团管理-社团公告
    def Society_announcement(self):
        self.driver.find_id(self.id + 'edit_gonggao').click()
        time.sleep(2)
        choice = random.choice('这是一个严肃的社团公告')
        self.driver.find_id(self.id + 'content').send_keys(choice)
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        gonggao_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        assert check in gonggao_toast
        check_content = self.driver.find_id(self.id + 'tv_gonggao').text
        if check_content != choice:
            print('社团公告修改后文案显示不正确',choice)
        time.sleep(2)

    #社团作品-作品管理
    def Society_Work_Manager(self):
        self.driver.find_id(self.id + 'film_manage').click()
        self.driver.wait_id(self.id + 'filmBg')
        #审核标准协议
        self.driver.find_id(self.id + 'middle').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        #社团作品-添加作品
        self.driver.find_id(self.id + 'addfilm').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.875)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        time.sleep(2)
        self.driver.find_ids('android:id/title')[1].click()
        self.driver.wait_id(self.id + 'next')
        time.sleep(2)
        #作品标题
        self.driver.find_id(self.id + 'title').send_keys('随便传个社团原创作品')
        time.sleep(2)
        #作品封面
        self.driver.find_id(self.id + 'upload_cover').click()
        self.driver.wait_id(self.id + 'photo_wall_item_photo')
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        self.driver.wait_id(self.id + 'confirm')
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(2)
        #添加配音表用户
        self.driver.find_id(self.id + 'mem').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'role').send_keys('我')
        time.sleep(2)
        self.driver.find_id(self.id + 'add_mem').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        #添加作品频道
        self.driver.find_id(self.id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        while True:
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                if self.y == 1920:
                    self.driver.tap(self.x * 0.5, self.y * 0.542)
                elif self.y >= 2280:
                    self.driver.tap(self.x * 0.5, self.y * 0.547)
                    time.sleep(6)
            try:
                self.driver.find_id(self.id + 'filmBg')
                break
            except:
                pass
            time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath('随便传个社团原创作品')
        except:
            print('未获取到上传的作品信息')
        time.sleep(2)

        #社团作品-删除作品
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'setting').click()
            try:
                time.sleep(2)
                if self.y == 1920:
                    self.driver.tap(self.x * 0.5, self.y * 0.875)
                elif self.y >= 2280:
                    self.driver.tap(self.x * 0.5, self.y * 0.87)
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
                delet_toast = self.driver.wait_toast('//android.widget.Toast')
                check = '删除作品成功'
                assert check in delet_toast
                time.sleep(2)
                self.driver.swip_down()
                time.sleep(2)
            except:
                pass
        except:
            print('非社长身份，无法删除社团作品')

    #社团作品-创建合辑
    def Society_create_collection(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'addfilm').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.802)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('测试合辑')
        time.sleep(2)
        self.driver.find_id(self.id + 'ok').click()
        self.driver.wait_id(self.id + 'choice')
        time.sleep(2)
        select = self.driver.find_ids(self.id + 'choice')
        for i in range(len(select)):
            self.driver.find_ids(self.id + 'choice')[i].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        try:
            create_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '创建成功'
            assert check in create_toast
        except:
            pass
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath('测试合辑')
        except:
            print('未显示创建的合辑')
        time.sleep(2)

    #我的社团-编辑合辑作品
    def Society_edit_collection(self):
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)
        #点击合辑作品
        self.driver.find_id(self.id + 'img').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #长按调节作品列表
        el = self.driver.find_id(self.id + 'img')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_zhiding').click()
        try:
            zd_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '第一个位置'
            assert check in zd_toast
        except:
            pass
        time.sleep(2)
        el2 = self.driver.find_ids(self.id + 'img')[-1]
        self.driver.Long_Touche(el2, 2000)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_zhiding').click()
        try:
            SY_toast = self.driver.wait_toast('//android.widget.Toast')
            check1 = '上移成功'
            assert check1 in SY_toast
        except:
            pass
        time.sleep(2)

        #移除作品
        el3 = self.driver.find_id(self.id + 'img')
        self.driver.Long_Touche(el3, 2000)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_shanchu').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast == '无权操作' or del_toast == '删除成功':
            pass
        else:
            print('合辑作品移除失败')

        #添加合辑作品
        self.driver.find_id(self.id + 'right_icon1').click()
        self.driver.wait_id(self.id + 'choice')
        title_before = self.driver.find_id(self.id + 'title').text
        self.driver.find_id(self.id + 'choice').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        add_toast = self.driver.wait_toast('//android.widget.Toast')
        check3 = '添加成功'
        assert check3 in add_toast
        time.sleep(2)
        try:
            self.driver.find_xpath(title_before)
        except:
            print('合辑作品列表未显示添加的新作品')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #我的社团-编辑合辑
        el = self.driver.find_id(self.id + 'filmBg')
        self.driver.Long_Touche(el,2000)
        time.sleep(2)
        #合辑置顶
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.807)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        zhiding_toast = self.driver.wait_toast('//android.widget.Toast')
        zhiding_check = '成功'
        assert zhiding_check in zhiding_toast
        time.sleep(2)

        #删除合辑
        self.driver.Long_Touche(el, 2000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.885)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.87)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast == '无权操作' or del_toast == '删除成功':
            pass
        else:
            print('合辑删除失败')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的社团-申请蓝V
    def Society_V(self):
        self.driver.find_id(self.id + 'apply_lv').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('立即申请')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass

    #我的社团-入社权限
    def Society_Entry_conditions(self):
        self.driver.find_id(self.id + 'society_apply_jurisdiction').click()
        time.sleep(2)
        #招募内容
        self.driver.find_id(self.id + 'modify').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('本社团并不招人')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        #申请要求
        self.driver.find_id(self.id + 'addFilm').click()
        time.sleep(1)
        self.driver.find_id(self.id + 'addSource').click()
        time.sleep(1)
        #入社申请开关
        self.driver.find_id(self.id + 'choice').click()
        time.sleep(1)
        self.driver.find_id(self.id + 'choice1').click()
        time.sleep(1)
        self.driver.find_id(self.id + 'choice2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        #我的社团-社团消息通知开关
        self.driver.find_id(self.id + 'btn_push').click()
        time.sleep(2)

    #我的社团-社团财富、社团钱包
    def Society_Wealth(self):
        self.driver.swip_up()
        self.driver.find_id(self.id + 'gold_match')
        time.sleep(2)
        self.driver.find_id(self.id + 'gold_match').click()
        time.sleep(2)
        # 分配钻石
        self.driver.find_id(self.id + 'distribution_diamond').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'gold_count').send_keys('100')
        time.sleep(2)
        self.driver.find_id(self.id + 'remark').send_keys('分配钻石')
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        Diamond_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '钻石'
        assert check in Diamond_toast
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        # 分配金币
        self.driver.find_id(self.id + 'distribution_gold').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'gold_count').send_keys('10000')
        time.sleep(2)
        self.driver.find_id(self.id + 'remark').send_keys('分配金币')
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        gold_toast = self.driver.wait_toast('//android.widget.Toast')
        check1 = '金币'
        assert check1 in gold_toast
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)



    def Society_other_function(self):
        # 我的社团-允许他人下载社团作品
        self.driver.find_id(self.id + 'btn_load')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_load').click()
        time.sleep(2)
        #我的社团-社团管理须知
        self.driver.find_xpath('《社团管理须知》').click()
        self.driver.wait_id(self.id + 'webview')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的社团-转让社团/解散社团
    def Society_Transfer_Dissolved(self):
        self.driver.find_id(self.id + 'right_icon1')
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.807)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        self.driver.wait_xpath('转让社团')
        self.driver.find_ids(self.id + 'username')[-1].click()
        time.sleep(2)
        Transfer_content = self.driver.find_id(self.id + 'txtContent').text
        check = '您确定要将社团转让给'
        assert check in Transfer_content
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.885)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.87)
        time.sleep(2)
        dissolved_content = self.driver.find_id(self.id + 'txtContent').text
        check1 = '你真的要解散社团吗？请提前处理好社团钱包中的收益，解散后无法恢复社团'
        assert check1 in dissolved_content
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)

    #返回社团主界面#
    def Society_Quit_Manager(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(self.id + 'task_box')
        self.driver.find_id(self.id + 'ivNewsTab').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'society').click()
        time.sleep(2)
