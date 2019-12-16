#coding = utf-8
#防止中文显示乱码
#coding = gb18030
'''
author:Alvins.zhu
time:2019年6月3日

New:
time:2019年12月5日15:12:02
function:暂无
'''


import random
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()
'''首页关注'''
class Home_Follow():
    def start_app(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/task_box')
            print('===开始===')
        except:
            print('应用启动失败')
    '''点击进入首页关注列表'''
    def Follows(self):
        print("点击进入关注")
        OP.find_id("com.happyteam.dubbingshow:id/circlesTab").click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            print('显示用户头像')
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                time.sleep(4)
            except:
                OP.swip_up()
        time.sleep(2)

    '''直播消息'''
    def Live_news(self):
        print("点击语聊消息通知按钮")
        OP.find_id('com.happyteam.dubbingshow:id/musicPlayView').click()
        time.sleep(10)
        OP.back()
        time.sleep(2)

    '''关注列表'''
    def Follow_list(self):
        print("点击头像进入空间")
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            time.sleep(2)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            print("空间加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(2)
        print('推荐关注')
        for i in range(5):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iwant')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/content').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(2)
                    OP.back()
                except:
                    pass
                time.sleep(2)
                list = []
                contents = OP.find_ids('com.happyteam.dubbingshow:id/content')
                for i in range(len(contents)):
                    content = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                    user = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                    list.append(user)
                    list.append(content)
                    time.sleep(1)
                print(list)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/follow').click()
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except:
                    pass
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/iwant').click()
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit')
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                except:
                    OP.wait_id('com.happyteam.dubbingshow:id/now_money_month')
                    print('未购买会员')
                    time.sleep(1)
                    OP.back()
                time.sleep(2)
                break
            except:
                devc.swipe(0.5 * x, 0.85 * y, 0.5 * x, 0.4 * y, 700)
            time.sleep(2)

        time.sleep(2)
        print('素材')
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/top_left_tag')
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/imgGirl')
                    print('双人素材')
                    OP.find_id('com.happyteam.dubbingshow:id/action').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/roleall')
                        OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
                        time.sleep(1)
                        OP.back()
                        time.sleep(1)
                        print("退出配音界面")
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutException):
                        pass
                except:
                    print('单人素材')
                    OP.find_id('com.happyteam.dubbingshow:id/action').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/action')
                        time.sleep(2)
                        OP.back()
                        time.sleep(1)
                        print("退出配音界面")
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutException):
                        pass
                break
            except(NoSuchElementException,TimeoutException):
                OP.swip_up()
                time.sleep(4)

        time.sleep(2)

        print('帖子')
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/good')
                Circle_tag = OP.find_id('com.happyteam.dubbingshow:id/good').text
                print(Circle_tag)
                print("点击进入帖子详情")
                OP.find_id('com.happyteam.dubbingshow:id/content').click()
                OP.wait_xpath('帖子详情')
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                        print("帖子详情重载失败")
                        time.sleep(1)
                        OP.back()
                    except:
                        pass
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/tag').click()
                    print("点击进入话题详情")
                    OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
                    OP.back()
                    time.sleep(2)
                    OP.back()
                except(TimeoutException,NoSuchElementException):
                    print("话题详情加载失败")
                    time.sleep(1)
                    OP.back()
                    time.sleep(2)
                    OP.back()
                break
            except(NoSuchElementException,TimeoutException):
                OP.swip_up()
                time.sleep(4)

        print('视频')
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/play')
                OP.find_id('com.happyteam.dubbingshow:id/play').click()
                print("点击播放视频")
                time.sleep(5)
                device().keyevent(3)
                time.sleep(2)
                device().launch_app()
                time.sleep(2)
                break
            except:
                OP.swip_up()
                time.sleep(4)

        '''分享'''
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num')
                break
            except:
                pass
            OP.swip_up()
            time.sleep(4)
        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        print("点击朋友圈")
        time.sleep(2)
        TouchAction(device()).press(x=0.12 * x, y=0.68 * y).release().perform()
        time.sleep(4)
        try:
            OP.wait_xpath('帐号')
            print("微信未登录")
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.wait_xpath('发表')
                print("微信跳转成功，点击发布后返回视频详情")
                time.sleep(2)
                el = OP.wait_xpath('发表')
                el.click()
                time.sleep(2)
            except:
                print("微信跳转失败")
                OP.back()

        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        time.sleep(2)
        print("点击QQ空间")
        TouchAction(device()).press(x=0.49 * x, y=0.68 * y).release().perform()
        time.sleep(5)
        try:
            OP.wait_xpath('发表')
            print("QQ空间加载成功，点击发布后返回视频详情")
            time.sleep(2)
            OP.wait_xpath('发表').click()
            time.sleep(2)
        except:
            print("QQ空间跳转失败")
            time.sleep(1)
            OP.back()
        time.sleep(2)

        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        time.sleep(2)
        print("点击新浪")
        TouchAction(device()).press(x=0.68 * x, y=0.68 * y).release().perform()
        time.sleep(2)
        try:
            OP.find_id('确定')
            time.sleep(2)
            OP.find_id('确定').click()
        except:
            try:
                OP.find_id('允许')
                time.sleep(2)
                OP.find_id('允许').click()
            except:
                pass
        time.sleep(4)
        try:
            OP.find_id('允许')
            OP.find_id('允许').click()
            time.sleep(2)
        except:
            pass
        OP.back()
        time.sleep(1)
        try:
            OP.find_xpath('不保存')
            OP.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        print("点击私信")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        time.sleep(2)
        TouchAction(device()).press(x=0.12 * x, y=0.83 * y).release().perform()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filter_edit')
            print("进入私信列表界面")
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("15697802")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                print("搜索成功")
                name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                print(name)
                name2 = "米爱"
                if name == name2:
                    print("点击进入私信聊天界面")
                    OP.find_id('com.happyteam.dubbingshow:id/name').click()
                    time.sleep(5)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/btnRight')
                        print("进入私信聊天界面,返回视频详情")
                        time.sleep(2)
                        OP.back()
                    except:
                        OP.back()
                else:
                    print("未搜索到指定用户")
                    time.sleep(2)
                    OP.back()
            except(TimeoutException, NoSuchElementException):
                print("搜索失败，返回视频详情")
                OP.back()
        except(TimeoutException, NoSuchElementException):
            print("私信列表跳转失败，请检查！")
            OP.back()
        time.sleep(2)

        print("点击复制链接")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        time.sleep(2)
        TouchAction(device()).press(x=0.31 * x, y=0.83 * y).release().perform()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/txtContent')
                print('此为下载视频按钮，不是复制链接按钮')
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                pass
        time.sleep(2)

        print("点击转发")
        OP.find_id('com.happyteam.dubbingshow:id/item_attention_share_num').click()
        time.sleep(2)
        TouchAction(device()).press(x=0.88 * x, y=0.83 * y).release().perform()
        try:
            OP.find_id('com.happyteam.dubbingshow:id/reprint')
            OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("不错，转发了！")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/reprint').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/circlesTab')
            except(TimeoutException, NoSuchElementException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/reprint')
                    print("转发失败，再次尝试")
                    OP.find_id('com.happyteam.dubbingshow:id/reprint').click()
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/reprint')
                        print("再次转发失败，请检查网络！！！")
                        OP.back()
                    except:
                        pass
                except(TimeoutException, NoSuchElementException):
                    print("转发成功！")
        except(NoSuchElementException, TimeoutException):
            print('未显示转发弹窗')
            OP.back()

        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/fl_gift').click()
            print("点击送礼按钮")
            OP.wait_id('com.happyteam.dubbingshow:id/confirm')
            try:
                OP.find_id('com.happyteam.dubbing:id/confirm').click()
                toast = OP.wait_xpath('//android.widget.Toast')
                print(toast)
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
            OP.back()
            time.sleep(2)

            print("点击发送评论")
            OP.find_id('com.happyteam.dubbingshow:id/fl_comment').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/editContent').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("赞一个！")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
            try:
                Comment_toast= OP.wait_toast('//android.widget.Toast')
                print(Comment_toast)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btn_send')
                    print("评论发送失败")
                except:
                    pass
            except:
                pass
            print("上滑列表")
            num = random.randint(3, 10)
            for i in range(num):
                OP.swip_up()
                time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            pass

if __name__=="__main__":
    F = Home_Follow()
    F.start_app()
    F.Follows()
    F.Live_news()
    F.Follow_list()