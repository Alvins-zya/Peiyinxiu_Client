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
        self.driver.find_id(self.id + 'img_hot').click()
        time.sleep(2)

    #每日任务列表加载
    def task_list(self):
        self.driver.find_id(self.id + 'task_box').click()
        self.driver.wait_id(self.id + 'rl1')

    #每日签到
    def task_daily_attendance(self):
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
            raise ('每日签到错误')

    #日常任务
    def task_Daily_tasks(self):
        check = ['上传一个带频道的作品','分享作品至朋友圈','收听语聊10分钟','用钻石曝光1个作品','评论5个曝光区作品','看完5个作品']
        task_list = []
        tasks = self.driver.find_ids(self.id + 'title')
        for i in range(len(tasks)):
            task = self.driver.find_ids(self + 'title')[i].text
            task_list.append(task)
        time.sleep(2)
        if sorted(check) != sorted(task_list):
            raise
        time.sleep(2)
        for i in range(len(task_list)):
            result = ('{0},{1}',format(i,task_list[i]))
            num = int(result[1])
            if task_list[num] == '上传一个带频道的作品':
                self.driver.find_ids(self.id + 'tv_lingqu')[num].click()
                self.driver.wait_id(self.id + 'rl_coor')
                time.sleep(1)
                self.driver.find_id(self.id + 'ivDubbingTab').click()
                time.sleep(2)
                self.driver.find_id(self.id +'task_box').click()
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
        self.driver.find_id(self.id + 'btnBack').click()
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
        for i in range(len(hot_workes)):
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
        user_list = ['148207791','152726825','159420264','141130466']
        for i in user_list:
            self.driver.find_id(self.id +'txtKeyword').send_keys(i)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSearch').click()
            self.driver.wait_id(self.id +'userhead')
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

    #返回上一界面
    def Btnback(self):
        self.driver.find_id(self.id + 'btnBack').click()
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
    def touch_into_video(self):
        #点击作品封面进入视频详情
        self.driver.find_id(self.id + 'film_img2').click()
        self.driver.wait_id(self.id + 'userhead')
        self.Btnback()

        #列表界面点击用户头像进入视频详情
        self.driver.find_id(self.id + 'user_head').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.Btnback()

        #列表界面点击作品标题进入视频详情
        self.driver.find_id(self.id + 'title2').click()
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.Background()
        time.sleep(2)
        self.Btnback()

        #列表界面点击作品标签
        self.driver.find_id(self.id + 'film2_channel1').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.Btnback()
        self.driver.find_id(self.id + 'film2_channel2').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.Btnback()











