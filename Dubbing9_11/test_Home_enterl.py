#coding=utf-8
import unittest
import time
import re
import random
from Dubbing9_11.Front import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Channel(Dubbing):
    #进入首页频道列表界面
    def test_a(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(soucred_id + 'task_box')
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854 ,self.y * 0.189,self.x * 0.249,self.y *0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('频道').click()
        while True:
            try:
                self.driver.wait_id(soucred_id + 'tv')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #频道界面标签列表
    def test_b(self):
        labels = self.driver.find_ids(soucred_id + 'tv')
        time.sleep(2)
        for i in range(len(labels)-4):
            name = self.driver.find_ids(soucred_id + 'tv')[i].text
            self.driver.find_ids(soucred_id + 'tv')[i].click()
            self.driver.wait_xpath('排行榜')
            channel_name = self.driver.find_id(soucred_id + 'txtTitle').text
            self.assertEqual(name,channel_name,msg='频道列表界面标签名称与标签详情界面标签名称校验不一致')
            time.sleep(1)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)

    #更多频道-搜索频道
    def test_c(self):
        self.driver.find_xpath('更多频道').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'edit_text').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_search').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'tv')
        tv_name = self.driver.find_id(soucred_id + 'tv').text
        check = '配音'
        self.assertIn(check,tv_name,msg='标签搜索结果校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv').click()
        self.driver.wait_xpath('排行榜')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'filmBg').click()
        self.driver.wait_id(soucred_id + 'follow_ta')
        #退出视频详情
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        #退出作品列表
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        #退出标签搜索
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #热门频道
    def test_d(self):
        title  = self.driver.find_id(soucred_id + 'tv2').text
        self.driver.find_id(soucred_id + 'tv2').click()
        self.driver.wait_id(soucred_id + 'follow_ta')
        self.driver.Background()
        time.sleep(2)
        video_title = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
        self.assertIn(title,video_title,msg='频道主界面点击的视频标题与视频详情的标题校验失败')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        while True:
            name = self.driver.find_ids(soucred_id + 'tv')[-1].text
            self.driver.swip_up()
            time.sleep(2)
            Name = self.driver.find_ids(soucred_id + 'tv')[-1].text
            if name == Name:
                break
            else:
                pass
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_b_Near(Dubbing):
    #附近
    def test_a(self):
        while True:
            try:
                self.driver.find_xpath('附近')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('附近').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            self.driver.find_id(soucred_id + 'next').click()
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
                self.driver.wait_id(soucred_id + 'distance')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #附近列表
    def test_b(self):
        try:
            self.driver.find_id(soucred_id + 'channel1')
        except:
            raise ('当前列表界面作品未显示频道标签')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'look')
        except:
            raise ('当前列表界面作品未显示播放量')
        time.sleep(2)
        distance = self.driver.find_ids(soucred_id + 'distance')
        count = self.driver.find_ids(soucred_id + 'userHead')
        if len(distance) == len(count):
            pass
        else:
            raise ('附近当前界面有个别作品未显示距离信息')
        time.sleep(2)

    #视频详情切换-列表作品名称与视频详情作品名称校验
    def test_c(self):
        name = self.driver.find_ids(soucred_id + 'title')
        title_list = []
        for  title in range(len(name)):
            title_name = self.driver.find_ids(soucred_id + 'title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'title').click()
        for i in range(len(name)):
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            Name = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
            label1 = 'ch'
            label2 = 'lr'
            if label2 in Name:
                new_Name = re.findall(r"lr (.*)",Name)#获取list类型的字符串['xxxx']
                str_name = ''.join(new_Name)#转换成纯字符串'xxxx'
                assert str_name in title_list,u'视频详情标题不在标题列表中'
                time.sleep(2)
            else:
                new_Name1 = re.findall(r"ch (.*)",Name)
                str_name1 = ''.join(new_Name1)
                assert str_name1 in title_list,u'视频详情标题不在标题列表中'
                time.sleep(2)
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #作品列表下拉刷新-上滑加载
    def test_d(self):
        for i in range(3):
            self.driver.swip_down()
            time.sleep(2)
        for p in range(3):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_c_exposure(Dubbing):
    #进入曝光去
    def test_a(self):
        while True:
            try:
                self.driver.find_xpath('曝光区')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('曝光区').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id(soucred_id + 'filmBg')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #曝光作品评论
    def test_b(self):
        progress_before = self.driver.find_id(soucred_id + 'progress_bar').text
        self.driver.find_id(soucred_id + 'filmBg').click()
        while True:
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'comment').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'editContent').send_keys('^.^')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_send').click()
        try:
            self.driver.wait_xpath('^.^')
        except:
            raise ('未检测到发送的评论')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        progress_after = self.driver.find_id(soucred_id + 'progress_bar').text
        if progress_after == progress_before:
            value = '100.0'
            if progress_after ==value:
                pass
            else:
                raise ('曝光评论进度显示错误')
        elif progress_after > progress_before:
            pass
        else:
            pass
        time.sleep(2)

    #曝光作品预览-视频详情切换，标题名称校验
    def test_c(self):
        name = self.driver.find_ids(soucred_id + 'title')
        title_list = []
        for title in range(len(name)):
            title_name = self.driver.find_ids(soucred_id + 'title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'title').click()
        for i in range(len(name)):
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            Name = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
            label1 = 'ch'
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
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 作品列表下拉刷新-上滑加载
    def test_d(self):
        for i in range(3):
            self.driver.swip_down()
            time.sleep(2)
        for p in range(3):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_d_Rank(Dubbing):
    # 进入排行榜
    def test_a(self):
        while True:
            try:
                self.driver.find_xpath('排行榜')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('排行榜').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id(soucred_id + 'iv_source')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #富豪榜-列表加载
    def test_b(self):
        self.driver.find_id(soucred_id + 'tv_rich_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(soucred_id + 'username1')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'tv_rich_rank').click()
        time.sleep(2)

    #富豪榜-金额排序检查
    def test_c(self):
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'消费(.*)万金币', limit)
            str_Screening = ''.join(Screening)
            int_num = int(float(str_Screening))
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='富豪榜榜单金额排序验证错误')
        time.sleep(2)

    #富豪榜-用户信息
    def test_d(self):
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name,No1_zoom_name,msg='富豪榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    #富豪榜-周榜，月榜查看
    def test_e(self):
        self.driver.find_id(soucred_id + 'rl_tag2').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='富豪榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'消费(.*)万金币', limit)
            str_Screening = ''.join(Screening)
            int_num = int(float(str_Screening))
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='富豪榜榜单金额排序验证错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'rl_tag3').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='富豪榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'消费(.*)万金币', limit)
            str_Screening = ''.join(Screening)
            int_num = int(float(str_Screening))
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='富豪榜榜单金额排序验证错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #主播榜
    def test_f(self):
        self.driver.find_id(soucred_id + 'tv_live_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(soucred_id + 'userHead1')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'tv_live_rank').click()
        time.sleep(2)

    #主播榜-参与人排序检查
    def test_g(self):
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'直播总参与(.*)人', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='=主播榜人数排序验证错误')
        time.sleep(2)

    #主播榜-周榜-月榜检查
    def test_h(self):
        self.driver.find_id(soucred_id + 'rl_tag2').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='主播榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'直播总参与(.*)人', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='主播榜人数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'rl_tag3').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='主播榜第一用户名称与空间中的用户名校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'直播总参与(.*)人', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='主播榜人数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 社团榜
    def test_i(self):
        self.driver.find_id(soucred_id + 'tv_society_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(soucred_id + 'userHead1')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'tv_society_rank').click()
        time.sleep(2)

    # 社团榜-作品数排序检查
    def test_j(self):
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)作品', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='=社团榜作品数排序验证错误')
        time.sleep(2)

    # 社团榜-周榜-月榜检查
    def test_k(self):
        self.driver.find_id(soucred_id + 'rl_tag2').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_fan')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='社团榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)作品', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='=社团榜作品数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'rl_tag3').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='社团榜第一用户名称与空间中的用户名校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)作品', limit)
            str_Screening = ''.join(Screening)
            list.append(str_Screening)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='社团榜作品数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 素材榜
    def test_l(self):
        self.driver.find_id(soucred_id + 'tv_source_rank').click()
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id(soucred_id + 'userHead1')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'tv_source_rank').click()
        time.sleep(2)

    # 素材榜-素材数排序检查
    def test_m(self):
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)收录', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='=素材榜素材收录数排序验证错误')
        time.sleep(2)

    # 素材榜-周榜-月榜检查
    def test_n(self):
        self.driver.find_id(soucred_id + 'rl_tag2').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='素材榜第一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)收录', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='=素材榜素材收录数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'rl_tag3').click()
        time.sleep(2)
        No1_name = self.driver.find_id(soucred_id + 'username1').text
        self.driver.find_id(soucred_id + 'userHead1').click()
        self.driver.wait_id(soucred_id + 'll_follow')
        No1_zoom_name = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(No1_name, No1_zoom_name, msg='素材榜第一用户名称与空间中的用户名校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        count = self.driver.find_ids(soucred_id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(soucred_id + 'desc')[i].text
            Screening = re.findall(r'(.*)收录', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        self.assertEqual(list, list_set, msg='素材榜素材收录数排序验证错误')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #作品榜-列表标题是视频详情标题校验
    def test_o(self):
        self.driver.find_id(soucred_id + 'film').click()
        time.sleep(2)
        list_title = self.driver.find_ids(soucred_id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(soucred_id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_source_title').click()
        for i in range(len(list_title)):
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            Name = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
            label1 = 'ch'
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
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #作品榜列表加载
    def test_o_a(self):
        while True:
            name = self.driver.find_ids(soucred_id + 'rank')[-1].text
            self.driver.swip_up()
            time.sleep(2)
            Name = self.driver.find_ids(soucred_id + 'rank')[-1].text
            if name == Name:
                if Name == '300':
                    break
                else:
                    pass
            else:
                pass
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_xpath('排行榜').click()
        time.sleep(2)

    #热门标签tab-列表切换数据检查
    def test_p(self):
        self.driver.find_id(soucred_id + 'commentary').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'top')
            self.driver.find_id(soucred_id + 'close').click()
        except:
            pass
        time.sleep(2)
        list_title = self.driver.find_ids(soucred_id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(soucred_id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'film').click()
        time.sleep(2)
        list_title1 = self.driver.find_ids(soucred_id + 'tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids(soucred_id + 'tv_source_title')[title].text
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.assertNotEqual(list_title,list_title1,msg='排行榜与热门标签榜作品标题校验错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'commentary').click()
        time.sleep(2)

    #切换热门标签
    def test_p_a(self):
        label_name = self.driver.find_id(soucred_id +'commentary').text
        list_title = self.driver.find_ids(soucred_id + 'tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids(soucred_id + 'tv_source_title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'commentary').click()
        time.sleep(2)
        label_tv = self.driver.find_ids(soucred_id + 'tv')
        tv_list = []
        for i in range(len(label_tv)):
            tv_name = self.driver.find_ids(soucred_id + 'tv')[i].text
            tv_list.append(tv_name)
            time.sleep(1)
        tv_list.remove(label_name)
        select = random.randint(0,len(tv_list))
        self.driver.find_ids(soucred_id + 'tv')[select].click()
        self.driver.wait_id(soucred_id + 'iv_source')
        list_title1 = self.driver.find_ids(soucred_id + 'tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids(soucred_id + 'tv_source_title')[title].text
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.assertNotEqual(title_list,title_list1,msg='切换不同的热门标签后，列表中的作品未刷新')
        time.sleep(2)

    #切换标签后返回首页再进检查热门标签
    def test_p_b(self):
        name_before = self.driver.find_id(soucred_id + 'commentary').text
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_xpath('排行榜').click()
        time.sleep(2)
        name_after = self.driver.find_id(soucred_id + 'commentary').text
        self.assertEqual(name_after,name_before,msg='热门标签未保存')
        time.sleep(2)

    #列表作品查看
    def test_p_c(self):
        name = self.driver.find_id(soucred_id + 'tv_source_title').text
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        name1 = self.driver.find_id(soucred_id +'tv_video_detail_title').text
        self.driver.find_id(soucred_id + 'btnBack').click()
        self.assertIn(name,name1,msg='列表标题与视频详情标题不一致')
        time.sleep(2)
        for i in range(3):
            self.driver.swip_up()
            time.sleep(2)

    #潜力榜
    def test_q(self):
        self.driver.find_id(soucred_id + 'potential').click()
        time.sleep(2)
        name = self.driver.find_id(soucred_id + 'tv_source_title').text
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        name1 = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
        self.driver.find_id(soucred_id + 'btnBack').click()
        self.assertIn(name, name1, msg='列表标题与视频详情标题不一致')
        time.sleep(2)
        for i in range(3):
            self.driver.swip_up()
            time.sleep(2)

    #社作榜
    def test_r(self):
        self.driver.find_id(soucred_id + 'society_film').click()
        time.sleep(2)
        titles = self.driver.find_ids(soucred_id +'tv_source_title')
        for i in range(len(titles)):
            self.driver.find_ids(soucred_id + 'iv_source')[i].click()
            self.driver.wait_id(soucred_id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)

            try:
                self.driver.find_id(soucred_id + 'dubbing')
                raise ('社团作品显示有配音按钮')
            except:
                pass
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)

    #榜单列表加载
    def test_r_a(self):
        while True:
            ranking = self.driver.find_ids(soucred_id + 'rank')[-1].text
            if ranking =='300':
                break
            else:
                pass
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_e_Pia(Dubbing):
    #进入在线pia戏
    def test_a(self):
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
                self.driver.wait_id(soucred_id + 'start')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #勋章列表
    def test_b(self):
        self.driver.find_id(soucred_id + 'goXun').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'userHead')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except:
            raise ('未加载显示勋章列表')
        time.sleep(2)

    #道具商城
    def test_c(self):
        self.driver.find_xpath('道具商城').click()
        time.sleep(2)
        num = self.driver.find_id(soucred_id + 'diamond').text
        self.driver.find_id(soucred_id + 'diamond').click()
        time.sleep(2)
        num1 = self.driver.find_id(soucred_id +'diamond_count_tv').text
        time.sleep(2)
        self.assertIn(num,num1,msg='钻石额度校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    #幸运宝箱
    def test_c_a(self):
        self.driver.find_id(soucred_id + 'diamond').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'diamond_count_tv')
        except:
            raise ('幸运夺宝界面跳转至钻石充值界面失败')
        time.sleep(2)
        self.driver.find_id(soucred_id +'back').click()
        time.sleep(2)
        num = self.driver.find_id(soucred_id + 'diamond').text
        if num >49 :
            pass
        else:
            self.driver.find_id(soucred_id +'smoke_ten').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id +'btnSubmit').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'back').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #切换动画
    def test_c_b(self):
        num = self.driver.find_ids(soucred_id + 'img')
        for i in range(len(num)):
            self.driver.find_ids(soucred_id + 'img')[i].click()
            time.sleep(1)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #创建pia戏房间
    def test_d(self):
        self.driver.find_id(soucred_id + 'create_room').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'check_normal').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'crate_room').click()
        try:
            self.driver.wait_id(soucred_id + 'chat')
        except:
            raise ('pia戏房间创建失败')
        time.sleep(2)

    #评论
    def test_d_a(self):
        self.driver.find_id(soucred_id + 'show_comment').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'editContent').send_keys('哈哈哈')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_send').click()
        self.driver.wait_id(soucred_id + 'rl')
        time.sleep(2)

    #用户头像
    def test_d_a_a(self):
        self.driver.find_id(soucred_id + 'head').click()
        self.driver.wait_id(soucred_id + 'user_id')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'username')
            try:
                self.driver.find_id(soucred_id +'gender')
                try:
                    self.driver.find_id(soucred_id +'user_id')
                    try:
                        self.driver.find_id(soucred_id + 'user_detail')
                    except:
                        raise ('未显示用户简介')
                except:
                    raise ('未显示用户ID')

            except:
                raise ('未显示性别')
        except:
            raise ('未显示用户名')
        time.sleep(2)
        self.driver.find_id(soucred_id +'icon_close').click()
        time.sleep(2)

    #房间私密
    def test_d_b(self):
        self.driver.find_id(soucred_id + 'private_btn').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        self.assertEqual(tip,check,msg='普通房间设置私密，提示文案错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'close').click()
        time.sleep(2)

    #邀请好友
    def test_d_c(self):
        self.driver.find_ids(soucred_id + 'head')[-1].click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        self.assertEqual(tip, check, msg='普通房间邀请好友，提示文案错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'close').click()
        time.sleep(2)

    #剧本列表
    def test_d_d(self):
        self.driver.find_id(soucred_id + 'script').click()
        time.sleep(2)
        source = self.driver.find_ids(soucred_id + 'sourcename')
        source_list = []
        for i in range(len(source)):
            name = self.driver.find_ids(soucred_id + 'sourcename')[i].text
            source_list.append(name)

        No1 = source_list[0]
        No2 = source_list[1]
        self.assertNotEqual(No1,No2,msg='剧本列表校验失败')
        time.sleep(2)

    #添加剧本
    def test_d_e(self):
        self.driver.find_id(soucred_id + 'add_drama').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        self.assertEqual(tip, check, msg='添加剧本，提示文案错误')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'close').click()
        time.sleep(2)

    #退出在线pia戏房间
    def test_d_f(self):
        self.driver.find_id(soucred_id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'create_room')
        time.sleep(2)

    #在线匹配
    def test_e(self):
        while True:
            self.driver.find_id(soucred_id + 'start')
            try:
                self.driver.find_id(soucred_id + 'script')
                break
            except:
                pass
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'home_close')
        self.driver.find_id(soucred_id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'create_room')
        time.sleep(2)

    #跟随进入
    def test_f(self):
        self.driver.find_id(soucred_id + 'follow').click()
        time.sleep(2)
        self.driver.find_id(soucred_id +'refresh').click()
        try:
            self.driver.wait_toast(soucred_id +'//android.widget.Toast')
        except:
            raise ('未检测到刷新toast提示')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'close').click()
        time.sleep(2)


    #作品列表
    def test_g(self):
        self.driver.find_id(soucred_id + 'draft' ).click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_f_shenman(Dubbing):
    #有声漫画
    def test_a(self):
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
                self.driver.wait_id(soucred_id + 'collect')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)

    #推荐列表-声漫名称校验
    def test_b(self):
        name = self.driver.find_id(soucred_id + 'title').text
        self.driver.find_id(soucred_id + 'title').click()
        self.driver.wait_id(soucred_id + 'start_play')
        detail_name = self.driver.find_id(soucred_id + 'tvTitle').text
        self.assertEqual(name,detail_name,msg='推荐列表中声漫名称与声漫详情界面名称不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #声漫更新集数校验
    def test_b_a(self):
        update = self.driver.find_id(soucred_id + 'update').text
        num = re.findall(r'更新至(.*)话',update)
        self.driver.find_id(soucred_id + 'update').click()
        self.driver.wait_id(soucred_id + 'start_play')
        while True:
            number = self.driver.find_ids(soucred_id + 'name')[-1].text
            self.driver.swip_up()
            time.sleep(2)
            number1 = self.driver.find_ids(soucred_id + 'name')[-1].text
            if number == number1:
                break
            else:
                pass
        time.sleep(2)
        new = re.findall(r'第 (.*) 话',number1)
        self.assertEqual(num,new,msg='列表更新集数与声漫详情界面更新集数不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)














































if __name__ == '__main__':
    unittest.main()
