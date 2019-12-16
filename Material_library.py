#coding = utf-8
#防止中文显示乱码
#coding = gb18030
'''
author:Alvins.zhu
time:2019年6月3日
function:Login

New:
time:2019年12月5日15:12:47
function:暂无
'''

import random
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
from pprint import pprint
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()
class Libery():
    def Libery_list(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/task_box')
            print('===开始===')
        except:
            print('应用启动失败')
        '''点击首页的配音按钮'''
        OP.find_id('com.happyteam.dubbingshow:id/btn_more').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/sj')
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbignshow:id/btnReload')
                OP.find_id('com.happyteam.dubbignshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/sj')
                except(NoSuchElementException, TimeoutException):
                    print('素材库加载失败')
                    driver.quit()
            except:
                pass
        time.sleep(2)
    '''声音鉴定'''
    def Sound_warning(self):

        '''点击声鉴按钮'''
        OP.find_id('com.happyteam.dubbingshow:id/sj')
        OP.find_id('com.happyteam.dubbingshow:id/sj').click()
        time.sleep(1)

        '''
        判断是否显示的是声鉴结果页面，是则点击重新鉴定按钮
        '''
        try:
            OP.find_id('com.happyteam.dubbingshow:id/reIndetify')
            OP.find_id('com.happyteam.dubbingshow:id/reIndetify').click()
        except:
            pass
        time.sleep(1)

        '''
        选择性别男
        '''
        OP.find_id('com.happyteam.dubbingshow:id/boy').click()
        time.sleep(1)

        '''
        选择性别女
        '''
        OP.find_id('com.happyteam.dubbingshow:id/girl').click()
        time.sleep(1)

        '''
        循环三次点击换一个按钮
        '''
        for i in range(3):
            OP.find_id('com.happyteam.dubbingshow:id/change').click()
        OP.back()
        time.sleep(2)

        #     '''
        #     点击配音按钮
        #     '''
        #     OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #     time.sleep(2)
        #
        #     '''
        #     若显示权限弹窗，则点击允许
        #     '''
        #     try:
        #         OP.wait_xpath('允许')
        #         OP.find_xpath('允许').click()
        #         time.sleep(2)
        #     except:
        #         pass
        #
        #     '''
        #     点击录音按钮，录制10秒进入声鉴结果界面
        #     '''
        #     OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #     time.sleep(20)
        #     OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #
        #
        #     '''
        #     等待跳转至声鉴结果界面
        #     '''
        #     for i in range(5):
        #         try:
        #             OP.wait_xpath('您的声鉴报告')
        #             print('跳转至声鉴结果界面')
        #             break
        #         except(NoSuchElementException,TimeoutException):
        #             print('界面跳转失败')
        #             time.sleep(1)
        #             OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #             time.sleep(10)
        #             OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #         time.sleep(1)
        #
        #     time.sleep(2)
        #     '''获取视频标题'''
        #     Name = OP.find_id('com.happyteam.dubbingshow:id/title').text
        #     print(Name)
        #     time.sleep(2)
        #     '''播放视频'''
        #     OP.find_id('com.happyteam.dubbingshow:id/play').click()
        #     time.sleep(5)
        #     device().keyevent(3)
        #     time.sleep(2)
        #     device().launch_app()
        #     time.sleep(2)
        #     '''点击素材来源'''
        #     OP.find_id('com.happyteam.dubbingshow:id/source_from').click()
        #     try:
        #         OP.wait_id('com.happyteam.dubbingshow:id/txtKeyword')
        #         time.sleep(2)
        #         OP.back()
        #     except(NoSuchElementException, TimeoutException):
        #         pass
        #     '''
        #     点击配音按钮进入配音界面
        #     '''
        #     for i in range(5):
        #         OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        #         try:
        #             OP.wait_download('com.happyteam.dubbingshow:id/action')
        #             time.sleep(1)
        #             OP.back()
        #             time.sleep(1)
        #             OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        #             break
        #         except(NoSuchElementException,TimeoutException):
        #             try:
        #                 OP.find_id('com.happyteam.dubbingshow:id/action1')
        #                 OP.find_id('com.happyteam.dubbingshow:id/action1').click()
        #                 time.sleep(1)
        #                 OP.back()
        #                 time.sleep(1)
        #                 OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        #                 break
        #             except:
        #                 print('素材下载失败')
        #         time.sleep(2)
        #     '''上滑加载列表'''
        #     for i in range(3):
        #         OP.swip_up()
        #         time.sleep(3)
        #         Names = OP.find_ids('com.happyteam.dubbingshow:id/title')
        #         Name_list = []
        #         for i in range(len(Names)):
        #             name = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
        #             Name_list.append(name)
        #             time.sleep(1)
        #         print(Name_list)
        #         time.sleep(2)
        #     '''
        #     返回到素材库界面
        #     '''
        #     OP.back()
        # except :
        #     print('素材库加载失败')
        #     time.sleep(1)
        #     device().close()
        #     time.sleep(1)
        #     device().quit()

    '''分类列表'''
    def classification(self):
        Classify = OP.find_ids('com.happyteam.dubbingshow:id/img')
        for i in range(len(Classify)):
            Name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].text
            print (Name)
            time.sleep(2)
            for x in range(3):
                OP.find_ids('com.happyteam.dubbingshow:id/img')[i].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tv')
                    break
                except:
                    print (name,'详情加载失败')
                    time.sleep(2)
                    OP.back()
            time.sleep(2)
            '''获取合集界面中素材频道列表'''
            TVs = OP.find_ids('com.happyteam.dubbingshow:id/tv')
            Tv_Name_list = []
            for i in range(len(TVs)):
                Tv_name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].text
                Tv_Name_list.append(Tv_name)
            print(Tv_Name_list)

            '''点击进入素材频道详情界面再返回'''
            time.sleep(1)
            for i in range(len(TVs)):
                OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].click()
                OP.wait_id('com.happyteam.dubbingshow:id/tag_name')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(2)

            '''点击热门频道标签'''
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/tv1').click()
            OP.wait_id('com.happyteam.dubbingshow:id/txtTitle')
            while True:
                count = OP.find_ids('com.happyteam.dubbingshow:id/rank_pos')[-1].text
                OP.swip_up()
                time.sleep(2)
                count1 = OP.find_ids('com.happyteam.dubbingshow:id/rank_pos')[-1].text
                if count == count1:
                    break
                else:
                    OP.swip_up()
                time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
            time.sleep(2)

            '''点击筛选条件选项'''
            Tv_list = OP.find_ids('com.happyteam.dubbingshow:id/types_name')
            for i in reversed(range(len(Tv_list))):
                OP.find_ids('com.happyteam.dubbingshow:id/types_name')[i].click()
                time.sleep(1)

            # 点击进入素材详情
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            time.sleep(5)
            OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
            time.sleep(2)
            '''退出合辑详情界面'''
            OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
            time.sleep(2)

    '''素材库界面素材列表'''
    def Material_list(self):
        OP.wait_xpath('男')
        print("点击角色男")
        OP.find_xpath('男').click()
        time.sleep(2)

        print("点击角色女")
        OP.find_xpath('女').click()
        time.sleep(2)

        print("点击合作")
        OP.find_xpath('合作').click()
        time.sleep(2)

        print("点击热门")
        OP.find_xpath('热门').click()
        time.sleep(2)

        print("点击收录")
        OP.find_xpath('最新').click()
        time.sleep(2)

        print("点击不限")
        OP.find_xpath('不限').click()
        time.sleep(2)

        print("点击推荐")
        OP.find_xpath('推荐').click()
        time.sleep(2)

        print("点击角色男")
        OP.find_xpath('男').click()
        time.sleep(2)

        print("点击热门")
        OP.find_xpath('热门').click()
        time.sleep(2)


        num =random.randint(5,10)
        print("上滑:",num,"次")
        for i in range(num):
            #上滑
            OP.swip_up()
            time.sleep(2)
            Source_name = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')
            Name_list = []
            for i in range(len(Source_name)):
                Name = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[i].text
                Name_list.append(Name)
            print (Name_list)
            time.sleep(1)

        print("点击进入素材详情界面")
        OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
        try:
            OP.find_id('com.happyteam.dubbingshow:id/userhead')
            time.sleep(5)
            print("点击头像进入个人空间")
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            try:
                OP.find_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()#返回素材详情界面
            except:
                OP.back()#返回素材详情界面
                time.sleep(1)

            time.sleep(2)
            '''素材频道标签'''
            try:
                OP.find_id('com.happyteam.dubbingshow:id/types_name').click()
                OP.wait_id('com.happyteam.dubbingshow:id/tag_name')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(2)
                '''获取素材标题'''
                Source_names = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')
                Name_list = []
                for i in range(len(Source_names)):
                    Name = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[i].text
                    Name_list.append(Name)
                    time.sleep(0.5)
                print (Name_list)
            except(NoSuchElementException,TimeoutException):
                print ('该素材暂无素材频道标签')
                time.sleep(2)
            time.sleep(2)


            user_name = OP.find_id('com.happyteam.dubbingshow:id/name1').text
            name = '未上榜'
            if user_name == name:
                print('该素材暂无用户配音')
            else:
                OP.find_id('com.happyteam.dubbingshow:id/name1').click()
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(2)
                '''上滑排行榜'''
                OP.swip_up()
                time.sleep(3)
                User_name = OP.find_ids('com.happyteam.dubbingshow:id/title')
                Name_list = []
                for i in range(len(User_name)):
                    Name = OP.find_ids('com.happyteam.dubbingshow:id/nickname')[i].text
                    Play_count = OP.find_ids('com.happyteam.dubbingshow:id/play_count')[i].text
                    Name_list.append(Name)
                    Name_list.append(Play_count)
                    time.sleep(1)
                print (Name_list)
                time.sleep(2)

            '''点击收藏按钮'''
            OP.find_xpath('收藏').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                pass
            time.sleep(1)


            print("转发按钮")
            OP.find_id('com.happyteam.dubbingshow:id/zhuanfa_fake').click()
            time.sleep(2)
            print("输入用户ID")
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(1)
            print("点击搜索")
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            time.sleep(2)
            OP.wait_xpath('配音秀官方号')
            try:
                OP.find_xpath('配音秀官方号')
                print("点击进入聊天界面")
                OP.find_xpath('配音秀官方号').click()
                time.sleep(2)
                OP.back()  # 返回素材详情
            except:
                pass
            time.sleep(1)

            print("点击立即配音")
            OP.find_xpath('立即配音').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                time.sleep(2)
                OP.back()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print ('下载失败')
            time.sleep(2)

            print("点击素材详情的举报按钮")
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(1)
            print("政治、色情等敏感信息")
            OP.find_xpath('政治、色情等敏感信息').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)
            print("返回到素材库")
            OP.back()
        except(NoSuchElementException,TimeoutException):
            OP.back()
        time.sleep(1)



        print("点击TOP按钮")
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/top_img')
            OP.find_id('com.happyteam.dubbingshow:id/top_img').click()
        except:
           pass
        time.sleep(2)

        print("点击合作分类")
        OP.swip_down()
        OP.find_xpath('合作').click()
        time.sleep(2)

        print("点击进入合作素材详情")
        OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
        time.sleep(5)

        try:
            print("推荐合作")
            OP.find_id('com.happyteam.dubbingshow:id/right_rank_tv')
            time.sleep(1)

            print("点击切换角色")
            OP.find_id('com.happyteam.dubbingshow:id/left_name').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/right_name').click()
            time.sleep(2)

            print("点击合作预览")
            OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image').click()
            time.sleep(2)

            print("点击预览界面中的合作按钮进入配音")
            OP.find_id('com.happyteam.dubbingshow:id/btnCooperate').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                print("退出配音界面")
                OP.back()
                time.sleep(1)
                OP.find_xpath('确认').click()
                time.sleep(1)
                print("退出素材详情")
                OP.back()
            except:
                print("下载失败，退出素材详情")
                OP.back()
            time.sleep(1)
        except:
            OP.back()#退出素材详情
        time.sleep(2)

    '''素材库搜索素材'''
    def Search_source(self):
        '''点击素材库中的搜索'''
        OP.find_id('com.happyteam.dubbingshow:id/tv_search').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/tv').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/rl_left2')
            '''显示素材剧集列表'''
            OP.find_id('com.happyteam.dubbingshow:id/img_bottom')
            time.sleep(2)
            '''点击搜索框清除按钮'''
            OP.find_id('com.happyteam.dubbingshow:id/btnClear').click()
        except(NoSuchElementException, TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnClear').click()
            except:
                print('搜索无结果')
                OP.find_id('com.happyteam.dubbingshow:id/btnClear')
        time.sleep(2)

        '''点击更多热点'''
        OP.find_id('com.happyteam.dubbingshow:id/tv1').click()
        OP.wait_id('com.happyteam.dubbingshow:id/txtTitle')
        Names = OP.find_ids('com.happyteam.dubbingshow:id/rank_name')
        Name_list = []
        count_list = []
        for i in range(len(Names)):
            name = OP.find_ids('com.happyteam.dubbingshow:id/rank_name')[i].text
            count = OP.find_ids('com.happyteam.dubbingshow:id/rank_count')[i].text
            Name_list.append(name)
            count_list.append(count)
            time.sleep(0.5)
        list = dict(zip(Name_list,count_list))
        print(list)
        time.sleep(1)
        OP.back()
        time.sleep(2)
        '''清空搜索历史记录'''
        OP.find_id('com.happyteam.dubbingshow:id/clear').click()
        OP.back()
        time.sleep(2)

    '''合作广场'''
    def Cooperation_square(self):
        print("点击合作广场")
        OP.find_id('com.happyteam.dubbingshow:id/rl_coor').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnRetry')
            print("合作广场加载失败")
            OP.find_id('com.happyteam.dubbingshow:id/btnRetry').click()
            time.sleep(4)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnRetry')
                print("重载失败！")
                devc.close_app()
                devc.quit()
            except:
                pass
        except:
            pass
        time.sleep(1)

        print("点击热门")
        OP.find_xpath('热门').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            Titles = OP.find_ids('com.happyteam.dubbingshow:id/item_sh_cooperate_article_title')
            for i in range(len(Titles)):
                Title_name = OP.find_ids('com.happyteam.dubbingshow:id/item_sh_cooperate_article_title')[i].text
                print(Title_name)
                time.sleep(1)
        except(NoSuchElementException,TimeoutException):
            print("热门列表数据加载失败")
        time.sleep(2)

        print("点击我的")
        OP.find_xpath('我的').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        except(NoSuchElementException,TimeoutException):
            print("我的列表数据加载失败")

        print("点击广场")
        OP.find_xpath('广场').click()
        time.sleep(2)
        Titles = OP.find_ids('com.happyteam.dubbingshow:id/item_sh_cooperate_article_title')
        for i in range(len(Titles)):
            Title_name = OP.find_ids('com.happyteam.dubbingshow:id/item_sh_cooperate_article_title')[i].text
            print(Title_name)
            time.sleep(1)
        time.sleep(2)
        print("点击用户头像进入个人空间")
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            print("个人空间加载成功")
            time.sleep(2)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            OP.back()

        time.sleep(2)
        num = random.randint(2,5)
        print("下拉刷新", num, "次")
        for i in range(num):
            OP.swip_down()
            time.sleep(2)

        print("上滑加载",num,"次")
        for i in range(num):
            OP.swip_up()
            time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/top_img')
            print("点击top按钮")
            OP.find_id('com.happyteam.dubbingshow:id/top_img').click()
        except:
            pass
        time.sleep(2)
        print("点击发起：男、女")
        OP.find_id('com.happyteam.dubbingshow:id/fq_male').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/fq_female').click()
        time.sleep(2)

        print("点击待配：男，女")
        OP.find_id('com.happyteam.dubbingshow:id/dp_male').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/dp_female').click()
        time.sleep(2)

        print("点击预览")
        OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image').click()
        time.sleep(5)
        print("退到后台3秒后再打开")
        devc.keyevent(3)
        time.sleep(2)
        devc.launch_app()
        time.sleep(1)

        print("点击视频预览中的合作按钮")
        OP.find_id('com.happyteam.dubbingshow:id/btnCooperate').click()
        try:
            OP.wait_download('com.happyteam.dubbingshow:id/action')
            print("返回合作广场")
            OP.back()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except(NoSuchElementException,TimeoutException):
            print("素材下载失败！")
        time.sleep(2)

        print("点击合作广场中的配音按钮")
        OP.find_id("com.happyteam.dubbingshow:id/btnCooperate").click()
        try:
            OP.wait_download('com.happyteam.dubbingshow:id/action')
            print("返回合作广场")
            OP.back()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except(NoSuchElementException,TimeoutException):
            print("素材下载失败！")
        time.sleep(2)

        print("点击合作广场-热门")
        OP.find_xpath('热门').click()
        time.sleep(2)
        print("点击配音按钮")
        OP.find_id("com.happyteam.dubbingshow:id/btnCooperate").click()
        try:
            OP.wait_download('com.happyteam.dubbingshow:id/action')
            print("点击配音")
            OP.find_id('com.happyteam.dubbingshow:id/action').click()
            time.sleep(10)
            devc.keyevent(3)
            time.sleep(2)
            devc.launch_app()
            time.sleep(2)
            OP.wait_id('com.happyteam.dubbingshow:id/complete')
            OP.find_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/dubbingSeekbar')
                devc.keyevent(3)
                time.sleep(2)
                devc.launch_app()
                time.sleep(2)
                print('点击完成')
                OP.find_id('com.happyteam.dubbingshow:id/complete').click()
                try:
                    OP.wait_xpath('上传作品')
                    print("点击私密按钮")
                    OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
                    time.sleep(2)
                    print("点击上传作品")
                    OP.find_id('com.happyteam.dubbingshow:id/uploadbtn').click()
                    time.sleep(2)
                    try:
                        OP.wait_xpath('上传作品成功！')
                        print("作品上传成功")
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/close').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutException):
                        OP.find_id('com.happyteam.dubbingshow:id/txtContent')
                        el = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                        print(el)
                        OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
                        time.sleep(2)
                        print("保存草稿箱")
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/saveToDraft').click()
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        save_toast = OP.wait_toast('//android.widget.toast')
                        print(save_toast)
                except(NoSuchElementException,TimeoutException):
                    print("预览界面->上传界面跳转失败")
            except(NoSuchElementException,TimeoutException):
                print("配音界面跳转失败")
        except(NoSuchElementException,TimeoutException):
            print("素材下载失败！")
        time.sleep(2)

        print("点击我的")
        OP.find_xpath('我的').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            print("点击预览")
            OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image').click()
            time.sleep(5)
            print("退到后台3秒")
            devc.keyevent(3)
            time.sleep(2)
            devc.launch_app()
            time.sleep(2)
            OP.back()
            time.sleep(4)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnCooperate')
                print("点击置顶")
                OP.find_id('com.happyteam.dubbingshow:id/btnCooperate').click()
                time.sleep(2)
                try:
                    OP.find_xpath('我知道了')
                    OP.find_xpath('我知道了').click()
                    time.sleep(2)
                except:
                    pass
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(10)
            print("删除求合作")
            el = OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image')
            TouchAction(devc).long_press(el).wait(2000).perform()
            time.sleep(2)
            tips = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
            print(tips)
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(10)
        except(NoSuchElementException,TimeoutException):
            print("我的界面中作品为空")
        time.sleep(2)

        print("点击搜索")
        OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/et_search_keyword').send_keys(u"你")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.find_id('com.happyteam.dubbingshow:id/userhead')
            print("点击预览")
            OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image').click()
            time.sleep(5)
            print("退到后台3秒")
            devc.keyevent(3)
            time.sleep(2)
            devc.launch_app()
            time.sleep(2)
            OP.back()
            time.sleep(2)
            print("点击配音按钮")
            OP.find_id('com.happyteam.dubbingshow:id/btnCooperate').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                time.sleep(2)
                OP.back()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print("素材下载失败！")
        except(NoSuchElementException,TimeoutException):
            print("搜索无结果")
        time.sleep(2)
        print("返回合作广场")
        OP.back()
        time.sleep(2)
        print('返回素材库')
        OP.back()





if __name__=="__main__":
    L = Libery()
    L.Libery_list()
    # L.Sound_warning()
    # L.classification()
    # L.Material_list()
    L.Search_source()
    L.Cooperation_square()
    print ('====结束====')
    devc.quit()