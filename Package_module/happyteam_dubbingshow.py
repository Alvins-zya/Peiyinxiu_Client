#encoding: utf-8

'''
@author:alvin.zhu
@file:happyteam_dubbingshow.py
@time:2020/11/6 10:27
@description:
'''
import unittest
import datetime
import warnings
import re,os,sys
import time, random
# from time import sleep,ctime
from typing import Counter
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath)[0]
sys.path.append(rootpath)

# file = open('D:\Git_pyhthon\Package_module\\topic_words.txt', 'r', encoding='utf-8')
from Public.Driver_Operate import BaseOperate,location,touche_Y,touche_X
# from public.unittest_import import dubbing
# from Package_module.Location_list import location

class home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()

    @classmethod
    def tearDownClass(self):
        pass

    def test_a_tips(self):
        try:
            self.driver.find_id('img_hot')
            self.driver.find_id_click('img_hot')
            time.sleep(2)
            self.driver.find_id_click('img_hot')
            time.sleep(2)
        except:
            pass
    #每日任务列表加载
    def test_a_a_task_list(self):
        self.driver.wait_id_click('task_box')
        self.driver.wait_id('rl1')

    #每日签到
    def test_b_task_daily_attendance(self):
        #奖池
        self.driver.find_id_click('tv_right')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)

        #签到
        self.driver.find_id_click('rl1')
        time.sleep(2)
        try:
            self.driver.find_id('img_double')
            time.sleep(2)
            self.driver.wait_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('img_one')
            self.driver.wait_toast('//android.widget.Toast')
        except:
            self.driver.find_id_click('complete')
        time.sleep(2)
        try:
            self.driver.find_id('tv_count1')
        except:
            print('每日签到错误')

    #日常任务
    def test_c_task_daily_tasks(self):
        check = ['上传一个带频道的作品', '分享作品至朋友圈', '收听语聊10分钟', '用钻石曝光1个作品', '评论5个曝光区作品', '看完5个作品']
        task_list = []
        self.driver.swip_up()
        tasks = self.driver.find_ids('title')
        for i in range(len(tasks)):
            task = self.driver.find_ids_text('title',i)
            task_list.append(task)
        time.sleep(2)
        if sorted(check) != sorted(task_list):
            print('日常任务列表校验错误')
        time.sleep(2)
        for j in range(len(task_list)):
            self.driver.swip_up()
            result = ('{0}, {1}'.format(j, task_list[j]))
            num = int(result[0])
            if task_list[num] == '上传一个带频道的作品':
                self.driver.find_ids_click('tv_lingqu',num)
                self.driver.wait_id('rl_coor')
                time.sleep(1)
                self.driver.find_id_click('ivDubbingTab')
                time.sleep(2)
                self.driver.find_id_click('task_box')
                time.sleep(2)

            elif task_list[num] == '分享作品至朋友圈':
                self.driver.find_ids_click('tv_lingqu',num)
                time.sleep(2)
                self.driver.wait_id_click('btnBack')
                time.sleep(2)

            elif task_list[num] == '收听语聊10分钟':
                self.driver.find_ids_click('tv_lingqu',num)
                time.sleep(2)
                self.driver.wait_id_click('btnBack')
                time.sleep(2)

            elif task_list[num] == '用钻石曝光1个作品':
                self.driver.find_ids_click('tv_lingqu',num)
                time.sleep(2)
                self.driver.wait_id_click('btnBack')
                time.sleep(2)

            elif task_list[num] == '评论5个曝光区作品':
                self.driver.find_ids_click('tv_lingqu',num)
                time.sleep(2)
                self.driver.wait_id_click('btnBack')
                time.sleep(2)

            elif task_list[num] == '看完5个作品':
                self.driver.find_ids_click('tv_lingqu',num)
                self.driver.wait_id_click('task_box')
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 首页搜索
    def test_d_home_search(self):
        self.driver.find_id_click('iv_search')
        self.driver.wait_id('txtKeyword')

    #首页素材搜索
    def test_e_source_search(self):
        self.driver.find_id_click('tv_source')
        time.sleep(2)
        self.driver.find_id_click('tv')
        self.driver.wait_id_click('iv_source')
        self.driver.wait_id('dubbing_fake')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnClear')
        time.sleep(1)
        self.driver.find_id_click('clear')
        time.sleep(2)

    # 首页作品搜索
    def test_f_work_search(self):
        self.driver.find_id_click('tv_work')
        time.sleep(2)
        self.driver.find_id_click('tv')
        self.driver.wait_id_click('filmBg')
        self.driver.wait_id('tv_comment')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnClear')
        time.sleep(2)
        self.driver.find_id_click('clear')
        time.sleep(2)

    #首页用户搜索
    def test_g_user_search(self):
        self.driver.find_id_click('tv_user')
        time.sleep(2)
        self.driver.find_id_click('txtKeyword')
        user_list = ['148207791', '152726825', '159420264', '141130466']
        for i in user_list:
            self.driver.find_id_send('txtKeyword',i)
            time.sleep(2)
            self.driver.find_id_click('btnSearch')
            self.driver.wait_id('userhead')
            self.driver.find_id_click('btnClear')
            time.sleep(2)
        self.driver.find_id_click('clear')
        time.sleep(2)

    #推荐用户
    def test_h_user_recommend(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('status_icon')
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('fanscount')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('status_icon')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #列表上、下滑动
    def test_i_work_list_load(self):
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    #作品列表界面点击进入视频详情
    def test_j_touch_into_video(self):
        #点击作品封面进入视频详情
        self.driver.find_id_click('film_img2')
        self.driver.wait_id('userhead')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #列表界面点击用户头像进入视频详情
        self.driver.find_id_click('user_head')
        self.driver.wait_id('btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #列表界面点击作品标题进入视频详情
        self.driver.find_id_click('title2')
        self.driver.wait_id('btnBack')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #列表界面点击作品标签
        self.driver.find_id_click('film2_channel1')
        self.driver.wait_id('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('film2_channel2')
        self.driver.wait_id('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

class home_function(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()

    @classmethod
    def tearDownClass(self):
        pass

    # 进入首页频道列表界面
    def test_a_function_channel(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id('task_box')
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        self.driver.find_xpath('频道').click()
        self.driver.wait_id('tv')
        time.sleep(2)

    # 频道界面标签列表
    def test_b_function_channel_tvs(self):
        labels = self.driver.find_ids('tv')
        time.sleep(2)
        for i in range(len(labels) - 4):
            name = self.driver.find_ids_text('tv',i)
            self.driver.find_ids_click('tv',i)
            self.driver.wait_xpath('排行榜')
            channel_name = self.driver.find_id_text('txtTitle')
            if name != channel_name:
                print('频道列表界面标签名称与标签详情界面标签名称校验不一致')
            time.sleep(1)
            self.driver.find_id_click('btnBack')
            time.sleep(2)

    # 热门频道
    def test_c_function_channel_hot(self):
        title = self.driver.find_id_text('tv2')
        self.driver.find_id_click('tv2')
        self.driver.wait_id('follow_ta')
        self.driver.Background()
        time.sleep(2)
        video_title = self.driver.find_id_text('tv_video_detail_title')
        if title not in video_title:
            print('频道主界面点击的视频标题与视频详情的标题校验失败')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('count')
        self.driver.wait_id('txtTitle')
        self.driver.find_id_click('btnBack')
        self.driver.swip_up()
        time.sleep(2)

    # 附近
    def test_d_function_channel_nearby(self):
        while True:
            try:
                self.driver.find_xpath('附近')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        self.driver.find_xpath('附近').click()
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('next')
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
                self.driver.wait_id('distance')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        time.sleep(2)

    # 附近列表
    def test_e_function_channel_nearby_work_list(self):
        distance = self.driver.find_ids('distance')
        count = self.driver.find_ids('userhead')
        if len(distance) != len(count):
            print('附近当前界面有个别作品未显示距离信息')
        time.sleep(2)
        try:
            self.driver.find_id('channel1')
        except:
            print('当前列表界面作品未显示频道标签')
        time.sleep(2)

    # 视频详情切换-列表作品名称与视频详情作品名称校验
    def test_f_function_channel_nearby_work_detail(self):
        name = self.driver.find_ids('title')
        title_list = []
        for title in range(len(name)):
            title_name = self.driver.find_ids_text('title',title)
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id_click('title')
        for i in range(len(name)):
            self.driver.wait_id('follow_ta')
            self.driver.Background()
            time.sleep(2)
            name = self.driver.find_id_text('tv_video_detail_title')
            label1 = 'ch'
            label2 = 'lr'
            if label2 in name :
                new_name = re.findall(r"lr (.*)", name)  # 获取list类型的字符串['xxxx']
                str_name = ''.join(new_name)  #转换成纯字符串xxxx
                assert str_name in title_list, '视频详情标题不在标题列表中'
            elif label1 in name:
                new_name1 = re.findall(r" (.*)", name)
                str_name1 = ''.join(new_name1)
                assert str_name1 in title_list, u'视频详情标题不在标题列表中'
            else:
                assert name in title_list,'视频详情标题不在标题列表中'
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #进入曝光区
    def test_g_function_exposure(self):
        while True:
            # noinspection pybroadexception
            try:
                self.driver.find_xpath('曝光区')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        self.driver.find_xpath('曝光区').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id('filmBg')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        time.sleep(2)

    #曝光作品评论
    def test_h_function_exposure_comment(self):
        progress_before = self.driver.find_id_text('progress_bar')
        self.driver.find_id_click('filmBg')
        self.driver.wait_id('follow_ta')
        self.driver.Background()
        time.sleep(2)
        while True:
            try:
                self.driver.find_id('comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('tv_comment')
        time.sleep(2)
        self.driver.find_id_send('editContent','哈哈')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        try:
            self.driver.wait_xpath('哈哈')
        except:
            print('未检测到发送的评论')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        progress_after = self.driver.find_id_text('progress_bar')
        if progress_after == progress_before:
            value = '100.0'
            if progress_after != value:
                print('曝光评论进度显示错误')
        time.sleep(2)

    #进入排行榜
    def test_i_function_rank(self):
        while True:
            try:
                self.driver.find_xpath('排行榜')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        self.driver.find_xpath('排行榜').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id('iv_source')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        time.sleep(2)

    #获赞榜-列表加载
    def test_j_function_rank_good_rank(self):
        self.driver.find_id_click('tv_rich_rank')
        while True:
            try:
                self.driver.wait_id('userHead1')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('tv_rich_rank')
            time.sleep(2)

    #获赞榜-点赞数排序检查
    def test_k_function_rank_good_rank_sort(self):
        count = self.driver.find_ids('desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids_text('desc',i)
            goods = re.findall(r'获赞(.*)', limit)
            str_good_count = ''.join(goods)
            int_num = int(str_good_count)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=true)
        assert lists == list_set, '获赞榜点赞排序验证错误'
        time.sleep(2)

    #获赞榜-用户信息
    def test_l_function_rank_good_rank_userinfo(self):
        no1_name = self.driver.find_id_text('username1')
        self.driver.find_id_click('userHead1')
        self.driver.wait_id('ll_fan')
        no1_zoom_name = self.driver.find_id_text('username')
        assert no1_name == no1_zoom_name, '获赞榜第一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    #获赞榜-周榜，月榜查看
    def test_m_function_rank_good_rank_table(self):
        self.driver.find_id_click('rl_tag2')
        time.sleep(2)
        no1_name = self.driver.find_id_text('username1')
        self.driver.find_id_click('userHead1')
        self.driver.wait_id('ll_follow')
        no1_zoom_name = self.driver.find_id_text('username')
        assert no1_name == no1_zoom_name, '榜一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id_click('rl_tag3')
        time.sleep(2)
        no1_name = self.driver.find_id_text('username1')
        self.driver.find_id_click('userHead1')
        self.driver.wait_id('ll_follow')
        no1_zoom_name = self.driver.find_id_text('username')
        assert no1_name == no1_zoom_name, '榜一用户名称与空间中的用户名称校验不一致'
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    #主播榜
    def test_n_function_rank_anchor(self):
        self.driver.find_id_click('tv_live_rank')
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id('userHead1')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('tv_live_rank')
        time.sleep(2)

    #主播榜-参与人排序检查
    def test_o_function_rank_anchor_sort(self):
        count = self.driver.find_ids('desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids_text('desc',i)
            screening = re.findall(r'直播总参与(.*)人', limit)
            str_screening = ''.join(screening)
            int_num = int(str_screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=true)
        assert lists == list_set, '主播榜人数排序验证错误'
        time.sleep(2)

    #社团榜
    def test_p_function_rank_societies(self):
        self.driver.find_id_click('tv_society_rank')
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id('userHead1')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('tv_society_rank')
        time.sleep(2)

    #社团榜-作品数排序检查
    def test_q_function_rank_societies_sort(self):
        count = self.driver.find_ids('desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids_text('desc',i)
            screening = re.findall(r'(.*)作品', limit)
            str_screening = ''.join(screening)
            int_num = int(str_screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=true)
        assert lists == list_set, '=社团榜作品数排序验证错误'
        time.sleep(2)

    #素材榜
    def test_r_function_rank_sources(self):
        self.driver.find_id_click('tv_source_rank')
        while True:
            time.sleep(2)
            try:
                self.driver.wait_id('userHead1')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('tv_source_rank')
        time.sleep(2)

    #素材榜-素材数排序检查
    def test_s_function_rank_sources_sort(self):
        count = self.driver.find_ids('desc')
        lists = []
        for i in range(len(count)):
            limit = self.driver.find_ids_text('desc',i)
            screening = re.findall(r'(.*)收录', limit)
            str_screening = ''.join(screening)
            int_num = int(str_screening)
            lists.append(int_num)
            time.sleep(1)
        list_set = sorted(lists, reverse=true)
        assert lists == list_set, '素材榜素材收录数排序验证错误'
        time.sleep(2)

    #作品榜-列表标题是视频详情标题校验
    def test_t_function_rank_works_title_check(self):
        self.driver.find_id_click('film')
        time.sleep(2)
        list_title = self.driver.find_ids('tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids_text('tv_source_title',title)
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id_click('tv_source_title')
        for i in range(len(list_title)):
            self.driver.wait_id('follow_ta')
            self.driver.Background()
            time.sleep(2)
            name = self.driver.find_id_text('tv_video_detail_title')
            # label1 = 'ch'
            label2 = 'lr'
            if label2 in name:
                new_name = re.findall(r"lr (.*)", name)  # 获取list类型的字符串['xxxx']
                str_name = ''.join(new_name)  # 转换成纯字符串xxxx
                assert str_name in title_list, u'视频详情标题不在标题列表中'
                time.sleep(2)
            else:
                new_name1 = re.findall(r"ch (.*)", name)
                str_name1 = ''.join(new_name1)
                assert str_name1 in title_list, u'视频详情标题不在标题列表中'
                time.sleep(2)
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #热门标签tab-列表切换数据检查
    def test_u_function_rank_hot_label(self):
        self.driver.find_id_click('commentary')
        time.sleep(2)
        try:
            self.driver.find_id('top')
            self.driver.find_id_click('close')
        except:
            pass
        time.sleep(2)
        list_title = self.driver.find_ids('tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids_text('tv_source_title',title)
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id_click('film')
        time.sleep(2)
        list_title1 = self.driver.find_ids('tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids_text('tv_source_title',title)
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        assert list_title != list_title1, '排行榜与热门标签榜作品标题校验错误'
        time.sleep(2)
        self.driver.find_id_click('commentary')
        time.sleep(2)

    #切换热门标签
    def test_v_function_rank_hot_label_change(self):
        label_name = self.driver.find_id_text('commentary')
        list_title = self.driver.find_ids('tv_source_title')
        time.sleep(1)
        title_list = []
        for title in range(len(list_title)):
            title_name = self.driver.find_ids_click('tv_source_title',title)
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id_click('commentary')
        time.sleep(2)
        label_tv = self.driver.find_ids('tv')
        tv_list = []
        for i in range(len(label_tv)):
            tv_name = self.driver.find_ids_click('tv',i)
            tv_list.append(tv_name)
            time.sleep(1)
        tv_list.remove(label_name)
        select = random.randint(0, len(tv_list))
        self.driver.find_ids_click('tv',select)
        self.driver.wait_id('iv_source')
        list_title1 = self.driver.find_ids('tv_source_title')
        time.sleep(1)
        title_list1 = []
        for title in range(len(list_title1)):
            title_name = self.driver.find_ids_click('tv_source_title',title)
            title_list1.append(title_name)
            time.sleep(1)
        time.sleep(2)
        assert title_list != title_list1, '切换不同的热门标签后，列表中的作品未刷新'
        time.sleep(2)

    #潜力榜
    def test_w_function_rank_potential_list(self):
        self.driver.find_id_click('potential')
        time.sleep(2)
        name = self.driver.find_id_text('tv_source_title')
        self.driver.find_id_click('iv_source')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        name1 = self.driver.find_id_text('tv_video_detail_title')
        self.driver.find_id_click('btnBack')
        assert name in name1, '列表标题与视频详情标题不一致'
        time.sleep(2)
        for i in range(3):
            self.driver.swip_up()
            time.sleep(2)

    # 社作榜
    def test_x_function_rank_society_works(self):
        self.driver.find_id_click('society_film')
        time.sleep(2)
        titles = self.driver.find_ids('tv_source_title')
        for i in range(len(titles)):
            self.driver.find_ids_click('iv_source',i)
            self.driver.wait_id('tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)

            try:
                self.driver.find_id('dubbing')
                print('社团作品显示有配音按钮')
            except:
                pass
            self.driver.find_id_click('btnBack')
            time.sleep(2)

    # 榜单列表加载
    def test_y_function_rank_works_list_load(self):
        while True:
            ranking = self.driver.find_ids_click('rank',-1)
            if ranking == '300':
                break
            else:
                pass
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    # 进入在线pia戏
    def test_z_function_pia(self):
        while True:
            try:
                self.driver.find_xpath('在线pia戏')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        self.driver.find_xpath('在线pia戏').click()
        time.sleep(2)
        while True:
            try:
                self.driver.wait_id('start')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        time.sleep(2)

    # 勋章列表
    def test_z_a_function_pia_medal_list(self):
        self.driver.find_id_click('goXun')
        time.sleep(2)
        try:
            self.driver.find_id('userhead')
            time.sleep(2)
        except:
            print('未加载显示勋章列表')
        time.sleep(2)

    # 道具商城
    def test_z_b_function_pia_prop_mall(self):
        self.driver.find_xpath('道具商城').click()
        time.sleep(2)
        num = self.driver.find_id_text('diamond')
        self.driver.find_id_click('diamond')
        time.sleep(2)
        num1 = self.driver.find_id_text('diamond_count_tv')
        time.sleep(2)
        assert num in num1, '钻石额度校验不一致'
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    # 幸运宝箱
    def test_z_c_function_pia_prop_mall_lucky_box(self):
        self.driver.find_id_click('box')
        time.sleep(2)
        num = self.driver.find_id_text('diamond')
        if int(num) < 49:
            self.driver.find_id_click('smoke_ten')
            time.sleep(2)
            try:
                self.driver.find_id_click('btnSubmit')
                time.sleep(2)
                self.driver.find_id_click('back')
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    # pia戏装扮
    def test_z_d_function_pia_prop_mall_dress_up(self):
        num = self.driver.find_ids('img')
        for i in range(len(num)):
            self.driver.find_ids_click('img',i)
            time.sleep(1)

    # 创建pia戏房间
    def test_z_e_function_pia_create_room(self):
        self.driver.find_id_click('create_room')
        time.sleep(2)
        self.driver.find_id_click('check_normal')
        time.sleep(2)
        self.driver.find_id_click('crate_room')
        try:
            self.driver.wait_id('chat')
        except:
            print('pia戏房间创建失败')
        time.sleep(2)

    # 评论
    def test_z_f_function_pia_room_comment(self):
        self.driver.find_id_click('show_comment')
        time.sleep(2)
        self.driver.find_id_send('editContent','哈哈哈')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.wait_id('rl')
        time.sleep(2)

    # 用户头像
    def test_z_g_function_pia_room_userhead(self):
        self.driver.find_id_click('head')
        self.driver.wait_id('user_id')
        time.sleep(2)
        try:
            self.driver.find_id('username')
            try:
                self.driver.find_id('gender')
                try:
                    self.driver.find_id('user_id')
                    try:
                        self.driver.find_id('user_detail')
                    except:
                        print('未显示用户简介')
                except:
                    print('未显示用户id')

            except:
                print('未显示性别')
        except:
            print('未显示用户名')
        time.sleep(2)
        self.driver.find_id_click('icon_close')
        time.sleep(2)

    # 房间私密
    def test_z_h_function_pia_room_private(self):
        self.driver.find_id_click('private_btn')
        time.sleep(2)
        tip = self.driver.find_id_text('btnSubmit')
        check = '升级房间(5钻/小时)'
        assert tip == check, '普通房间设置私密，提示文案错误'
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 邀请好友
    def test_z_i_function_pia_room_invite_friend(self):
        self.driver.find_ids_click('head',-1)
        time.sleep(2)
        tip = self.driver.find_id_text('btnSubmit')
        check = '升级房间(5钻/小时)'
        assert tip == check, '普通房间邀请好友，提示文案错误'
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 剧本列表
    def test_z_j_function_pia_room_script_list(self):
        self.driver.find_id_click('script')
        time.sleep(2)
        source = self.driver.find_ids('sourcename')
        source_list = []
        for i in range(len(source)):
            name = self.driver.find_ids_text('sourcename',i)
            source_list.append(name)
        no1 = source_list[0]
        no2 = source_list[1]
        assert no1 != no2, '剧本列表校验失败'
        time.sleep(2)
        # 添加剧本
        self.driver.find_id_click('add_drama')
        time.sleep(2)
        tip = self.driver.find_id_text('btnSubmit')
        check = '升级房间(5钻/小时)'
        assert tip == check, '添加剧本，提示文案错误'
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 退出在线pia戏房间
    def test_z_k_function_pia_room_exit(self):
        self.driver.find_id_click('home_close')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('create_room')
        time.sleep(2)

    # 在线匹配
    def test_z_l_function_pia_match_online(self):
        self.driver.find_id_click('start')
        time.sleep(5)
        try:
            self.driver.find_id_click('cancel')
        except:
            self.driver.find_id_click('home_close')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            self.driver.wait_id('create_room')
        time.sleep(2)

    # 跟随进入
    def test_z_m_function_pia_follow(self):
        self.driver.find_id_click('follow')
        time.sleep(2)
        self.driver.find_id_click('refresh')
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print('未检测到刷新toast提示')
        time.sleep(2)
        self.driver.find_id_click('close')
        time.sleep(2)

    # 作品列表
    def test_z_n_function_pia_draft(self):
        self.driver.find_id_click('pia_film')
        time.sleep(2)

    # 有声漫画
    def test_z_o_function_cartoon(self):
        while True:
            try:
                self.driver.find_xpath('有声漫画')
                break
            except:
                self.loc.home_func()
        time.sleep(2)
        while True:
            self.driver.find_xpath('有声漫画').click()
            time.sleep(2)
            try:
                self.driver.wait_id('collect')
                break
            except:
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        time.sleep(2)

    # 推荐列表-声漫名称校验
    def test_z_p_function_cartoon_title_check(self):
        name = self.driver.find_id_text('title')
        self.driver.find_id_click('title')
        self.driver.wait_id('start_play')
        detail_name = self.driver.find_id_text('tvTitle')
        assert name == detail_name, '推荐列表中声漫名称与声漫详情界面名称不一致'
        time.sleep(2)

    # 推荐列表加载
    def test_z_q_function_cartoon_list_load(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        for i in range(4):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)

    # 声漫剧集详情
    def test_z_r_function_cartoon_episodes_detail(self):
        i = 0
        while i <= 10:
            self.driver.find_id_click('imgHead')
            try:
                self.driver.wait_id('start_play')
                break
            except:
                self.driver.find_id_click('btnBack')
            time.sleep(2)
            if i == 10:
                break
            else:
                pass
            i = i + 1
            time.sleep(2)

    # 剧集列表界面点击声漫收藏
    def test_z_s_function_cartoon_collection(self):
        self.driver.find_id_click('collect')
        toast = self.driver.wait_toast('//android.widget.Toast')
        check = '收藏成功'
        assert toast == check, '收藏toast校验不一致'
        time.sleep(2)
        self.driver.find_id_click('collect')
        cancel_toast = self.driver.wait_toast('//android.widget.Toast')
        cancel_check = '取消收藏成功'
        assert cancel_check == cancel_toast, '声漫取消收藏toast校验不一致'
        time.sleep(2)

    # 声漫制作相关社团列表
    def test_z_t_function_cartoon_make_society(self):
        self.driver.find_id_click('right_rl')
        try:
            self.driver.wait_id('count')
        except:
            print('声漫制作社团列表加载失败')
        time.sleep(2)
        self.driver.find_ids_click('name',1)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 连载漫画集数查看
    def test_z_u_function_cartoon_episode_check(self):
        num = self.driver.find_id_text('name')
        self.driver.find_id_click('name')
        self.driver.wait_id('userhead')
        self.driver.Background()
        time.sleep(2)
        re_num = re.findall(r'第 (.*) 话', num)
        new_num = ''.join(re_num)
        title_name = self.driver.find_id_text('tv_video_detail_title')
        assert new_num in title_name, '声漫切换集数校验不一致'
        time.sleep(2)

    #最新列表-话集更新检查
    def test_z_v_function_cartoon_update_check(self):
        self.driver.find_id_click('tab2')
        time.sleep(2)
        # update = self.driver.find_id_text('update')
        union = self.driver.find_id_text('union_name')
        # new_update = re.findall(r'更新至(.*)', update)
        self.driver.find_id_click('play')
        self.driver.wait_id('userhead')
        self.driver.Background()
        time.sleep(2)
        detail_name = self.driver.find_id_text('user_name')
        assert union == detail_name, '社团名称校验不一致'
        time.sleep(2)

    # 声漫分类列表
    def test_z_w_function_cartoon_classification_list(self):
        self.driver.find_id_click('tab3')
        time.sleep(2)
        title = self.driver.find_ids('title')
        for i in range(len(title) - 1, -1, -1):
            self.driver.find_ids_click('title',i)
        time.sleep(1)

    # 声漫制作
    def test_z_x_function_cartoon_make(self):
        self.driver.find_id_click('sm')
        time.sleep(2)
        title = self.driver.find_ids('title')
        for i in range(len(title) - 1, -1, -1):
            self.driver.find_ids_click('title',i)
        time.sleep(1)

    # 漫画详情
    def test_z_y_function_cartoon_detail(self):
        self.driver.find_id_click('btn_add')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','你听说过女大学生吗')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        time.sleep(2)
        self.driver.find_id_click('iv_pic1')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)

    # 制作声漫
    def test_z_z_function_cartoon_making(self):
        self.driver.find_id_click('tv_make')
        time.sleep(2)
        try:
            self.driver.find_id('btnSubmit')
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
            self.driver.find_id_click('tv_make')
            time.sleep(2)
        except:
            pass
        while True:
            try:
                self.driver.find_xpath('添加配音者')
                self.driver.find_xpath('添加配音者').click()
                time.sleep(2)
                self.driver.wait_id_click('socialstatus')
                time.sleep(2)
            except:
                break
        time.sleep(1)
        self.driver.find_id_click('tv_sure')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    # 我的漫画
    def test_z_z_a_function_cartoon_my(self):
        self.driver.find_id_click('tab2')
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        self.driver.wait_xpath('你听说过女大学生吗')
        time.sleep(2)

    # 声漫统筹界面-更新配音者
    def test_z_z_b_function_cartoon_change_voiceover(self):
        self.driver.find_id_click('iv_pic1')
        time.sleep(2)
        self.driver.find_id_click('change')
        time.sleep(2)
        self.driver.find_id_click('change')
        time.sleep(2)
        self.driver.wait_id('socialstatus')
        time.sleep(1)
        self.driver.find_ids_click('socialstatus',-1)
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id_click('change')
        time.sleep(2)
        self.driver.find_id_click('change')
        time.sleep(2)
        self.driver.wait_id_click('socialstatus')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    # 进入统筹界面-添加音效
    def test_z_z_c_function_cartoon_making_insert_sound(self):
        self.driver.find_id_click('make')
        self.driver.wait_id('upload')
        self.driver.find_xpath('添加音效').click()
        time.sleep(2)

    # 点击录音
    def test_z_z_d_function_cartoon_record(self):
        self.driver.find_id_click('transcribe')
        time.sleep(5)
        self.driver.find_id_click('transcribe')
        time.sleep(4)

    # 点击试听音效
    def test_z_z_e_function_cartoon_making_listening_test(self):
        sounds = self.driver.find_ids('effect_types_img')
        for i in range(len(sounds)):
            self.driver.find_ids_click('effect_types_img',i)
            time.sleep(3)
            sounds_classification = self.driver.find_ids('effect_sound_name')
            for y in range(len(sounds_classification)):
                self.driver.find_ids_click('effect_sound_name',y)
                time.sleep(2)

        # 播放整体动漫音效
        self.driver.find_id_click('preview')
        time.sleep(10)

    # 进入添加背景音界面
    def test_z_z_f_function_cartoon_making_background_music(self):
        self.driver.find_id_click('upload')
        self.driver.wait_id('comic_sound_class_name')
        time.sleep(2)
        self.driver.find_xpath('舒缓').click()
        time.sleep(2)
        self.driver.find_id_click("add")
        self.driver.find_id_click('tv_preview')
        time.sleep(2)
        # 声漫背景音界面裁剪添加背景
        self.loc.carton_cut_music()
        time.sleep(2)
        self.driver.find_id_click('tv_preview')
        time.sleep(5)
        self.driver.find_xpath('完成').click()
        time.sleep(5)
        self.driver.wait_xpath('保存')
        time.sleep(2)
        self.driver.find_xpath('保存').click()
        self.driver.wait_xpath('下一步')
        self.driver.find_id_click('preview')
        self.driver.wait_id('preview')
        time.sleep(2)
        self.driver.find_id_click('next')
        self.driver.wait_id('upload')
        time.sleep(2)

    # 声漫上传界面-保存并退出
    def test_z_z_g_function_cartoon_making_save(self):
        self.driver.find_id_click('preview')
        self.driver.wait_id('preview')
        time.sleep(2)
        self.driver.find_id_click('savebtn')
        self.driver.wait_id('make')
        time.sleep(2)

    # 声漫上传
    def test_z_z_h_function_cartoon_making_upload(self):
        self.driver.find_id_click('make')
        self.driver.wait_id('upload')
        time.sleep(2)
        self.driver.find_id_click('upload')
        self.driver.wait_id('comic_sound_class_name')
        time.sleep(2)
        self.driver.find_id_click('next')
        self.driver.wait_id_click('upload')
        try:
            self.driver.wait_id('imgurl')
        except:
            print('声漫上传失败')
        time.sleep(2)

    # 声漫删除
    def test_z_z_i_function_cartoon_delete(self):
        try:
            self.driver.find_id('imgurl')
            self.driver.find_id_click('imgurl')
            self.driver.wait_id('userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('tv_good')
            time.sleep(2)
            self.driver.find_id_click('setting')
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(0.5 * self.x, 0.867 * self.y)
            elif self.y >= 2280:
                self.driver.tap(0.5 * self.x, 0.883 * self.y)
                time.sleep(2)
                self.driver.find_id_click('btnSubmit')
                try:
                    self.driver.wait_toast('//android.widget.Toast')
                except:
                    print('未检测到声漫删除toast')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(3)
                self.driver.find_id_click('close1')
                time.sleep(2)
                self.driver.find_id_click('btnSubmit')
                time.sleep(2)
        except:
            print('未位于声漫剧集列表界面')

class dub(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    #合作素材
    def test_a_material_library_dubble(self):
        self.driver.wait_id('task_box')
        self.driver.find_id_click('btn_more')
        self.driver.wait_id_click('coor')
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)

    def test_a_a(self):
        try:
            self.driver.find_id('dubbing')
        except:
            self.driver.find_id_click('change_type')
        time.sleep(2)

    # 双配素材-进入配音界面
    def test_b_into_dubbing_double(self):
        self.driver.find_id_click('dubbing')
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('close')
            time.sleep(2)
            try:
                self.driver.find_id('dubbing_fake')
                self.driver.find_id_click('dubbing_fake')
                time.sleep(3)
                self.driver.find_id_click('next')
                time.sleep(2)
                try:
                    self.driver.wait_sys('始终允许')
                except:
                    self.driver.wait_sys('允许')
            except:
                print('未返回到素材预览界面')
                self.driver.quit()
        except:
            pass
        self.driver.wait_id_click('roleall')
        time.sleep(2)

    #退出配音界面
    def test_c_dub_exit_dubbing(self):
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnCancel')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(3)
        self.test_b_into_dubbing_double()

    # 双配素材配音界面配音角色切换
    def test_d_dub_exchange_roles(self):
        self.driver.find_id_click('coopera')
        time.sleep(2)
        self.driver.find_id_click('role1_tv')
        time.sleep(2)
        self.driver.find_id_click('coopera')
        time.sleep(2)
        self.driver.find_id_click('role2_tv')
        time.sleep(2)
        self.driver.find_id_click('coopera')
        time.sleep(2)
        self.driver.find_id_click('roleall')
        time.sleep(2)

    # 配音界面背景音开关
    def test_e_dub_background_sound(self):
        self.driver.find_id_click('headset')
        time.sleep(2)
        try:
            tips = self.driver.find_id_text('txtContent')
            check = '开启背景音需要插上耳机！'
            assert tips == check, '耳机提示文案不一致'
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
        except:
            pass

    # 开启实况
    def test_f_dub_start_camera(self):
        # 开启实况权限检查
        self.driver.find_id_click('living')
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('next')
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
            self.driver.find_id('cameraView2')
        except:
            self.driver.find_id_click('living')
            time.sleep(4)

    #关闭实况开关
    def test_g_dub_close_camera(self):
        self.driver.find_id_click('living')
        time.sleep(4)
        try:
            self.driver.find_id('cameraView2')
            self.driver.find_id_click('living')
        except:
            pass
        time.sleep(2)

    #配音界面台词列表
    def test_h_dub_script_list_swip(self):
        self.driver.find_id_click('scirpt')
        time.sleep(2)
        self.driver.wait_id('titletextView')
        count = self.driver.find_ids('titletextView')
        num = len(count)
        if num > 4:
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('cancelBn')
        self.driver.wait_id('scirpt')
        time.sleep(2)

    # 台词列表切换台词
    def test_i_dub_script_change(self):
        script_cout = int(self.driver.find_id_text('scirpt_count'))
        if script_cout > 1:
            self.driver.find_id_click('scirpt')
            self.driver.wait_id('titletextView')
            count = self.driver.find_ids('titletextView')
            for i in range(len(count) -1, -1, -1):
                self.driver.find_ids_click('titletextView',i)
                try:
                    self.driver.find_id('roleall')
                    self.driver.find_id_click('roleall')
                except:
                    pass
                self.driver.wait_id('edit_subtitle')
                self.driver.find_id_click('scirpt')
                self.driver.wait_id('titletextView')
                time.sleep(2)
            self.driver.find_id_click('cancelBn')
        time.sleep(2)

    # 修改台词后点击完成，再次进入编辑界面查看修改后的台词
    def test_j_dub_script_edit(self):
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.hide_keyboard()
        self.driver.find_ids('content_editor')[0].clear()
        time.sleep(2)
        self.driver.find_ids_send('content_editor',0,"台词修改")
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)
        tip = self.driver.find_id_text('txtContent')
        tip_check = '修改台词将移除当前的配音进度'
        assert tip == tip_check
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        try:
            self.driver.find_id('roleall')
            self.driver.find_id_click('roleall')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.hide_keyboard()
        content = self.driver.find_ids_text('content_editor',0)
        content_check = '台词修改'
        assert content_check in content
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)

    # 修改首句台词后不保存返回配音界面再进，查看台词首句显示
    def test_k_dub_script_edit_nosave(self):
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.hide_keyboard()
        self.driver.find_ids_send('content_editor',0,'台词修改')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        tip = self.driver.find_id_text('txtContent')
        tip_check = '真的要放弃本次台词编辑吗？'
        assert tip_check in tip
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(3)

    # 切换系统默认台词
    def test_l_dub_script_default(self):
        self.driver.find_id_click('scirpt')
        self.driver.wait_id_click('titletextView')
        time.sleep(3)
        try:
            self.driver.find_id('roleall')
            self.driver.find_id_click('roleall')
        except:
            pass
        time.sleep(2)

    # 清空字幕所有内容
    def test_m_dub_script_clearall(self):
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.driver.hide_keyboard()
        time.sleep(2)
        for i in range(2):
            subtitles = self.driver.find_ids('content_editor')
            for y in range(len(subtitles)):
                self.driver.find_ids('content_editor')[y].clear()
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id_click('complete')
        toast = self.driver.wait_toast('//android.widget.Toast')
        toast_check = '台词不能为空，请输入至少一句台词'
        assert toast == toast_check
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)

    # 编辑台词输入特殊符号后保存
    def test_n_dub_script_special_char(self):
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.hide_keyboard()
        self.driver.find_id_clear('content_editor')
        time.sleep(2)
        self.driver.find_id_send('content_editor','∯∰∱∲∳')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(3)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        try:
            self.driver.find_id('roleall')
            self.driver.find_id_click('roleall')
        except:
            pass
        time.sleep(2)

    #单行台词输入超过30个字符
    def test_o_dub_script_char_lenth(self):
        self.driver.find_id_click('edit_subtitle')
        time.sleep(2)
        self.driver.hide_keyboard()
        self.driver.find_id_clear('content_editor')
        time.sleep(2)
        self.driver.find_id_send('content_editor','123456789012345678901234567890123456789')
        tip = self.driver.wait_toast('//android.widget.Toast')
        check = '单行台词不能超过30个字符'
        assert tip in check
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('edit_subtitle')

    #耳返开关
    def test_p_dub_earreturn(self):
        self.driver.find_id_click('earreturn')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '耳返'
            assert check in toast
        except:
            print('点击耳返开关未弹出toast提示')
        time.sleep(2)

    # 配音界面点击预览原声视频
    def test_q_dub_video_play(self):
        self.driver.find_id_click('play')
        try:
            self.driver.find_id('video_time')
        except:
            print('未发现配音视频播放时间进度')
        self.driver.wait_download('play')

    # 播放过程中暂停
    def test_r_dub_video_pause(self):
        self.driver.find_id_click('play')
        self.driver.find_id_click('fl_video')
        # self.driver.Background()
        self.driver.wait_download('play')
        time.sleep(2)

    # 播放过程中推到后台
    def test_s_dub_video_background(self):
        self.driver.find_id_click('play')
        self.driver.Background()
        self.driver.wait_id('play')
        time.sleep(2)

    # 录音权限
    def test_t_dub_record_permissions(self):
        self.driver.find_id_click('action')
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('next')
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            self.driver.wait_download('title')
            self.driver.Background()
            self.driver.find_id_click('back')
            time.sleep(2)
        time.sleep(2)

    # 手动点击提交进入配音预览界面
    def test_u_dub_manual_into_preview(self):
        self.driver.find_id_click('complete')
        self.driver.wait_download('title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    # 在完整录制后的基础上点击原声试听，查看视频播放是否从头开始播放
    def test_v_dub_video_play_time(self):
        time1 = datetime.datetime.now()
        self.driver.find_id_click('play')
        self.driver.wait_download('play')
        time2 = datetime.datetime.now()
        time_result = time2 - time1
        time_video = self.driver.find_id_text('video_time')
        print('视频时间：', time_video, '实际播放时间：', time_result)
        time.sleep(2)

    # 配音试听
    def test_w_dub_video_review(self):
        self.driver.find_id_click('review')
        self.driver.wait_download('play')
        time.sleep(2)

    # 试听过程中点击提交进入预览界面
    def test_x_dub_review_into_preview(self):
        self.driver.find_id_click('review')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('complete')
        self.driver.wait_id('title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    # 试听过程中，点击退出配音界面
    def test_y_dub_video_review_quit(self):
        self.driver.find_id_click('review')
        self.driver.back()
        time.sleep(2)
        tip = self.driver.find_id_text('txtContent')
        tip_check = '确定放弃吗？'
        assert tip == tip_check, "退出配音界面弹窗提示文案错误"
        self.driver.find_id_click('btnCancel')
        time.sleep(2)

    # 点击回撤按钮
    def test_z_dub_video_withdraw(self):
        while True:
            try:
                self.driver.find_id('withdraw')
                self.driver.find_id_click('withdraw')
            except:
                break
        time.sleep(2)

    # 录制过程中暂停
    def test_z_a_dub_record_pause(self):
        self.driver.find_id_click('action')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id('dubbingWaveform')
        except:
            print('没有显示音轨，未录制进人声')
        time.sleep(2)

    # 录制完成后自动跳转再返回配音界面
    def test_z_b_preview_back_dubbing(self):
        self.driver.find_id_click('action')
        self.driver.wait_download('title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    # 手动拖音轨
    def test_z_c_dub_audio_track_move(self):
        self.loc.dub_track()

    # 重新录制
    def test_z_d_dub_restart_record_dubbing(self):
        self.driver.find_id_click('review')
        self.driver.wait_id('play')
        self.driver.find_id_click('action')
        self.driver.wait_download('title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(4)

    # 长按回撤按钮
    def test_z_e_dub_long_withdraw(self):
        self.driver.Long_Touche('withdraw', 3000)
        time.sleep(2)

    #点击配音进入预览界面
    def test_z_f_dub_into_preview(self):
        self.driver.find_id_click('action')
        self.driver.wait_download('title')
        self.driver.Background()
        time.sleep(2)

    # 播放完整的视频
    def test_z_g_preview_video_play(self):
        self.driver.find_id_click('play_button')
        time.sleep(3)
        self.driver.Background()
        time.sleep(2)
        self.driver.wait_download('play_button')
        time.sleep(2)

    # 字幕开关
    def test_z_h_preview_subtitle_onoff(self):
        el = self.driver.find_id_state('add_subtitle_cb')
        self.driver.find_id_click('add_subtitle_cb')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('complete')
        self.driver.wait_id('title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id_state('add_subtitle_cb')
        if el != el1:
            print('字幕开关状态显示错误，未显示默认状态')
        time.sleep(2)
    #降噪开关
    def test_z_i_preview_voice_onoff(self):
        el = self.driver.find_id_state('clear_voice')
        self.driver.find_id_click('clear_voice')
        time.sleep(4)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('complete')
        self.driver.wait_id('title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id_state('clear_voice')
        assert el != el1,'降噪开关状态校验失败'
        self.driver.find_id_click('clear_voice')
        self.driver.Background()
        time.sleep(2)

    # 预览界面人声
    def test_z_j_preview_voice_volume(self):
        #调节人声音量
        self.loc.voice_increase()
        time.sleep(2)
        self.loc.voice_reduce()
        time.sleep(4)

    # 声音校准
    def test_z_k_preview_voice_calibration(self):
        self.driver.find_id_click('trim')
        time.sleep(2)
        self.loc.voice_increase()
        self.driver.Background()
        time.sleep(2)
        self.loc.voice_reduce()
        self.driver.Background()
        time.sleep(2)

    # 人声变声调节
    def test_z_l_preview_voice_changer(self):
        self.driver.find_id_click('pitch')
        time.sleep(2)
        self.loc.voice_increase()
        self.driver.Background()
        time.sleep(2)
        self.loc.voice_reduce()
        self.driver.Background()
        time.sleep(2)

    #人声混响调节
    def test_z_m_preview_reverberation(self):
        self.driver.find_id_click('fx')
        time.sleep(2)
        self.loc.voice_reverberation_increase()
        self.driver.find_id_click('play_button')
        self.driver.Background()
        time.sleep(2)
        self.loc.voice_reverberation_reduce()
        self.driver.find_id_click('play_button')
        self.driver.Background()
        time.sleep(2)

    # 背景音音量调节
    def test_z_n_preview_background_music(self):
        self.loc.back_music_increase()
        self.driver.find_id_click('play_button')
        self.driver.Background()
        time.sleep(2)
        self.loc.back_music_reduce()
        time.sleep(2)
        self.loc.back_music_increase()
        time.sleep(2)

    #关闭背景音音量
    def test_z_o_preview_close_background_music(self):
        self.driver.find_id_click('voice_open')
        el = self.driver.find_id_state('voice_open')
        if el != 'true':
            print ('状态点击背景音关闭按钮后，状态没有显示关闭')
        self.driver.find_id_click('play_button')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)

    # 背景音音乐列表中选择其它音乐
    def test_z_p_preview_change_music(self):
        count = self.driver.find_id_text('tvBgCount')
        if int(count) > 1:
            self.driver.find_id_click('imgBgCount')
            time.sleep(4)
            if self.y == 1920:
                self.driver.tap(self.x*0.5,self.y*0.469)
            elif self.y > 2250:
                self.driver.tap(self.x*0.5,self.y*0.464)
            else:
                pass
        time.sleep(4)

    # 背景音混响调节
    def test_z_q_preview_background_reverberation(self):
        self.driver.find_id_click('bgfx')
        time.sleep(2)
        el = self.driver.find_id_state('bgfx')
        if el != 'true':
            print('状态点击背景音混响按钮后，状态没有显示选中')
        time.sleep(2)
        self.loc.back_music_reverberation_increase()
        self.driver.find_id_click('play_button')
        self.driver.wait_download('play_button')
        time.sleep(2)
        self.loc.back_music_reverberation_reduce()
        time.sleep(2)

    # 下载系统推荐背景音音乐
    def test_z_r_preview_download_music(self):
        self.driver.find_id_click('bgvol')
        time.sleep(2)
        self.driver.find_id_click('imgBgCount')
        time.sleep(2)
        self.loc.one_from_last()
        self.driver.wait_id('btnRight')
        while True:
            try:
                self.driver.find_id('btnDownload')
                self.driver.find_id_click('btnDownload')
            except:
                break

    # 随机选中背景音音乐
    def test_z_s_preview_select_music(self):
        count = self.driver.find_ids('title')
        select = random.randint(0,len(count)-1)
        self.driver.find_ids_click('title',select)
        time.sleep(2)
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.driver.find_id_click('play_button')
        self.driver.wait_download('play_button')
        time.sleep(2)

        #选中音乐后进入音乐试听界面，拖动视频进度条
        el = 'video_seekbar'
        if self.y == 1920:
            self.driver.tap_el(el)
        elif self.y > 2250:
            self.driver.tap_el(el)
        time.sleep(2)
        el = self.driver.find_id('waveformview').rect
        el_x = int(el['x'] + el['width'] / 2.0)
        el_y = int(el['y'] + el['height'] / 2.0)
        if self.y == 1920:
            self.driver.swip_move(el_x, el_y,el_x - 300, el_y)
        elif self.y > 2250:
            self.driver.swip_move(el_x, el_y,el_x - 300, el_y)
        time.sleep(2)
        self.driver.find_id_click('play_button')
        self.driver.wait_download('play_button')
        time.sleep(2)
        self.driver.find_id_click('complete')
        self.driver.wait_id('clear_voice')
        time.sleep(2)

    # 上滑加载背景音音乐列表
    def test_z_t_preview_load_music_list(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    #预览界面点击完成
    def test_z_u_preview_into_upload(self):
        self.driver.find_xpath('完成').click()
        self.driver.wait_id('txtTitle')
        time.sleep(2)

    #修改作品封面-视频截图
    def test_z_v_upload_work_cover_screenshots(self):
        self.driver.find_id_click('btn_setting_cover_tip')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        el = 'seekbar'
        self.driver.tap_el(el)
        time.sleep(4)
        self.driver.find_id_click('complete')
        time.sleep(2)

    #修改作品封面-拍照
    def test_z_w_dubbing_work_cover_photo(self):
        self.driver.find_id_click('btn_setting_cover_tip')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(5)
        try:
            # 米5
            self.driver.find_id('com.android.camera:id/v9_camera_picker')
            self.driver.find_id_third_part('com.android.camera:id/v9_camera_picker')
            time.sleep(5)
            self.driver.find_id_third_part('com.android.camera:id/inten_done_apply')
            time.sleep(4)
        except:
            try:
                # vivox21、vivox9

                self.driver.find_id_third_part('com.android.camera:id/shutter_button')
                time.sleep(4)
                self.driver.find_id_third_part('com.android.camera:id/done_button')
                time.sleep(4)
            except:
                try:

                    self.driver.find_id_third_part('com.huawei.camera:id/shutter_button')
                    time.sleep(4)
                    self.driver.find_id_third_part('com.huawei.camera:id/done_button')
                    time.sleep(4)
                except:
                    try:
                        self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                        time.sleep(4)
                        self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                    except:
                        pass
        self.driver.find_id_click('confirm')
        time.sleep(3)

    # 修改作品封面——相册
    def test_z_x_dubbing_work_cover_album(self):
        self.driver.find_id_click('btn_setting_cover_tip')
        time.sleep(3)
        self.loc.two_from_last()
        time.sleep(2)
        photo_count = self.driver.find_ids('photo_wall_item_photo')
        select = random.randint(0, len(photo_count) - 1)
        self.driver.find_ids_click('photo_wall_item_photo',select)
        try:
            self.driver.wait_toast('//android.widget.Toast')
            select = random.randint(0, len(photo_count) - 1)
            self.driver.find_ids_click('photo_wall_item_photo',select)
        except:
            pass
        self.driver.find_id_click('confirm')
        time.sleep(4)

    # 标题名称-输入30个字符
    def test_z_y_upload_title(self):
        self.driver.find_id_send('title','123456789012345678901234567890')
        time.sleep(2)
        char = self.driver.find_id_text('title')
        char_check = '123456789012345678901234567890'
        assert char == char_check
        time.sleep(2)

    # 标题名称-清空标题
    def test_z_z_upload_title_clear(self):
        self.driver.find_id_clear('title')
        num = self.driver.find_id_text('title_count')
        check = '0/30'
        assert num == check
        time.sleep(2)

    # 上传界面标签显示检查
    def test_z_z_a_upload_channel_select(self):
        try:
            self.driver.find_xpath('添加')
        except:
            self.driver.find_id_click('tv1')
        time.sleep(2)
        self.driver.find_xpath('添加').click()
        self.driver.wait_id('edit_text')
        time.sleep(2)
        try:
            self.driver.find_id('tv')
        except:
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_xpath('添加').click()
            self.driver.wait_id('edit_text')
        time.sleep(2)
        try:
            self.driver.find_id('tv1')
            self.driver.find_id_click('tv1')
            time.sleep(2)
            hot_lable = self.driver.find_ids('tv')
            select = random.randint(0, len(hot_lable))
            self.driver.find_ids_click('tv',select)
            time.sleep(2)
            label_name = self.driver.find_id_text('tv1')
            self.driver.find_id_click('tv_right')
            time.sleep(2)
            label_check = self.driver.find_id_text('tv1')
            assert label_name == label_check,'标签对比不一致，%s,%s' % (label_name, label_check)
            time.sleep(2)
        except:
            self.driver.find_id_click('btnBack')
        time.sleep(2)

    #上传界面设置私密
    def test_z_z_a_b_upload_privacy(self):
        try:
            self.driver.find_id('tv1')
            self.driver.find_id_click('pri_switch_tv')
            time.sleep(2)
            try:
                self.driver.find_id('private_top_tv2')
            except:
                print('点击私密后未显示私密提示文案')
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 上传界面-求合作开关
    def test_z_z_a_c_dubbing_coor_switch(self):
        try:
            self.driver.find_id_click('check_box_add_square')
            state = self.driver.find_id_state('check_box_add_square')
            if state:
                self.driver.find_id_click('check_box_add_square')
                time.sleep(2)
            else:
                pass
        except:
            pass
        time.sleep(2)

    # 作品上传按钮
    def test_z_z_a_d_upload(self):
        self.driver.find_id_click('uploadbtn')

    # 上传结果
    def test_z_z_a_e_upload_result(self):
        while True:
            try:
                self.driver.find_id('wx')
                return true
            except:
                try:
                    self.driver.find_id('re_update')
                    return false
                except:
                    pass

    #上传成功后点击查看视频详情
    def test_z_z_a_f_upload_video_detail(self):
        if self.test_z_z_a_e_upload_result() == true:
            #点击查看视频详情
            self.driver.find_id_click('img_url')
            self.driver.wait_id('tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)

            #微信分享
            self.driver.find_id_click('wx')
            time.sleep(2)
            self.driver.wait_id_three_party('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id_third_part('com.tencent.mm:id/dn')
            self.driver.wait_id('close')
            time.sleep(2)

            #朋友圈分享
            self.driver.find_id_click('wxf')
            self.driver.wait_id_three_party('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id_third_part('com.tencent.mm:id/dn')
            self.driver.wait_id('close')
            time.sleep(2)

            #qq分享
            self.driver.find_id_click('qq')
            self.driver.wait_id_three_party('com.tencent.mobileqq:id/ivtitlebtnRighttext')
            time.sleep(2)
            self.driver.find_id_third_part('com.tencent.mobileqq:id/ivtitlebtnleftbutton')
            time.sleep(2)

            #qq空间分享
            self.driver.find_id_click('qqz')
            self.driver.wait_id_three_party('com.tencent.mobileqq:id/ivtitlebtnRighttext')
            time.sleep(2)
            self.driver.find_id_third_part('com.tencent.mobileqq:id/ivtitlebtnleft')
            time.sleep(2)

            # 视频下载
            self.loc.upload_share_swipe()
            time.sleep(2)
            self.driver.find_id_click('down')
            time.sleep(2)
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id('btnSubmit')
                self.driver.find_id_click('btnSubmit')
            except:
                self.driver.wait_id('btnSubmit')
                self.driver.find_id_click('btnSubmit')
            time.sleep(2)

            #上传成功进入视频详情删除视频
            self.driver.find_id_click('img_url')
            self.driver.wait_id('btnBack')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('setting')
            time.sleep(2)
            self.loc.two_from_last()
            time.sleep(2)
            tip = self.driver.find_id_text('txtContent')
            check = '删除作品'
            assert check in tip,'作品删除提示内容校验不一致'
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
        #上传失败保存草稿箱
        elif self.test_z_z_a_e_upload_result() == false:
            self.driver.find_id_click('saveToDraft')
            time.sleep(3)
            self.driver.find_xpath('保存草稿').click()
            self.driver.wait_id_click('btnSubmit')
            time.sleep(2)
            #上传失败查看失败原因
            self.driver.find_id_click('re_update')
            self.driver.find_id_click('rl_bg')
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                print('上传失败的情况下，点击作品封面：', toast)
            except:
                pass
            time.sleep(2)
            reason = self.driver.find_id_text('re_update')
            reason_state1 = '修改标题'
            reason_state2 = '重新上传'
            if reason == reason_state1:
                self.driver.find_id_click('re_update')
                time.sleep(2)
                self.driver.find_id_clear('edit')
                time.sleep(2)
                self.driver.find_id_send('edit','标题修改')
                self.driver.find_id_click('btnSubmit')
                time.sleep(2)
                try:
                    self.driver.wait_id('wx')
                except:
                    print('修改标题后重新上传失败')
            elif reason_state2 == reason_state2:
                self.driver.find_id_click('re_update')
                try:
                    self.driver.wait_id('wx')
                except:
                    print('点击重新上传按钮后，作品依然上传失败')
            else:
                print('未知错误')
            time.sleep(2)

class follow(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    #首页关注主界面
    def test_a_follow_jump(self):
        self.driver.find_id_click('ivCirclesTab')
        self.driver.wait_id('musicPlayView')
        time.sleep(2)

    #语聊推荐列表
    def test_b_follow_chat_list(self):
        self.driver.find_id_click('musicPlayView')
        self.driver.wait_id_click('item_theme_image')
        self.driver.wait_download('user_list')
        self.driver.find_id_click('home_close')
        time.sleep(2)
        self.driver.find_id_click('item_theme_image')
        time.sleep(2)

    #首页关注列表进入个人空间
    def test_c_follow_person_zoom(self):
        name = self.driver.find_id_text('textView')
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_follow')
        name = self.driver.find_id_text('username')
        assert name == name

    #切换分类
    def test_d_follow_switch_classification(self):
        #作品tab
        self.driver.find_id_click('tv_film')
        time.sleep(2)
        try:
            self.driver.find_id('userhead')
        except:
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_fan')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('content')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('play')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)

        # 朋友圈
        self.loc.share_pyq()
        self.driver.wait_xpath('发表')
        self.driver.find_id_third_part('com.tencent.mm:id/dn')
        time.sleep(3)

        # qq空间
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)
        self.loc.share_qq_zone()
        self.driver.wait_xpath('发表')
        self.driver.find_id_third_part('com.tencent.mobileqq:id/ivtitlebtnleft')
        time.sleep(3)

        # 点击新浪
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)
        self.loc.share_sina()
        self.driver.wait_xpath('发送')
        time.sleep(2)
        self.driver.find_id_third_part('com.sina.weibo:id/titleBack')
        time.sleep(2)
        try:
            self.driver.find_xpath('不保存')
            self.driver.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        # 点击私信
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)
        self.loc.share_message_friend()
        self.driver.wait_id_click('filter_edit')
        time.sleep(2)
        self.driver.find_id_send('filter_edit',"15697802")
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        try:
            self.driver.wait_id('userhead')
            name = self.driver.find_id_click('name').text
            name2 = '米爱'
            if name == name2:
                self.driver.find_id_click('name')
                self.driver.wait_id('right_icon1')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            else:
                print("未搜索到指定用户")
                time.sleep(2)
                self.driver.find_id_click('btnBack')
        except:
            self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 点击下载视频到本地
        self.driver.find_id_click('item_attention_share_num')
        self.loc.share_download()
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
                self.driver.wait_id_click('btnSubmit')
            except:
                try:
                    self.driver.wait_id_click('btnSubmit')
                except:
                    pass

        # 点击复制链接
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)
        self.loc.share_copy_link()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.wait_id('txtContent')
                time.sleep(2)
                self.driver.find_id_click('btnSubmit')
            except:
                pass
        time.sleep(2)

        # 点击转发
        self.driver.find_id_click('item_attention_share_num')
        time.sleep(2)
        self.loc.share_forward()
        time.sleep(2)
        try:
            self.driver.find_id('reprint')
            self.driver.find_id_send('content',"不错，转发了！")
            time.sleep(2)
            self.driver.find_id_click('reprint')
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                try:
                    self.driver.find_id('reprint')
                    self.driver.find_id_click('reprint')
                    self.driver.wait_toast('//android.widget.Toast')
                except exception as e:
                    print(e)
        except:
            # 点击取消分享弹窗按钮
            self.loc.one_from_last()
        time.sleep(2)
        # 关注界面点赞
        while True:
            try:
                self.driver.find_id('item_attention_pprint()')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        num = self.driver.find_id_text('item_attention_pprint()')
        self.driver.find_id_click('item_attention_pprint()')
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            pass
        new_num = self.driver.find_id_text('item_attention_pprint()')
        assert num == new_num
        time.sleep(2)

        # 关注界面评论作品
        while True:
            try:
                self.driver.find_id('item_attention_comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('item_attention_comment_count')
        time.sleep(2)
        self.driver.find_id_send('editContent','日常评论下！^.^')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast,'关注界面发送评论提示校验不一致'
        except:
            print('未检测到评论发送toast提示')
        time.sleep(2)

        #帖子tab
        self.driver.find_id_click('tv_tiezi')
        time.sleep(3)
        # 设置关注区权限
        self.driver.find_id_click('more')
        time.sleep(2)
        self.loc.five_from_last()
        time.sleep(2)
        self.driver.find_id_click('check')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id_click('check')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 特别关注
        for i in range(2):
            self.driver.find_id_click('more')
            time.sleep(2)
            self.loc.four_from_last()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败'+toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)

        #转发私信
        self.driver.find_id_click('more')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(2)
        self.driver.find_id_click('group_chat')
        self.driver.wait_id_click('userhead')
        self.driver.wait_id('editContent')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #帖子举报
        self.driver.find_id_click('more')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('tv_action_other')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','举报功能测试！')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '举报成功'
            if toast != check:
                print(toast)
                self.driver.find_id_click('btnBack')
        except:
            print('未检测到举报toast提示')
        time.sleep(2)
        self.driver.find_id_click('tag')
        self.driver.wait_id('img_subscribe')
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('content')
        self.driver.wait_id('right_icon1')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        try:
            self.driver.find_id('img1')
            self.driver.find_id_click('img1')
            time.sleep(2)
            self.driver.back()
        except:
            try:
                self.driver.find_id('play')
                self.driver.find_id_click('play')
                time.sleep(2)
            except:
                try:
                    self.driver.find_id('playBtn')
                    self.driver.find_id_click('playBtn')
                    self.driver.wait_id('tv_video_detail_title')
                    self.driver.back()
                except:
                    pass
        time.sleep(2)

        #素材tab
        self.driver.find_id_click('tv_source')
        time.sleep(3)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_fan')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('more')
        time.sleep(2)
        #设置关注区权限
        self.loc.three_from_last()
        time.sleep(2)
        self.driver.find_id_click('check')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id_click('check')
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        #设置特别关注
        for i in range(2):
            self.driver.find_id_click('more')
            time.sleep(2)
            self.loc.two_from_last()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败' + toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)


        self.driver.find_id_click('content')
        self.driver.wait_id('right_icon1')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #点击素材标签
        self.driver.find_id_click('tv_source_from')
        self.driver.wait_id('right_icon1')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        try:
            self.driver.find_id('tv_source_right')
            self.driver.find_id_click('tv_source_right')
            self.driver.wait_id('right_icon1')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass
        #点击素材配音按钮
        self.driver.find_id_click('action')
        while True:
            try:
                self.driver.find_id('btnSubmit')
                self.driver.find_id_click('btnSubmit')
                try:
                    self.driver.find_id('roleall')
                    self.driver.find_id_click('roleall')
                except:
                    pass
                break
            except:
                try:
                    self.driver.find_id('roleall')
                    self.driver.find_id_click('roleall')
                    break
                except:
                    pass
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)

        #特别关注
        self.driver.find_id_click('tv_attention')
        time.sleep(2)
        for i in range(2):
            self.driver.find_id_click('more')
            time.sleep(2)
            self.loc.two_from_last()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '特别关注toast提示检验失败' + toast
            except:
                print('未检测到特别关注toast提示')
            time.sleep(2)

    def test_e_follow_up_refresh(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)

class live(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    def test_a_live_list(self):
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                self.loc.home_func()

        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        self.driver.find_id_click('create')

    #进入语聊间
    def test_b_live_into_live_detail(self):
        self.driver.find_id_click('fram')
        self.driver.wait_id('gift_value')

    #切换语聊间
    def test_c_live_switch_live(self):
        for i in range(3):
            self.driver.swip_left()
            self.driver.wait_id('gift_value')
            time.sleep(2)

    #语聊间创建界面编辑
    def test_d_livecreate_live_edit(self):
        self.driver.find_id_click('create')
        time.sleep(2)
        self.driver.find_id_click('img')
        time.sleep(2)
        self.driver.find_id_click('tv_photo')
        time.sleep(2)
        self.driver.find_id_click('photo_wall_item_photo')
        time.sleep(2)
        self.driver.find_id_click('confirm')
        time.sleep(2)
        self.driver.find_id_click('title')
        time.sleep(2)
        self.driver.find_id_send('title','空')
        time.sleep(2)
        self.driver.find_id_click('tag_name')
        time.sleep(2)
        self.driver.find_id_click('tv')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.find_id_click('right')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #创建进入语聊间
    def test_e_livecreate_room(self):
        self.driver.find_id_click('create')
        time.sleep(2)
        self.driver.find_id_click('check_box')
        self.driver.find_id_click('start_live')
        time.sleep(2)
        self.driver.find_id_click('btnCancel')
        self.driver.wait_id('name')

    #闭麦
    def test_f_live_close_mic(self):
        try:
            self.driver.find_id('mic_tag')
        except:
            self.driver.find_id_click('home_microphone1')
            time.sleep(2)
            self.driver.find_id_click('mic_own_control')
            self.driver.wait_id_click('mic_tag')
        time.sleep(2)

    #开麦
    def test_g_live_open_mic(self):
        try:
            self.driver.find_id('mic_tag')
            self.driver.find_id_click('home_microphone1')
            time.sleep(2)
            self.driver.find_id_click('mic_own_control')
            self.driver.wait_not_id('mic_tag')
            self.driver.find_id_click('name')
        except:
            pass
        time.sleep(2)

    #查看头像简介
    def test_h_live_head_introduction(self):
        self.driver.Long_Touche('userhead', 3000)
        try:
            self.driver.find_id('user_id')
            self.driver.find_id_click('icon_close')
        except:
            print('长按麦位用户头像未显示简介弹窗')
        time.sleep(2)

    #送礼
    def test_i_live_gift(self):
        self.driver.find_id_click('userhead')
        self.driver.wait_id('gift_img')
        time.sleep(2)
        self.driver.find_xpath('鲜花').click()
        self.driver.find_id_click('right_view')
        time.sleep(2)
        self.driver.find_id_click('right_view')
        time.sleep(2)
        self.driver.find_id_click('confirm')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    #点赞
    def test_j_live_good(self):
        self.driver.find_id_click('periscope_view')
        time.sleep(2)

    #语聊间发送评论
    def test_k_live_comments(self):
        self.driver.find_id_click('function_comment_layout')
        time.sleep(2)
        self.driver.find_id_send('editContent', '这是一个语聊间！')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.wait_id('home_comment_comments')
        self.driver.find_id_click('name')
        time.sleep(2)

    #长按用户名@用户
    def test_l_live_at(self):
        self.driver.Long_Touche('username', 3000)
        try:
            self.driver.find_id_click('editContent')
            content = self.driver.find_id_text('editContent')
            check = '@'
            assert check in content
            time.sleep(1)
            self.driver.find_id_click('btn_send')
            self.driver.wait_id('home_comment_comments')
            self.driver.find_id_click('name')
        except:
            print('长按用户名未出现@')
        time.sleep(2)

    #发红包
    def test_m_live_red(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_red()
        time.sleep(2)
        self.driver.find_id_send('cash_num','0.1')
        time.sleep(1)
        self.driver.find_id_send('people_num','1')
        time.sleep(2)
        self.driver.find_id_click('generate_red_packet')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('rl_red')
        time.sleep(2)
        self.driver.find_id_click('tv_more')
        self.driver.wait_id_click('open_red_packet_btn')
        self.driver.wait_id('diamond')
        self.driver.back()
        time.sleep(2)

    #语聊间分享
    def test_n_live_share(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_share()
        time.sleep(2)
        #私信
        self.loc.chat_share_message_friend()
        self.driver.wait_id('group_chat')
        self.driver.find_id_click('btnBack')
        time.sleep(3)

    #语聊间私信
    def test_o_live_persion_notice(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_message_friend()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #语聊间黑名单
    def test_p_live_blacklist(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_blacklist()
        time.sleep(2)
        self.driver.find_id_click('btn_close')
        time.sleep(2)

    #设置房管
    def test_q_live_manager(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_manager()
        time.sleep(2)
        self.driver.find_id_click('btn_close')
        time.sleep(2)

    #随机抽选游戏
    def test_r_live_games(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_games()
        time.sleep(2)
        self.driver.find_id_click('btn_close')
        time.sleep(2)
        self.driver.find_id_click('tv_turntable')
        time.sleep(2)
        self.driver.find_id_click('customize_back')
        time.sleep(2)
        self.driver.find_id_click('tv_random')
        time.sleep(2)
        self.driver.find_id_click('random_close')
        time.sleep(2)

    #麦位数量
    def test_s_live_mic_count(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_mic_num()
        time.sleep(2)
        self.driver.find_id_click('check2')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)

    #pia戏
    def test_t_live_pia(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_pia()
        time.sleep(2)
        self.driver.find_id_click('iv_close')
        time.sleep(2)

    #组cp
    def test_u_live_cp(self):
        self.driver.find_id_click('function_more')
        time.sleep(2)
        self.loc.chat_cp()
        time.sleep(2)
        self.driver.find_id_click('tv_check')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.find_id_click('name')
        time.sleep(2)

    #公告
    def test_v_live_notice(self):
        self.driver.find_id_click('marquee')
        time.sleep(2)
        self.driver.find_id_click('btn_sure')
        time.sleep(2)
        self.driver.find_id_send('et_title','哈哈')
        time.sleep(2)
        self.driver.find_id_send('et_content','哈哈')
        time.sleep(2)
        self.driver.find_id_click('tv_save')
        time.sleep(2)

    #房间成员列表
    def test_w_live_members(self):
        try:
            self.driver.find_id_click('pack_up')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('count')
        time.sleep(2)
        self.driver.find_id_click('room_user')
        time.sleep(2)
        self.driver.find_id_click('fast_room_check')
        time.sleep(2)
        self.driver.find_id_click('action')
        time.sleep(2)
        self.driver.wait_xpath('移除')
        self.driver.find_xpath('申请').click()
        time.sleep(2)
        self.driver.find_id_click('fast_room_check')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.find_id_click('close')
        time.sleep(2)

    #房间详情
    def test_x_live_room_detail(self):
        self.driver.find_id_click('user_list')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)

    #房间背景音音乐
    def test_y_live_music(self):
        self.driver.find_id_click('function_joke_articles')
        time.sleep(2)
        try:
            self.driver.find_id('title')
        except:
            self.driver.find_id_click('add_music')
            time.sleep(2)
            self.driver.find_id_click('rl')
            time.sleep(2)
            self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('play')
        time.sleep(2)
        self.driver.find_id_click('next')
        time.sleep(2)
        self.driver.find_id_click('previous')
        time.sleep(2)
        self.driver.find_id_click('change')
        time.sleep(2)
        self.driver.find_id_click('modify')
        time.sleep(2)
        self.driver.find_id_click('music_list')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('name')
        time.sleep(2)

    #语聊任务
    def test_z_live_tasks(self):
        self.driver.find_id_click('img')
        time.sleep(2)
        self.driver.find_id_click('name')
        time.sleep(2)


    #退出语聊间
    def test_z_a_live_room_exit(self):
        self.driver.find_id_click('home_close')
        time.sleep(2)
        try:
            self.driver.find_id('outlive')
            self.driver.find_id_click('outlive')
        except:
            pass
        time.sleep(2)

class material(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass


    #进入素材库
    def test_a_source_into_list(self):
        self.driver.find_id_click('btn_more')
        self.driver.wait_id('coor')

    # 素材库搜索素材
    def test_b_source_searchs(self):
        self.driver.wait_id('tv_search')
        self.driver.find_id_click('tv_search')
        time.sleep(4)

        #点击热门素材标签
        tv_name = self.driver.find_ids('tv')
        time.sleep(2)
        for i in range(len(tv_name)):
            self.driver.find_ids_click('tv',i)
            self.driver.wait_id('rl_left2')
            self.driver.find_id_click('btnClear')
            time.sleep(2)

        # 历史搜索记录
        try:
            self.driver.find_id('item')
            self.driver.wait_id('iv_source')
            time.sleep(2)
            self.driver.find_id_click('btnClear')
            time.sleep(2)
        except:
            print('未显示有历史搜索记录')
        time.sleep(2)
        # 清空搜索记录
        self.driver.find_id_click('clear')
        time.sleep(2)

        # 推荐搜索-更多热点
        self.driver.find_id_click('tv1')
        self.driver.wait_id_click('rank_name')
        try:
            self.driver.wait_id('iv_source')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            print('素材标签详情界面未显示素材信息')

        # 上滑加载标签列表
        while True:
            self.driver.swip_up()
            time.sleep(2)
            label_name = self.driver.find_ids_text('rank_name',-1)
            self.driver.swip_up()
            label_name1 = self.driver.find_ids_text('rank_name',-1)
            if label_name == label_name1:
                self.driver.find_id_click('btnBack')
                break
            else:
                pass
        time.sleep(2)

    # 进入标签详情界面
    def test_c_source_tv_detail(self):
        self.driver.find_id_click('tv1')
        self.driver.wait_id('iv_source')
        time.sleep(2)
        # 依次点击切换标签，且点击标签后进入素材预览界面再返回
        label_touche = self.driver.find_ids('types_name')
        for i in range(len(label_touche) - 1, -1, -1):
            self.driver.find_ids_click('types_name',i)
            self.driver.wait_id('iv_source')
            try:
                self.driver.find_id('iv_source')
                self.driver.wait_id('userhead')
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            except:
                pass
        time.sleep(2)

        # 上滑加载素材搜索结果列表
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('btnClear')
        time.sleep(2)

    # 搜索素材
    def test_d_source_search(self):
        self.driver.find_id_send('txtKeyword','配音')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        self.driver.wait_id_click('iv_source')
        self.driver.wait_id('userhead')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        el = self.driver.find_ids('types_name')
        for i in reversed(el):
            self.driver.find_ids_click('types_name',i)
            time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 素材库主界面8个大分类
    def test_e_source_classification(self):
        tv_main = self.driver.find_ids('tv')
        for i in range(len(tv_main)):
            self.driver.find_ids_click('tv',i)
            self.driver.wait_id('iv_source')
            # 热门推荐标签
            tv_branch = self.driver.find_ids('tv')
            for x in range(len(tv_branch)):
                self.driver.find_ids_click('tv',x)
                self.driver.wait_id('img_url')
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            # 更多热门标签
            self.driver.find_id_click('tv1')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            screening = self.driver.find_ids('types_name')
            for j in range(len(screening) - 1, -1, -1):
                self.driver.find_ids_click('types_name',j)
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id_click('iv_source')
            self.driver.wait_id('userhead')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        time.sleep(2)

    # 合作广场-广场列表
    def test_f_source_coor(self):
        self.driver.find_id_click('rl_coor')
        self.driver.wait_id('item_sh_cooperate_article_image')
        self.driver.find_id_click('userhead')
        self.driver.wait_id('followcount')
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('item_sh_cooperate_article_image')
        self.driver.wait_download('play')
        time.sleep(2)
        self.driver.find_id_click('play')
        self.driver.wait_download('play')
        time.sleep(2)

        # 点击视频预览界面的合作按钮进入配音界面
        self.driver.find_id_click('btnCooperate')
        self.driver.wait_download('action')
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('item_sh_cooperate_article_image')

        # 点击广场列表中的配音按钮进入配音界面
        self.driver.find_id_click('btnCooperate')
        self.driver.wait_download('action')
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('item_sh_cooperate_article_image')
        time.sleep(2)

        # 获取广场中的求合作剩余时间
        try:
            self.driver.find_id('item_sh_clock_time')
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
            self.driver.find_id('top_img')
            self.driver.find_id_click('top_img')
            time.sleep(5)
        except:
            pass
        time.sleep(2)

    # 合作广场角色tab筛选项切换
    def test_g_source_role_change(self):
        self.driver.find_id_click('fq_male')
        time.sleep(2)
        self.driver.find_id_click('fq_female')
        time.sleep(2)
        self.driver.find_id_click('dp_male')
        time.sleep(2)
        self.driver.find_id_click('dp_female')
        time.sleep(2)

    # 合作广场-热门列表
    def test_h_source_coor_hot(self):
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        # 显示合作次数
        try:
            self.driver.find_id('count')
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
            self.driver.find_id('top_img')
            self.driver.find_id_click('top_img')
            time.sleep(5)
        except:
            pass
        time.sleep(2)


    # 合作广场-我的
    def test_i_my_coor(self):
        time.sleep(2)
        self.driver.find_xpath('我的').click()
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('followcount')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 合作广场-搜索
    def test_j_source_coor_search(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.find_id_send('et_search_keyword','配音')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        self.driver.wait_id_click('item_sh_cooperate_article_image')
        time.sleep(2)
        self.driver.wait_download('play')
        self.driver.find_id_click('btnCooperate')
        self.driver.wait_download('action')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id('item_sh_cooperate_article_image')
        # 滑动加载列表
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.find_id_send('et_search_keyword','槛花笼鹤')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        time.sleep(5)
        try:
            self.driver.find_xpath('没有搜索到任何内容')
        except:
            print('检查搜索无结果显示失败')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # # 声音鉴定
    # def test_z(self):
    #     self.driver.find_id_click()('sj')
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id_click()('reindetify')
    #         self.driver.find_id_click()('reindetify')
    #         time.sleep(2)
    #     except:
    #         pass
    #     self.driver.find_id_click()('boy')
    #     time.sleep(2)
    #     self.driver.find_id_click()('girl')
    #     time.sleep(2)
    #     content = self.driver.find_id_click()('text').text
    #     self.driver.find_id_click()('change')
    #     time.sleep(2)
    #     content_new = self.driver.find_id_click()('text').text
    #     assert content != content_new,'切换朗读的前后内容对比一致，切换失败'
    #     time.sleep(2)
    #
    # # 录音
    # def test_b(self):
    #     i = 1
    #     while   True:
    #         i = i + 1
    #         try:
    #             self.driver.find_id_click()('dubbing')
    #             time.sleep(15)
    #             self.driver.find_id_click()('dubbing')
    #             self.driver.wait_id('preview')
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
    #         self.driver.find_id_click()('play')
    #         return true
    #     except:
    #         return false
    #
    # # 声鉴报告界面
    # def test_c(self):
    #     state = test_c_voicetest().test_b_a()
    #     print(state)
    #     if state == true:
    #         voice_style = self.driver.find_id_click()('voice_type').text
    #         print(voice_style)
    #         time.sleep(2)
    #         self.driver.find_id_click()('play')
    #         self.driver.wait_download('play')
    #         time.sleep(2)
    #         self.driver.find_id_click()('title')
    #         self.driver.wait_id('userhead')
    #         self.driver.find_id_click()('btnBack')
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
    #     state = test_c_voicetest().test_b_a()
    #     if state == true:
    #         self.driver.find_id_click()('action')
    #         time.sleep(2)
    #         self.driver.wait_download('action')
    #         self.driver.find_id_click()('action')
    #         self.driver.wait_download('title')
    #         self.driver.Background()
    #         time.sleep(2)
    #         self.driver.find_id_click()('complete')
    #         self.driver.wait_id('txtTitle')
    #         time.sleep(2)
    #         self.driver.find_id_click()('pri_switch_tv')
    #         time.sleep(2)
    #         self.driver.find_id_click()('saveToDraft')
    #         time.sleep(2)
    #         self.driver.find_id_click()('btnSubmit')
    #         time.sleep(2)
    #         self.driver.wait_xpath('退出配音')
    #         self.driver.find_xpath('退出配音')
    #         time.sleep(2)
    #         for i in range(6):
    #             self.driver.swip_down()
    #             time.sleep(2)
    #         self.driver.find_id_click()('reindetify')
    #         time.sleep(2)
    #         # 返回素材库
    #         self.driver.find_id_click()('back')
    #         time.sleep(2)
    #     else:
    #         print('声鉴结果界面跳转失败，跳过此测试步骤')
    #         self.driver.back()

    '''素材列表'''
    def test_k_source_list(self):
        self.driver.find_id_click('unlimited')
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        for i in range(15):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id('top_img')
            self.driver.find_id_click('top_img')
        except:
            pass
        time.sleep(4)

    #素材列表预览模式
    def test_l_source_preview(self):
        try:
            self.driver.find_id('tv_title')
        except:
            self.driver.find_id_click('change_type')
        time.sleep(2)
        self.driver.swip_up()
        self.driver.find_id_click('bg_view')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('subtitleView')
        self.driver.wait_id('userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('change_type')
        time.sleep(2)

        # 点击进入素材预览界面
        self.driver.find_id_click('iv_source')
        self.driver.wait_id('userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 切换角色筛选项
        self.driver.find_id_click('boy')
        time.sleep(2)
        try:
            self.driver.find_id_click('tv_girl')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('coor')
        time.sleep(2)
        num = self.driver.find_ids('tv_source_from')
        for i in range(len(num)):
            try:
                self.driver.find_ids_click('tv_boy',i)
            except:
                name = self.driver.find_ids_text('tv_source_title',i)
                print("合作素材列表中未显示双人角色:%s" % name)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('unlimited')
        time.sleep(4)

    # 素材预览详情界面查看视频是否循环播放
    def test_m_source_detail(self):
        self.driver.find_id_click('iv_source')
        self.driver.wait_id('userhead')

        # 进入素材作者个人空间
        name1 = self.driver.find_id_text('user_name')
        self.driver.find_id_click('userhead')
        self.driver.wait_id('fanscount')
        name2 = self.driver.find_id_text('username')
        assert name1 in name2,'素材视频详情界面的用户名称与空间中的用户名称校验不一致'
        time.sleep(2)

    # 关注按钮
    def test_n_source_detail_follow(self):
        self.driver.find_id_click('btn_video_detail_follow')
        try:
            follow_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '关注成功'
            assert check in follow_toast, '关注toast内容校验不一致'
        except:
            try:
                self.driver.find_id('editContent')
                self.driver.find_id_click('btnBack')
            except:
                pass
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('fanscount')
        self.driver.find_id_click('follow_status')
        time.sleep(4)

    # 素材预览界面点击素材标签
    def test_o_source_detail_types(self):
        lable_name = self.driver.find_ids('types_name')
        for i in range(len(lable_name)):
            name = self.driver.find_ids_text('types_name',i)
            self.driver.find_ids_click('types_name',i)
            self.driver.wait_id('tag_name')
            name1 = self.driver.find_id_text('tag_name')
            assert name1 in name,'素材预览界面点击的标签与标签详情界面的标签校验不一致'
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        time.sleep(2)

    # 退出素材预览界面
    def test_p_source_detail_exit(self):
        try:
            self.driver.find_id('tag_name')
            self.driver.find_id_click('btnBack')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        self.driver.wait_id('iv_source')
        time.sleep(2)


    # 素材库界面素材上传按钮
    def test_q_source_upload(self):
        self.driver.find_id_click('upload')
        time.sleep(2)
        self.driver.wait_id('tv_upload')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

class person(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = BaseOperate()
        self.loc = location()
        self.x = touche_X()
        self.y = touche_Y()

    @classmethod
    def tearDownClass(self):
        pass


    # 退出当前界面
    def bcak(self):
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # # 首页进入“我的”界面
    # def test_a_person_my(self):
    #     self.driver.wait_id('ivMineTab')
    #     self.driver.find_id_click('ivMineTab')
    #     self.driver.wait_id('username')
    #     time.sleep(2)
    #
    # # 我的界面点击头像进入个人空间
    # def test_b_person_into_my_zoom(self):
    #     self.driver.find_id_click('userhead')
    #     self.driver.wait_id('followcount')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 我的界面点击关注进入关注列表
    # def test_c_person_home_into_follow(self):
    #     follow_count = self.driver.find_id_text('followed_count')
    #     time.sleep(1)
    #     self.driver.find_id_click('followed_count')
    #     self.driver.wait_id('filter_edit')
    #     time.sleep(2)
    #     if int(follow_count) > 9:
    #         self.driver.back()
    #     else:
    #         follow_count1 = self.driver.find_ids('username')
    #         assert int(len(follow_count1)) == int(follow_count)
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 我的界面点击粉丝进入粉丝列表
    # def test_d_person_home_into_fans(self):
    #     fan_count = self.driver.find_id_text('fans_count')
    #     time.sleep(1)
    #     self.driver.find_id_click('fans_count')
    #     self.driver.wait_id('vip_tag')
    #     time.sleep(2)
    #     if int(fan_count) < 8:
    #         fan_count1 = self.driver.find_ids('username')
    #         assert int(len(fan_count1)) == int(fan_count)
    #         time.sleep(2)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 用户id
    # def test_e_person_copy_id(self):
    #     self.driver.find_id_click('tv_uid')
    #     try:
    #         self.driver.wait_toast('//android.widget.Toast')
    #     except:
    #         pass
    #     time.sleep(2)
    #     self.driver.find_id_click('userhead')
    #     self.driver.wait_id('followcount')
    #     time.sleep(2)
    #
    # # 个人空间搜索-作品
    # def test_f_person_zoom_works_search(self):
    #     search_title = self.driver.find_id_text('title')
    #     time.sleep(2)
    #     self.driver.find_id_click('photo')
    #     time.sleep(2)
    #     self.driver.find_id_send('txtKeyword',search_title)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnSearch')
    #     self.driver.wait_id_click('filmBg')
    #     self.driver.wait_id('userhead')
    #     self.driver.Background()
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(4)
    #     self.driver.find_id_click('photo')
    #     self.driver.wait_id('txtKeyword')
    #     try:
    #         self.driver.find_id('clear')
    #         self.driver.find_id_click('clear')
    #         time.sleep(2)
    #         try:
    #             self.driver.find_id('clear')
    #             print('个人空间搜索作品后，点击清空搜索记录，依然显示有搜索记录')
    #         except:
    #             pass
    #     except:
    #         print('个人空间搜索作品后退出再进，未显示作品搜索历史记录')
    #     time.sleep(2)
    #
    #     # 个人空间搜索——作品搜索无结果显示
    #     self.driver.find_id_send('txtKeyword','配音秀')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnSearch')
    #     try:
    #         self.driver.wait_xpath('ll_noSearchResult')
    #     except:
    #         print('作品搜索无结果时未显示任何提示信息')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 个人空间—搜索-搜索个人素材
    # def test_g_person_zoom_source_search(self):
    #     self.driver.find_id_click('source_text')
    #     time.sleep(2)
    #     search_title = self.driver.find_id_text('source_text')
    #     time.sleep(2)
    #     self.driver.find_id_click('photo')
    #     time.sleep(2)
    #     self.driver.find_id_click('ll_source')
    #     time.sleep(2)
    #     self.driver.find_id_send('txtKeyword','配音秀')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnSearch')
    #     try:
    #         self.driver.wait_xpath('没有搜到任何内容')
    #     except:
    #         print('素材搜索无结果时未显示任何提示信息')
    #     time.sleep(2)
    #     self.driver.find_id_click('ll_source')
    #     time.sleep(2)
    #     self.driver.find_id_send('txtKeyword',search_title)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnSearch')
    #     time.sleep(4)
    #     try:
    #         self.driver.find_id('iv_source')
    #         name = self.driver.find_id_text('tv_source_title')
    #         assert search_title in name
    #         time.sleep(2)
    #         self.driver.find_id_click('tv_source_title')
    #         self.driver.wait_id('userhead')
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #     except:
    #         pass
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 编辑资料
    # def test_h_person_zoom_edit_info(self):
    #     self.driver.find_id_click('userhead')
    #     time.sleep(2)
    #     self.loc.four_from_last()
    #     time.sleep(4)
    #     try:
    #         self.driver.find_xpath('个人资料')
    #     except:
    #         print('未跳转到个人资料界面')
    #     time.sleep(2)

    # 更换头像
    # def test_i_person_zoom_change_head(self):
    #     # 点击头像-拍照
    #     self.driver.find_id_click('userhead')
    #     time.sleep(2)
    #     self.loc.three_from_last()
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id('next')
    #         self.driver.find_id_click('next')
    #         try:
    #             self.driver.wait_sys('始终允许')
    #         except:
    #             try:
    #                 self.driver.wait_sys('允许')
    #             except:
    #                 pass
    #         self.driver.find_id_click('userhead')
    #         time.sleep(2)
    #         self.loc.three_from_last()
    #         time.sleep(2)
    #     except:
    #         pass
    #     time.sleep(3)
    #     try:
    #         '''
    #         以下操作只适用vivox9
    #         '''
    #
    #         self.driver.find_id_third_part('com.android.camera:id/shutter_button')
    #         time.sleep(4)
    #         self.driver.find_id_click('com.android.camera:id/done_button')
    #     except:
    #         try:
    #             '''
    #             oppo r11
    #             '''
    #             self.driver.find_id('com.oppo.camera:id/shutter_button')
    #             self.driver.find_id_click('com.oppo.camera:id/shutter_button')
    #             time.sleep(4)
    #             self.driver.find_id_click('com.oppo.camera:id/done_button')
    #         except:
    #             try:
    #
    #                 self.driver.find_id_click('com.huawei.camera:id/shutter_button')
    #                 time.sleep(4)
    #                 self.driver.find_id_click('com.huawei.camera:id/done_button')
    #             except:
    #                 try:
    #                     self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
    #                     time.sleep(4)
    #                     self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
    #                 except:
    #                     pass
    #     time.sleep(4)
    #     self.driver.find_id_click('confirm')
    #     try:
    #         toast = self.driver.wait_toast('//android.widget.Toast')
    #         check = '修改成功'
    #         assert toast == check
    #     except:
    #         print('拍照更换头像未检测到toast提示')
    #     time.sleep(2)
    #     # 更换相册图片
    #     self.driver.find_id_click('userhead')
    #     time.sleep(2)
    #     self.loc.two_from_last()
    #     time.sleep(2)
    #     self.driver.find_id_click('com.android.gallery3d:id/ic_public_arrow_right')
    #     time.sleep(2)
    #     self.driver.find_id_click('com.android.gallery3d:id/top_frame')
    #     time.sleep(2)
    #     self.driver.find_id_click('com.android.gallery3d:id/head_select_right')
    #     try:
    #         toast1 = self.driver.wait_toast('//android.widget.Toast')
    #         check1 = '视频'
    #         assert check1 in toast1, toast1
    #     except:
    #         self.driver.find_id_click('confirm')
    #         try:
    #             toast1 = self.driver.wait_toast('//android.widget.Toast')
    #             check1 = '修改成功'
    #             assert check1 in toast1,'相册替换头像toast提示内容校验不一致'
    #         except:
    #             print('相册更换头像未检测到toast提示')
    #         time.sleep(2)
    #
    # # 输入个人简介
    # def test_j_person_zoom_introduction(self):
    #     self.driver.find_id_clear('tv_sign')
    #     time.sleep(2)
    #     self.driver.find_id_send('tv_sign','空空空')
    #     time.sleep(2)
    #
    # # 修改性别
    # def test_k_person_zoom_change_gender(self):
    #     gender = self.driver.find_id_text('tv_gender')
    #     if gender == '女':
    #         self.driver.find_id_click('tv_gender')
    #         time.sleep(2)
    #         self.loc.three_from_last()
    #         time.sleep(2)
    #     else:
    #         self.driver.find_id_click('tv_gender')
    #         time.sleep(2)
    #         self.loc.two_from_last()
    #         time.sleep(2)
    #
    # # 修改地区
    # def test_m_person_zoom_change_area(self):
    #     area = self.driver.find_id_text('tv_area')
    #     self.driver.find_id_click('tv_area')
    #     self.driver.wait_id('name')
    #     areas = self.driver.find_ids('name')
    #     select = random.randint(0, len(areas))
    #     self.driver.find_ids_click('name',select)
    #     time.sleep(2)
    #     area1 = self.driver.find_id_text('tv_area')
    #     assert area != area1, '地区修改前后显示未刷新,%s' %area1
    #     time.sleep(2)
    #
    # # 修改生日
    # def test_n_person_zoom_change_birthday(self):
    #     self.driver.find_id_click('tv_time')
    #     time.sleep(2)
    #     self.driver.find_id_click('tv_ensure')
    #     time.sleep(2)
    #
    # # 用户名敏感词检测
    # def test_o_person_zoom_username_check(self):
    #     self.driver.find_id_clear('et_nickname')
    #     time.sleep(2)
    #     self.driver.find_id_send('et_nickname','政府')
    #     time.sleep(2)
    #     self.driver.find_id_click('tv_right')
    #     try:
    #         toast = self.driver.wait_toast('//android.widget.Toast')
    #         check = '敏感词'
    #         assert check in toast
    #     except:
    #         print('用户名包含有敏感词，点击保存未弹出敏感词toast提示')
    #     time.sleep(2)
    #     self.driver.find_id_clear('et_nickname')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_third_part('android:id/button1')
    #     time.sleep(2)
    #
    # # 会员头像挂件
    # def test_p_person_zoom_vip_headwear(self):
    #     self.driver.find_id_click('userhead')
    #     time.sleep(2)
    #     self.loc.three_from_last()
    #     self.driver.wait_id('txtTitle')
    #     count = self.driver.find_ids('img')
    #     for i in range(len(count) - 1, -1, -1):
    #         self.driver.find_ids_click('img',i)
    #         time.sleep(1)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id('txtContent')
    #         self.driver.find_id_click('btnSubmit')
    #         time.sleep(2)
    #         try:
    #             self.driver.find_id('renew')
    #             self.driver.find_id_click('btnBack')
    #         except:
    #             pass
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #         self.driver.find_id_click('btnCancel')
    #         time.sleep(2)
    #     except:
    #         pass
    #
    # # 会员空间装扮
    # def test_q_person_zoom_vip_dress(self):
    #     self.driver.find_id_click('userhead')
    #     time.sleep(2)
    #     self.loc.two_from_last()
    #     self.driver.wait_id('txtTitle')
    #     time.sleep(2)
    #     count = self.driver.find_ids('img')
    #     for i in range(len(count) - 1, -1, -1):
    #         self.driver.find_ids_click('img',i)
    #         time.sleep(2)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 用户演绎等级
    # def test_r_person_zoom_user_level(self):
    #     self.driver.find_id_click('source_level')
    #     time.sleep(2)
    #     self.driver.find_id_click('img_vip')
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id('renew')
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #         self.driver.find_id_click('guize1')
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #     except:
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #
    # # 身份认证
    # def test_s_person_zoom_authentication(self):
    #     self.driver.find_id_click('vip_description')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #
    # # 粉丝列表
    # def test_t_person_zoom_fans(self):
    #     self.driver.find_id_click('ll_fan')
    #     time.sleep(2)
    #     self.driver.find_id_click('vip_tag')
    #     self.driver.find_id_click('iwant')
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id('renew')
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #     except:
    #         self.driver.find_id_click('btnSubmit')
    #     time.sleep(2)
    #     self.driver.find_id_click('userhead')
    #     self.driver.wait_id('ll_fan')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_click('status_icon')
    #     time.sleep(3)
    #     self.driver.find_id_click('status_icon')
    #     time.sleep(3)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #
    # # 关注列表
    # def test_u_person_zoom_follows(self):
    #     self.driver.find_id_click('ll_follow')
    #     self.driver.wait_id('status_icon')
    #     self.driver.find_id_click('username')
    #     self.driver.wait_id('ll_fan')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_click('status_icon')
    #     time.sleep(3)
    #     self.driver.find_id_click('status_icon')
    #     time.sleep(3)
    #     self.driver.find_id_click('btnBack')
    #
    # # 社团列表
    # def test_v_person_zoom_societies(self):
    #     self.driver.find_id_click('ll_society')
    #     self.driver.wait_id_click('status_icon')
    #     time.sleep(3)
    #     self.driver.find_id_click('status_icon')
    #     time.sleep(3)
    #     self.driver.find_id_click('user_image')
    #     self.driver.wait_id('ll_fan')
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     time.sleep(3)
    #     self.driver.find_id_click('btnBack')
    #
    # # 作品上榜列表
    # def test_w_person_zoom_crunchies_list(self):
    #     self.driver.find_id_click('ll_rank')
    #     self.driver.wait_id('middle_img')
    #     time.sleep(2)
    #     try:
    #         self.driver.find_id('tv_vip')
    #         self.driver.find_id_click('tv_vip')
    #         time.sleep(2)
    #         self.driver.wait_id('renew')
    #         time.sleep(2)
    #         self.driver.find_id_click('back')
    #         time.sleep(2)
    #     except:
    #         self.driver.find_id_click('img_url')
    #         self.driver.wait_id('userhead')
    #         self.driver.Background()
    #         time.sleep(2)
    #         self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_click('back')
    #     time.sleep(2)
    #
    # # 作品列表
    # def test_x_person_zoom_work_list(self):
    #     for i in range(10):
    #         self.driver.swip_up()
    #         time.sleep(2)
    #     time.sleep(2)
    #     self.driver.find_id_click('btnBack')
    #     time.sleep(2)
    #     self.driver.find_id_click('userhead')
    #     self.driver.wait_id('ll_follow')
    #     time.sleep(2)
    #
    # # 切换作品列表tab
    # def test_y_person_zoom_work_switch_label(self):
    #     self.driver.find_id_click('film_all_count')
    #     time.sleep(2)
    #     count = self.driver.find_ids('title')
    #     time.sleep(2)
    #     self.driver.back()
    #     time.sleep(2)
    #     for i in range(len(count) - 1, -1, -1):
    #         self.driver.find_id_click('film_all_count')
    #         time.sleep(2)
    #         self.driver.find_ids_click('title',i)
    #         time.sleep(2)

    # 置顶作品
    # def test_z_person_zoom_work_top(self):
    #     self.driver.Long_Touche('filmBg1', 3000)
    #     time.sleep(2)
    #     self.loc.three_from_last()
    #     time.sleep(4)
    #     try:
    #         self.driver.find_id('img')
    #     except:
    #         self.loc.one_from_last()
    #         time.sleep(2)
    #         self.driver.find_id_click('filmBg1')
    #         self.driver.wait_id('tv_video_detail_title')
    #         self.driver.Background()
    #         time.sleep(2)
    #         self.driver.find_id_click('setting')
    #         time.sleep(2)
    #         self.loc.four_from_last()
    #         time.sleep(2)
    #         self.driver.find_id_click('btnSubmit')
    #         time.sleep(3)
    #         self.driver.find_id_click('btnBack')
    #         time.sleep(2)
    #         self.driver.swip_down()
    #         time.sleep(4)
    #         self.driver.Long_Touche('filmBg1', 3000)
    #         time.sleep(2)
    #         self.loc.three_from_last()
    #         time.sleep(4)
    #         try:
    #             self.driver.find_id('img')
    #         except:
    #             print('未显示置顶标签')
    #     time.sleep(2)

    # 作品列表界面长按删除作品
    # def test_z_a_person_zoom_work_delete(self):
    #     self.driver.Long_Touche('filmBg1', 3000)
    #     time.sleep(2)
    #     self.loc.two_from_last()
    #     time.sleep(4)
    #     self.driver.find_id_click('btnSubmit')
    #     time.sleep(4)

    # 个人空间-求合作
    def test_z_b_person_zoom_coors(self):
        self.driver.find_id_click('coor_text')
        self.driver.wait_id('btnCooperate')
        self.driver.find_id_click('islook')
        self.driver.wait_download('video_play_btn')
        self.driver.back()
        time.sleep(2)
        self.driver.find_id_click('btnCooperate')
        self.driver.wait_download('action')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    # 求合作-邀请好友
    def test_z_c_person_zoom_coor_invite(self):
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('invitation_count')
        self.driver.wait_id('item_sh_cooperate_article_image')
        time.sleep(2)
        self.driver.Long_Touche('item_sh_cooperate_article_image', 3000)
        time.sleep(2)
        self.loc.five_from_last()
        self.driver.wait_id_click('socialstatus')
        time.sleep(2)
        self.driver.find_id_send('content','给自己的合作！')
        time.sleep(2)
        self.driver.find_id_click('reprint')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            success_check = '邀请成功'
            not_accept_check = '该用户暂不接受合作'
            if toast == success_check:
                pass
            elif toast == not_accept_check:
                self.driver.find_id_click('cancel')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
        except:
            print('发送邀请后未检测到toast提示')
        time.sleep(2)

    # 求合作-私密（公开）
    def test_z_d_person_zoom_coor_private_public(self):
        self.driver.Long_Touche('item_sh_cooperate_article_image', 3000)
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = "公开成功"
            assert check in toast,'求合作私密转公开toast校验不一致'
        except:
            try:
                self.driver.find_id_click('renew')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.back()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    # 求合作删除
    def test_z_e_person_zoom_coor_delete(self):
        self.driver.Long_Touche('item_sh_cooperate_article_image', 3000)
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast,'求合作删除失败'
        except:
            pass
        time.sleep(2)

    # 素材-视频预览
    def test_z_f_person_zoom_source_preview(self):
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id_click('source_text')
        self.driver.wait_id_click('imgSource')
        self.driver.wait_id('right_icon1')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 素材配音
    def test_z_g_person_zoom_source_dubbing(self):
        self.driver.find_id_click('imgSource')
        self.driver.wait_id('right_icon1')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id('yinpin')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('imgTip')
            while True:
                try:
                    self.driver.find_id('roleall')
                    break
                except:
                    self.driver.find_id('btnSubmit')
                    time.sleep(1)
                    self.driver.find_id_click('btnSubmit')
                    break
            self.driver.wait_id_click('roleall')
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
        except:
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('imgTip')
            while True:
                try:
                    self.driver.find_id('action')
                    break
                except:
                    try:
                        self.driver.find_id('btnSubmit')
                        time.sleep(1)
                        self.driver.find_id_click('btnSubmit')
                        break
                    except:
                        pass
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
        time.sleep(2)

    # 更多-点赞
    def test_z_h_person_zoom_goods_record(self):
        self.driver.find_id_click('more_text')
        time.sleep(2)
        self.driver.wait_id('filmBg')
        time.sleep(2)
        num = self.driver.find_id_text('look')
        if num == '0':
            self.driver.Long_Touche('filmBg', 3000)
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
        self.driver.find_id_click('filmBg')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('tv_good')
        good1 = self.driver.find_id_text('tv_good')
        self.driver.find_id_click('tv_good')
        time.sleep(1)
        good2 = self.driver.find_id_text('tv_good')
        if good1 != good2:
            print(good1,good2)
        time.sleep(3)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 更多-转发
    def test_z_i_person_zoom_forward(self):
        self.driver.find_id_click('film_all_count')
        time.sleep(2)
        self.driver.find_xpath('转发').click()
        self.driver.wait_id('filmBg')
        name = self.driver.find_id_text('username')
        self.driver.find_id_click('filmBg')
        try:
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '不存在'
            assert check in tip, '转发作品点击进入失败，提示信息错误'
        except:
            self.driver.wait_id('tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            detail_name = self.driver.find_id_text('user_name')
            assert name == detail_name,'转发列表界面用户名与视频详情界面用户名不一致'
            time.sleep(2)
            self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 作品转发列表——删除作品
        title = self.driver.find_id_text('title')
        count = self.driver.find_id_text('film_all_count')
        self.driver.Long_Touche('filmBg', 3000)
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        try:
            self.driver.find_xpath(title)
            print('转发作品删除失败')
        except:
            pass
        time.sleep(2)
        count1 = self.driver.find_id_text('film_all_count')
        assert count != count1,'转发作品删除失败'
        time.sleep(2)

    # 帖子列表
    def test_z_j_person_zoom_post_list(self):
        self.driver.find_id_click('film_all_count')
        time.sleep(2)
        self.driver.find_xpath('帖子').click()
        time.sleep(4)
        self.driver.find_id_click('good')
        time.sleep(4)
        self.driver.find_id_click('tag')
        self.driver.wait_id('img_subscribe')
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('comment')
        self.driver.wait_id('editContent')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 帖子-转发私信-删除
    def test_z_k_person_zoom_forword_and_delete(self):
        self.driver.find_id_click('action')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(2)
        self.driver.find_id_click('group_chat')
        time.sleep(2)
        self.driver.find_id_click('name')
        time.sleep(4)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('action')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            print('帖子删除未检测到toast提示')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('username')
        self.driver.wait_id('film_all_count')
        time.sleep(2)
        self.driver.find_id_click('more_text')
        time.sleep(2)

    # 语聊列表
    def test_z_l_person_chat_list(self):
        self.driver.find_id_click('film_all_count')
        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        time.sleep(4)

    # 创建合辑
    def test_z_m_person_zoom_create_compilation(self):
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_send('content','合辑')
        time.sleep(2)
        self.driver.find_id_click('ok')
        time.sleep(3)
        try:
            self.driver.find_id('choice')
            self.driver.find_id_click('choice')
            time.sleep(2)
            self.driver.find_id_click('tv_right')
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '创建成功'
                assert toast == check
                time.sleep(2)
            except:
                pass
        except:
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)

    # 合辑删除
    def test_z_n_person_zoom_delete_compilation(self):
        self.driver.find_id_click('single_text')
        time.sleep(4)
        self.driver.find_id_click('film_all_count')
        time.sleep(2)
        self.driver.find_xpath('合辑')
        self.driver.wait_id('filmBg')
        self.driver.Long_Touche('filmBg', 3000)
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            pass
        time.sleep(2)

    # 退出个人空间
    def test_z_o_person_zoom_quit(self):
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 我的界面vip入口
    def test_z_p_person_vip_enter(self):
        # 会员首次购买优惠入口
        try:
            self.driver.find_id('right_huiyuan')
            self.driver.wait_id('renew')
            self.driver.find_id_click('btnBack')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('img_vip')
        self.driver.wait_id('renew')
        time.sleep(2)

    # 会员权益计算
    def test_z_q_person_vip_equity(self):
        self.driver.find_id_click('img_right')
        time.sleep(2)
        try:
            self.driver.find_id('price')
        except:
            print('会员权益计算弹窗中未检测到相关控件')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)

    # 会员价格
    def test_z_r_person_vip_price(self):
        price = self.driver.find_ids('tv_now_money')
        for i in range(len(price)):
            price = self.driver.find_ids_text('tv_now_money',i)
            self.driver.find_ids_click('rl_all',i)
            time.sleep(1)
            self.driver.find_id_click('renew')
            time.sleep(2)
            price_buy = self.driver.find_id_text('tv_money')
            assert price in price_buy
            time.sleep(2)
            self.driver.find_id_click('close_icon')
            time.sleep(2)
            self.driver.find_id_click('cancel')
            time.sleep(2)

    # 会员赠送
    def test_z_s_person_vip_give(self):
        self.driver.find_id_click('tv_right')
        self.driver.wait_id_click('user_head')
        self.driver.wait_id('ll_follow')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('send')
        time.sleep(2)
        self.driver.wait_id('renew')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 会员特权
    def test_z_t_person_vip_privileges(self):
        member_privileges_page1 = self.driver.find_ids('name')
        privileges_list = []
        for i in range(len(member_privileges_page1)):
            name = self.driver.find_ids_text('name',i)
            privileges_list.append(name)
        time.sleep(2)
        start_locat = self.driver.find_ids('name')[-1].location
        end_locat = self.driver.find_ids('name')[-4].location
        start_swip_x = start_locat['x']
        start_swip_y = start_locat['y']
        end_swip_x = end_locat['x']
        end_swip_y = end_locat['y']
        if self.y >= 2280:
            self.driver.swip_move(start_swip_x, start_swip_y, end_swip_x, end_swip_y)
        time.sleep(2)
        member_privileges_page2 = self.driver.find_ids('name')
        for i in range(len(member_privileges_page2)):
            name1 = self.driver.find_ids_text('name',i)
            privileges_list.append(name1)
        privileges_check_list = ['双倍金币', '免费曝光', '推荐涨粉', '升级加速', '上榜历史', '作品下载', '评论置顶',
                                '作品编辑', '云端存储', '语聊麦位', '专属挂件', '空间装扮']
        assert sorted(privileges_list) == sorted(privileges_check_list)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #cp邀请
    def test_z_u_person_cp_invite(self):
        self.driver.find_id_click('img_cp')
        time.sleep(2)
        try:
            self.driver.find_id('invite')
            self.driver.find_id_click('invite')
            time.sleep(2)
            self.driver.find_id_send('filter_edit','1247792')
            time.sleep(2)
            self.driver.find_id_click('btnSearch')
            time.sleep(2)
            self.driver.wait_xpath('逍遥剑仙')
            time.sleep(2)
            self.driver.find_id_click('userhead')
            self.driver.wait_id('right_icon1')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
        except:
            self.driver.find_id_click('cancel_invite')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            self.driver.wait_id_click('invite')
            time.sleep(2)
            self.driver.find_id_send('filter_edit','1247792')
            time.sleep(2)
            self.driver.find_id_click('btnSearch')
            time.sleep(2)
            self.driver.wait_xpath('逍遥剑仙')
            time.sleep(2)
            self.driver.find_id_click('userhead')
            self.driver.wait_id('right_icon1')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
        time.sleep(2)

    #cp空间
    def test_z_v_person_cp_zoom(self):
        pass

    #达人
    def test_z_w_person_daren(self):
        pass
        # self.driver.find_id_click()('img_daren')

    # 系统消息
    def test_z_x_person_system_notices(self):
        self.driver.find_id_click('system_notice')
        self.driver.wait_id_click('userhead')
        self.driver.wait_id('ll_follow')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        try:
            self.driver.find_id('agree')
            self.driver.find_id_click('agree')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('more')
        time.sleep(2)
        self.driver.find_id_click('btnCancel')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 点赞消息
    def test_z_y_person_good_notices(self):
        try:
            self.driver.find_id('gift_point')
            self.driver.find_id_click('gift')
            self.driver.wait_id('userhead')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            try:
                self.driver.find_id('gift_point')
                print('点赞红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('gift')
        time.sleep(2)
        self.driver.wait_id_click('userhead')
        self.driver.wait_id('ll_follow')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('content')
        try:
            self.driver.wait_toast('//android.widget.Toast')
            time.sleep(2)
        except:
            self.driver.wait_id('tv_video_detail_title')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        time.sleep(2)

        # 回赞
        self.driver.find_id_click('guanzhu')
        self.driver.wait_id('tv_video_detail_title')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 合作消息
    def test_z_z_person_coor_notices(self):
        try:
            self.driver.find_id_click('cooper_count')
            self.driver.find_id_click('textView15')
            self.driver.wait_id('userhead')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            try:
                self.driver.find_id('cooper_count')
                print('合作消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('textView15')
        self.driver.wait_id('more')
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_follow')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 合作配音
    def test_z_z_a_person_coor_dubbing(self):
        try:
            self.driver.find_xpaths('合作配音')[1].click()
            self.driver.wait_download('action')
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
            self.driver.find_id_click('play')
            time.sleep(3)
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 删除合作消息
    def test_z_z_b_person_coor_delete(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('more')
        time.sleep(2)
        self.loc.two_from_last()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除合作消息成功'
            assert check in toast, '合作消息删除失败'
        except:
            print('未检测到合作消息删除toast提示')
        time.sleep(2)

    # 生成作品
    def test_z_z_c_person_coor_generate_works(self):
        self.driver.find_id_click('rl_tag2')
        time.sleep(2)
        self.driver.find_xpaths('生成作品')[1].click()
        time.sleep(2)
        self.driver.find_id_click('head_name')
        time.sleep(2)
        self.driver.find_id_click('tv_take_photo')
        time.sleep(5)
        try:
            '''
            以下操作只适用vivox9
            '''

            self.driver.find_id_click('com.android.camera:id/shutter_button')
            time.sleep(4)
            self.driver.find_id_click('com.android.camera:id/done_button')
        except:
            try:
                '''
                oppo r11/r15
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id_click('com.oppo.camera:id/shutter_button')
                time.sleep(4)
                self.driver.find_id_click('com.oppo.camera:id/done_button')
            except:
                try:

                    self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                    time.sleep(4)
                    self.driver.find_id_click('com.huawei.camera:id/done_button')
                except:
                    try:
                        self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                        time.sleep(4)
                        self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                    except:
                        pass
        time.sleep(4)
        self.driver.find_id_click('confirm')
        time.sleep(3)
        self.driver.find_id_click('head_name')
        time.sleep(2)
        self.driver.find_id_click('tv_photo')
        time.sleep(3)
        self.driver.find_id_click('photo_wall_item_photo')
        time.sleep(2)
        self.driver.find_id_click('confirm')
        time.sleep(3)
        self.driver.find_id_send('title','功能测试')
        time.sleep(2)
        try:
            self.driver.find_id('tv')
            self.driver.find_id_click('tv')
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('btn_close')
        time.sleep(2)

    # 生成作品tab界面预览视频
    def test_z_z_d_person_coor_video_play(self):
        self.driver.find_id_click('play')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast,'视频详情界面进入失败'
        except:
            self.driver.wait_id('tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)

    # 合作消息设置
    def test_z_z_e_person_coor_notice_setting(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(4)
        # 获取当前界面所有resourceid,但部分id不可用，因此无法区分筛选出真正可以点击的id
        # count = self.driver.search_id()
        # print(count)
        # self.id = re.findall(r'resource-id="com.happyteam.dubbingshow:id/(.*?)"',count)
        # print(self.id)
        el_list = ['acceptAll','acceptFirends','acceptNone','clearAllInviter','btnCancel']
        for i in el_list:
            self.driver.find_id_click(i)
            time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 评论消息-跳转个人空间
    def test_z_z_f_person_comment_notices(self):
        try:
            self.driver.find_id('comment_count')
            self.driver.find_id_click('textView16')
            self.driver.wait_id('reply')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            try:
                self.driver.find_id('comment_count')
                print('评论消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('textView16')
        self.driver.wait_id('reply')
        time.sleep(2)
        name = self.driver.find_id_text('textView')
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_follow')
        time.sleep(2)
        zoom_name = self.driver.find_id_text('username')
        assert name == zoom_name
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 评论消息-关注
    def test_z_z_g_person_comment_follows(self):
        self.driver.find_id_click('guanzhu')
        time.sleep(2)
        try:
            self.driver.find_id_click('editContent')
            time.sleep(2)
            self.driver.find_id_click('right_icon1')
            time.sleep(2)
            self.loc.two_from_last()
            self.driver.wait_id('ll_follow')
            time.sleep(2)
            self.driver.find_id_click('follow_status')
            time.sleep(3)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.swip_down()
        except:
            self.driver.find_id_click('guanzhu')
            time.sleep(2)
            self.driver.find_id_click('right_icon1')
            time.sleep(2)
            self.loc.two_from_last()
            self.driver.wait_id('ll_follow')
            time.sleep(2)
            self.driver.find_id_click('follow_status')
            time.sleep(3)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id_click('guanzhu')
        time.sleep(2)

    # 评论消息-进入作品详情
    def test_z_z_h_person_comment_video_detail(self):
        self.driver.find_id_click('content')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast
        except:
            self.driver.wait_id('tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        time.sleep(2)

    # 评论消息-回复评论
    def test_z_z_i_person_comment_reply(self):
        self.driver.find_id_click('reply_btn')
        time.sleep(2)
        self.driver.find_id_send('editContent','哈哈哈')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.wait_toast('//android.widget.Toast')
        try:
            self.driver.find_id_click('editContent')
            self.driver.back()
        except:
            pass

    # 评论消息-帖子消息
    def test_z_z_j_person_comment_post_notices(self):
        self.driver.find_id_click('tab2')
        self.driver.wait_id_click('content')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check == toast, '帖子跳转失败'
        except:
            self.driver.wait_id('editContent')
            time.sleep(2)
            self.driver.find_id_send('editContent','hhh')
            time.sleep(2)
            self.driver.find_id_click('btn_send')
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in toast, '帖子发布评论失败'
            except:
                pass
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)

    # 聊天消息
    def test_z_z_k_person_chat_notices(self):
        try:
            self.driver.find_id('chat_count')
            self.driver.find_id_click('chat')
            self.driver.wait_id('right_icon1')
            time.sleep(2)
            while True:
                try:
                    self.driver.find_id('txtCount')
                    self.driver.find_id_click('txtCount')
                    self.driver.wait_id('editContent')
                    time.sleep(2)
                    self.driver.find_id_click('btnBack')
                    time.sleep(2)
                except:
                    break
                time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            try:
                self.driver.find_id('chat_count')
                print('私信消息红点未消失')
            except:
                pass
        except:
            pass
        self.driver.find_id_click('chat')
        time.sleep(2)
        self.driver.wait_id('right_icon1')
        time.sleep(2)

    # 聊天列表界面用户
    def test_z_z_l_person_chat_user_list(self):
        try:
            self.driver.find_id_click('userhead')
            count = self.driver.find_ids('userhead')
            for i in range(len(count)):
                self.driver.find_ids_click('userhead',i)
                self.driver.wait_id('editContent')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 用户聊天
    def test_z_z_m_person_user_chat(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.find_id_clear('filter_edit')
        time.sleep(2)
        self.driver.find_id_send('filter_edit','1247792')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        self.driver.wait_xpath('逍遥剑仙')
        self.driver.find_id_click('name')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_xpath('逍遥剑仙').click()
        time.sleep(2)

        # 清除聊天记录
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送文字
        self.driver.find_id_send('editContent','功能测试')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        time.sleep(2)
        self.driver.wait_id('content')
        time.sleep(2)
        try:
            self.driver.find_xpath('功能测试')
        except:
            print('聊天内容区域未找到发送的文案')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送表情
        self.driver.find_id_click('btn_send_smile')
        time.sleep(2)
        self.driver.find_id_click('emojicon_icon')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.wait_id('content')
        time.sleep(2)
        try:
            self.driver.find_id('content')
        except:
            print('聊天内容区域未找到发送的表情')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送语音
        self.driver.find_id_click('btn_change_input_mode')
        time.sleep(2)
        self.driver.Long_Touche('btn_record_voice', 3000)
        self.driver.wait_id('btn_play_sound_content_layout')
        time.sleep(2)
        self.driver.find_id_click('btn_play_sound_content_layout')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送图片
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('photo')
        time.sleep(4)
        self.driver.find_id_click('cb_select_tag')
        time.sleep(2)
        self.driver.find_id_click('next_step_tv')
        self.driver.wait_id('chat_image')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 拍照发送私信信息
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('camera')
        time.sleep(4)
        try:

            self.driver.find_id_click('com.android.camera:id/shutter_button')
            time.sleep(3)
            self.driver.find_id_click('com.android.camera:id/done_button')
        except:
            try:

                self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                time.sleep(3)
                self.driver.find_id_click('com.huawei.camera:id/done_button')
            except:
                try:
                    self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                    time.sleep(4)
                    self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                except:
                    pass
        self.driver.wait_id('chat_image')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送作品
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('film')
        time.sleep(4)
        self.driver.find_id_click('filmBg')
        time.sleep(3)
        self.driver.find_id_click('btnSelect')
        self.driver.wait_id('chat_film_title')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送红包
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('redpacket')
        time.sleep(2)
        self.driver.find_id_send('cash_num','0.1')
        time.sleep(3)
        self.driver.find_id_click('generate_red_packet')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id_click('red_packet')
        time.sleep(2)
        self.driver.find_id_click('open_red_packet_btn')
        self.driver.wait_id('diamond')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

        # 发送社团邀请
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('union_inviter')
        time.sleep(4)
        self.driver.find_id_click('username')
        self.driver.wait_id_click('union_inviter_apply')
        time.sleep(2)
        self.driver.wait_id('ll_fan')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.four_from_last()
        time.sleep(2)
        self.loc.screen_confirm_buttem()
        time.sleep(2)

    # 私信聊天界面举报用户-其它原因
    def test_z_z_n_person_chat_report(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.five_from_last()
        time.sleep(2)
        self.driver.find_id_click('tv_action_other')
        time.sleep(2)
        self.driver.find_id_clear('txtKeyword')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','功能测试，可忽略此举报信息')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '举报成功'
            assert check == toast, '私信聊天用户举报toast校验不一致'
        except:
            print('未检测到举报成功toast')
        time.sleep(2)

    # 私信聊天界面-进入对方空间
    def test_z_z_o_person_chat_user_zoom(self):
        try:
            self.driver.find_id('txtKeyword')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.two_from_last()
        self.driver.wait_id('ll_fan')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 私信列表界面长按删除
    def test_z_z_p_person_chat_list_delete(self):
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        el = 'textView'
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        self.driver.find_id_click('delete')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        try:
            self.driver.find_xpath('逍遥剑仙')
            print('列表中长按用户删除失败')
        except:
            pass
        time.sleep(2)

    # 私信消息-未关注
    def test_z_z_q_person_chat_not_follow(self):
        self.driver.find_id_click('tab2')
        time.sleep(2)
        try:
            self.driver.find_id('userhead')
            self.driver.find_id_click('userhead')
            time.sleep(3)
            try:
                self.driver.find_id('tishi')
            except:
                print('私信未关注界面，私信详情界面未显示谨防诈骗信息')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            el = 'userhead'
            self.driver.Long_Touche(el, 3000)
            time.sleep(2)
            self.driver.find_id_click('delete')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 草稿箱-会员同步
    def test_z_z_r_person_vip_draft_synchronous(self):
        self.driver.find_id_click('draft')
        time.sleep(2)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        try:
            self.driver.find_id('renew')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            self.driver.wait_load('同步')
        time.sleep(2)

    # 草稿箱作品断网后删除再重新同步下载
    def test_z_z_s_person_draft_reload(self):
        date_before = self.driver.find_id_text('date')
        self.driver.disconnect_network()
        time.sleep(2)
        el = 'date'
        self.driver.Long_Touche(el, 3000)
        self.loc.screen_confirm_buttem()
        time.sleep(2)
        self.driver.only_wifi()
        time.sleep(15)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        self.driver.wait_xpath('同步')
        date_after = self.driver.find_id_text('date')
        assert date_before == date_after, '草稿箱断网情况删除以后联网再同步，作品时间校验不一致'
        time.sleep(2)

    # 草稿箱-草稿箱作品视频预览
    def test_z_z_t_person_draft_video_preview(self):
        self.driver.find_id_click('imgSource')
        time.sleep(10)
        try:
            self.driver.find_id('imgSource')
            self.driver.find_id_click('imgSource')
        except:
            pass
        self.driver.wait_download('video_play_btn')
        time.sleep(2)
        self.driver.back()
        time.sleep(3)

    # 草稿箱作品时间重复性检查
    def test_z_z_u_person_draft_repeat(self):
        date = self.driver.find_ids('date')
        lists = []
        for i in range(len(date)):
            times = self.driver.find_ids_text('date',i)
            lists.append(times)
            time.sleep(1)
        set_list = set(lists)  # set会生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
        if len(lists) == len(set_list):
            pass
        else:
            dic = dict(counter(lists))
            print([key for key, value in dic.items() if value > 1])  # 展示重复元素
        time.sleep(2)

    # 草稿箱作品重配
    def test_z_z_v_person_draft_reassignment(self):
        count = self.driver.find_ids('imgSource')
        for i in range(len(count)):
            self.driver.find_ids_click('upload',i)
            time.sleep(2)
            try:
                self.driver.find_id('reDubbing')
                self.driver.find_id_click('reDubbing')
                break
            except:
                self.driver.find_id_click('btnBack')
            time.sleep(2)
        time.sleep(2)
        while True:
            try:
                self.driver.find_id('roleall')
                self.driver.find_id_click('roleall')
                break
            except:
                try:
                    self.driver.find_id('btnSubmit')
                    self.driver.find_id_click('btnSubmit')
                    try:
                        self.driver.find_id('roleall')
                        self.driver.find_id_click('roleall')
                        break
                    except:
                        pass
                    break
                except:
                    break
        time.sleep(2)
        self.driver.wait_id_click('action')
        self.driver.wait_download('title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('complete')
        self.driver.wait_id('txtTitle')
        time.sleep(2)
        self.driver.find_id_click('pri_switch_tv')
        time.sleep(2)
        self.driver.find_id_click('saveToDraft')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        self.bcak()

    # 已配素材列表
    def test_z_z_w_person_already_source_list(self):
        self.driver.find_id_click('source')
        time.sleep(2)
        self.driver.wait_id('iv_source')
        time.sleep(2)

    # 已配素材列表界面点击配音
    def test_z_z_x_person_already_source_dubbing(self):
        self.driver.find_id_click('iv_dub')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '素材不存在'
            assert check in toast,'素材配音下载失败'
        except:
            while True:
                try:
                    self.driver.find_id('roleall')
                    self.driver.find_id_click('roleall')
                    break
                except:
                    try:
                        self.driver.find_id('btnSubmit')
                        self.driver.find_id_click('btnSubmit')
                        try:
                            self.driver.find_id('roleall')
                            self.driver.find_id_click('roleall')
                            break
                        except:
                            pass
                        break
                    except:
                        break
            time.sleep(2)
            self.driver.wait_id('action')
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)

    # 已配素材列表界面删除已配素材
    def test_z_z_y_person_alread_source_delete(self):
        source = 'iv_source'
        self.driver.Long_Touche(source, 3000)
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除成功'
            assert check in toast, '已配素材长按删除toast提示检验不一致'
            time.sleep(2)
        except:
            print('未检测到素材删除toast提示')
        time.sleep(2)

    # 断网环境下删除已配素材，联网后再刷新
    def test_z_z_z_person_alread_source_delete_network(self):
        delete_before = self.driver.find_id_text('tv_source_title')
        self.driver.disconnect_network()
        time.sleep(2)
        el = 'tv_source_title'
        self.driver.Long_Touche(el, 3000)
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            pass
        self.driver.only_wifi()
        time.sleep(10)
        self.driver.swip_down()
        time.sleep(2)
        refresh_after = self.driver.find_id_text('tv_source_title')
        assert delete_before == refresh_after, '断网情况下删除已配素材再联网刷新列表，未显示之前删除的素材'
        time.sleep(2)

    # 已配素材批量删除
    def test_z_z_z_a_person_alread_source_bulk_deletion(self):
        self.driver.find_id_click('delete')
        time.sleep(2)
        self.driver.find_id_click('choice')
        time.sleep(2)
        delete = self.driver.find_id_text('tv_source_title')
        time.sleep(2)
        self.driver.find_id_click('toDelete')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_toast('//android.widget.Toast')
        delete_after = self.driver.find_id_text('tv_source_title')
        assert delete != delete_after, '批量删除未成功删除'
        time.sleep(2)
        self.driver.find_id_click('cancel')
        time.sleep(2)
        self.bcak()

    # 素材收藏
    def test_z_z_z_b_person_source_collection(self):
        self.driver.find_id_click('collect')
        time.sleep(2)
        try:
            self.driver.find_xpath('您还没有收藏任何素材哦~')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btn_more')
            self.driver.wait_id('iv_source')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            count = self.driver.find_ids('iv_source')
            for i in range(len(count)):
                self.driver.find_ids_click('iv_source',i)
                self.driver.wait_id('btn_video_detail_follow')
                self.driver.Background()
                time.sleep(2)
                self.driver.find_id_click('shouchang_tv_fake')
                self.driver.wait_toast('//android.widget.Toast')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            time.sleep(2)
            self.driver.find_id_click('ivMineTab')
            time.sleep(2)
            self.driver.find_id_click('collect')
            self.driver.wait_id('iv_source')
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    # 素材预览界面取消收藏后刷新收藏列表
    def test_z_z_z_c_person_source_collection_refresh(self):
        self.driver.find_id_click('iv_source')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '素材不存在'
            assert check in toast, '进入素材详情失败'
        except:
            self.driver.wait_id('userhead')
            self.driver.Background()
            time.sleep(2)
            cancel_before = self.driver.find_id_text('source_title')
            self.driver.find_id_click('shouchang_tv_fake')
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '取消收藏成功'
                assert check in toast, '素材取消收藏失败'
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            except:
                self.driver.find_id_click('btnBack')
                print("未检测到取消收藏的toast提示")
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(2)
            try:
                self.driver.find_id('source_title')
                cancel_after = self.driver.find_id_text('source_title')
                assert cancel_before != cancel_after, '素材取消收藏，收藏列表刷新依然显示有该素材'
                time.sleep(2)
            except:
                pass
            time.sleep(2)
        self.test_z_z_x_person_already_source_dubbing()
        self.test_z_z_y_person_alread_source_delete()
        self.driver.find_id_click('btnBack')
        time.sleep(2)


    # 自制素材列表
    def test_z_z_z_d_person_self_control_source(self):
        self.driver.find_id_click('upload_source')
        time.sleep(2)
        self.driver.find_id_click('middle')
        self.driver.wait_id('btnClose')
        time.sleep(2)
        try:
            self.driver.find_id('titlebar')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            self.driver.find_id_click('btnBack')
            print('未加载出素材收录标准文案')
        time.sleep(2)

    # 上传自制素材
    def test_z_z_z_e_person_self_control_video_select(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.find_id_click('ll_upload')
        time.sleep(2)
        self.driver.find_ids_click('android:id/title',1)
        self.driver.wait_id('next')
        time.sleep(2)

    # 视频剪辑
    def test_z_z_z_f_person_self_control_video_clip(self):
        self.driver.find_id_click('play_button')
        time.sleep(5)
        self.driver.Background()
        time.sleep(2)
        self.driver.wait_id('play_button')
        time.sleep(2)
        try:
            self.driver.find_id('cant_clip_tip')
        except:
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.124, self.y * 0.385, self.x * 0.688, self.y * 0.385)
            elif self.y >= 2280:
                self.driver.swip_move(self.x * 0.903, self.y * 0.472, self.x * 0.5, self.y * 0.472)
        time.sleep(2)
        self.driver.find_id_click('next')
        self.driver.wait_id('et_content')
        time.sleep(2)

        # 素材添加角色名称
        self.driver.find_id_send('et_content','角色1')
        time.sleep(2)
        self.driver.find_id_click('rl_role2')
        time.sleep(2)
        self.driver.find_id_click('add_role_tv')
        time.sleep(2)
        self.driver.find_id_send('et_content2','角色2')
        self.driver.find_id_click('rl_role3')
        time.sleep(2)
        self.driver.find_id_click('sure')
        time.sleep(2)

        # 添加字幕
        self.driver.find_id_click('tv_add_zimu')
        self.driver.wait_id('et')
        time.sleep(2)
        self.driver.find_id_click('close_zimu')
        time.sleep(2)
        roles = ['tv_role1', 'tv_role2']
        words = ['角色1的台词', '角色2的台词']
        for i in range(len(roles)):
            self.driver.find_id_click('tv_add_zimu')
            self.driver.wait_id('et')
            time.sleep(2)
            self.driver.find_id_click(roles[i])
            self.driver.find_id_send('et',words[i])
            time.sleep(2)
            self.driver.find_id_click('complete_zimu')
            time.sleep(2)
            self.driver.find_id_click('rl_bottom')
            time.sleep(2)
        content = ['tv_content2', 'tv_content2']
        for i in range(len(content)):
            try:
                self.driver.find_id_click(content[i])
            except:
                print('字幕显示错误')
        time.sleep(2)

        # 编辑字幕
        self.driver.find_id_click('linear_view2')
        time.sleep(2)
        # 无效
        # left_el = self.driver.find_id('left_view_bottom')
        # right_el = self.driver.find_id('right_view_bottom')
        # el = right_el.rect
        # el_x = int(el['x'] + el['width'] / 2.0)
        # el_y = int(el['y'] + el['height'] / 2.0)
        # self.driver.long_press_move(left_el,el_x,el_y)
        # time.sleep(2)
        self.driver.find_id_click('tv_delete_zimu')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)

        # 裁剪视频预览
        self.driver.find_id_click('play_button')
        time.sleep(2)
        try:
            self.driver.find_id_click('stop_button')
            #视频无法正常播放
        except:
            self.driver.wait_id('play_button')
        time.sleep(2)

        # 存草稿
        self.driver.find_id_click('save')
        time.sleep(2)

        # 退出素材制作再进
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.find_id_click('ll_upload')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)

        # 进入上传素材界面
        self.driver.find_id_click('next')
        time.sleep(2)

        # 素材上传封面中添加文字
        self.driver.find_id_click('add_text')
        time.sleep(2)
        self.driver.find_id_send('editContent','素材封面图')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        time.sleep(2)

        # 素材封面更换
        self.driver.find_xpath('更换封面').click()
        time.sleep(2)
        self.driver.find_id_click('next')
        time.sleep(2)

        # 素材名称
        self.driver.find_id_send('et_title','素材上传测试')
        time.sleep(2)

        # 添加素材音乐
        self.driver.find_id_click('addMusic')
        self.driver.wait_id_click('title')
        time.sleep(2)
        self.driver.find_id_click('local_music')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id_click('local_video_music')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id_click('btnDownload')
        self.driver.wait_id_click('tv_use')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)

        # 添加素材标签
        self.driver.find_id_click('tv1')
        time.sleep(2)
        self.driver.find_id_send('edit_text','测试')
        self.driver.find_id_click('btn_search')
        time.sleep(2)
        self.driver.find_id_click('tv')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        time.sleep(2)

        # 上传素材
        self.driver.find_id_click('next')
        while True:
            try:
                self.driver.find_id('iv_dub')
                break
            except:
                self.driver.find_id_click('linear_biaoqian')
            time.sleep(10)
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('iv_source')
        self.driver.wait_id('userhead')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id('video_play_btn')
        except:
            print('新上传的素材未显示播放按钮，素材播放有问题')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    #素材信息编辑/删除
    def test_z_z_z_g_person_self_control_source_delete(self):
        self.driver.find_id_click('iv_source')
        self.driver.wait_id('userhead')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)

        #素材信息编辑
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(4)
        self.driver.find_id_send('et_title','素材信息修改测试')
        time.sleep(2)
        self.driver.find_id_click('next')
        while True:
            try:
                self.driver.find_id('iv_dub')
                break
            except:
                self.driver.find_id_click('music_text')
            time.sleep(10)
        time.sleep(2)

        #素材删除
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(4)
        self.driver.find_id_click('btnSubmit')
        time.sleep(4)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 个人中心-我的财富
    def test_z_z_z_h_person_my_wealth(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('money')
        self.driver.wait_id('diamond_count_tv')
        time.sleep(2)

        # 个人中心-我的账单
        self.driver.find_id_click('toBill')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)

        # 点击购买钻石
        for i in range(6):
            time.sleep(1)
            self.driver.find_ids_click('price_tv',i)
            time.sleep(2)
            self.driver.find_id_click('tv_pay')
            self.driver.wait_id('android:id/text1')
            time.sleep(2)
            self.driver.find_id_click('com.tencent.mm:id/dn')
            time.sleep(2)
            self.driver.find_id_click('com.tencent.mm:id/dm3')
            time.sleep(2)
            self.driver.find_id_click('close_icon')
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    # 个人中心-我的收益
    def test_z_z_z_i_person_my_earnings(self):
        self.driver.find_id_click('gold')
        self.driver.wait_id('gold_count')
        time.sleep(2)

        # 常见问题
        self.driver.find_id_click('tv_right')
        self.driver.wait_id('btnClose')
        time.sleep(2)
        # ids = self.driver.search_id()
        # print(ids)
        # list = re.findall('content-desc="(.*?)"', ids)
        # print(list)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 绑定支付宝
        self.driver.find_id_click('right')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(4)
        self.driver.find_id_click('send_code')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast, '验证码发送失败'
        except:
            print('未检测到验证码发送toast提示')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        try:
            self.driver.find_id('userhead')
            self.driver.find_id_click('userhead')
            self.driver.wait_id('ll_fan')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 我的成就
    def test_z_z_z_j_person_my_achievements(self):
        self.driver.find_id_click('achievement')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 邀请好友
    def test_z_z_z_k_person_invite_friend(self):
        self.driver.find_id_click('addfriend')
        time.sleep(2)

        # 规则
        self.driver.find_id_click('tv_right')
        time.sleep(2)
        self.driver.wait_id('btnClose')
        time.sleep(2)
        self.driver.find_id_click('btnClose')
        time.sleep(2)

        # 邀请好友
        self.driver.find_id_click('tv_invite')
        time.sleep(2)

        # 朋友圈
        self.loc.share_pyq()
        self.driver.wait_xpath('发表')
        time.sleep(2)
        self.driver.find_id_third_part('com.tencent.mm:id/dn')
        time.sleep(3)

        # qq空间
        self.driver.find_id_click('tv_invite')
        time.sleep(2)
        self.loc.share_qq_zone()
        self.driver.wait_xpath('发表')
        time.sleep(2)
        self.driver.find_id_third_part('com.tencent.mobileqq:id/ivtitlebtnleft')
        time.sleep(3)

        # 点击复制链接（qq取消分享返回应用，分享弹窗还会显示）
        self.loc.share_message_friend()
        try:
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in tip,'邀请好友链接复制失败'
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        #好友召回
        self.driver.find_id_click('tv_recall')
        time.sleep(2)
        try:
            self.driver.find_id('userhead')
            self.driver.find_id_click('re_update')
            time.sleep(2)
            self.loc.share_message_friend()
            try:
                tip = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                assert check in tip, '召回好友链接复制失败'
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            self.driver.find_id_click('btnBack')
        except:
            self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 积分商城
    def test_z_z_z_l_person_points_mall(self):
        self.driver.find_id_click('exchange')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 夜间模式
    def test_z_z_z_m_person_mode_switch(self):
        self.driver.find_id_click('tvChange')
        time.sleep(5)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id_click('tvChange')
        time.sleep(5)

class video_detail(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    def btnBack(self):
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 首页点击作品封面进入视频详情
    def test_a_into_video(self):
        self.driver.find_id_click('film_img2')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)

    # 点击用户头像进入个人空间
    def test_b_head_into_zoom_back(self):
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_fan')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 视频详情点击关注
    def test_c_video_follow(self):
        self.driver.find_id_click('follow_ta')
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.find_id('right_icon1')
                time.sleep(2)
                self.btnBack()
            except:
                pass
        time.sleep(2)

    # 视频-弹幕开关
    def test_d_video_danmu(self):
        try:
            self.driver.find_id('media_danmu_img')
            self.driver.find_id_click('media_danmu_img')
            time.sleep(2)
            self.driver.find_id_click('video_play_btn')
            time.sleep(20)
            self.driver.Background()
            self.driver.wait_id('video_play_btn')
            time.sleep(2)
        except:
            pass

    # 全屏播放
    def test_e_video_fullscreen(self):
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('iv_fullscreen_open')
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        self.test_a_into_video()

    # 点赞
    def test_f_video_good(self):
        num = self.driver.find_id_text('tv_good')
        try:
            self.driver.find_id_click('good_svga')
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '恭喜你获得300金币'
            if tip != check:
                print('未获取到点赞奖励金币toast提示')
        except:
            self.driver.find_id_click('tv_good')
        num1 = self.driver.find_id_text('tv_good')
        try:
            if num != num1:
                print('点赞后数量未变化')
        except exception as e:
            print(e)
        time.sleep(2)

    # 曝光界面功能按钮点击
    def test_g_video_exposure_touch(self):
        tv_title = self.driver.find_id_text('tv_video_detail_title')
        self.driver.find_id_click('tv_exposure')
        self.driver.wait_id('txtTitle')
        time.sleep(2)
        tv_title1 = self.driver.find_id_text('tv_source_title')
        try:
            assert tv_title1 == tv_title
        except exception as e:
            print(e)
        time.sleep(2)

        #曝光券
        self.driver.find_id_click('tv_right')
        time.sleep(2)
        self.driver.find_id_click('tab2')
        time.sleep(1)
        self.driver.find_id_click('tab1')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        self.driver.wait_id('btnClose')
        self.btnBack()
        self.btnBack()


        #评论推荐人简介预览
        self.driver.find_id_click('tv_preview')
        time.sleep(2)
        self.driver.find_id_click('sure')
        time.sleep(2)

        #充值界面跳转
        self.driver.find_id_click('img_right')
        time.sleep(2)
        self.driver.find_id_click('price_tv')
        time.sleep(2)
        self.driver.find_id_click('close_icon')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

        #曝光价格列表
        prices = self.driver.find_ids('rl')
        for i in range(len(prices) - 1):
            self.driver.find_ids_click('rl',i)
        time.sleep(2)

        #曝光服务协议
        self.driver.find_id_click('tv_xieyi')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)

        #作品曝光要求
        self.driver.find_id_click('tv_yaoqiu')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)

        #自定义钻石价格
        self.driver.find_ids_click('rl',-1)
        time.sleep(2)
        self.driver.find_id_send('edit','20000')
        time.sleep(1)
        self.driver.find_id_click('sure')
        time.sleep(2)
        self.btnBack()

    # 金币曝光
    def test_h_video_exposure_gold(self):
        self.driver.find_id_click('tv_exposure')
        time.sleep(2)
        self.driver.find_id_click('rl')
        time.sleep(2)
        golds = self.driver.find_id_text('tv_gold')
        if int(golds) >= 5000:
            self.driver.find_id_click('gold_count')
        else:
            self.driver.find_id_click('gold_count')
            gold_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '金币余额不足'
            if check not in gold_toast:
                print('金币曝光余额不足toast提示校验失败')
        self.driver.wait_id('btnBack')
        self.btnBack()

    # 会员曝光
    def test_i_video_exposure_freevip(self):
        self.driver.find_id_click('tv_exposure')
        time.sleep(2)
        count = self.driver.find_id_text('free_count')
        if count == '当前剩余0次':
            self.driver.find_id_click('free_count')
            exp_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '曝光机会用完'
            assert check in exp_toast
        self.driver.find_id_click('free_count')
        time.sleep(2)
        try:
            self.driver.find_xpath('会员中心')
            self.btnBack()  # 返回曝光界面
        except:
            pass
        self.btnBack()#返回视频详情

    # 自定义钻石曝光
    def test_j_video_exposure_diamond(self):
        self.driver.find_id_click('tv_exposure')
        time.sleep(2)
        self.driver.find_ids_click('rl',-1)
        time.sleep(2)
        self.driver.find_id_send('edit','20000')
        time.sleep(1)
        self.driver.find_id_click('sure')
        time.sleep(2)
        self.driver.find_xpath('200钻曝光').click()
        time.sleep(2)
        self.driver.find_xpath('确定').click()
        time.sleep(2)
        self.driver.wait_xpath('钻石余额不足')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        self.driver.find_id_click('price_tv')
        time.sleep(2)
        self.driver.find_id_click('close_icon')
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)
        self.btnBack()

    # 视频评论
    def test_k_video_comments(self):
        while True:
            try:
                self.driver.find_id('comment_count')
                break
            except:
                self.driver.swip_up()
                self.driver.Background()
            time.sleep(2)

    # 发送评论
    def test_l_video_comment_send(self):
        self.driver.find_id_click('comment_count')
        time.sleep(2)
        self.driver.find_id_send('editContent','暖一个！')
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id('item_comment_video_more')
        except:
            self.driver.find_id_click('tv_comment')
        self.driver.wait_id('item_comment_video_more')
        time.sleep(2)
        self.driver.find_id_click('shunxu')
        time.sleep(2)

    # 评论举报
    def test_m_video_comment_report(self):
        self.driver.find_ids_click('item_comment_video_more',-1)
        time.sleep(2)
        self.driver.find_id_click('tv_action_one')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '举报'
            assert check_toast in toast,toast
        except:
            pass
        self.driver.find_id_click('item_comment_video_more')
        time.sleep(2)
        self.driver.find_id_click('tv_action_other')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','举报功能测试')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        try:
            toast1 = self.driver.wait_toast('//android.widget.Toast')
            assert check_toast in toast1
        except:
            pass
        time.sleep(2)

    # 评论列表上滑加载
    def test_n_video_comments_load(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id_click('follow_ta')
        time.sleep(2)

    # 点击合作配音
    def test_o_video_coor_dubbing(self):
        while True:
            try:
                self.driver.find_xpath('配音/合作').click()
                break
            except:
                self.btnBack()
                self.driver.swip_down()
                time.sleep(2)
                self.driver.find_id_click('film_img2')
                self.driver.Background()
            time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id('coor')
            self.driver.find_id_click('coor')
            while True:
                try:
                    #素材下载失败/素材已被删除
                    self.driver.wait_toast('//android.widget.Toast')
                    break
                except:
                    try:
                        self.driver.find_id('action')
                        break
                    except:
                        #限制素材进入配音界面显示限制弹窗
                        try:
                            self.driver.find_id('btnSubmit')
                            self.driver.find_id_click('btnSubmit')
                            break
                        except:
                            pass
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(3)
        except:
            print('未显示合作按钮')
        time.sleep(2)
        self.driver.find_id_click('close')
        time.sleep(2)

    # 视频详情界面进入素材预览界面
    def test_p_video_source(self):
        self.driver.find_id_click('tvsource')
        self.driver.wait_id('source_title')
        self.driver.Background()
        time.sleep(2)
        self.btnBack()

    # 作品分享
    def test_q_video_share(self):
        self.driver.find_id_click('tv_share')
        time.sleep(2)

        # 朋友圈
        self.loc.share_pyq()
        self.driver.wait_xpath('发表')
        self.driver.find_id_third_part('com.tencent.mm:id/dn')
        time.sleep(3)

        # qq空间
        self.driver.find_id_click('tv_share')
        time.sleep(2)
        self.loc.share_qq_zone()
        self.driver.wait_xpath('发表')
        self.driver.find_id_third_part('com.tencent.mobileqq:id/ivtitlebtnleft')
        time.sleep(3)

        # 点击新浪
        self.driver.find_id_click('tv_share')
        time.sleep(2)
        self.loc.share_sina()
        self.driver.wait_xpath('发送')
        time.sleep(2)
        self.driver.find_id_third_part('com.sina.weibo:id/titleBack')
        time.sleep(2)
        try:
            self.driver.find_xpath('不保存')
            self.driver.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        # 点击私信
        self.driver.find_id_click('tv_share')
        time.sleep(2)
        self.loc.share_message_friend()
        self.driver.wait_id_click('filter_edit')
        time.sleep(2)
        self.driver.find_id_send('filter_edit',"15697802")
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        time.sleep(2)
        try:
            self.driver.wait_id('userhead')
            name = self.driver.find_id_text('name')
            name2 = '米爱'
            if name == name2:
                self.driver.find_id_click('name')
                self.driver.wait_id('right_icon1')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
            else:
                print("未搜索到指定用户")
                time.sleep(2)
                self.driver.find_id_click('btnBack')
        except:
            self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 点击下载视频到本地
        self.driver.find_id_click('tv_share')
        self.loc.share_download()
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
                self.driver.wait_id_click('btnSubmit')
            except:
                try:
                    self.driver.wait_id_click('btnSubmit')
                except:
                    pass

        # 点击复制链接
        self.driver.find_id_click('tv_share')
        time.sleep(2)
        self.loc.share_copy_link()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.find_id('tv_action_one')
                self.driver.find_id_click('tv_action_one')
                self.driver.wait_id('txtContent')
                time.sleep(2)
                self.driver.find_id_click('btnSubmit')
            except:
                pass
        time.sleep(2)

        # 点击转发
        self.driver.find_id_click('tv_share')
        time.sleep(2)
        self.loc.share_forward()
        time.sleep(2)
        try:
            self.driver.find_id('reprint')
            self.driver.find_id_send('content',"不错，转发了！")
            time.sleep(2)
            self.driver.find_id_click('reprint')
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                try:
                    self.driver.find_id('reprint')
                    self.driver.find_id_click('reprint')
                    self.driver.wait_toast('//android.widget.Toast')
                except exception as e:
                    print(e)
        except:
            # 点击取消分享弹窗按钮
            self.loc.one_from_last()
        time.sleep(2)

    # 切换视频
    def test_r_video_switch(self):
        for i in range(10):
            self.driver.swip_up()
            self.driver.wait_id('userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.swip_left()
            self.driver.wait_id('ll_fan')
            self.btnBack()

    #热门作品标签
    def test_s_video_hot_work(self):
        while True:
            title = self.driver.find_id_text('tv_video_detail_title')
            hot_tv = 'ch'
            if hot_tv in title:
                self.driver.find_xpath('ch')
                try:
                    self.driver.find_id('txtTitle')
                    self.driver.find_id_click('btnBack')
                    time.sleep(2)
                except:
                    try:
                        self.driver.find_id('close')
                        self.driver.find_id_click('close')
                        break
                    except:
                        pass
            self.driver.swip_up()
            time.sleep(2)

class circle(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    #进入圈子界面
    def test_a_circle_into(self):
        self.driver.find_id_click('ivnewstab')
        time.sleep(2)

    #帖子浏览历史
    def test_b_circle_post_history(self):
        self.driver.find_id_click('history')
        time.sleep(2)

    #进入帖子详情
    def test_c_circle_post_detail(self):
        try:
            self.driver.find_id_click('title')
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.wait_id('userhead')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
        except exception as e:
            print(e)

    #历史记录帖子删除
    def test_d_circle_post_history_delete(self):
        delete_before = self.driver.find_id_text('title')
        el = 'title'
        self.driver.Long_Touche(el, 3000)
        time.sleep(1)
        self.driver.find_id_click('btnSubmit')
        time.sleep(2)
        try:
            self.driver.find_xpath(delete_before)
            print('帖子长按删除失败')
        except:
            pass
        time.sleep(2)

    #清空帖子浏览记录
    def test_e_circle_history_clear(self):
        try:
            self.driver.find_id('empty_text')
        except:
            self.driver.find_id_click('tv_right')
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.find_id('btnSubmit')
                time.sleep(2)
                try:
                    self.driver.find_id('title')
                    print('帖子清空失败')
                except:
                    pass
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    # 圈子主界面帖子转发
    def test_f_circle_post_forward(self):
        self.driver.find_id_click('action')
        time.sleep(2)
        self.loc.three_from_last()
        self.driver.wait_id('group_chat')
        self.driver.find_id_click('group_chat')
        time.sleep(2)
        self.driver.wait_id_click('name')
        self.driver.wait_id('btn_change_input_mode')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #圈子列表界面点击圈子标签
    def test_g_circle_tag(self):
        tag_name = self.driver.find_id_text('tag')
        self.driver.find_id_click('tag')
        self.driver.wait_id('img_subscribe')
        tag_detail_name = self.driver.find_id_text('topic_name')
        assert tag_detail_name == tag_name
        time.sleep(2)
        self.driver.find_id_click('back')
        time.sleep(2)

    #圈子热门帖子列表界面点击评论按钮进入帖子详情
    def test_h_circle_comment_detail(self):
        self.driver.find_id_click('comment')
        self.driver.wait_id('guanzhu')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #圈子热门帖子列表界面点赞
    def test_i_circle_good(self):
        self.driver.swip_up()
        time.sleep(1)
        touche_good_before = self.driver.find_id_text('good')
        self.driver.find_id_click('good')
        time.sleep(2)
        touche_good_later = self.driver.find_id_text('good')
        if int(touche_good_later) > int(touche_good_before):
            pass
        else:
            print('点赞数量未变化',touche_good_before,touche_good_later)
        time.sleep(2)

    # 点击帖子内容进入帖子详情
    def test_j_circle_content(self):
        self.driver.find_id_click('content')
        self.driver.wait_id('right_icon1')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #圈子热门列表刷新
    def test_k_circle_refresh(self):
        for i in range(5):
            self.driver.swip_up()
        time.sleep(1)
        #一键返回列表顶部
        self.driver.find_id_click('ivnewstab')
        self.driver.wait_id('tv_key_word_help')
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)

    #圈子搜索界面显示
    def test_m_circle_search(self):
        i = 0
        while True:
            self.driver.find_id_click('tv_key_word_help')
            try:
                self.driver.wait_id('tv')
                break
            except:
                #界面显示失败时返回上一界面再进
                self.driver.find_id_click('btnBack')
            #尝试10次后停止以上操作
            if i == 10:
                break
            else:
                pass
            time.sleep(2)

    #帖子搜索界面热门话题点击跳转
    def test_n_circle_hot_tv_jump(self):
        tvs = self.driver.find_ids('tv')
        for i in range(len(tvs)):
            tv_name = self.driver.find_ids_text('tv',i)
            self.driver.find_ids_click('tv',i)
            self.driver.wait_id('img_subscribe')
            tv_detail_name = self.driver.find_id_text('topic_name')
            assert tv_detail_name in tv_name, '标签名称校验不一致'
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)

    #已订阅的话题
    def test_o_circle_topic_subscribes(self):
        try:
            self.driver.find_id_click('title')
            name = self.driver.find_id_text('title')
            self.driver.find_id_click('title')
            self.driver.wait_id('img_subscribe')
            tv_detail_name = self.driver.find_id_text('topic_name')
            assert tv_detail_name in name, '标签名称校验不一致'
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
        except:
            pass

    #话题搜索
    def test_p_circle_topic_search(self):
        self.driver.find_id_clear('et_key_word')
        time.sleep(1)
        self.driver.find_id_send('et_key_word','测试')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        time.sleep(2)
        self.driver.find_id_click('title')
        self.driver.wait_id('img_subscribe')
        check = '测试'
        tv_detail_name = self.driver.find_id_text('topic_name')
        assert check in tv_detail_name, '标签名称校验不一致'
        self.driver.find_id_click('back')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #圈子主界面发帖-图文贴
    def test_q_circle_home_word_topic(self):
        self.driver.find_id_click('send')
        time.sleep(2)
        self.driver.find_id_click('image_tie')
        time.sleep(4)

    #图文贴内容
    def test_r_circle_word_topic_content(self):
        topic_read = file.read()
        self.driver.find_id_send('content',(topic_read,'\n'))
        time.sleep(2)
        self.driver.find_id_clear('content')
        time.sleep(2)
        self.driver.find_id_send('content',(topic_read,'\n'))
        time.sleep(2)

    #添加图片
    def test_s_circle_word_topic_add_image(self):
        self.driver.find_id_click('add_img')
        time.sleep(2)

    #选择图片
    def test_t_circle_word_topic_select_image(self):
        self.driver.find_id_click('tv_photo')
        self.driver.wait_id('imgQueue')
        num = self.driver.find_ids('cb_select_tag')
        for i in range(len(num)):
            self.driver.find_ids_click('cb_select_tag',i)
            try:
                self.driver.wait_toast('//android.widget.Toast')
                break
            except:
                pass
        time.sleep(1)
        self.driver.find_id_click('next_step_tv')
        time.sleep(2)
        self.driver.find_id_click('del')
        time.sleep(2)

    # 拍照
    def test_u_circle_word_topic_photo(self):
        self.driver.find_id_click('tv_take_photo')
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('next')
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
            self.driver.find_id_click('com.oppo.camera:id/shutter_button')
            time.sleep(4)
            self.driver.find_id_click('com.oppo.camera:id/done_button')
            self.driver.wait_id('right_icon1')
        except:
            try:

                self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                time.sleep(4)
                self.driver.find_id_click('com.huawei.camera:id/done_button')
            except:
                try:
                    self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                    time.sleep(4)
                    self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                except:
                    pass
        time.sleep(2)

    #添加话题
    def test_v_circle_word_topic_insert_topic(self):
        self.driver.find_id_click('add_topic')
        self.driver.wait_id('tv')
        self.driver.find_id_send('et_key_word','一个人的话题')
        time.sleep(1)
        self.driver.find_id_click('btnSearch')
        time.sleep(2)
        self.driver.wait_id_click('title')
        time.sleep(2)

    #添加好友
    def test_w_circle_word_topic_at(self):
        self.driver.find_id_click('at')
        time.sleep(2)
        self.driver.find_id_send('filter_edit','16461675')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        time.sleep(2)
        try:
            self.driver.find_id('no_data_msg')
            self.driver.find_id_click('btnBack')
        except:
            self.driver.find_id_click('name')
        time.sleep(2)

    #发布图文帖
    def test_x_circle_word_topic_release(self):
        self.driver.find_id_click('right_icon1')
        try:
            self.driver.wait_id('img_subscribe')
            self.driver.swip_down()
            time.sleep(2)
            self.driver.find_id_click('content')
            self.driver.wait_id('editContent')
        except:
            self.driver.find_id_click('btnBack')
            print('帖子发布失败')
        time.sleep(2)

    #删除图文帖
    def test_y_circle_word_topic_delete(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        assert del_toast == check
        self.driver.find_id_click('back')
        time.sleep(2)

    #发布语音帖
    def test_z_circle_home_voice_topic(self):
        self.driver.find_id_click('send')
        time.sleep(2)
        self.driver.find_id_click('voice_tie')
        time.sleep(2)


    #录制语音
    def test_z_a_circle_voice_topic_record(self):
        self.driver.find_id_click('dubbing')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #试听
        self.driver.find_id_click('review')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #重录
        self.driver.find_id_click('reDo')
        time.sleep(2)
        date_check = '00:00'
        el = self.driver.find_id_text('time')
        if el != date_check:
            print('点击重录按钮音轨没有恢复默认状态')
        time.sleep(2)
        self.driver.find_id_click('dubbing')
        time.sleep(10)
        self.driver.Background()
        time.sleep(4)

    #语音帖发布界面
    def test_z_b_circle_voice_topic_next(self):
        self.driver.find_id_click('tv_right')
        self.driver.wait_id('play')
        time.sleep(2)
        self.driver.find_id_send('content','有什么好说的呢？么有哦~')
        time.sleep(2)
        self.driver.find_id_click('play')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('change_cover')
        time.sleep(2)
        self.driver.find_id_click('tv_photo')
        self.driver.wait_id_click('photo_wall_item_photo')
        time.sleep(2)


    #圈子主页发布听评帖
    def test_z_c_circle_home_listen_topic(self):
        self.driver.find_id_click('send')
        time.sleep(2)
        self.driver.find_id_click('film_tie')
        time.sleep(2)

    #听评帖添加作品
    def test_z_d_circle_listen_insert_work(self):
        self.driver.find_id_click('add_img')
        self.driver.wait_id('filmBg')
        self.driver.find_id_click('myLike')
        time.sleep(2)
        self.driver.wait_id_click('filmBg')
        self.driver.wait_id('playBtn')
        self.driver.find_id_click('btnSelect')
        time.sleep(2)

class society(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = BaseOperate()
        # self.x = self.driver.touch_X()
        # self.y = self.driver.touch_Y()
        # self.id = resource_id
        # self.d = dub()
        # self.home_enter = home_function()
        # self.l = live()
        # self.f = follow()
        # self.m = material()
        # self.p = person()
        # self.v = video_detail()
        # self.c = circle()
        # self.s = society()
        self.driver = BaseOperate()
        self.loc = location()
        self.y = self.driver.touch_Y()
        self.x = self.driver.touch_X()

    @classmethod
    def tearDownClass(self):
        pass

    #点击进入社团主界面
    def test_a_society_home(self):
        self.driver.find_id_click('society')
        self.driver.wait_id('userhead')
        time.sleep(2)

    #我的社团-检查是否拥有社团
    def test_b_society_my_society(self):
        self.driver.find_id_click('ivMineTab')
        time.sleep(2)
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_fan')
        num = self.driver.find_id_text('societyCount')
        check = '0'
        if num == check:
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('ivnewstab')
            time.sleep(2)
        else:
            self.driver.find_id_click('ll_society')
            time.sleep(2)
            self.driver.wait_id('status_icon')
            societys = self.driver.find_ids('username')
            list_society = []
            for i in range(len(societys)):
                title = self.driver.find_ids_text('username',i)
                list_society.append(title)
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('ivnewstab')
            time.sleep(2)
            print(list_society)

    '''我的社团聊天-文字'''
    def test_c_society_group_chat(self):
        self.driver.find_id_click('time')
        self.driver.wait_id('btn_change_input_mode')
        select = random.choice('社团聊天文字测试')
        self.driver.find_id_send('editContent',select)
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            self.driver.wait_id('content')
            check = self.driver.find_ids_text('content',-1)
            assert select == check,'发送文字校验不一致'
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #我的社团聊天-语音
        self.driver.find_id_click('time')
        self.driver.wait_id_click('btn_change_input_mode')
        time.sleep(2)
        el = 'btn_record_voice'
        #发送60s语音
        self.driver.Long_Touche(el, 60000)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            self.driver.wait_id('btn_play_sound_content_layout')
            self.driver.find_ids_click('btn_play_sound_content_layout',-1)
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                pass
        time.sleep(2)
        #录制语音过程中上滑取消
        self.driver.long_press_move(el, self.x * 0.5, self.y * 0.5)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #我的社团聊天-发送表情
        self.driver.find_id_click('time')
        self.driver.wait_id_click('btn_send_smile')
        time.sleep(2)
        emoji = self.driver.find_ids('emojicon_icon')
        for i in range(len(emoji)):
            self.driver.find_ids_click('emojicon_icon',i)
        time.sleep(2)
        self.driver.find_id_click('btn_send')
        self.driver.wait_id('content')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #我的社团聊天-其它按钮
        self.driver.find_id_click('time')
        self.driver.wait_id('btn_change_input_mode')
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('photo')
        time.sleep(4)
        self.driver.find_id_click('cb_select_tag')
        time.sleep(2)
        self.driver.find_id_click('next_step_tv')
        self.driver.wait_id('chat_image')
        time.sleep(2)

        # 拍照发送私信信息
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('camera')
        time.sleep(4)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id_click('com.oppo.camera:id/shutter_button')
            time.sleep(4)
            self.driver.find_id_click('com.oppo.camera:id/done_button')
        except:
            try:

                self.driver.find_id_click('com.android.camera:id/done_button')
            except:
                try:

                    self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                    time.sleep(4)
                    self.driver.find_id_click('com.huawei.camera:id/done_button')
                except:
                    try:
                        self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                        time.sleep(4)
                        self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                    except:
                        pass
        self.driver.wait_id('chat_image')
        time.sleep(2)

        # 发送作品
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('film')
        self.driver.wait_id('filmBg')
        self.driver.find_id_click('myLike')
        self.driver.wait_id_click('filmBg')
        self.driver.Background()
        self.driver.find_id_click('btnSelect')
        time.sleep(2)
        self.driver.swip_up()
        self.driver.wait_id('chat_film_title')
        time.sleep(2)

        # 发送红包
        self.driver.find_id_click('show_action')
        time.sleep(2)
        self.driver.find_id_click('redpacket')
        time.sleep(2)
        self.driver.find_id_send('cash_num','0.1')
        time.sleep(2)
        self.driver.find_id_send('people_num','1')
        time.sleep(3)
        self.driver.find_id_click('generate_red_packet')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        self.driver.wait_id_click('red_packet')
        time.sleep(2)
        self.driver.find_id_click('open_red_packet_btn')
        self.driver.wait_id('diamond')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #我的社团-活动-每日活动
    def test_d_society_activity_day(self):
        self.driver.find_id_click('time')
        self.driver.wait_id('btn_change_input_mode')
        self.driver.find_xpath('活动').click()
        time.sleep(2)
        title = self.driver.find_id_text('desc')
        if title == '给社团成员作品点赞2次':
            # 点赞两次
            self.driver.find_id_click('task_box')
            time.sleep(2)
            try:
                self.driver.find_id('btn_close')
                self.driver.find_id_click('btn_close')
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('给社团成员作品点赞2次')
            except:
                self.driver.wait_id('filmBg')
                self.driver.find_ids_click('filmBg',0)
                self.driver.wait_id('tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id_click('tv_good1')
                except:
                    self.driver.find_id_click('tv_good')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_ids('filmBg', 1)
                self.driver.wait_id('tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id_click('tv_good1')
                except:
                    self.driver.find_id_click('tv_good')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '评论社团成员的作品2次':
            # 社团作品评论两次
            self.driver.find_id_click('task_box')
            time.sleep(2)
            try:
                self.driver.find_id('btn_close')
                self.driver.find_id_click('btn_close')
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('评论社团成员的作品2次')
            except:
                self.driver.wait_id('filmBg')
                self.driver.find_ids_click('filmBg',0)
                self.driver.wait_id('tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id_click('tv_comment')
                time.sleep(2)
                self.driver.find_id_send('editContent','作品评论')
                time.sleep(2)
                self.driver.find_id_click('btn_send')
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    assert check_toast in toast, '评论发送失败'
                except:
                    pass
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_ids_click('filmBg',1)
                self.driver.wait_id('tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id_click('tv_comment')
                time.sleep(2)
                self.driver.find_id_send('editContent','作品评论')
                time.sleep(2)
                self.driver.find_id_click('btn_send')
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    assert check_toast in toast, '评论发送失败'
                except:
                    pass
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '与社团成员完成合作作品':
            # 完成社团合作
            self.driver.find_id_click('task_box')
            time.sleep(2)
            try:
                self.driver.find_id('btn_close')
                self.driver.find_id_click('btn_close')
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('与社团成员完成合作作品')
            except:
                self.driver.wait_id('filmBg')
                self.driver.find_xpath('求合作')
                self.driver.wait_id_click('btnCooperate')
                while True:
                    try:
                        self.driver.find_id('btnSubmit')
                        self.driver.find_id_click('btnSubmit')
                        break
                    except:
                        try:
                            self.driver.find_id('action')
                            break
                        except:
                            pass
                self.driver.find_id_click('action')
                self.driver.wait_download('title')
                self.driver.Background()
                self.driver.find_id_click('complete')
                self.driver.wait_id('pri_switch_tv')
                self.driver.swip_up()
                self.driver.find_id_click('check_box_add_square')
                time.sleep(2)
                self.driver.find_id_click('uploadbtn')
                self.driver.wait_download('down')
                self.driver.find_id_click('ivnewstab')
                time.sleep(2)
                self.driver.find_id_click('society')
                time.sleep(2)
                self.driver.find_id_click('time')
                self.driver.wait_id('btn_change_input_mode')
                self.driver.find_xpath('活动').click()
                time.sleep(2)

    #我的社团-活动-历时活动
    def test_e_society_activity_week(self):
        self.driver.swip_up()
        time.sleep(2)

        # 社团活动查看历时素材
        try:
            self.driver.find_id('film_look')
            self.driver.find_id_click('film_look')
            self.driver.wait_id('userhead')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('playBtn')
            self.driver.wait_download('playBtn')
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        # 社团活动社长添加活动素材
        try:
            self.driver.find_id('choice_source')
            self.driver.find_id_click('choice_source')
            self.driver.wait_id('txtKeyword')
            self.driver.find_id_send('txtKeyword','配音')
            self.driver.find_id_click('btnSearch')
            self.driver.wait_id_click('iv_source')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '创建成功'
            check1 = '配音秀:创建成功'
            if toast != check and toast != check1:
                self.driver.find_id_click('btnBack')
        except:
            pass
        time.sleep(2)

        # 社团活动素材配音
        self.driver.find_id_click('dubbing')
        try:
            self.driver.find_id('btn_close')
            self.driver.find_id_click('btn_close')
        except:
            pass
        try:
            self.driver.find_id('complete_count')
        except:
            while True:
                try:
                    self.driver.find_id('btnSubmit')
                    self.driver.find_id_click('btnSubmit')
                    try:
                        self.driver.find_id('roleall')
                        self.driver.find_id_click('roleall')
                    except:
                        pass
                    break
                except:
                    try:
                        self.driver.find_id('action')
                        break
                    except:
                        try:
                            self.driver.find_id('roleall')
                            self.driver.find_id_click('roleall')
                            break
                        except:
                            pass
            time.sleep(2)
            self.driver.find_id_click('action')
            self.driver.wait_download('title')
            self.driver.Background()
            self.driver.find_id_click('complete')
            self.driver.wait_id('pri_switch_tv')
            self.driver.swip_up()
            try:
                self.driver.find_id('check_box_add_square')
                self.driver.find_id_click('check_box_add_square')
            except:
                pass
            time.sleep(2)
            self.driver.find_id_click('uploadbtn')
            self.driver.wait_download('exposure')
            self.driver.find_id_click('ivnewstab')
            time.sleep(2)
            self.driver.find_id_click('society')
            time.sleep(2)
            self.driver.find_id_click('time')
            self.driver.wait_id('btn_change_input_mode')
            self.driver.find_xpath('活动').click()
            time.sleep(2)

    #我的社团-榜单
    def test_f_society_rank(self):
        self.driver.find_xpath('榜单').click()
        time.sleep(2)
        try:
            self.driver.find_id('username')
            self.driver.find_id_click('username')
            self.driver.wait_id('ll_fan')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('look_rank')
        self.driver.wait_id('tv_right')
        time.sleep(2)
        try:
            self.driver.find_id('username1')
            self.driver.find_id_click('userHead1')
            self.driver.wait_id('ll_fan')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        ranks = self.driver.find_ids('img_rank')
        for i in range(len(ranks)):
            self.driver.find_ids_click('img_rank',i)
            self.driver.wait_id('tv_right')
            self.driver.find_id_click('btnBack')
            time.sleep(1)
        time.sleep(2)

    #我的社团-社团空间
    def test_g_society_space(self):
        self.driver.find_id_click('btn_space_jump')
        self.driver.wait_id('ll_fan')
        #社团空间-头像
        self.driver.find_id_click('userhead')
        time.sleep(2)
        try:
            self.driver.find_id('tv_id')
        except:
            print ('社团id信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id('tv_nickname')
        except:
            print('社团昵称信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id('tv_sign')
        except:
            print ('社团简介信息未显示')
        time.sleep(2)
        #举报
        self.driver.find_id_click('tv_right')
        time.sleep(2)
        self.driver.find_id_click('tv_action_other')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','测试')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        try:
            report_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in report_toast, '举报失败'
        except:
            pass
        time.sleep(2)

        #社团空间-社团财富
        self.driver.find_id_click('gold_match')
        time.sleep(2)
        try:
            self.driver.find_id('tv_gold')
            try:
                self.driver.find_id('tv_diamond')
            except:
                print ('社团财富界面未显示余额信息')
        except:
            print ('社团财富界面未显示余额信息')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #社团空间-聊天
        self.driver.find_id_click('photo')
        time.sleep(2)
        self.driver.wait_id('editContent')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        # 设置关注区权限
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.six_from_last()
        time.sleep(2)
        self.driver.find_id_click('check')
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print ('动态开关设置后没有toast提示')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #特别关注
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.five_from_last()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print ('特别关注没有toast提示')
        time.sleep(2)

        #消息免打扰
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.four_from_last()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            print('消息免打扰没有toast提示')
        time.sleep(2)

        #添加社团素材
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(2)
        self.driver.wait_id_click('iv_source')
        time.sleep(2)
        self.driver.Background()
        self.driver.find_id_click('btnSelect')
        insert_toast = self.driver.wait_toast('//android.widget.Toast')
        if insert_toast == '该素材存在':
            self.driver.find_id_click('btnCancelselect')
            time.sleep(2)
            self.driver.find_id_click('btnBack')
        time.sleep(2)

        #管理/退出社团
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        try:
            self.driver.find_id('btnSubmit')
            self.driver.find_id_click('btnCancel')
        except:
            self.driver.find_id_click('btnBack')
        time.sleep(2)

        #社团空间-粉丝
        self.driver.find_id_click('ll_fan')
        self.driver.wait_id('status_icon')
        status = self.driver.find_ids('status_icon')
        for i in range(len(status)):
            self.driver.find_ids_click('status_icon',i)
            time.sleep(1)
        user_name = self.driver.find_ids_text('username',-1)
        self.driver.find_ids_click('username',-1)
        self.driver.wait_id('ll_fan')
        user_name1 = self.driver.find_id_text('username')
        self.driver.find_id_click('btnBack')
        assert user_name == user_name1,'粉丝列表用户名与空间用户名校验失败'
        time.sleep(2)
        user_list = self.driver.find_ids('username')
        new_user_list = []
        for i in range(len(user_list)):
            name = self.driver.find_ids_text('username',i)
            new_user_list.append(name)
        time.sleep(1)
        d_user_list = dict(counter(new_user_list))
        for key,value in d_user_list.items():
            if value > 1:
                print(key,'粉丝列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #社团空间-成员
        self.driver.find_id_click('ll_member')
        self.driver.wait_id('manager')
        user_name = self.driver.find_ids_text('name',-1)
        self.driver.find_ids_click('userhead',-1)
        self.driver.wait_id('ll_fan')
        user_name1 = self.driver.find_id_text('username')
        self.driver.find_id_click('btnBack')
        assert user_name == user_name1,'成员列表用户名与空间用户名校验失败'
        time.sleep(2)
        user_list = self.driver.find_ids('username')
        new_user_list = []
        for i in range(len(user_list)):
            name = self.driver.find_ids_text('name',i)
            new_user_list.append(name)
        time.sleep(1)
        d_user_list = dict(counter(new_user_list))
        for key, value in d_user_list.items():
            if value > 1:
                print(key, '成员列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #社团空间-社团作品
        self.driver.find_id_click('filmBg')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #社团空间-社团素材
        self.driver.find_id_click('btnMember')
        time.sleep(2)
        count = self.driver.find_id_text('film_all_count')
        num = re.findall(r'素材(.*)',count)
        new = "".join(num)
        if new != '0':
            time.sleep(2)
            self.driver.find_id_click('imgSource')
            self.driver.wait_id('shouchang_tv_fake')
            self.driver.Background()
            self.driver.find_id_click('btnBack')
            time.sleep(2)
            self.driver.find_id_click('imgTip')
            while True:
                try:
                    self.driver.find_id('btnSubmit')
                    self.driver.find_id_click('btnSubmit')
                    try:
                        self.driver.find_id('roleall')
                        self.driver.find_id_click('roleall')
                    except:
                        pass
                    break
                except:
                    try:
                        self.driver.find_id('roleall')
                        self.driver.find_id_click('roleall')
                        break
                    except:
                        try:
                            self.driver.find_id_click('action')
                            break
                        except:
                            pass
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id_click('back')
            time.sleep(2)
            self.driver.find_id_click('btnSubmit')
            time.sleep(2)

        #社团空间-合辑
        self.driver.find_id_click('btnCollect')
        time.sleep(2)
        count = self.driver.find_id_text('film_all_count')
        num = re.findall(r'合辑(.*)', count)
        new = ''.join(num)
        if new != '0':
            self.driver.find_id_click('filmBg')
            try:
                self.driver.wait_id('username')
                self.driver.find_id_click('filmBg')
                self.driver.wait_id('tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id('follow_ta')
                    self.driver.find_id_click('follow_ta')
                    try:
                        follow_toast = self.driver.wait_toast('//android.widget.Toast')
                        check = '社团成员不可取消关注'
                        assert check in follow_toast
                    except:
                        pass
                except:
                    pass
                time.sleep(2)
                self.driver.find_id_click('btnBack')
                time.sleep(2)
                self.driver.find_id_click('btnBack')
            except exception as e:
                print(e)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #社团管理
    def test_h_society_manager(self):
        self.driver.find_id_click('tv_key_word_help')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','141095541')
        self.driver.find_id_click('btnSearch')
        time.sleep(1)
        self.driver.wait_id_click('userhead')
        self.driver.wait_id('ll_fan')
        self.driver.find_id_click('btnRight')
        time.sleep(2)
        self.loc.two_from_last()
        self.driver.wait_id('userhead')
        time.sleep(2)

    #社团管理-编辑资料
    def test_i_society_edit_info(self):
        self.driver.find_id_click('edit_profile')
        time.sleep(2)
        # 点击头像-拍照
        self.driver.find_id_click('userhead')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(2)
        try:
            self.driver.find_id('next')
            self.driver.find_id_click('next')
            try:
                self.driver.wait_sys('始终允许')
            except:
                try:
                    self.driver.wait_sys('允许')
                except:
                    pass
            self.driver.find_id_click('userhead')
            time.sleep(2)
            self.loc.three_from_last()
            time.sleep(2)
        except:
            pass
        time.sleep(3)
        try:
            '''
            以下操作只适用vivox9
            '''
            self.driver.find_id_click('com.android.camera:id/shutter_button')
            self.driver.find_id_click('com.android.camera:id/shutter_button')
            time.sleep(4)
            self.driver.find_id_click('com.android.camera:id/done_button')
        except:
            try:
                '''
                oppo r11
                '''
                self.driver.find_id_click('com.oppo.camera:id/shutter_button')
                self.driver.find_id_click('com.oppo.camera:id/shutter_button')
                time.sleep(4)
                self.driver.find_id_click('com.oppo.camera:id/done_button')
            except:
                try:
                    self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                    self.driver.find_id_click('com.huawei.camera:id/shutter_button')
                    time.sleep(4)
                    self.driver.find_id_click('com.huawei.camera:id/done_button')
                except:
                    try:
                        self.driver.find_id_third_part('com.android.camera:id/v9_shutter_button_internal')
                        time.sleep(4)
                        self.driver.find_id_third_part('com.android.camera:id/intent_done_apply')
                    except:
                        pass
        time.sleep(6)
        self.driver.find_id_click('confirm')
        time.sleep(2)

        #修改社团名称
        before_name = self.driver.find_id_text('society_name')
        time.sleep(2)
        self.driver.find_id_send('society_name','属于我自己的社团哦~')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        try:
            fail_toast = self.driver.wait_toast('//android.widget.Toast')
            fail_check = '社团名称只支持空格、中英文、数字'
            assert fail_check in fail_toast
        except:
            pass
        time.sleep(2)
        self.driver.find_id_send('society_name',before_name)
        time.sleep(2)

        #社团简介
        self.driver.find_id_send('brief_content','这是一个严肃的社团简介~')
        time.sleep(2)

        #社团频道
        self.driver.find_ids_click('tv',-1)
        self.driver.wait_id('edit_text')
        try:
            self.driver.find_id('tv1')
            self.driver.find_id_click('tv1')
            time.sleep(2)
        except:
            pass
        self.driver.find_id_send('edit_text','测试')
        time.sleep(2)
        self.driver.find_id_click('btn_search')
        time.sleep(2)
        self.driver.find_id_click('tv')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        time.sleep(2)

        #完成社团资料修改
        self.driver.find_id_click('tv_right')
        try:
            edit_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            assert check in edit_toast
            time.sleep(2)
        except:
            pass

    #社团管理-社团成员
    def test_j_society_members(self):
        self.driver.find_id_click('userhead')
        self.driver.wait_id('shezhang')
        self.driver.find_id_click('userhead')
        self.driver.wait_id('ll_fan')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        #添加成员
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.driver.wait_id('ischeck')
        #搜索用户
        self.driver.find_id_send('filter_edit','15697799')
        time.sleep(2)
        self.driver.find_id_click('btnSearch')
        self.driver.wait_xpath('大黑')
        self.driver.find_id_click('ischeck')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        invited_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        try:
            self.driver.find_id('ischeck')
            self.driver.find_id_click('btnBack')
        except:
            pass
        assert check in invited_toast, '社团成员邀请发送失败'
        time.sleep(2)

        #社团管理-成员权限
        self.driver.find_id_click('more')
        time.sleep(2)
        # 社团管理权限
        self.driver.find_id_click('check_box1')
        time.sleep(1)
        state1 = self.driver.find_id_state('check_box1')
        time.sleep(1)
        self.driver.find_id_click('check_box2')
        time.sleep(1)
        state2 = self.driver.find_id_state('check_box2')
        time.sleep(2)
        self.driver.find_id_click('save')
        save_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '保存成功'
        assert check in save_toast
        time.sleep(2)
        if state1 == 'true':
            try:
                self.driver.find_id('power')
            except:
                print('开启社团管理权限后，成员一栏中未显示管理图标')
        elif state1 == 'false':
            try:
                self.driver.find_id('power')
                print('关闭社团管理权限后，成员一栏中依然显示管理图标')
            except:
                pass
        time.sleep(2)
        if state2 == 'true':
            try:
                self.driver.find_id('comic')
            except:
                print('开启社团声漫权限后，成员一栏中未显示声漫制作图标')
        elif state2 == 'false':
            try:
                self.driver.find_id('comic')
                print('关闭社团声漫权限后，成员一栏中依然显示声漫制作图标')
            except:
                pass
        time.sleep(2)

        #社团管理-移除成员
        self.driver.Long_Touche('username', -1, 2000)
        time.sleep(2)
        self.driver.find_id_click('txtContent')
        content = self.driver.find_id_text('txtContent')
        check = '移出'
        assert check in content
        time.sleep(2)
        self.driver.find_id_click('btnCancel')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #社团管理-社团公告
    def test_k_society_announcement(self):
        self.driver.find_id_click('edit_gonggao')
        time.sleep(2)
        choice = random.choice('这是一个严肃的社团公告')
        self.driver.find_id_send('content',choice)
        time.sleep(2)
        self.driver.find_id_click('complete')
        gonggao_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        assert check in gonggao_toast
        check_content = self.driver.find_id_text('tv_gonggao')
        if check_content != choice:
            print('社团公告修改后文案显示不正确',choice)
        time.sleep(2)

    #社团作品-作品管理
    def test_l_society_work_manager(self):
        self.driver.find_id_click('film_manage')
        self.driver.wait_id('filmBg')
        #审核标准协议
        self.driver.find_id_click('middle')
        self.driver.wait_id_click('btnClose')
        time.sleep(2)

        #社团作品-添加作品
        self.driver.find_id_click('addFilm')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_ids_click('android:id/title',1)
        time.sleep(2)
        #作品标题
        self.driver.find_id_send('title','随便传个社团原创作品')
        time.sleep(2)
        #作品封面
        self.driver.find_id_click('upload_cover')
        self.driver.wait_id_click('photo_wall_item_photo')
        self.driver.wait_id_click('confirm')
        time.sleep(2)
        #添加配音表用户
        self.driver.find_id_click('mem')
        time.sleep(2)
        self.driver.find_id_send('role','我')
        time.sleep(2)
        self.driver.find_id_click('add_mem')
        self.driver.wait_id_click('userhead')
        time.sleep(2)
        #添加作品频道
        self.driver.find_id_click('tv')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
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
                self.driver.find_id('filmBg')
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
        self.driver.find_id_click('filmBg')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id_click('setting')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        delete_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '删除作品成功'
        assert check in delete_toast
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)

    #社团作品-创建合辑
    def test_m_society_create_collection(self):
        self.driver.find_id_click('tab2')
        time.sleep(2)
        self.driver.find_id_click('addFilm')
        time.sleep(2)
        self.loc.three_from_last()
        time.sleep(2)
        self.driver.find_id_send('content','测试合辑')
        time.sleep(2)
        self.driver.find_id_click('ok')
        self.driver.wait_id('choice')
        time.sleep(2)
        select = self.driver.find_ids('choice')
        for i in range(len(select)):
            self.driver.find_ids_click('choice',i)
        time.sleep(2)
        self.driver.find_id_click('tv_right')
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
    def test_n_society_edit_collection(self):
        self.driver.find_id_click('title')
        time.sleep(2)
        #点击合辑作品
        self.driver.find_id_click('img')
        self.driver.wait_id('tv_video_detail_title')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #长按调节作品列表
        self.driver.Long_Touche('img',3000)
        time.sleep(2)
        self.driver.find_id_click('tv_zhiding')
        try:
            zd_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '第一个位置'
            assert check in zd_toast
        except:
            pass
        time.sleep(2)
        self.driver.Long_Touches('img', -1, 2000)
        time.sleep(2)
        self.driver.find_id_click('tv_zhiding')
        try:
            sy_toast = self.driver.wait_toast('//android.widget.Toast')
            check1 = '上移成功'
            assert check1 in sy_toast
        except:
            pass
        time.sleep(2)

        #移除作品
        self.driver.Long_Touche('img', 2000)
        time.sleep(2)
        self.driver.find_id_click('tv_shanchu')
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast != '无权操作' and del_toast != '删除失败':
            print('合辑作品移除失败')

        #添加合辑作品
        self.driver.find_id_click('right_icon1')
        self.driver.wait_id('choice')
        title_before = self.driver.find_id_text('title')
        self.driver.find_id_click('choice')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        add_toast = self.driver.wait_toast('//android.widget.Toast')
        check3 = '添加成功'
        if check3 not in add_toast:
            print('合辑作品添加',add_toast)
        time.sleep(2)
        try:
            self.driver.find_xpath(title_before)
        except:
            print('合辑作品列表未显示添加的新作品')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

        #我的社团-编辑合辑
        self.driver.Long_Touche('filmBg', 2000)
        time.sleep(2)
        #合辑置顶
        self.loc.three_from_last()
        zhiding_toast = self.driver.wait_toast('//android.widget.Toast')
        zhiding_check = '成功'
        if zhiding_check not in zhiding_toast:
            print('合辑置顶',zhiding_toast)
        time.sleep(2)

        #删除合辑
        self.driver.Long_Touche('filmBg', 2000)
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        self.driver.find_id_click('btnSubmit')
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast == '无权操作' or del_toast == '删除成功':
            pass
        else:
            print('合辑删除失败')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #我的社团-申请蓝v
    def test_o_society_v(self):
        self.driver.find_id_click('apply_lv')
        time.sleep(2)
        try:
            self.driver.find_xpath('立即申请')
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        except:
            pass

    #我的社团-入社权限
    def test_p_society_entry_conditions(self):
        self.driver.find_id_click('society_apply_jurisdiction')
        time.sleep(2)
        #招募内容
        self.driver.find_id_click('modify')
        time.sleep(2)
        self.driver.find_id_send('content','本社团并不招人')
        time.sleep(2)
        self.driver.find_id_click('complete')
        time.sleep(2)
        #申请要求
        self.driver.find_id_click('addFilm')
        time.sleep(1)
        self.driver.find_id_click('addSource')
        time.sleep(1)
        #入社申请开关
        self.driver.find_id_click('choice')
        time.sleep(1)
        self.driver.find_id_click('choice1')
        time.sleep(1)
        self.driver.find_id_click('choice2')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        time.sleep(2)
        #我的社团-社团消息通知开关
        self.driver.find_id_click('btn_push')
        time.sleep(2)

    #我的社团-社团财富、社团钱包
    def test_q_society_wealth(self):
        self.driver.swip_up()
        self.driver.find_id_click('gold_match')
        time.sleep(2)
        # 分配钻石
        self.driver.find_id_click('distribution_diamond')
        self.driver.wait_id_click('userhead')
        time.sleep(2)
        self.driver.find_id_send('gold_count','100')
        time.sleep(2)
        self.driver.find_id_send('remark','分配钻石')
        time.sleep(2)
        self.driver.find_id_click('sure')
        diamond_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '钻石'
        if check not in diamond_toast:
            print('社团分配钻石',diamond_toast)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        # 分配金币
        self.driver.find_id_click('distribution_gold')
        self.driver.wait_id_click('userhead')
        time.sleep(2)
        self.driver.find_id_send('gold_count','10000')
        time.sleep(2)
        self.driver.find_id_send('remark','分配金币')
        time.sleep(2)
        self.driver.find_id_click('sure')
        gold_toast = self.driver.wait_toast('//android.widget.Toast')
        check1 = '金币'
        if check1 not in gold_toast:
            print('社团分配金币', gold_toast)
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    def test_r_society_works_download(self):
        # 我的社团-允许他人下载社团作品
        self.driver.find_id_click('btn_load')
        time.sleep(2)
        self.driver.find_id_click('btn_load')
        time.sleep(2)

        #我的社团-社团管理须知
        self.driver.find_xpath('《社团管理须知》')
        self.driver.wait_id('titlebar')
        self.driver.find_id_click('btnBack')
        time.sleep(2)

    #我的社团-转让社团/解散社团
    def test_s_society_transfer_dissolved(self):
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.three_from_last()
        self.driver.wait_xpath('转让社团')
        self.driver.find_ids_click('username', -1)
        time.sleep(2)
        transfer_content = self.driver.find_id_text('txtContent')
        check = '您确定要将社团转让给'
        if check not in transfer_content:
            print(transfer_content)
        self.driver.find_id_click('btnCancel')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('right_icon1')
        time.sleep(2)
        self.loc.two_from_last()
        time.sleep(2)
        dissolved_content = self.driver.find_id_text('txtContent')
        check1 = '你真的要解散社团吗？请提前处理好社团钱包中的收益，解散后无法恢复社团'
        assert check1 in dissolved_content
        self.driver.find_id_click('btnCancel')
        time.sleep(2)

    #返回社团主界面#
    def test_t_society_quit_manager(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id('task_box')
        self.driver.find_id_click('ivnewstab')
        time.sleep(2)
        self.driver.find_id_click('society')
        time.sleep(2)

    #推荐社团
    def test_u_society_recommend(self):
        self.driver.find_id_click('guize')
        time.sleep(2)
        content = self.driver.find_id_text('content')
        content_check = '推荐社团是根据当前正在开启招募社团按活跃度'
        if content not in content_check:
            print('推荐社团简介内容校验失败')
        time.sleep(2)
        self.driver.find_id_click('delete')
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        lists = ['content','member_film_count','userhead']
        for i in lists:
            members = self.driver.find_id_text('member_film_count')
            self.driver.find_id_click(i)
            self.driver.wait_id('ll_fan')
            member = self.driver.find_id_text('membercount')
            if member not in members:
                print('社团成员显示不一致',members,member)
            self.driver.find_id_click('btnBack')
            time.sleep(2)
        self.driver.find_id_click('join')
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)
        self.driver.find_id_click('ivnewstab')
        time.sleep(3)
        self.driver.find_id_click('tv_key_word_help')
        time.sleep(2)
        self.driver.find_id_send('txtKeyword','10885432')
        time.sleep(1)
        self.driver.find_id_click('btnSearch')
        self.driver.wait_xpath('天魔琴音')
        self.driver.find_id_click('join')
        time.sleep(2)
        self.driver.find_id_send('content','社团加入申请测试')
        time.sleep(2)
        self.driver.find_id_click('bg_rl1')
        self.driver.wait_id_click('filmBg')
        self.driver.wait_id_click('btnSelect')
        time.sleep(2)
        self.driver.find_id_click('bg_rl2')
        time.sleep(2)
        self.driver.wait_id_click('iv_source')
        time.sleep(2)
        self.driver.find_id_click('tv_right')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '已提交申请'
            if check not in toast:
                print(toast)
                self.driver.find_id_click('btnBack')
        except:
            pass
        time.sleep(2)
        self.driver.find_id_click('btnBack')
        time.sleep(2)