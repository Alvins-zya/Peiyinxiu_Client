#encoding: utf-8
'''
@author:alvin.zhu
@file:Home_Function_List.py
@time:2020/11/5 10:56
@Description:

'''
from Public.Driver_Operate import BaseOperate,resource_id
import time

class Home_Function():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入首页频道列表界面
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
                    self.driver.swip_move(self.x * 0.854 ,self.y * 0.197,self.x * 0.249,self.y *0.197)
                    time.sleep(2)
                elif self.y >=2280:
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

    #频道界面标签列表
    def Function_Channel_Tvs(self):
        labels = self.driver.find_ids(self.id + 'tv')
        time.sleep(2)
        for i in range(len(labels)-4):
            name = self.driver.find_ids(self.id + 'tv')[i].text
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_xpath('排行榜')
            channel_name = self.driver.find_id(self.id + 'txtTitle').text
            assert name == channel_name,'频道列表界面标签名称与标签详情界面标签名称校验不一致'
            time.sleep(1)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #热门频道
    def Function_Channel_Hot(self):
        title  = self.driver.find_id(self.id + 'tv2').text
        self.driver.find_id(self.id + 'tv2').click()
        self.driver.wait_id(self.id + 'follow_ta')
        self.driver.Background()
        time.sleep(2)
        video_title = self.driver.find_id(self.id + 'tv_video_detail_title').text
        assert title in video_title,'频道主界面点击的视频标题与视频详情的标题校验失败'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'count').click()
        self.driver.wait_id(self.id + 'txtTitle')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)

    #附近
    def Function_Channel_Nearby(self):
        while True:
            try:
                self.driver.find_xpath('附近')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >=2280:
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

    #附近列表
    def Function_Channel_Nearby_work_list(self):
        distance = self.driver.find_ids(self.id + 'distance')
        count = self.driver.find_ids(self.id + 'userHead')
        if len(distance) != len(count):
            raise ('附近当前界面有个别作品未显示距离信息')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'channel1')
        except:
            raise ('当前列表界面作品未显示频道标签')
        time.sleep(2)
        

    #视频详情切换-列表作品名称与视频详情作品名称校验
    def Function_Channel_Nearby_work_detail(self):
        name = self.driver.find_ids(self.id + 'title')
        title_list = []
        for  title in range(len(name)):
            title_name = self.driver.find_ids(self.id + 'title')[title].text
            title_list.append(title_name)
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'title').click()
        for i in range(len(name)):
            self.driver.wait_id(self.id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            Name = self.driver.find_id(self.id + 'tv_video_detail_title').text
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
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    #进入曝光去
    def Function_Exposure(self):
        while True:
            try:
                self.driver.find_xpath('曝光区')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >=2280:
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
            raise ('未检测到发送的评论')
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
                raise ('曝光评论进度显示错误')
        time.sleep(2)



    # 进入排行榜
    def Function_Rank(self):
        while True:
            try:
                self.driver.find_xpath('排行榜')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854, self.y * 0.189, self.x * 0.249, self.y * 0.197)
                    time.sleep(2)
                elif self.y >=2280:
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
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            goods = re.findall(r'获赞(.*)', limit)
            str_good_count = ''.join(goods)
            int_num = int(str_good_count)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        assert list == list_set, '获赞榜点赞排序验证错误'
        time.sleep(2)

    #获赞榜-用户信息
    def Function_Rank_Good_Rank_UserInfo(self):
        No1_name = self.driver.find_id(self.id + 'username1').text
        self.driver.find_id(self.id + 'userHead1').click()
        self.driver.wait_id(self.id + 'll_follow')
        No1_zoom_name = self.driver.find_id(self.id + 'username').text
        assert No1_name == No1_zoom_name,'获赞榜第一用户名称与空间中的用户名称校验不一致'
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
        assert  No1_name == No1_zoom_name, '榜一用户名称与空间中的用户名称校验不一致'
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
        self.assertEqual(No1_name, No1_zoom_name, msg='榜一用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
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
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'直播总参与(.*)人', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        assert list == list_set,'=主播榜人数排序验证错误'
        time.sleep(2)


    # 社团榜
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

    # 社团榜-作品数排序检查
    def Function_Rank_Societies_Sort(self):
        count = self.driver.find_ids(self.id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'(.*)作品', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        assert list == list_set, '=社团榜作品数排序验证错误'
        time.sleep(2)


    # 素材榜
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

    # 素材榜-素材数排序检查
    def test_m(self):
        count = self.driver.find_ids(self.id + 'desc')
        list = []
        for i in range(len(count)):
            limit = self.driver.find_ids(self.id + 'desc')[i].text
            Screening = re.findall(r'(.*)收录', limit)
            str_Screening = ''.join(Screening)
            int_num = int(str_Screening)
            list.append(int_num)
            time.sleep(1)
        list_set = sorted(list, reverse=True)
        assert list == list_set, '素材榜素材收录数排序验证错误'
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
        assert list_title != list_title1,'排行榜与热门标签榜作品标题校验错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'commentary').click()
        time.sleep(2)

    #切换热门标签
    def Function_Rank_Hot_Label_change(self):
        label_name = self.driver.find_id(self.id +'commentary').text
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
        select = random.randint(0,len(tv_list))
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
        assert title_list != title_list1,'切换不同的热门标签后，列表中的作品未刷新'
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

    #社作榜
    def Function_Rank_society_works(self):
        self.driver.find_id(self.id + 'society_film').click()
        time.sleep(2)
        titles = self.driver.find_ids(self.id +'tv_source_title')
        for i in range(len(titles)):
            self.driver.find_ids(self.id + 'iv_source')[i].click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)

            try:
                self.driver.find_id(self.id + 'dubbing')
                raise ('社团作品显示有配音按钮')
            except:
                pass
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    #榜单列表加载
    def Function_Rank_Works_list_load(self):
        while True:
            ranking = self.driver.find_ids(self.id + 'rank')[-1].text
            if ranking =='300':
                break
            else:
                pass
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #进入在线pia戏
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

    #勋章列表
    def Function_Pia_Medal_list(self):
        self.driver.find_id(self.id + 'goXun').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userHead')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            raise ('未加载显示勋章列表')
        time.sleep(2)

    #道具商城
    def Function_Pia_Prop_Mall(self):
        self.driver.find_xpath('道具商城').click()
        time.sleep(2)
        num = self.driver.find_id(self.id + 'diamond').text
        self.driver.find_id(self.id + 'diamond').click()
        time.sleep(2)
        num1 = self.driver.find_id(self.id +'diamond_count_tv').text
        time.sleep(2)
        assert num in num1,'钻石额度校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #幸运宝箱
    def Function_Pia_Prop_Mall_Lucky_Box(self):
        self.driver.find_id(self.id + 'diamond').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'diamond_count_tv')
        except:
            raise ('幸运夺宝界面跳转至钻石充值界面失败')
        time.sleep(2)
        self.driver.find_id(self.id +'back').click()
        time.sleep(2)
        num = self.driver.find_id(self.id + 'diamond').text
        if num < 49 :
            self.driver.find_id(self.id +'smoke_ten').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id +'btnSubmit').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'back').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #Pia戏装扮
    def Function_Pia_Prop_Mall_Dress_up(self):
        num = self.driver.find_ids(self.id + 'img')
        for i in range(len(num)):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(1)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #创建pia戏房间
    def Function_Pia_Create_room(self):
        self.driver.find_id(self.id + 'create_room').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'check_normal').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'crate_room').click()
        try:
            self.driver.wait_id(self.id + 'chat')
        except:
            raise ('pia戏房间创建失败')
        time.sleep(2)

    #评论
    def Function_Pia_Room_comment(self):
        self.driver.find_id(self.id + 'show_comment').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('哈哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'rl')
        time.sleep(2)

    #用户头像
    def Function_Pia_Room_Userhead(self):
        self.driver.find_id(self.id + 'head').click()
        self.driver.wait_id(self.id + 'user_id')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'username')
            try:
                self.driver.find_id(self.id +'gender')
                try:
                    self.driver.find_id(self.id +'user_id')
                    try:
                        self.driver.find_id(self.id + 'user_detail')
                    except:
                        raise ('未显示用户简介')
                except:
                    raise ('未显示用户ID')

            except:
                raise ('未显示性别')
        except:
            raise ('未显示用户名')
        time.sleep(2)
        self.driver.find_id(self.id +'icon_close').click()
        time.sleep(2)

    #房间私密
    def Function_Pia_Room_Private(self):
        self.driver.find_id(self.id + 'private_btn').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert  tip == check,'普通房间设置私密，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #邀请好友
    def Function_Pia_Room_invite_friend(self):
        self.driver.find_ids(self.id + 'head')[-1].click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert tip  == check, '普通房间邀请好友，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #剧本列表
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
        assert No1 == No2,'剧本列表校验失败'
        time.sleep(2)

        #添加剧本
        self.driver.find_id(self.id + 'add_drama').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'btnSubmit').text
        check = '升级房间(5钻/小时)'
        assert tip == check, '添加剧本，提示文案错误'
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #退出在线pia戏房间
    def Function_Pia_Room_exit(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'create_room')
        time.sleep(2)

    #在线匹配
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

    #跟随进入
    def Function_Pia_Follow(self):
        self.driver.find_id(self.id + 'follow').click()
        time.sleep(2)
        self.driver.find_id(self.id +'refresh').click()
        try:
            self.driver.wait_toast(self.id +'//android.widget.Toast')
        except:
            raise ('未检测到刷新toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #作品列表
    def Function_Pia_Draft(self):
        self.driver.find_id(self.id + 'draft' ).click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    #有声漫画
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

    #推荐列表-声漫名称校验
    def Function_Cartoon_title_check(self):
        name = self.driver.find_id(self.id + 'title').text
        self.driver.find_id(self.id + 'title').click()
        self.driver.wait_id(self.id + 'start_play')
        detail_name = self.driver.find_id(self.id + 'tvTitle').text
        assert name == detail_name,'推荐列表中声漫名称与声漫详情界面名称不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
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
    #     self.assertEqual(num,new,msg='列表更新集数与声漫详情界面更新集数不一致')
    #     time.sleep(2)
    #     self.driver.find_id(self.id + 'btnBack').click()
    #     time.sleep(2)

    #推荐列表加载
    def Function_Cartoon_list_load(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        for i in range(4):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)


    #声漫剧集详情
    def Function_Cartoon_Episodes_detail(self):
        i = 0
        while i <=10:
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

    #剧集列表界面点击声漫收藏
    def Function_Cartoon_collection(self):
        self.driver.find_id(self.id + 'collect').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        check = '收藏成功'
        assert toast == check,'收藏toast校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'collect').click()
        cancel_toast = self.driver.wait_toast('//android.widget.Toast')
        cancel_check = '取消收藏成功'
        assert cancel_check == cancel_toast,'声漫取消收藏toast校验不一致'
        time.sleep(2)

    #声漫制作相关社团列表
    def Function_Cartoon_Make_society(self):
        self.driver.find_id(self.id + 'right_rl').click()
        try:
            self.driver.wait_id(self.id + 'count')
        except:
            raise ('声漫制作社团列表加载失败')
        time.sleep(2)
        self.driver.find_ids(self.id + 'name')[1].click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    #连载漫画集数查看
    def Function_Cartoon_Episode_check(self):
        num = self.driver.find_id(self.id + 'name').text
        self.driver.find_id(self.id + 'name').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        Re_num = re.findall(r'第 (.*) 话',num)
        new_num = ''.join(Re_num)
        title_name = self.driver.find_id(self.id + 'tv_video_detail_title').text
        assert new_num == title_name,'声漫切换集数校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #最新列表-话集更新检查
    def Function_Cartoon_Update_check(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        update = self.driver.find_id(self.id + 'update').text
        union = self.driver.find_id(self.id + 'union_name').text
        new_update = re.findall(r'更新至(.*)',update)
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        detail_name = self.driver.find_id(self.id + 'user_name').text
        assert union == detail_name,'社团名称校验不一致'
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    #声漫分类列表
    def Function_Cartoon_Classification_list(self):
        self.driver.find_id(self.id + 'tab3').click()
        time.sleep(2)
        title = self.driver.find_ids(self.id +'title')
        for i in range(len(title)-1,-1,-1):
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(1)



    #声漫制作
    def Function_Cartoon_Make(self):
        self.driver.find_id(self.id + 'sm').click()
        time.sleep(2)
        title = self.driver.find_ids(self.id + 'title')
        for i in range(len(title) - 1, -1, -1):
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(1)

    #漫画详情
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

    #制作声漫
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
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的漫画
    def Function_Cartoon_My(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.wait_xpath('你听说过女大学生吗')
        time.sleep(2)

    #声漫统筹界面-更新配音者
    def Function_Cartoon_change_Voiceover(self):
        self.driver.find_id(self.id + 'iv_pic1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.wait_id(self.id +'socialstatus')
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

    #进入统筹界面-添加音效
    def Function_Cartoon_Making_insert_Sound(self):
        self.driver.find_id(self.id + 'make').click()
        self.driver.wait_id(self.id + 'upload')
        self.driver.find_xpath('添加音效').click()
        time.sleep(2)

    #点击录音
    def Function_Cartoon_Record(self):
        self.driver.find_id(self.id + 'transcribe').click()
        time.sleep(5)
        self.driver.find_id(self.id + 'transcribe').click()
        time.sleep(4)

    #点击试听音效
    def Function_Cartoon_Making_listening_test(self):
        Sounds = self.driver.find_ids(self.id + 'effect_types_img')
        for i in range(len(Sounds)):
            self.driver.find_ids(self.id + 'effect_types_img')[i].click()
            time.sleep(3)
            Sounds_Classification = self.driver.find_ids(self.id + 'effect_sound_name')
            for i in range(len(Sounds_Classification)):
                self.driver.find_ids(self.id + 'effect_sound_name')[i].click()
                time.sleep(2)

        #播放整体动漫音效
        self.driver.find_id(self.id + 'preview').click()
        time.sleep(10)

    #进入添加背景音界面
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

    #声漫上传界面-保存并退出
    def Function_Cartoon_Making_Save(self):
        self.driver.find_id(self.id + 'preview').click()
        self.driver.wait_id(self.id + 'preview')
        time.sleep(2)
        self.driver.find_id(self.id + 'savebtn').click()
        self.driver.wait_id(self.id + 'make')
        time.sleep(2)

    #声漫上传
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
            raise ('声漫上传失败')
        time.sleep(2)

    #声漫删除
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
            elif self.y >=2280:
                self.driver.tap(0.5 * self.x, 0.883 * self.y)
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
                try:
                    self.driver.wait_toast('//android.widget.Toast')
                except:
                    raise ('未检测到声漫删除toast')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(3)
                self.driver.find_id(self.id + 'close1').click()
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
        except:
            raise ('未位于声漫剧集列表界面')

  
