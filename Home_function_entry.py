#coding = utf-8
#防止中文显示乱码
#coding = gb18030
import random
import os
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
def fuyong(i):
    print(i)
    if i == "有声漫画":
        OP.find_xpath('有声漫画').click()
        time.sleep(5)
        FC=Sound_Cartoon()
        FC.Cartoon()
        FC.Comics_collection()
        FC.Cartoon_details()
        FC.Newest()
        FC.Play_video()
        OP.back()
    elif i == "附近":
        OP.find_xpath('附近').click()
        time.sleep(5)
        Nearby().Near()
        OP.back()
    elif i == "频道":
        OP.find_xpath('频道').click()
        time.sleep(5)
        Label().Label_list()
        Label().Hot_label()
        OP.back()
    elif i == "在线pia戏":
        OP.find_xpath('在线pia戏').click()
        time.sleep(10)
        # online_pia()
        OP.back()
    elif i == "语聊":
        OP.find_xpath('语聊').click()
        time.sleep(5)
        Chat().Into_chat()
        Chat().banner()
        Chat().Chat_List()
        Chat().chat_personal()
        Chat().enter_chat()
        Chat().create_chat()
        Chat().chat_New()
        Chat().chat_follow()
        OP.back()
    elif i == "曝光区":
        OP.find_xpath('曝光区').click()
        time.sleep(5)
        Exposure().Exposure_area()
        OP.back()
    elif i == "排行榜":
        OP.find_xpath('排行榜').click()
        time.sleep(5)
        Ranking_List().Rank()
        Ranking_List().RichRank()
        Ranking_List().LiveRank()
        Ranking_List().SocietyRank()
        Ranking_List().SourceRank()
        Ranking_List().Film()
        Ranking_List().Commentary()
        Ranking_List().Potential()
        Ranking_List().SocietyFilm()
        OP.back()
    else:
        pass
    time.sleep(2)

def Enter_list():
    try:
        OP.wait_id('com.happyteam.dubbingshow:id/task_box')
        print('===开始===')
        OP.swip_down()
        time.sleep(4)
    except:
        print('应用启动失败')
    time.sleep(2)
    names = OP.find_ids('com.happyteam.dubbingshow:id/title')
    enter_check_list = ['有声漫画', '附近', '频道', '在线pia戏', '语聊', '曝光区', '排行榜']
    list = []
    for  i in range(len(names)):
        name = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
        list.append(name)
        time.sleep(1)
    print(list)
    time.sleep(2)
    for i in list:
        fuyong(i)
        time.sleep(1)
    device().swipe(x*0.83,y*0.162,x*0.3,y*0.162,300)
    time.sleep(4)
    list_new = []
    for i in enter_check_list:
        if i not in list:
            list_new.append(i)
    print(list_new)
    for i in list_new:
        fuyong(i)
        time.sleep(1)
        device().swipe(x * 0.83, y * 0.162, x * 0.3, y * 0.162, 300)
        time.sleep(4)


'''点击在线pia戏'''
def online_pia():
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/goXun')
            user_name = OP.find_id('com.happyteam.dubbingshow:id/user_name').text
            time.sleep(1)
            Scene_count = OP.find_id('com.happyteam.dubbingshow:id/mvpCount').text
            time.sleep(1)
            role_count = OP.find_id('com.happyteam.dubbingshow:id/getCount').text
            time.sleep(1)
            Detonation_lamp = OP.find_id('com.happyteam.dubbingshow:id/baoCount').text
            time.sleep(1)
            print("用户:",    user_name,
                  "参与场次:", Scene_count, "次,",
                  "抢到角色:", role_count, "次,",
                  "获得爱心:", Detonation_lamp, "次,")
            time.sleep(2)
            print("我的勋章")
            OP.find_id('com.happyteam.dubbingshow:id/goXun').click()
            time.sleep(2)
            el = OP.find_id('com.happyteam.dubbingshow:id/my_medal_count').text
            print(el)
            time.sleep(2)
            OP.back()
            time.sleep(2)
            print('道具商城')
            OP.find_id("com.happyteam.dubbingshow:id/propshop").click()
            try:
                OP.wait_id("com.happyteam.dubbingshow:id/box")
                OP.find_id('com.happyteam.dubbingshow:id/left_rl').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    print('充值界面跳转失败')
                    time.sleep(2)
                    OP.back()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/box').click()
                time.sleep(2)
                patch_count = OP.find_id('com.happyteam.dubbingshow:id/patch').text
                time.sleep(0.5)
                diamond_count = OP.find_id('com.happyteam.dubbingshow:id/diamond').text
                print(patch_count,diamond_count)
                time.sleep(2)
                print('点击10抽')
                OP.find_id('com.happyteam.dubbingshow:id/diamonds_count').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/txtContent')
                    content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                    print(content)
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                        time.sleep(2)
                        OP.back()
                    except(NoSuchElementException,TimeoutException):
                        print('充值界面跳转失败')
                        time.sleep(1)
                        OP.back()
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    OP.back()
                time.sleep(2)
                print('道具列表')
                time.sleep(1)
                names = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')
                num = len(names)
                for i in range(num):
                    OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].click()
                    time.sleep(1)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/guize').click()
                        time.sleep(2)
                        content = OP.find_id('com.happyteam.dubbingshow:id/tv_content').text
                        print(content)
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/go_back').click()
                        time.sleep(2)
                    except:
                        pass
                time.sleep(2)
                print('点击合成/分解按钮')
                OP.find_id('com.happyteam.dubbingshow:id/dispose').click()
                time.sleep(2)
                fenjie = '确定要分解吗？'
                hecheng = '确定要合成吗？'
                content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                if content == fenjie:
                    print('显示分解提示')
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                elif content == hecheng:
                    print('显示合成提示')
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                else:
                    pass
                time.sleep(8)
                print('比心动画')
                OP.find_id('com.happyteam.dubbingshow:id/view_love').click()
                time.sleep(2)
                names = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')
                name_list = []
                for i in range(len(names)):
                    OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].click()
                    time.sleep(1)
                    name = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].text
                    name_list.append(name)
                    time.sleep(1)
                '''列表去重'''
                bixin =[]
                for i in name_list:
                    if not i in bixin:
                        bixin.append(i)
                print(bixin)
                time.sleep(2)
                print('头像框')
                OP.find_id('com.happyteam.dubbingshow:id/view_num').click()
                time.sleep(2)
                names = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')
                name_list = []
                for i in range(len(names)):
                    OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].click()
                    time.sleep(1)
                    name = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].text
                    name_list.append(name)
                    time.sleep(1)
                '''列表去重'''
                Head = []
                for i in name_list:
                    if not i in Head:
                        Head.append(i)
                print(Head)
                time.sleep(2)
                print('聊天气泡')
                OP.find_id('com.happyteam.dubbingshow:id/view_bubble').click()
                time.sleep(2)
                names = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')
                name_list = []
                for i in range(len(names)):
                    OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].click()
                    time.sleep(1)
                    name = OP.find_ids('com.happyteam.dubbingshow:id/prop_name')[i].text
                    name_list.append(name)
                    time.sleep(1)
                chat = []
                for i in name_list:
                    if not i in chat:
                        chat.append(i)
                print(chat)
                time.sleep(2)
                #返回匹配首页
                OP.back()
            except(NoSuchElementException,TimeoutException):
                print('道具商城界面跳转失败')
            time.sleep(2)
            print('跟随')
            OP.find_id('com.happyteam.dubbingshow:id/follow').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/refresh').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/close').click()
            time.sleep(2)
            print('开始匹配')
            OP.find_id('com.happyteam.dubbingshow:id/start').click()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/txtContent')
                content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                print(content)
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/show_comment')
                    for i in range(3):
                        OP.find_id('com.happyteam.dubbingshow:id/show_comment').click()
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys('哇喔~~~')
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
                        time.sleep(2)
                    time.sleep(2)
                    OP.back()
                    time.sleep(10)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/start')
                        OP.back()
                    except(NoSuchElementException,TimeoutException):
                        pass
                except(NoSuchElementException,TimeoutException):
                    pass
            time.sleep(2)
            print('退出pia戏')
            time.sleep(1)
            OP.back()
        except(NoSuchElementException,TimeoutError):
            print("在线Pia戏界面跳转失败")

'''有声漫画'''
class Sound_Cartoon():
    '''声漫推荐列表'''
    def Cartoon(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/title')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/title')
                except:
                    print("有声漫画重载失败")
                    OP.back()
                    device().close_app()
            except:
                pass
        time.sleep(2)
        print("上滑列表")
        num = random.randint(5, 10)
        for i in range(num):
            OP.swip_up()
            time.sleep(2)
        time.sleep(3)
        print("返回主界面后再进")
        OP.back()
        time.sleep(3)
        OP.wait_xpath('有声漫画').click()
        time.sleep(2)

    '''声漫集详情'''
    def Comics_collection(self):
        print("点击进入漫画集详情界面")
        OP.wait_id('com.happyteam.dubbingshow:id/imgHead')
        OP.find_ids('com.happyteam.dubbingshow:id/imgHead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/start_play')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(10)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/start_play')
                except:
                    print("漫画集详情重载失败")
                    OP.back()
                    device().close_app()
            except:
                pass
        time.sleep(2)

        try:
            el2 = OP.find_id("com.happyteam.dubbingshow:id/more_content")
            el2.click()
            print("点击简介全部")
        except:
            pass
        time.sleep(2)
        print("点击添加收藏")
        el1 = OP.find_id("com.happyteam.dubbingshow:id/collect")
        el1.click()
        time.sleep(2)
        print("点击提供商")
        OP.find_id('com.happyteam.dubbingshow:id/img').click()
        try:
            OP.wait_not_id('com.happyteam.dubbingshow:id/num_one')
            time.sleep(1)
            OP.back()
        except:
            pass
        time.sleep(1)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/start_play')
        except:
            OP.back()
        time.sleep(2)
        print("点击声漫制作社团排行榜")
        OP.find_id('com.happyteam.dubbingshow:id/num_one').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_top')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("声漫制作社团排行榜列表重载失败")
                    OP.back()
                    device().close_app()
                except:
                    pass
            except:
                pass
        time.sleep(2)
        num_list =[0,1,3,4]
        for i in num_list:
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/tv_top')[i].click()
            except:
                pass
            time.sleep(2)
        try:
            OP.find_ids('com.happyteam.dubbingshow:id/tv_top')[0].click()
        except:
            pass
        time.sleep(2)
        OP.back()
        time.sleep(3)
        print("点击开始播放按钮")
        OP.find_id('com.happyteam.dubbingshow:id/start_play').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/textView')
            OP.find_id('com.happyteam.dubbingshow:id/start_play')
            time.sleep(2)
            print("漫画视频详情加载失败")
        except(TimeoutException,NoSuchElementException):
            pass
        time.sleep(2)
        print("退出漫画视频详情")
        OP.back()
        time.sleep(2)

        print("分别点击每集漫画")
        for i in range(6):
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/name')[i].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/textView')
                    time.sleep(2)
                    print("退出漫画视频详情")
                    OP.back()
                    time.sleep(2)
                except(TimeoutException, NoSuchElementException):
                    OP.find_id('com.happyteam.dubbingshow:id/start_play')
                    time.sleep(2)
                    print("漫画视频详情加载失败")
            except:
                pass

    '''声漫视频详情'''
    def Cartoon_details(self):
        print("点击进入第一话")
        OP.find_ids('com.happyteam.dubbingshow:id/name')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/textView')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/start_play')
                time.sleep(2)
                print("漫画视频详情加载失败")
            except:
                pass
        time.sleep(2)
        print("切换漫画集")
        num_list3 =[1,2,3]
        for i in num_list3:
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/name')[i].click()
                time.sleep(3)
            except:
                pass
            time.sleep(2)
        try:
            OP.find_ids('com.happyteam.dubbingshow:id/name')[0].click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        print("点击配音表第一个用户")
        union_user_name1 = OP.find_ids('com.happyteam.dubbingshow:id/roles_user_name')[0].text
        print("视频详情用户名:", union_user_name1)
        OP.find_ids('com.happyteam.dubbingshow:id/roles_user_name')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
            print("个人空间加载成功")
            time.sleep(3)
            union_user_name2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print("个人空间用户名:", union_user_name2)
            if union_user_name1 == union_user_name2:
                print("用户跳转正确")
            else:
                print("视频详情点击用户与空间跳转后的用户名称不一致！！！")
            time.sleep(3)
            OP.back()
            time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(3)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/more_roles')
            print('点击配音表第二个用户')
            union_user_name3 = OP.find_ids('com.happyteam.dubbingshow:id/roles_user_name')[1].text
            print("视频详情用户名:", union_user_name3)
            OP.find_ids('com.happyteam.dubbingshow:id/roles_user_name')[1].click()

            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                print("个人空间加载成功")
                time.sleep(3)
                union_user_name4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
                print("个人空间用户名:", union_user_name4)
                if union_user_name3 == union_user_name4:
                    print("用户跳转正确")
                else:
                    print("视频详情点击用户与空间跳转后的用户名称不一致！！！")
                time.sleep(3)
                OP.back()
            except(TimeoutException,NoSuchElementException):
                print("空间加载失败")
                time.sleep(3)
                OP.back()
            time.sleep(2)
            print("点击配音表更多")
            OP.find_id('com.happyteam.dubbingshow:id/more_roles').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                print("点击头像进入空间")
                union_user_name5 = OP.find_ids('com.happyteam.dubbingshow:id/name')[0].text
                print("配音表用户名:", union_user_name5)
                OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                    print("个人空间加载成功")
                    time.sleep(3)
                    union_user_name6 = OP.find_id('com.happyteam.dubbingshow:id/username').text
                    print("个人空间用户名:", union_user_name6)
                    if union_user_name5 == union_user_name6:
                        print("用户跳转正确")
                    else:
                        print("配音表列表用户与空间跳转后的用户名称不一致！！！")
                    time.sleep(3)
                    OP.back()
                    time.sleep(2)
                    OP.back()
                except(TimeoutException,NoSuchElementException):
                    print("空间加载失败")
                    time.sleep(3)
                    OP.back()
                time.sleep(2)
            except(TimeoutException,NoSuchElementException):
                print("配音表列表加载失败")
                time.sleep(3)
                OP.back()
        except:
            pass
        time.sleep(2)
        print("收藏声漫")
        OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        time.sleep(3)


        print("上滑切换集数")
        num = random.randint(1, 4)
        for i in range(num):
            OP.swip_up()
            time.sleep(2)
        time.sleep(3)

        print("左滑进入社团空间")
        OP.swip_left()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')
            print("空间加载成功")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)
        print("返回推荐列表界面")
        OP.back()
        time.sleep(3)
        print("返回发现主界面")
        OP.back()
        time.sleep(3)

    '''声漫最新列表'''
    def Newest(self):
        print("点击进入最新列表")
        OP.wait_xpath('最新').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/title')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(3)
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/title')
                    pass
                except:
                    print("有声漫画重载失败")
                    OP.back()
                    driver.close_app()
            except:
                pass
        time.sleep(2)
        print("上滑列表")
        num = random.randint(5, 10)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回发现主界面后再进")
        OP.back()
        time.sleep(3)
        OP.wait_xpath('有声漫画').click()
        time.sleep(2)
        OP.wait_xpath('最新').click()
        time.sleep(2)

    '''点击播放按'''
    def Play_video(self):
        print("点击播放按钮进入声漫视频详情")
        OP.find_id('com.happyteam.dubbingshow:id/play').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/textView')
            time.sleep(2)
            OP.back()
            time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            print("漫画视频详情加载失败")

    '''声漫分类'''
    def Classification(self):
        print("点击分类")
        OP.wait_xpath('分类').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(3)
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/iv_pic1')
                    pass
                except:
                    print("漫画分类重载失败")
                    OP.back()
                    driver.close_app()
            except:
                pass
        time.sleep(2)

        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回发现主界面后再进")
        OP.back()
        time.sleep(3)
        OP.wait_xpath('有声漫画').click()
        time.sleep(2)
        OP.wait_xpath('最新').click()
        time.sleep(2)
        OP.wait_xpath('分类').click()
        time.sleep(2)
        print("点击漫画分类标签")
        OP.wait_xpath('恋爱').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
                except(TimeoutException,NoSuchElementException):
                    print("分类标签中界面重载失败")
            except:
                pass
        time.sleep(2)
        OP.wait_xpath('搞笑').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
                except(TimeoutException,NoSuchElementException):
                    print("分类标签中界面重载失败")
            except:
                pass
        time.sleep(2)
        OP.wait_xpath('热血').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
                except(TimeoutException,NoSuchElementException):
                    print("分类标签中界面重载失败")
            except:
                pass
        time.sleep(2)

        print("点击进入漫画集详情")
        OP.find_id('com.happyteam.dubbingshow:id/iv_pic1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/start_play')
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/start_play')
                    time.sleep(3)
                    OP.back()
                except(TimeoutException,NoSuchElementException):
                    print("漫画集详情重载失败")
                    time.sleep(3)
                    OP.back()
            except:
                pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/iv_pic2').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/start_play')
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/start_play')
                    time.sleep(3)
                    OP.back()
                except(TimeoutException,NoSuchElementException):
                    print("漫画集详情重载失败")
                    time.sleep(3)
                    OP.back()
            except:
                pass
        time.sleep(2)

    '''制作声漫'''
    def Acoustic_diffusion(self):
        print("点击制作声漫")
        OP.find_id('com.happyteam.dubbingshow:id/sm').click()
        try:
            OP.wait_xpath('漫画库')

            print("点击热血")
            OP.find_xpath('热血').click()
            time.sleep(1)

            print("点击恋爱")
            OP.find_xpath('恋爱').click()
            time.sleep(1)

            print("点击搞笑")
            OP.find_xpath('搞笑').click()
            time.sleep(1)

            num = random.randint(2, 6)
            print("上滑:", num, "次")
            for i in range(num):
                # 上滑
                x = driver.get_window_size()['width']
                y = driver.get_window_size()['height']
                devc.swipe(start_x=0.5*x,start_y=0.8*y,end_x=0.5*x,end_y=0.4*y,duration=300)
                time.sleep(2)

            time.sleep(2)
            print("点击声漫搜索")
            OP.find_id('com.happyteam.dubbingshow:id/btn_add').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys(u"你听说过女大学生吗")
            time.sleep(1)
            print("点击搜索")
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            time.sleep(2)
            OP.wait_id('com.happyteam.dubbingshow:id/tv_name1')
            time.sleep(1)
            print("点击声漫进入漫画详情界面")
            OP.find_id('com.happyteam.dubbingshow:id/iv_pic1').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_make')
                Make = OP.find_id('com.happyteam.dubbingshow:id/tv_make').text
                print(Make)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/tv_make').click()
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit')
                    title = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                    print(title)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_make').click()
                except:
                    pass
            except(NoSuchElementException,TimeoutException):
                print('漫画详情加载失败')
            time.sleep(2)
            for i in range(4):
                try:
                    OP.find_xpath('添加配音者')
                    print("点击添加配音者")
                    OP.find_xpath('添加配音者').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/socialstatus')
                    except(NoSuchElementException, TimeoutException):
                        OP.back()
                        time.sleep(1)
                        OP.find_xpath('添加配音者').click()
                    time.sleep(2)
                    print("选择自己配")
                    OP.find_ids('com.happyteam.dubbingshow:id/socialstatus')[0].click()
                    time.sleep(1)
                except:
                    break
            time.sleep(2)
            print("点击发送邀请")
            OP.find_id('com.happyteam.dubbingshow:id/tv_sure').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/sure')
                    OP.find_id('com.happyteam.dubbingshow:id/sure').click()
                except:
                    pass
            time.sleep(5)
            print("返回漫画库")
            OP.back()

            print("点击全部")
            OP.find_xpath('全部').click()
            time.sleep(1)
            num = random.randint(3, 6)
            print("上滑:", num, "次")
            for i in range(num):
                # 上滑
                OP.swip_up()
                time.sleep(2)
            time.sleep(1)
            print("点击我的漫画")
            OP.find_xpath('我的漫画').click()
            time.sleep(1)
            print("下拉刷新")
            OP.swip_down()
            time.sleep(4)
            OP.wait_id('com.happyteam.dubbingshow:id/iv_pic1')
            print("点击漫画")
            OP.find_ids('com.happyteam.dubbingshow:id/iv_pic1')[0].click()
            time.sleep(4)
            print("点击更换配音者")
            OP.find_id('com.happyteam.dubbingshow:id/change').click()
            time.sleep(2)
            OP.find_ids('com.happyteam.dubbingshow:id/change')[0].click()

            try:
                OP.wait_id('com.happyteam.dubbingshow:id/socialstatus')
                print("邀请他人")
                OP.find_ids('com.happyteam.dubbingshow:id/socialstatus')[1].click()
                time.sleep(3)
                Content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                print(Content)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except(NoSuchElementException,TimeoutException):
                    pass
                time.sleep(2)
                print("换回自己")
                OP.find_id('com.happyteam.dubbingshow:id/change').click()
                time.sleep(1)
                OP.find_ids('com.happyteam.dubbingshow:id/change')[0].click()
                OP.wait_id('com.happyteam.dubbingshow:id/socialstatus')
                OP.find_ids('com.happyteam.dubbingshow:id/socialstatus')[0].click()
                time.sleep(4)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except(NoSuchElementException, TimeoutException):
                    pass
            except(NoSuchElementException,TimeoutException):
                OP.back()
            time.sleep(2)

            print("点击后期制作")
            OP.find_id('com.happyteam.dubbingshow:id/make').click()
            time.sleep(3)
            print("切换图片")
            OP.find_ids('com.happyteam.dubbingshow:id/img')[1].click()
            time.sleep(2)
            OP.find_ids('com.happyteam.dubbingshow:id/img')[2].click()
            time.sleep(2)
            print("添加音效")
            OP.find_xpath('添加音效').click()
            time.sleep(3)
            One_level = OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')
            for i in range(len(One_level)):
                class_name = OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')[i].text
                print (class_name)
                OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')[i].click()
                time.sleep(1)
                Second_level = OP.find_ids('com.happyteam.dubbingshow:id/effect_types_img')
                for x in range(len(Second_level)):
                    Name = OP.find_ids('com.happyteam.dubbingshow:id/effect_types_name')[x].text
                    print (Name)
                    time.sleep(1)
                    OP.find_ids('com.happyteam.dubbingshow:id/effect_types_name')[x].click()
                    time.sleep(3)
                    Three_level = OP.find_ids('com.happyteam.dubbingshow:id/effect_sound_name')
                    Three_Name_list = []
                    for y in range(len(Three_level)):
                        Name = OP.find_ids('com.happyteam.dubbingshow:id/effect_sound_name')[y].text
                        Three_Name_list.append(Name)
                        time.sleep(1)
                        OP.find_ids('com.happyteam.dubbingshow:id/effect_sound_name')[y].click()
                        time.sleep(3)
                    print (Three_Name_list)
                time.sleep(2)
            print("点击添加音效")
            OP.find_id('com.happyteam.dubbingshow:id/tag').click()
            time.sleep(2)
            print ('点击录音按钮')
            OP.find_id('com.happyteam.dubbingshow:id/transcribe').click()
            time.sleep(10)
            OP.find_id('com.happyteam.dubbingshow:id/transcribe').click()
            time.sleep(4)
            print("点击图片播放按钮")
            OP.find_id('com.happyteam.dubbingshow:id/preview').click()
            time.sleep(10)
            print("点击进入添加背景音界面")
            OP.find_id('com.happyteam.dubbingshow:id/upload').click()
            try:
                OP.wait_load('添加背景音')
                print ('获取背景音列表')
                One_level = OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')
                for i in range(len(One_level)):
                    OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')[i].click()
                    time.sleep(2)
                    Name = OP.find_ids('com.happyteam.dubbingshow:id/comic_sound_class_name')[i].text
                    print (Name)
                    Second_level = OP.find_ids('com.happyteam.dubbingshow:id/name')
                    Name_list = []
                    for x in range(len(Second_level)):
                        Name = OP.find_ids('com.happyteam.dubbingshow:id/name')[x].text
                        Name_list.append(Name)
                        time.sleep(1.5)
                    print (Name_list)
                    time.sleep(2)
                time.sleep(2)

                print("点击添加背景音分类")
                OP.find_xpath('舒缓').click()
                time.sleep(1)
                print("点击播放背景音")
                OP.find_ids('com.happyteam.dubbingshow:id/preview')[1].click()
                time.sleep(10)
                print("添加背景音")
                OP.find_ids("com.happyteam.dubbingshow:id/add")[0].click()
                time.sleep(5)
                devc.keyevent(3)
                time.sleep(2)
                devc.launch_app()
                time.sleep(4)
                TouchAction(devc).press(x=0.925*x, y=0.738*y).move_to(x=0.069*x, y=0.738*y).release().perform()
                time.sleep(2)
                OP.find_xpath('完成').click()
                time.sleep(10)
                try:
                    OP.find_xpath('完成')
                    time.sleep(2)
                    print('背景音添加失败')
                    OP.back()
                except:
                    pass
                time.sleep(1)
                print("点击视频中的播放按钮")
                OP.find_id('com.happyteam.dubbingshow:id/preview').click()
                time.sleep(10)
                try:
                    OP.find_xpath('保存')
                    print("点击保存")
                    OP.find_xpath('保存').click()
                except:
                    pass
                time.sleep(3)
                print("点击下一步")
                time.sleep(1)
                OP.find_xpath('下一步').click()
                try:
                    OP.wait_download('com.happyteam.dubbingshow:id/upload')
                    print("进入声漫上传界面")
                    time.sleep(1)
                    print("点击播放")
                    OP.find_id('com.happyteam.dubbingshow:id/preview').click()
                    time.sleep(5)
                    print("应用退到后台停留3秒")
                    devc.keyevent(3)
                    time.sleep(3)
                    devc.launch_app()
                    time.sleep(1)
                    print("点击保存并退出")
                    OP.find_id('com.happyteam.dubbingshow:id/savebtn').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/make')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/make')
                        print("保存成功")
                    except:
                        OP.find_id('com.happyteam.dubbingshow:id/savebtn')
                        OP.find_id('com.happyteam.dubbingshow:id/savebtn').click()
                    time.sleep(2)
                    print("点击后期制作")
                    OP.find_id('com.happyteam.dubbingshow:id/make').click()
                    time.sleep(2)
                    print("点击下一步")
                    OP.find_id('com.happyteam.dubbingshow:id/upload').click()
                    try:
                        OP.wait_xpath('添加背景音')
                        print("进入添加背景音界面")
                        OP.find_xpath('下一步').click()
                        try:
                            OP.wait_id('com.happyteam.dubbingshow:id/upload')
                            print("进入声漫上传界面")
                            OP.find_id('com.happyteam.dubbingshow:id/upload').click()
                            try:
                                OP.find_xpath('创建社团')
                                print("创建社团")
                                Union_name = random.randint(100, 10000)
                                OP.find_id('com.happyteam.dubbingshow:id/nick').send_keys(Union_name)
                                time.sleep(2)
                                OP.find_id('com.happyteam.dubbingshow:id/tv_sure').click()
                            except:
                                pass
                            time.sleep(2)
                            try:
                                OP.wait_id('com.happyteam.dubbingshow:id/container')
                                print("声漫上传成功")
                                OP.find_id('com.happyteam.dubbingshow:id/imgurl').click()
                                try:
                                    OP.wait_id('com.happyteam.dubbingshow:id/gift')
                                    print("进入声漫作品详情界面")
                                    time.sleep(10)
                                    OP.back()
                                except(NoSuchElementException,TimeoutException):
                                    print('声漫视频详情界面加载失败')
                                time.sleep(2)
                                el = OP.find_id('com.happyteam.dubbingshow:id/imgurl')
                                print("长按删除")
                                TouchAction(device()).long_press(el).perform()
                                time.sleep(2)
                                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                                time.sleep(2)
                                print("返回我的漫画列表界面")
                                OP.back()
                                time.sleep(2)
                                print("删除漫画合辑")
                                OP.find_ids('com.happyteam.dubbingshow:id/close1')[0].click()
                                time.sleep(2)
                                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                                time.sleep(5)
                                print("返回素材库界面")
                                OP.back()
                            except:
                                print("声漫上传失败5")
                                print("退出APP")
                                driver.close_app()
                        except:
                            print("声漫合成失败4")
                            print("退出APP")
                            driver.close_app()
                    except(NoSuchElementException,TimeoutException):
                        print("声漫合成失败3")
                        print("退出APP")
                        driver.close_app()
                except(NoSuchElementException,TimeoutException):
                    print("声漫合成失败2")
                    print("退出APP")
                    driver.close_app()
            except:
                print("声漫合成失败1")
                print("退出APP")
                driver.close_app()
        except(NoSuchElementException,TimeoutException):
            print("返回素材库")
            OP.back()

    '''漫画收藏'''
    def Collect(self):
        print("点击收藏")
        OP.find_id('com.happyteam.dubbingshow:id/collect').click()
        try:
            OP.wait_xpath('收藏')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(3)
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("漫画收藏列表重载失败")
                    OP.back()
                except:
                    pass
            except:
                pass
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/imgHead').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(3)
                OP.back()
            except(TimeoutException,NoSuchElementException):
                print("点击进入漫画视频详情失败")
            time.sleep(3)
            print("删除收藏漫画")
            el = OP.find_id('com.happyteam.dubbingshow:id/imgHead')
            TouchAction(driver).long_press(el).release().perform()
            try:
                OP.wait_xpath('确定')
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(3)
            except(TimeoutException,NoSuchElementException):
                pass
        except:
            print("未收藏漫画")
        time.sleep(2)
        print("返回分类界面")
        OP.back()
        time.sleep(2)
        print("返回发现界面")
        OP.back()
        time.sleep(2)

'''附近'''
class Nearby():
    def Near(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/txtTitle')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("附近列表重载失败")
                    OP.back()
                except:
                    pass
            except(TimeoutException,NoSuchElementException):
                pass
        time.sleep(2)
        print("点击进入视频详情")
        OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/filmBg')
                print("视频详情加载失败")
                OP.back()
            except:
                time.sleep(3)
                OP.back()
        time.sleep(2)
        print("上滑列表")
        num = random.randint(5, 10)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("退出视频详情")
        OP.back()
        time.sleep(2)
        OP.back()

'''曝光'''
class Exposure():
    def Exposure_area(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
            except(TimeoutException,NoSuchElementException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("曝光区列表重载失败")
                    OP.back()
                except:
                    pass
        time.sleep(2)
        print("点击进入视频详情")
        OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/filmBg')
                print("视频详情加载失败")
            except:
                pass
        time.sleep(3)
        print("点击评论按钮")
        OP.find_id('com.happyteam.dubbingshow:id/comment').click()
        time.sleep(3)
        try:
            OP.wait_xpath('作者已关闭评论，当前评论隐藏')
            off_comment = OP.wait_xpath('作者已关闭评论，当前评论隐藏').text
            print(off_comment, "收起评论弹窗")
            time.sleep(2)
            OP.back()
            time.sleep(2)
            print("退出视频详情")
            OP.back()
        except:
            print("发送评论")
            OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("赞一个!")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
            time.sleep(10)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btn_send')
                print("评论发送失败")
                OP.back()
                time.sleep(2)
                print("退出视频详情")
                OP.back()
            except:
                print("评论发送成功")
                time.sleep(4)
                OP.back()
                time.sleep(2)
                print("退出视频详情")
                OP.back()
        time.sleep(4)
        print("上滑列表")
        num = random.randint(5, 10)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回首页")
        OP.back()
        time.sleep(10)

'''排行榜'''
class Ranking_List():
    def Rank(self):
        try:
            OP.wait_xpath('排行榜')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("排行榜列表重载失败")
                    OP.back()
                except:
                    pass
            except(NoSuchElementException,TimeoutException):
                pass
        time.sleep(2)
        print("点击规则")
        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/close').click()
        time.sleep(2)

    '''富豪榜'''
    def RichRank(self):
        print("点击富豪榜")
        OP.find_id('com.happyteam.dubbingshow:id/rich_rank').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/username1')
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print("富豪榜重载失败")
                    time.sleep(3)
                    OP.back()
                except:
                    pass
            except(TimeoutException,NoSuchElementException):
                pass
        time.sleep(5)

        print("点击榜一用户")
        username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        print(username1)
        OP.find_id('com.happyteam.dubbingshow:id/userHead1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username2)
            if username1 == username2:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(2)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(4)

        print("点击榜二用户")
        username3 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        print(username3)
        OP.find_id('com.happyteam.dubbingshow:id/userHead2').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username4)
            if username3 == username4:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击其它用户")
        username5 = OP.find_ids('com.happyteam.dubbingshow:id/username')[0].text
        print(username5)
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username6 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username6)
            if username5 == username6:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("日榜1-4名用户及消费额度")
        T_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        T_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        T_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        T_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        T_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        T_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        T_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        T_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", T_Username1, T_Count1,
              "第二名:", T_Username2, T_Count2,
              "第三名:", T_Username3, T_Count3,
              "第四名:", T_Username4, T_Count4
              )
        time.sleep(3)

        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("周榜1-4名用户及消费额度")
        OP.wait_xpath('周榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("周榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass

        time.sleep(2)
        W_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        W_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        W_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        W_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        W_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        W_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        W_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        W_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", W_Username1, W_Count1,
              "第二名:", W_Username2, W_Count2,
              "第三名:", W_Username3, W_Count3,
              "第四名:", W_Username4, W_Count4
              )

        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("月榜1-4名用户及消费额度")
        OP.wait_xpath('月榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("月榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        M_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        M_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        M_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        M_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        M_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        M_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        M_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        M_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", M_Username1, M_Count1,
              "第二名:", M_Username2, M_Count2,
              "第三名:", M_Username3, M_Count3,
              "第四名:", M_Username4, M_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回排行榜")
        OP.back()
        time.sleep(2)

    '''主播榜'''
    def LiveRank(self):
        print("点击主播榜")
        OP.find_id('com.happyteam.dubbingshow:id/live_rank').click()
        OP.wait_id('com.happyteam.dubbingshow:id/username1')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("富豪榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击榜一用户")
        username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        print(username1)
        OP.find_id('com.happyteam.dubbingshow:id/userHead1').click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username2)
            if username1 == username2:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击榜二用户")
        username3 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        print(username3)
        OP.find_id('com.happyteam.dubbingshow:id/userHead2').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username4)
            if username3 == username4:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击其它用户")
        username5 = OP.find_ids('com.happyteam.dubbingshow:id/username')[0].text
        print(username5)
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            username6 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username6)
            if username5 == username6:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("日榜1-4名用户及参与人数")
        T_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        T_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        T_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        T_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        T_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        T_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        T_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        T_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", T_Username1, T_Count1,
              "第二名:", T_Username2, T_Count2,
              "第三名:", T_Username3, T_Count3,
              "第四名:", T_Username4, T_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("周榜1-4名用户及参与人数")
        OP.wait_xpath('周榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("周榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        W_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        W_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        W_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        W_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        W_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        W_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        W_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        W_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", W_Username1, W_Count1,
              "第二名:", W_Username2, W_Count2,
              "第三名:", W_Username3, W_Count3,
              "第四名:", W_Username4, W_Count4
              )

        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("月榜1-4名用户及参与人数")
        OP.wait_xpath('月榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("月榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        M_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        M_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        M_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        M_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        M_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        M_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        M_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        M_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", M_Username1, M_Count1,
              "第二名:", M_Username2, M_Count2,
              "第三名:", M_Username3, M_Count3,
              "第四名:", M_Username4, M_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回排行榜")
        OP.back()
        time.sleep(2)

    '''社团榜'''
    def SocietyRank(self):
        print("点击社团榜")
        OP.find_id('com.happyteam.dubbingshow:id/society_rank').click()
        OP.wait_id('com.happyteam.dubbingshow:id/username1')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("富豪榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击榜一用户")
        username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        print(username1)
        OP.find_id('com.happyteam.dubbingshow:id/userHead1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')
            username2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username2)
            if username1 == username2:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击榜二用户")
        username3 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        print(username3)
        OP.find_id('com.happyteam.dubbingshow:id/userHead2').click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')
            username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username4)
            if username3 == username4:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击其它用户")
        username5 = OP.find_ids('com.happyteam.dubbingshow:id/username')[0].text
        print(username5)
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')
            username6 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username6)
            if username5 == username6:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("日榜1-4名用户及作品数")
        T_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        T_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        T_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        T_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        T_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        T_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        T_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        T_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", T_Username1, T_Count1,
              "第二名:", T_Username2, T_Count2,
              "第三名:", T_Username3, T_Count3,
              "第四名:", T_Username4, T_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("周榜1-4名用户及作品数")
        OP.wait_xpath('周榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("周榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        W_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        W_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        W_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        W_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        W_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        W_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        W_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        W_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", W_Username1, W_Count1,
              "第二名:", W_Username2, W_Count2,
              "第三名:", W_Username3, W_Count3,
              "第四名:", W_Username4, W_Count4
              )

        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("月榜1-4名用户及作品数")
        OP.wait_xpath('月榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("月榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        M_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        M_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        M_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        M_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        M_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        M_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        M_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        M_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", M_Username1, M_Count1,
              "第二名:", M_Username2, M_Count2,
              "第三名:", M_Username3, M_Count3,
              "第四名:", M_Username4, M_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回排行榜")
        OP.back()
        time.sleep(2)

    '''素材榜'''
    def SourceRank(self):
        print("点击素材榜")
        OP.find_id('com.happyteam.dubbingshow:id/source_rank').click()
        OP.wait_id('com.happyteam.dubbingshow:id/username1')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("富豪榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击榜一用户")
        username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        print(username1)
        OP.find_id('com.happyteam.dubbingshow:id/userHead1').click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
            username2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username2)
            if username1 == username2:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击榜二用户")
        username3 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        print(username3)
        OP.find_id('com.happyteam.dubbingshow:id/userHead2').click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
            username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username4)
            if username3 == username4:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("点击其它用户")
        username5 = OP.find_ids('com.happyteam.dubbingshow:id/username')[0].text
        print(username5)
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()

        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
            username6 = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print(username6)
            if username5 == username6:
                print("用户名称一致")
            else:
                print("排行榜用户名与空间用户名不一致")
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(3)
            OP.back()
        time.sleep(2)

        print("日榜1-4名用户及收录素材数")
        T_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        T_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        T_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        T_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        T_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        T_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        T_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        T_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", T_Username1, T_Count1,
              "第二名:", T_Username2, T_Count2,
              "第三名:", T_Username3, T_Count3,
              "第四名:", T_Username4, T_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("周榜1-4名用户及收录素材数")
        OP.wait_xpath('周榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("周榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        W_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        W_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        W_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        W_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        W_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        W_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        W_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        W_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", W_Username1, W_Count1,
              "第二名:", W_Username2, W_Count2,
              "第三名:", W_Username3, W_Count3,
              "第四名:", W_Username4, W_Count4
              )

        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("月榜1-4名用户及收录素材数")
        OP.wait_xpath('月榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("月榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)
        M_Username1 = OP.find_id('com.happyteam.dubbingshow:id/username1').text
        M_Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1').text
        M_Username2 = OP.find_id('com.happyteam.dubbingshow:id/username2').text
        M_Count2 = OP.find_id('com.happyteam.dubbingshow:id/count2').text
        M_Username3 = OP.find_id('com.happyteam.dubbingshow:id/username3').text
        M_Count3 = OP.find_id('com.happyteam.dubbingshow:id/count3').text
        M_Username4 = OP.find_id('com.happyteam.dubbingshow:id/username').text
        M_Count4 = OP.find_ids('com.happyteam.dubbingshow:id/desc')[0].text
        print("第一名:", M_Username1, M_Count1,
              "第二名:", M_Username2, M_Count2,
              "第三名:", M_Username3, M_Count3,
              "第四名:", M_Username4, M_Count4
              )
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回排行榜")
        OP.back()
        time.sleep(2)

    '''作品榜'''
    def Film(self):
        print("点击作品榜")
        OP.find_id('com.happyteam.dubbingshow:id/film').click()
        OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("作品榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击进入视频详情")
        OP.find_ids('com.happyteam.dubbingshow:id/iv_source')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            time.sleep(3)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                print("视频详情进入失败")
            except:
                pass
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

    '''标签榜'''
    def Commentary(self):
        print("点击标签榜")
        OP.find_id('com.happyteam.dubbingshow:id/commentary').click()
        OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("作品榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击进入视频详情")
        works_name1 = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[0].text
        print("作品名称:", works_name1)
        print("点击进入视频详情")
        OP.find_ids('com.happyteam.dubbingshow:id/iv_source')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            time.sleep(3)
            OP.back()
        except:
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                print("视频详情进入失败")
            except:
                pass
        time.sleep(3)

        OP.find_id('com.happyteam.dubbingshow:id/commentary').click()
        try:
            OP.wait_xpath('热门频道')
            num = random.randint(1, 9)
            OP.find_ids('com.happyteam.dubbingshow:id/tv')[num].click()
            time.sleep(4)
            works_name2 = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[0].text
            print("作品名称:", works_name2)
            if works_name1 == works_name2:
                print("切换标签失败")
            else:
                print("标签切换成功")
        except(TimeoutException,NoSuchElementException):
            print("未显示出标签选择弹窗")
        time.sleep(3)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

    '''潜力榜'''
    def Potential(self):
        print("点击潜力榜")
        OP.find_id('com.happyteam.dubbingshow:id/potential').click()
        OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("作品榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击进入视频详情")
        OP.find_ids('com.happyteam.dubbingshow:id/iv_source')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            time.sleep(3)
            OP.back()
        except:
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                print("视频详情进入失败")
            except:
                pass
        time.sleep(3)
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

    '''社作榜'''
    def SocietyFilm(self):
        print("点击社作榜")
        OP.find_id('com.happyteam.dubbingshow:id/society_film').click()
        OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("作品榜重载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except:
            pass
        time.sleep(2)

        print("点击进入视频详情")
        OP.find_ids('com.happyteam.dubbingshow:id/iv_source')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            time.sleep(3)
            OP.back()
        except:
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                print("视频详情进入失败")
            except:
                pass
        time.sleep(3)
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("返回发现界面")
        OP.back()
        time.sleep(2)

'''频道'''
class Label():
    '''发现-标签列表'''
    def Label_list(self):
        try:
            OP.find_id('com.happyteam.dubbingshow:id/img_tv')
            print("存在活动标签,点击标签")
            OP.find_ids('com.happyteam.dubbingshow:id/')[0].click()
            time.sleep(3)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/img_tv')
                print("标签跳转失败")
            except:
                pass
        except:
            print('不存在活动标签')
        time.sleep(2)
        print("点击其它标签")
        OP.find_ids('com.happyteam.dubbingshow:id/tv')[1].click()
        OP.wait_xpath('最热')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("列表加载失败")
                time.sleep(3)
                OP.back()
            except:
                pass
        except(TimeoutException,NoSuchElementException):
            pass
        time.sleep(2)
        print("点击进入视频")
        OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
        time.sleep(3)
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except(TimeoutException,NoSuchElementException):
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(10)
                device().keyevent(3)
                time.sleep(3)
                device().launch_app()
                time.sleep(2)
                print("退出视频详情")
                OP.back()
            except:
                pass
        time.sleep(2)

        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

        print("切换tab")
        OP.wait_xpath('最新').click()
        OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("列表重载失败")
            except:
                pass
        except:
            pass
        time.sleep(2)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        OP.wait_xpath('排行榜').click()
        OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("列表重载失败")
            except:
                pass
        except:
            pass
        time.sleep(2)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)
        print("退出标签详情")
        OP.back()
        time.sleep(2)
        print("点击更多标签")
        OP.wait_xpath('更多频道').click()
        time.sleep(3)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/tv')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/tv')
                OP.find_id('com.happyteam.dubbingshow:id/tv').click()
                OP.wait_id('com.happyteam.dubbingshow:if/filmBg')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/filmBg')
                    time.sleep(2)
                    OP.back()
                except:
                    print("全部标签界面重载失败")
                    time.sleep(3)
                    OP.back()
            except:
                print("全部标签界面重载失败")
                time.sleep(3)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            OP.find_id('com.happyteam.dubbingshow:id/tv').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
                time.sleep(2)
                OP.back()
            except(TimeoutException,NoSuchElementException):
                print("点击标签跳转失败")
            time.sleep(2)
            print("标签搜索")
            OP.find_id('com.happyteam.dubbingshow:id/edit_text').send_keys("秀秀")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_search').click()
            time.sleep(2)
            try:
                OP.wait_xpath('暂时还没有该标签喔~')
                tip = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tip)
            except:
                label = OP.find_id('com.happyteam.dubbingshow:id/tv').text
                print(label)
                OP.find_id('com.happyteam.dubbingshow:id/tv').click()
                time.sleep(5)
                OP.back()
        time.sleep(2)
        OP.back()
        time.sleep(2)

    '''热门标签'''
    def Hot_label(self):
        print("点击热门标签的作品")
        OP.find_id('com.happyteam.dubbingshow:id/img').click()
        time.sleep(3)
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except(NoSuchElementException,TimeoutException):
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(3)
            except:
                pass
        time.sleep(2)

        print("上滑切换视频")
        num = random.randint(3, 7)
        for i in range(num):
            OP.swip_up()
            time.sleep(5)
        time.sleep(3)
        print("退出视频")
        OP.back()
        time.sleep(2)
        print("上滑列表")
        num = random.randint(3, 7)
        for i in range(num):
            print(i)
            OP.swip_up()
            time.sleep(3)
        time.sleep(3)

'''语聊'''
class Chat():
    '''点击进入语聊界面'''
    def Into_chat(self):
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_theme_image')
        except(NoSuchElementException,TimeoutException):
            print('语聊界面界面加载失败')
            devc.quit()
        time.sleep(2)
    '''语聊banner'''
    def banner(self):
        OP.find_id('com.happyteam.dubbingshow:id/img').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/titlebar')
            time.sleep(4)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            print('banner详情加载失败')
        time.sleep(2)

    '''榜单'''
    def List(self):
        OP.find_id('com.happyteam.dubbingshow:id/rl_all').click()
        OP.wait_id('com.happyteam.dubbingshow:id/title')
        Title = OP.find_id('com.happyteam.dubbingshow:id/title').text
        time.sleep(2)
        if Title == '收入榜':
            OP.find_xpath('收入榜')
            print('收入榜')
            time.sleep(1)
            OP.wait_id('com.happyteam.dubbingshow:id/user_img1')
            OP.find_id('com.happyteam.dubbingshow:id/user_img1').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                print('空间加载失败')
                time.sleep(1)
                OP.back()
            time.sleep(2)
            print('获取榜单用户名称、钻石额度')
            Count1_list = OP.find_ids('com.happyteam.dubbingshow:id/count1')
            List_day = []
            for i in range(len(Count1_list)):
                Name1 = OP.find_ids('com.happyteam.dubbingshow:id/name1')[i].text
                Count1 = OP.find_ids('com.happyteam.dubbingshow:id/count1')[i].text
                Name2 = OP.find_ids('com.happyteam.dubbingshow:id/name1')[i].text
                Count2 = OP.find_ids('com.happyteam.dubbingshow:id/count1')[i].text
                Name3 = OP.find_ids('com.happyteam.dubbingshow:id/name1')[i].text
                Count3 = OP.find_ids('com.happyteam.dubbingshow:id/count1')[i].text
                List_day.append(Name1)
                List_day.append(Count1)
                List_day.append(Name2)
                List_day.append(Count2)
                List_day.append(Name3)
                List_day.append(Count3)
                time.sleep(1)
            print(List_day)
            time.sleep(2)
            OP.back()
            time.sleep(2)
        elif Title =='贡献榜':
            OP.find_xpath('贡献榜')
            print('贡献榜')
            OP.wait_id('com.happyteam.dubbingshow:id/user_img1')
            OP.find_id('com.happyteam.dubbingshow:id/user_img1').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                print('空间加载失败')
                time.sleep(1)
                OP.back()
            time.sleep(2)
            '''获取榜单用户名称、钻石额度'''
            Count1_list = OP.find_ids('com.happyteam.dubbingshow:id/count1')
            List_day = []
            for i in range(len(Count1_list)):
                Name1 = OP.find_id('com.happyteam.dubbingshow:id/name1')[i].text
                Count1 = OP.find_id('com.happyteam.dubbingshow:id/count1')[i].text
                Name2 = OP.find_id('com.happyteam.dubbingshow:id/name1')[i].text
                Count2 = OP.find_id('com.happyteam.dubbingshow:id/count1')[i].text
                Name3 = OP.find_id('com.happyteam.dubbingshow:id/name1')[i].text
                Count3 = OP.find_id('com.happyteam.dubbingshow:id/count1')[i].text
                List_day.append(Name1)
                List_day.append(Count1)
                List_day.append(Name2)
                List_day.append(Count2)
                List_day.append(Name3)
                List_day.append(Count3)
                time.sleep(1)
            print(List_day)
            time.sleep(2)
            OP.back()
            time.sleep(2)
        elif Title=='等级榜':
            OP.find_xpath('等级榜')
            print('等级榜')
            OP.wait_id('com.happyteam.dubbingshow:id/user_head')
            OP.find_id('com.happyteam.dubbingshow:id/user_head').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                print('空间加载失败')
                time.sleep(1)
                OP.back()
            time.sleep(2)
            '''获取榜单用户名称'''
            User_name_list = OP.find_id('com.happyteam.dubbingshow:id/user_name')
            Name_list = []
            for i in range(len(User_name_list)):
                Name = OP.find_id('com.happyteam.dubbingshow:id/user_name')[i].text
                count = OP.find_id('com.happyteam.dubbingshow:id/tv_count')[i].text
                Name_list.append(Name)
                Name_list.append(count)
                time.sleep(1)
            print(Name_list)
            time.sleep(2)
            '''上滑'''
            for i in range(5):
                OP.swip_up()
                time.sleep(3)
            OP.back()
            time.sleep(2)
        else:
            print('界面加载失败')

    '''语聊房间列表'''
    def Chat_List(self):
        '''获取当前界面语聊房间信息'''
        user_names = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')
        Chat_list = []
        for  i in range(len(user_names)):
            chat_name = OP.find_ids('com.happyteam.dubbingshow:id/item_title')[i].text
            num_count = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')[i].text
            Chat_list.append('语聊房间名称:')
            Chat_list.append(chat_name)
            Chat_list.append('房间用户数量')
            Chat_list.append(num_count)
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/item_state_text')[i]
                chat_type = OP.find_ids('com.happyteam.dubbingshow:id/item_state_text')[i].text
                Chat_list.append('房间类型')
                Chat_list.append(chat_type)
            except:
                pass
            time.sleep(1)
            chat_name1 = OP.find_ids('com.happyteam.dubbingshow:id/item_title1')[i].text
            num_count1 = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number1')[i].text
            Chat_list.append('语聊房间名称:')
            Chat_list.append(chat_name1)
            Chat_list.append('房间用户数量')
            Chat_list.append(num_count1)
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/item_state_text1')[i]
                chat_type = OP.find_ids('com.happyteam.dubbingshow:id/item_state_text1')[i].text
                Chat_list.append('房间类型')
                Chat_list.append(chat_type)
            except:
                pass
            time.sleep(1)
        pprint(Chat_list)
        time.sleep(2)
        '''上滑加载列表'''
        i = 1
        while i<=3 :
            OP.swip_up()
            time.sleep(3)
            i+=1
        time.sleep(2)
        '''返回列表顶部'''
        OP.back()
        time.sleep(2)
        OP.wait_xpath('语聊').click()
        time.sleep(10)

    '''语聊中心'''
    def chat_personal(self):
        '''点击进入语聊中心'''
        OP.find_id('com.happyteam.dubbingshow:id/my_user_head').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/level_count')
            count=OP.find_id('com.happyteam.dubbingshow:id/level_count').text
            print('当前经验值:',count)
            time.sleep(2)
            Level = OP.find_id('com.happyteam.dubbingshow:id/left_level_name').text
            print('当前等级:',Level)
            time.sleep(2)
            print('麦位配饰')
            OP.find_id('com.happyteam.dubbingshow:id/peishi').click()
            time.sleep(8)
            OP.back()
            time.sleep(2)
            print ('聊天气泡')
            OP.find_id('com.happyteam.dubbingshow:id/qipao').click()
            time.sleep(8)
            OP.back()
            time.sleep(2)
            print ('日常任务')
            OP.swip_up()
            time.sleep(2)
            Tasks = OP.find_ids('com.happyteam.dubbingshow:id/level_desc')
            Task_list = []
            for i in range(len(Tasks)):
                Experience = OP.find_ids('com.happyteam.dubbingshow:id/level_desc')[i].text
                Name = OP.find_ids('com.happyteam.dubbingshow:id/name')[i].text
                Condition = OP.find_ids('com.happyteam.dubbingshow:id/day_desc')[i].text
                Task_list.append(Name)
                Task_list.append(Condition)
                Task_list.append(Experience)
                time.sleep(1)
            print (Task_list)
            time.sleep(2)
            '''退出语聊中心'''
            OP.back()
            time.sleep(2)
        except(NoSuchElementException,TimeoutException):
            print('语聊中心加载失败')
            time.sleep(2)
            OP.back()

    '''进入他人语聊房间'''

    def enter_chat(self):
        OP.find_id('com.happyteam.dubbingshow:id/item_theme_image').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/comfirm')
            OP.find_id('com.happyteam.dubbingshow:id/comfirm').click()
        except:
            pass
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/function_send_gift')
        except(NoSuchElementException, TimeoutException):
            print('语聊房间加载失败')
        print('关注主播')
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift_single_role_name')
            OP.find_id('com.happyteam.dubbingshow:id/gift_single_role_name').click()
            time.sleep(2)
            OP.wait_xpath('关注')
            OP.find_id('com.happyteam.dubbingshow:id/btn_follow').click()
        except:
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/icon_close').click()
        time.sleep(1)
        OP.back()
        time.sleep(2)
        print('热度值')
        time.sleep(1)
        hot_value = OP.find_id('com.happyteam.dubbingshow:id/gift_value_count').text
        print(hot_value)
        print('累计人数')
        time.sleep(1)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/pack_up')
            OP.find_id('com.happyteam.dubbingshow:id/pack_up').click()
        except:
            pass
        online_count = OP.find_id('com.happyteam.dubbingshow:id/count').text
        print(online_count)
        time.sleep(2)
        print('连麦人及礼物值')
        names = OP.find_ids('com.happyteam.dubbingshow:id/gift_value')
        num = len(names)
        if num == 8:
            list = []
            for i in range(len(names)):
                name = OP.find_ids('com.happyteam.dubbingshow:id/name')[i].text
                list.append(name)
                time.sleep(1)
            print(list)
        else:
            print('连麦人数不足8人，暂不统计')
        time.sleep(2)
        print('榜单')
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(3)
        value = OP.find_id('com.happyteam.dubbingshow:id/tv_rank').text
        print(value)
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/tv_rank').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/list_title')
            print('送礼用户列表')
            time.sleep(2)
            names = OP.find_ids('com.happyteam.dubbingshow:id/textView')
            name_list = []
            for i in range(len(names)):
                name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                name_list.append(name)
                time.sleep(1)
            print(name_list)
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/gift_img').click()
            time.sleep(2)
            gifts = OP.find_ids('com.happyteam.dubbingshow:id/text1')
            list = []
            for i in range(len(gifts)):
                name = OP.find_ids('com.happyteam.dubbingshow:id/text1')[i].text
                count = OP.find_ids('com.happyteam.dubbingshow:id/text2')[i].text
                list.append(name)
                list.append(count)
                time.sleep(0.5)
            print(list)
            time.sleep(2)
            OP.back()
            time.sleep(2)
            '''返回房间'''
            OP.back()
            time.sleep(2)
        except(NoSuchElementException, TimeoutException):
            print('送礼列表加载失败')
            OP.back()
        time.sleep(2)
        print('切换直播间')
        for i in range(10):
            OP.swip_left()
            time.sleep(4)
        print('退出语聊')
        OP.back()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)

    '''创建语聊'''
    def create_chat(self):
        print ('创建语聊')
        OP.find_id('com.happyteam.dubbingshow:id/create').click()
        time.sleep(4)
        try:
            OP.find_xpath('实名认证')
            print('该用户未开通创建语聊房间权限')
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/start_live')
                print ('选择图片')
                OP.find_id('com.happyteam.dubbingshow:id/img').click()
                time.sleep(2)
                '''选择相册'''
                OP.find_id('com.happyteam.dubbingshow:id/tv_photo').click()
                '''获取当前界面所有图片后随即选择一张图'''
                photos = OP.find_ids('com.happyteam.dubbingshow:id/photo_wall_item_photo')
                num = random.randint(0,int(len(photos)-1))
                OP.find_ids('com.happyteam.dubbingshow:id/photo_wall_item_photo')[num].click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                time.sleep(4)
                print ('输入标题')
                OP.find_id('com.happyteam.dubbingshow:id/title').send_keys(u'秀出天际')
                time.sleep(2)
                print ('取消复选框选择状态')
                '''通知粉丝'''
                Result = OP.find_id('com.happyteam.dubbingshow:id/check_box').get_attribute("checked")
                check = 'true'
                if Result == check:
                    OP.find_id('com.happyteam.dubbingshow:id/check_box').click()
                else:
                    pass
                time.sleep(2)
                '''通知社团'''
                Result1 = OP.find_id('com.happyteam.dubbingshow:id/check_box1').get_attribute("checked")
                if Result1 == check:
                    OP.find_id('com.happyteam.dubbingshow:id/check_box').click()
                else:
                    pass
                time.sleep(2)
                '''公约复选框'''
                Result2 = OP.find_id('com.happyteam.dubbingshow:id/tongyi').get_attribute("checked")
                if Result2 == check:
                    pass
                else:
                    OP.find_id('com.happyteam.dubbingshow:id/tongyi').click()
                time.sleep(2)
                print ('选择房间话题标签')
                OP.find_id('com.happyteam.dubbingshow:id/tag_name').click()
                time.sleep(2)
                TVs = OP.find_ids('com.happyteam.dubbingshow:id/tv')
                tv_name = []
                for tv in range(len(TVs)):
                    name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[tv].text
                    tv_name.append(name)
                    time.sleep(0.5)
                print(tv_name)
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/tv').click()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tag_name1')
                    print('房间话题添加成功')
                except:
                    print('话题添加失败')
                time.sleep(2)
                print ('点击创建房间')
                OP.find_id('com.happyteam.dubbingshow:id/start_live').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    print ('麦克风静音')
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/home_microphone1').click()
                    time.sleep(2)
                    OP.find_xpath('静音').click()
                    time.sleep(2)
                    OP.wait_xpath('结束静音').click()
                    print ('开启排麦')
                    time.sleep(2)
                    OP.find_xpath('开启排麦').click()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    print ('修改公告')
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/pack_up')
                        content = OP.find_id('com.happyteam.dubbingshow:id/marquee').text
                        print(content)
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/pack_up').click()
                    except:
                        pass
                    time.sleep(2)
                    OP.find_xpath('com.happyteam.dubbingshow:id/tv').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/marquee').click()
                    time.sleep(2)
                    content = "江南可采莲，莲叶何田田，鱼戏莲叶间。鱼戏莲叶东，鱼戏莲叶西，鱼戏莲叶南，鱼戏莲叶北。"
                    OP.find_id('com.happyteam.dubbingshow:id/notice_content').clear()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/notice_content').send_keys(content)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btn_sure').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/pack_up').click()
                    time.sleep(2)
                    # print ('添加音乐')
                    # OP.find_id('com.happyteam.dubbingshow:id/function_joke_articles').click()
                    # time.sleep(2)
                    # try:
                    #     OP.find_id('com.happyteam.dubbingshow:id/add_music').click()
                    #     time.sleep(5)
                    #     print('网络导入')
                    #     OP.find_id('com.happyteam.dubbingshow:id/internet').click()
                    #     time.sleep(2)
                    #     '''获取列表音乐名'''
                    #     OP.find_id('com.happyteam.dubbingshow:id/title').click()
                    #     time.sleep(5)
                    #     Musics = OP.find_ids('com.happyteam.dubbingshow:id/music_name')
                    #     Music_list = []
                    #     for i in range(len(Musics)):
                    #         Name = OP.find_ids('com.happyteam.dubbingshow:id/music_name')[i].text
                    #         Music_list.append(Name)
                    #         time.sleep(1)
                    #     print(Music_list)
                    #     time.sleep(2)
                    #     print('下载音乐')
                    #     Loads = OP.find_ids('com.happyteam.dubbingshow:id/load')
                    #     for i in range(len(Loads)):
                    #         OP.find_ids('com.happyteam.dubbingshow:id/load')[i].click()
                    #         time.sleep(1)
                    #     time.sleep(4)
                    #     print('返回类型列表')
                    #     OP.find_id('com.happyteam.dubbingshow:id/back').click()
                    #     time.sleep(4)
                    #     print('返回已下载音乐列表')
                    #     OP.find_id('com.happyteam.dubbingshow:id/back').click()
                    #     time.sleep(4)
                    #     OP.find_ids('com.happyteam.dubbingshow:id/add_music')[1].click()
                    #     time.sleep(4)
                    #     print('返回语聊房间')
                    #     OP.find_id('com.happyteam.dubbingshow:id/back').click()
                    #     time.sleep(2)
                    #     try:
                    #         OP.find_id('com.happyteam.dubbingshow:id/play')
                    #         OP.find_id('com.happyteam.dubbingshow:id/play').click()
                    #         time.sleep(2)
                    #         OP.back()
                    #     except:
                    #         OP.back()
                    #     time.sleep(2)
                    # except:
                    #     '''点击编辑按钮'''
                    #     OP.find_id('com.happyteam.dubbingshow:id/modify').click()
                    #     time.sleep(2)
                    #     OP.find_id('com.happyteam.dubbingshow:id/delete')
                    #     OP.find_id('com.happyteam.dubbingshow:id/delete').click()
                    #     time.sleep(2)
                    #     '''收起音乐列表'''
                    #     OP.back()
                    time.sleep(2)
                    print ('发红包')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.102*x,y=0.807*y).release().perform()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/cash_num').send_keys('0.1')
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/people_num').send_keys('1')
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(5)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet')
                        print ('红包发送失败')
                        OP.back()
                    except:
                        try:
                            OP.find_id('com.happyteam.dubbingshow:id/red_packet_btn')
                            OP.find_id('com.happyteam.dubbingshow:id/red_packet_btn').click()
                            time.sleep(2)
                            OP.find_id('com.happyteam.dubbingshow:id/open_red_packet_btn').click()
                            try:
                                OP.wait_id('com.happyteam.dubbingshow:id/user_head')
                                time.sleep(2)
                                OP.back()
                            except:
                                print('红包领取失败')
                        except:
                            pass
                    time.sleep(2)
                    print ('随机惩罚')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.102 * x, y=0.932 * y).release().perform()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    print ('黑名单')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.695 * x, y=0.807 * y).release().perform()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btn_close').click()
                    time.sleep(2)
                    print ('设置房管')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.898 * x, y=0.807 * y).release().perform()
                    time.sleep(2)
                    OP.wait_xpath('添加房管').click()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    print ('扩充麦位')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.269 * x, y=0.932 * y).release().perform()
                    time.sleep(2)
                    Content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                    print (Content)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                    print ('Pia戏')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.5 * x, y=0.932 * y).release().perform()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/game_icon')
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/game_icon').click()
                        OP.wait_id('com.happyteam.dubbingshow:id/title')
                        time.sleep(2)
                        titles = OP.find_ids('com.happyteam.dubbingshow:id/title')
                        title_list = []
                        for title in range(len(titles)):
                            title_name = OP.find_ids('com.happyteam.dubbingshow:id/title')[title].text
                            title_list.append(title_name)
                            time.sleep(1)
                        print(title_list)
                        time.sleep(2)
                        print('搜索剧本')
                        OP.find_id('com.happyteam.dubbingshow:id/search').click()
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/search').send_keys('配音')
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/title').click()
                        time.sleep(2)
                        print('设置剧本')
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/set_srt').click()
                        try:
                            toast = OP.wait_toast('//android.widget.Toast')
                            print(toast)
                        except(NoSuchElementException,TimeoutException):
                            pass
                        time.sleep(1)
                        OP.back()
                    except(NoSuchElementException,TimeoutException):
                        print ('Pia戏开启失败')
                    time.sleep(2)
                    print ('组CP')
                    OP.find_id('com.happyteam.dubbingshow:id/function_more').click()
                    time.sleep(2)
                    TouchAction(devc).press(x = 0.694 * x, y = 0.932 * y).release().perform()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    print('发送评论')
                    OP.find_id('com.happyteam.dubbingshow:id/function_comment_layout').click()
                    time.sleep(2)
                    for i in range(3):
                        OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys('哈哈哈哈')
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
                        time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    print('送礼')
                    OP.find_id('com.happyteam.dubbingshow:id/function_send_gift').click()
                    time.sleep(2)
                    Names = OP.find_ids('com.happyteam.dubbingshow:id/gift_name')
                    gift_list = []
                    for i in range(len(Names)):
                        name = OP.find_ids('com.happyteam.dubbingshow:id/gift_name')[i].text
                        value = OP.find_ids('com.happyteam.dubbingshow:id/gift_value')[i].text
                        gift_list.append(name)
                        gift_list.append(value)
                        time.sleep(1)
                    print(gift_list)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                    try:
                        Toast = OP.wait_toast('//android.widget.Toast')
                        print(Toast)
                    except(TimeoutException,NoSuchElementException):
                        OP.back()
                    time.sleep(2)
                    OP.find_ids('com.happyteam.dubbingshow:id/rl_all')[-1].click()
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                    try:
                        Toast = OP.wait_toast('//android.widget.Toast')
                        print(Toast)
                    except(TimeoutException, NoSuchElementException):
                        OP.back()
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/rl_all')
                        '''收起礼物列表弹窗'''
                        OP.back()
                    except:
                        pass
                    time.sleep(2)
                    print('点心')
                    #出现动效会影响控件点击效率，因此获取点心控件后使用坐标点击提高效率
                    local = OP.find_id('com.happyteam.dubbingshow:id/periscope_view').location
                    loc_x = int (local['x'])
                    loc_y = int (local['y'])+100
                    for i in range(100):
                        TouchAction(devc).press(x=loc_x,y=loc_y).release().perform()
                    time.sleep(2)
                    print('查看话题排行榜')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/linear_rank')
                        OP.find_id('com.happyteam.dubbingshow:id/linear_rank').click()
                        time.sleep(2)
                        counts = OP.find_ids('com.happyteam.dubbingshow:id/gift_value_count')
                        Ranking_List = []
                        for list in range(len(counts)):
                            number = OP.find_ids('com.happyteam.dubbingshow:id/user_name')[list].text
                            count = OP.find_ids('com.happyteam.dubbingshow:id/gift_value_count')[list].text
                            Ranking_List.append(number)
                            Ranking_List.append(count)
                            time.sleep(1)
                        print(Ranking_List)
                        time.sleep(2)
                        OP.back()
                    except:
                        print('该直播未选择话题')
                    time.sleep(2)
                    print('语聊背景图')
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/user_list').click()
                    time.sleep(2)
                    try:
                        OP.wait_xpath('更换背景')
                        OP.find_xpath('更换背景').click()
                        try:
                            OP.wait_xpath('更换房间背景')
                            time.sleep(2)
                            OP.back()
                        except:
                            OP.back()
                        time.sleep(2)
                        OP.back()
                    except:
                        print('网页加载失败')
                        OP.back()
                    time.sleep(2)
                    print('房间用户进场列表')
                    OP.find_id('com.happyteam.dubbingshow:id/count').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/userHeadView')
                        online = OP.find_id('com.happyteam.dubbingshow:id/line_count').text
                        print(online)
                        time.sleep(1)
                        history = OP.find_id('com.happyteam.dubbingshow:id/uv_count').text
                        print(history)
                        time.sleep(1)
                        users = OP.find_ids('com.happyteam.dubbingshow:id/username')
                        user_list = []
                        for user in range(len(users)):
                            name = OP.find_ids('com.happyteam.dubbingshow:id/username')[user].text
                            user_list.append(name)
                            time.sleep(0.5)
                        print(user_list)
                        time.sleep(2)
                        OP.back()
                    except:
                        print('进场列表加载失败')
                    time.sleep(2)
                    print('任务列表')
                    OP.find_id('com.happyteam.dubbingshow:id/task_button').click()
                    time.sleep(2)
                    tasks = OP.find_ids('com.happyteam.dubbingshow:id/tv_reward')
                    task_list = []
                    for i in range(len(tasks)):
                        task_name = OP.find_ids('com.happyteam.dubbingshow:id/desc')[i].text
                        reward = OP.find_ids('com.happyteam.dubbingshow:id/tv_reward')[i].text
                        task_list.append(task_name)
                        task_list.append(reward)
                        time.sleep(0.5)
                    pprint(task_list)
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/task_box')
                        OP.find_id('com.happyteam.dubbingshow:id/task_box').click()
                        try:
                            toast = OP.wait_toast('//android.widget.Toast')
                            print(toast)
                        except:
                            pass
                    except:
                        print('任务未完成')
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/tv_desc_reward')
                        OP.find_id('com.happyteam.dubbingshow:id/tv_desc_reward').click()
                        time.sleep(2)
                        OP.back()
                    except:
                        pass
                    time.sleep(2)
                    print('收起任务列表')
                    OP.back()
                    time.sleep(2)
                    print('关闭语聊')
                    OP.find_id('com.happyteam.dubbingshow:id/home_close').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/check_box').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/outLive').click()
                    time.sleep(2)
                except(NoSuchElementException,TimeoutException):
                    print ('语聊房间创建失败')
            except(NoSuchElementException,TimeoutException):
                print ('语聊创建界面加载失败')
                time.sleep(2)
                OP.back()
        time.sleep(2)



    '''语聊房间最新列表'''
    def chat_New(self):
        OP.find_id('com.happyteam.dubbingshow:id/tab2').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_title')
            chats = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')
            chat_list = []
            for i in range(len(chats)):
                chat_name = OP.find_ids('com.happyteam.dubbingshow:id/item_title')[i].text
                user_count  = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')[i].text
                chat_list.append(chat_name)
                chat_list.append(user_count)
                time.sleep(0.5)
            print(chat_list)
            time.sleep(2)
            for i in range(3):
                OP.swip_up()
                time.sleep(4)
                OP.find_id('com.happyteam.dubbingshow:id/item_title').click()
                time.sleep(2)
                try:
                    OP.find_xpath('该房间的语聊已结束')
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/home_close').click()
                    print('语聊房间已关闭')
                except(NoSuchElementException,TimeoutException):
                    OP.wait_id('com.happyteam.dubbingshow:id/home_microphone')
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
        except:
            print('语聊最新列表未显示房间信息')

    '''语聊房间关注列表'''
    def chat_follow(self):
        OP.find_id('com.happyteam.dubbingshow:id/tab3').click()
        time.sleep(2)
        try:
            OP.find_xpath('您关注的秀友都还没有创建房间哦')
            print('暂无关注用户创建语聊')
            time.sleep(2)
            print('推荐房间')
            chats = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')
            chat_list = []
            for i in range(len(chats)):
                chat_name = OP.find_ids('com.happyteam.dubbingshow:id/item_title')[i].text
                user_count = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')[i].text
                chat_list.append(chat_name)
                chat_list.append(user_count)
                time.sleep(0.5)
            print(chat_list)
        except:
            print('显示有关注用户语聊间')
            time.sleep(1)
            chats = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')
            chat_list = []
            for i in range(len(chats)):
                chat_name = OP.find_ids('com.happyteam.dubbingshow:id/item_title')[i].text
                user_count = OP.find_ids('com.happyteam.dubbingshow:id/item_user_number')[i].text
                chat_list.append(chat_name)
                chat_list.append(user_count)
                time.sleep(0.5)
            print(chat_list)
            time.sleep(2)



if __name__=="__main__":
    Enter_list()


