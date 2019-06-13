#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import random
import os,threading
# from appium import webdriver
import time
# from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
# #获取当前项目的根路径
# PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from Operate import BaseOperate
from devices import device
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()
'''首页热门列表'''
class Home_Hot():
    def Home_load(self):
        try:
            OP.find_id('com.happyteam.dubbingshow:id/film_img2')
            print("首页作品列表加载成功")
        except:
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnRetry').click()
                print("网络异常，首页加载失败")
                OP.wait_id('com.happyteam.dubbingshow:id/film_img2')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/film_img2')
                    print("首页作品列表加载成功")
                except:
                    print("首页作品列表加载失败")
            except(TimeoutException, NoSuchElementException):
                print("首页加载失败")

    '''首页作品列表'''
    def Home_List(self):
        print("获取当前页面作品名称")
        titles = OP.find_ids('com.happyteam.dubbingshow:id/title2')
        for name in range(len(titles)):
            title_name = OP.find_ids('com.happyteam.dubbingshow:id/title2')[name].text
            print(title_name)
            time.sleep(2)
        time.sleep(2)
        print("上滑列表")
        for i in range(10):
            OP.swip_up()
            time.sleep(2)
        time.sleep(2)
        print("返回列表顶部")
        OP.find_id('com.happyteam.dubbingshow:id/dubbingTab').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/img')
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)

    '''点击进入视频详情'''
    def Open_Video(self):
        print("点击进入作品详情")
        for  i in range(10):
            OP.find_id('com.happyteam.dubbingshow:id/film_img2').click()
            time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                print("退到后台再启动，停止视频播放")
                devc.keyevent(3)
                time.sleep(3)
                devc.launch_app()
                time.sleep(10)
                try:
                    OP.wait_xpath('原声素材')
                    break
                except(NoSuchElementException,TimeoutException):
                    OP.back()
                    time.sleep(2)
                    print("下拉刷新")
                    OP.swip_down()
                    time.sleep(3)
                    OP.find_id('com.happyteam.dubbingshow:id/film_img2').click()
                    time.sleep(2)
            except(NoSuchElementException ,TimeoutException):
                print("视频详情加载失败")
            time.sleep(2)
        time.sleep(4)
        '''点击作者头像进入个人空间'''
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/darenunion_img')
                print("达人用户")
            except:
                pass
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/photo_frame')
                print ('会员用户')
            except:
                print ('普通用户')
            time.sleep(2)
            OP.back()
            time.sleep(2)
            OP.back()
        except(NoSuchElementException, TimeoutException):
            OP.back()
        time.sleep(2)
        follow = OP.find_id('com.happyteam.dubbingshow:id/follow_ta').text
        follow_status = "关注"
        if follow == follow_status:
            print("点击关注")
            OP.find_id('com.happyteam.dubbingshow:id/follow_ta').click()
            time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/dialog_view')
            except(TimeoutException, NoSuchElementException):
                pass
        else:
            print("已关注该用户")
        time.sleep(2)

    '''视频播放'''
    def Play_video(self):
        try:
            OP.find_id('com.happyteam.dubbingshow:id/iv_fullscreen_open')
            print("点击全屏播放")
            OP.find_id('com.happyteam.dubbingshow:id/iv_fullscreen_open').click()
            time.sleep(2)
            print("拖动视频进度条")
            # 横屏下x，y值与竖屏x，y值相反
            devc.swipe(0.13 * y, 0.95 * x, 0.76 * y, 0.95 * x, 2000)
            time.sleep(2)
            print("点击播放")
            OP.find_id('com.happyteam.dubbingshow:id/play').click()
            time.sleep(2)
            print("收起全屏")
            OP.back()
            time.sleep(2)
            print("退到后台3秒在启动")
            devc.keyevent(3)
            time.sleep(2)
            devc.launch_app()
            time.sleep(2)
            print("点击弹幕开关")
            OP.find_id('com.happyteam.dubbingshow:id/media_danmu_view').click()
            time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            pass
        time.sleep(2)
        print("再次点击视频播放至结束")
        try:
            OP.find_id('com.happyteam.dubbingshow:id/play')
            OP.find_id('com.happyteam.dubbingshow:id/play').click()
            OP.wait_download('com.happyteam.dubbingshow:id/linear_gift')
        except:
            pass
        print("点击视频封面中的送礼按钮")
        OP.find_id('com.happyteam.dubbingshow:id/linear_gift').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_container')
            print("赠送鲜花")
            OP.find_ids('com.happyteam.dubbingshow:id/item_container')[0].click()
            time.sleep(2)
            print('修改赠送数量')
            OP.find_class('android.widget.EditText').clear()
            time.sleep(2)
            OP.find_class('android.widget.EditText').send_keys('2')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
                time.sleep(2)
                print('去充值')
                OP.find_id('com.happyteam.dubbingshow:id/goDeposit').click()
                try:
                    OP.wait_xpath('充值')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException, TimeoutException):
                    OP.back()
            except(NoSuchElementException, TimeoutException):
                print("收起礼物列表！")
                OP.back()
        except(NoSuchElementException, TimeoutException):
            print("礼物列表加载失败")
            try:
                OP.find_id('com.happyteam.dubbingshow:id/viewpager')
                OP.back()
            except:
                pass

    '''评论'''
    def Comment(self):
        print("获取评论总数")
        try:
            OP.find_id('com.happyteam.dubbingshow:id/comment_count')
            comment_counts = OP.find_id('com.happyteam.dubbingshow:id/comment_count').text
            print("评论总数：", comment_counts)
        except:
            print("未显示有评论数量icon")
        time.sleep(2)
        print("点击评论按钮")
        OP.find_id('com.happyteam.dubbingshow:id/comment').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_comment_video_more')
            print("点击排序按钮")
            OP.find_id('com.happyteam.dubbingshow:id/shunxu').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/shunxu').click()
            time.sleep(2)
            '''点击评论区用户头像进入空间'''
            Name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[-1].text
            print ('评论列表用户名：',Name)
            time.sleep(1)
            OP.find_ids('com.happyteam.dubbingshow:id/userhead')[-1].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                print("个人空间加载成功，返回视频详情界面")
                time.sleep(2)
                Zoom_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                print ('空间用户名：',Zoom_name)
                time.sleep(2)
                OP.back()
            except(TimeoutException, NoSuchElementException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("点击评论设置按钮")
            OP.find_id('com.happyteam.dubbingshow:id/item_comment_video_more').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/tv_action_one').click()
            print("点击政治、色情举报按钮")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(8)
            print("其它原因举报")
            OP.find_id('com.happyteam.dubbingshow:id/item_comment_video_more').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/tv_action_other').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys("测试")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(10)
            print("发送评论")
            OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("赞一个!")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/btn_send')
                print ('评论发送失败')
            except(NoSuchElementException,TimeoutException):
                print ('评论发送成功')
            time.sleep(4)
            print("发送表情")
            OP.find_id('com.happyteam.dubbingshow:id/btn_send_smile').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/iv_face_item').click()
            time.sleep(15)
            try:
                OP.wait_not_id('com.happyteam.dubbingshow:id/iv_face_item')
                print ('表情发送成功')
            except(NoSuchElementException, TimeoutException):
                print ('表情发送失败')
            time.sleep(4)
            '''删除评论'''
            OP.find_id('com.happyteam.dubbingshow:id/item_comment_video_more').click()
            time.sleep(1)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/tv_action_one')
                time.sleep(1)
                OP.back()
                print ('非本用户发送评论')
                time.sleep(2)
                OP.back()
            except:
                TouchAction(devc).press(x=0.5 * x, y=0.87 * y).release().perform()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(4)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btn_send_smile')
                time.sleep(1)
                OP.back()
            except:
                pass
        except:
            print("此作品暂无评论")
        time.sleep(2)
        print("退出视频详情")
        OP.back()
        time.sleep(2)

    '''作品分享'''
    def share(self):
        print("点击我的")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/mineTab').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
        except(NoSuchElementException ,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fancount')
                    print("个人空间加载成功")
                except(NoSuchElementException ,TimeoutException):
                    print("个人空间加载失败，退出")
                    driver.close_app()
            except:
                pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/filmBg1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
        except(TimeoutException ,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/filmBg1').click()
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
            except(NoSuchElementException ,TimeoutException):
                print("作品详情加载失败，退出测试")
                time.sleep(1)
                driver.close_app()
        time.sleep(2)
        print("点击分享按钮")
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        print("点击朋友圈")
        TouchAction(devc).press(x=0.14 * x, y=0.71 * y).release().perform()
        time.sleep(10)
        try:
            OP.find_xpath('帐号')
            print("微信未登录")
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.find_xpath('发表')
                print("微信跳转成功，点击发布后返回视频详情")
                time.sleep(4)
                OP.find_xpath('发表').click()
                time.sleep(4)
            except:
                print("微信跳转失败")
                time.sleep(1)
                OP.back()
        time.sleep(4)
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        print("点击QQ空间")
        TouchAction(devc).press(x=0.51 * x, y=0.71 * y).release().perform()
        time.sleep(10)
        try:
            OP.find_xpath('发表')
            print("QQ空间加载成功，点击发布后返回视频详情")
            time.sleep(2)
            OP.find_xpath('发表').click()
            time.sleep(2)
        except:
            print("QQ空间跳转失败")
            time.sleep(1)
            OP.back()
        time.sleep(4)

        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        print("点击新浪")
        TouchAction(devc).press(x=0.70 * x, y=0.71 * y).release().perform()
        time.sleep(2)
        '''判断是否显示权限弹窗'''
        try:
            OP.find_xpath('确定').click()
        except:
            try:
                OP.find_xpath('允许').click()
            except:
                try:
                    OP.find_xpath('始终允许').click()
                except:
                    pass
        time.sleep(4)
        OP.back()
        time.sleep(2)
        try:
            OP.find_xpath('不保存')
            OP.find_xpath('不保存').click()
        except:
            pass
        time.sleep(4)

        print("点击私信")
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.14 * x, y=0.83 * y).release().perform()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filter_edit')
            print("进入私信列表界面")
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("16685645")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                OP.find_id('com.happyteam.dubbingshow:id/userhead')
                print("搜索成功")
                name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                print(name)
                name2 = "撸串"
                if name == name2:
                    print("点击进入私信聊天界面")
                    OP.find_id('com.happyteam.dubbingshow:id/name').click()
                    time.sleep(5)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/right_icon1')
                        print("进入私信聊天界面,返回视频详情")
                        time.sleep(2)
                        OP.back()
                    except:
                        OP.back()
                else:
                    print("未搜索到指定用户")
                    time.sleep(2)
                    OP.back()
            except(TimeoutException,NoSuchElementException):
                print("搜索失败，返回视频详情")
                OP.back()
        except(TimeoutException ,NoSuchElementException):
            print("私信列表跳转失败，请检查！")
        time.sleep(4)

        print("点击下载视频")
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.32 * x, y=0.83 * y).release().perform()
        time.sleep(4)
        print('直接下载')
        OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/btnSubmit')
            content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
            print(content)
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except(TimeoutException ,NoSuchElementException):
            print("视频下载失败，请检查！")
            OP.back()
        time.sleep(2)
        print('去水印下载')
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.32 * x, y=0.83 * y).release().perform()
        time.sleep(4)
        OP.find_xpath('去水印').click()
        time.sleep(4)
        try:
            OP.find_xpath('会员中心')
            OP.back()
        except:
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/btnSubmit')
                content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                print(content)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(TimeoutException, NoSuchElementException):
                print("视频下载失败，请检查！")
                OP.back()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        print("点击复制链接")
        TouchAction(devc).press(x=0.51* x, y=0.83* y).release().perform()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except(TimeoutException ,NoSuchElementException):
            pass
        time.sleep(2)


        print("返回首页")
        OP.back()
        time.sleep(2)
        OP.back()
        time.sleep(4)
        print("点击首页按钮")
        OP.find_id('com.happyteam.dubbingshow:id/dubbingTab').click()
        time.sleep(1)
        print("点击进入视频详情")
        OP.find_id('com.happyteam.dubbingshow:id/film_img2').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            print("视频详情界面加载成功")
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/share').click()
            time.sleep(2)
            print("点击转发")
            TouchAction(devc).press(x=0.88 * x, y=0.83 * y).release().perform()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/reprint')
                print("转发作品")
                OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("不错，转发了！")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/reprint').click()
                time.sleep(2)
                try:
                    OP.wait_toast('//android.widget.Toast')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/reprint')
                        print("转发失败，请检查网络！！！")
                        OP.back()
                    except:
                        print("转发成功！")
                except(NoSuchElementException ,TimeoutException):
                    print("转发成功")
                time.sleep(2)
            except:
                print("未显示转发弹窗")
            time.sleep(1)
            print("点击曝光")
            OP.find_id('com.happyteam.dubbingshow:id/exposure').click()
            time.sleep(2)
            content1 = OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').text
            check = '每日免费10次'
            if content1 == check:
                print(content1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(4)
                OP.back()
                time.sleep(2)
            else:
                print(content1)
                print("点击确认曝光")
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit')
                OP.back()
            except:
                pass
            time.sleep(2)
            print('金币曝光')
            OP.swip_up()
            time.sleep(4)
            OP.find_id('com.happyteam.dubbingshow:id/gift').click()
            time.sleep(2)
            old_gold_count = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
            print("曝光前金币额度:", old_gold_count)
            OP.back()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/exposure').click()
            time.sleep(2)
            print("点击确认曝光")
            OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnCancel')
                    print("曝光失败")
                    OP.back()
                except:
                    pass
            except:
                pass
            print("查看金币额度")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/gift').click()
            time.sleep(2)
            new_gold_count = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
            print("曝光后金币额度:", new_gold_count)
            time.sleep(2)
            if old_gold_count == new_gold_count:
                print("金币额度未变化，请检查")
            else:
                print("曝光成功")
            OP.back()
        except:
            print("视频详情加载失败")
        time.sleep(2)


    '''礼物榜'''
    def Gift_List(self):
        try:
            OP.find_id('com.happyteam.dubbingshow:id/gift_headcontainer')
            print("存在送礼用户")
            time.sleep(1)
            print("点击更多进入礼物榜")
            OP.find_id('com.happyteam.dubbingshow:id/gift_more').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/send_gift')
                '''获取当前页面所有用户名名称'''
                User_Name_list = OP.find_ids('com.happyteam.dubbingshow:id/userhead')
                time.sleep(2)
                for i in range(len(User_Name_list)):
                    '''点击头像进入空间'''
                    OP.find_ids('com.happyteam.dubbingshow:id/userhead')[i].click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                        time.sleep(2)
                        Name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                        print(Name)
                        time.sleep(2)
                        OP.back()
                    except(NoSuchElementException, TimeoutException):
                        print('空间加载失败')
                        time.sleep(2)
                        OP.back()
                    time.sleep(2)
                time.sleep(2)

                Gift_list =OP.find_ids('com.happyteam.dubbingshow:id/gift_img')
                '''点击礼物进入礼物详情'''
                for i in range(len(Gift_list)):
                    OP.find_ids('com.happyteam.dubbingshow:id/gift_img')[i].click()
                    time.sleep(2)
                    Name = OP.find_id('com.happyteam.dubbingshow:id/txtTitle').text
                    Gift_Name = []
                    Gift_names = OP.find_ids('com.happyteam.dubbingshow:id/text1')
                    for x in range(len(Gift_names)):
                        Gift_name = OP.find_ids('com.happyteam.dubbingshow:id/text1')[x].text
                        Gift_count = OP.find_ids('com.happyteam.dubbingshow:id/text2')[x].text
                        Gift_Name.append(Name)
                        Gift_Name.append(Gift_name)
                        Gift_Name.append(Gift_count)
                        time.sleep(1)
                    print(Gift_Name)
                    time.sleep(1)
                    OP.back()
                    time.sleep(1)

                time.sleep(2)
                print("点击送礼按钮")
                OP.find_id('com.happyteam.dubbingshow:id/send_gift').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/item_container')
                    print("显示送礼列表，获取赠送之前的金币额度后赠送鲜花")
                    gold_count1 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                    print(gold_count1)
                    OP.find_ids('com.happyteam.dubbingshow:id/item_container')[0].click()
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                    try:
                        toast = OP.wait_toast('//android.widget.Toast')
                        print(toast)
                        print("获取送礼之后金币额度")
                        OP.find_id('com.happyteam.dubbingshow:id/send_gift').click()
                        time.sleep(3)
                        gold_count2 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                        print(gold_count2)
                        if gold_count1 > gold_count2:
                            print("送礼成功")
                        else:
                            print("金币额度未变化，请检查！")
                        time.sleep(1)
                        print("收起礼物列表")
                        OP.back()
                    except(TimeoutException ,NoSuchElementException):
                        print("获取送礼之后金币额度")
                        OP.find_id('com.happyteam.dubbingshow:id/send_gift').click()
                        time.sleep(3)
                        gold_count3 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                        print(gold_count3)
                        if gold_count1 > gold_count3:
                            print("送礼成功")
                        else:
                            print("金币额度未变化，请检查")
                        time.sleep(1)
                        print("收起礼物列表")
                        OP.back()
                except(TimeoutException ,NoSuchElementException):
                    print("礼物列表加载失败")
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/viewpager')
                        OP.back()
                    except:
                        pass
                print("返回视频详情")
                OP.back()
            except(TimeoutException ,NoSuchElementException):
                print("礼物榜列表详情加载失败，返回视频详情")
                OP.back()
        except:
            print("暂无用户送礼，进行赠送礼物操作")
            OP.find_id('com.happyteam.dubbingshow:id/gift').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/item_container')
                print("显示送礼列表，获取赠送之前的金币额度后赠送鲜花")
                gold_count1 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                print(gold_count1)
                OP.find_ids('com.happyteam.dubbingshow:id/item_container')[0].click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                time.sleep(2)
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/dialog_view')
                    print("获取送礼之后金币额度")
                    OP.find_id('com.happyteam.dubbingshow:id/send_gift').click()
                    time.sleep(3)
                    gold_count2 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                    print(gold_count2)
                    if gold_count1 > gold_count2:
                        print("送礼成功")
                    else:
                        print("金币额度未变化，请检查！")
                    time.sleep(1)
                    print("收起礼物列表")
                    OP.back()
                except(TimeoutException ,NoSuchElementException):
                    print("获取送礼之后金币额度")
                    OP.find_id('com.happyteam.dubbingshow:id/send_gift').click()
                    time.sleep(3)
                    gold_count3 = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
                    print(gold_count3)
                    if gold_count1 > gold_count3:
                        print("送礼成功")
                    else:
                        print("金币额度未变化，请检查")
                    time.sleep(1)
                    print("收起礼物列表")
                    OP.back()
            except(TimeoutException ,NoSuchElementException):
                print("礼物列表加载失败")
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/viewpager')
                    OP.back()
                except:
                    pass

    '''配音表'''
    def Dubbing(self):
        print("配音表中点击用户头像")
        user_heads = OP.find_ids('com.happyteam.dubbingshow:id/textView')
        for i in range(len(user_heads)):
            try:
                i += 1
                name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                print(name)
                Touch = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].location
                Loc_x = Touch['x'] - 90
                Loc_y = Touch['y']
                TouchAction(driver).press(x=int(Loc_x), y=int(Loc_y)).release().perform()
                time.sleep(2)
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    user_name2 = OP.find_id('com.happyteam.dubbingshow:id/username').text
                    print("个人空间用户名:", user_name2)
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    print("空间加载失败")
                    time.sleep(1)
                    OP.back()
            except:
                pass
            time.sleep(2)
        time.sleep(2)
        try:
            OP.find_xpath('与TA合作').click()
            print("点击与TA合作")
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                print("进入配音界面")
                time.sleep(1)
                OP.back()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(TimeoutException ,NoSuchElementException):
                print("求合作下载失败！！！")
        except:
            pass
        time.sleep(1)
        try:
            OP.find_xpath('原声素材')
            OP.find_xpath('原声素材').click()
            print("点击原声素材")
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/shouchang_tv_fake')
                print("素材详情加载成功")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/shouchang_tv_fake').click()
                try:
                    shouchang_toast=OP.wait_toast('//android.widget.Toast')
                    print(shouchang_toast)
                except(NoSuchElementException,TimeoutException):
                    pass
                time.sleep(2)
                OP.back()
            except(TimeoutException ,NoSuchElementException):
                print("素材详情加载失败！！")
                time.sleep(2)
                OP.back()
        except:
            pass
        time.sleep(2)

    '''视频详情界面作品上滑'''
    def Swip(self):
        '''上滑切换视频'''
        for i in range(10):
            OP.swip_up()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(10)
                '''左滑进入空间'''
                OP.swip_left()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                    print(name)
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    print('空间加载失败')
                    time.sleep(1)
                    OP.back()
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
        '''退出视频详情界面'''
        OP.back()
        time.sleep(2)

    '''首页搜索'''
    def Search(self):
        '''点击置顶'''
        OP.find_id('com.happyteam.dubbingshow:id/dubbingTab').click()
        time.sleep(5)
        print('点击搜索')
        OP.find_id('com.happyteam.dubbingshow:id/iv_search').click()
        time.sleep(4)
        print('作品搜索')
        OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys('配音')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_theme_bg')
            names = OP.find_ids('com.happyteam.dubbingshow:id/userName')
            work_list = []
            for i in range(len(names)):
                user_name = OP.find_ids('com.happyteam.dubbingshow:id/userName')[i].text
                work_name = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
                work_list.append(user_name)
                work_list.append(work_name)
                time.sleep(1)
            print(work_list)
            OP.find_id('com.happyteam.dubbingshow:id/item_theme_bg').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(10)
                devc.keyevent(3)
                time.sleep(3)
                devc.launch_app()
                time.sleep(2)
                print('左滑进入个人空间')
                OP.swip_left()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(3)
                    OP.back()
                except(NoSuchElementException,TimeoutError):
                    print('空间加载失败')
                    time.sleep(2)
                    OP.back()
                time.sleep(4)
                print('上滑切换视频')
                for i in range(5):
                    OP.swip_up()
                    time.sleep(5)
                OP.back()
                time.sleep(2)
            except(NoSuchElementException,TimeoutError):
                pass
            print('上滑切换视频')
            for i in range(10):
                OP.swip_up()
                time.sleep(2)
            time.sleep(2)
        except(NoSuchElementException,TimeoutError):
            print('搜索结果为空')
        time.sleep(2)
        print('用户搜索')
        OP.find_id('com.happyteam.dubbingshow:id/ll_user').click()
        time.sleep(4)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/userhead')
            names = OP.find_ids('com.happyteam.dubbingshow:id/textView')
            user_list = []
            for i in range(len(names)):
                user_name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                user_list.append(user_name)
                time.sleep(1)
            print(user_list)
            time.sleep(2)
            print('点击关注')
            OP.find_id('com.happyteam.dubbingshow:id/status_icon').click()
            time.sleep(2)
            print('点击进入社团空间')
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/membercount')
                OP.find_id('com.happyteam.dubbingshow:id/follow_status').click()
                time.sleep(2)
                OP.back()
            except(NoSuchElementException,TimeoutError):
                print('社团空间加载失败')
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print('搜索用户')
            OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys('配音')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutError):
                    print('个人空间加载失败')
                    time.sleep(1)
                    OP.back()
                time.sleep(2)
                print('清空输入框')
                OP.find_id('com.happyteam.dubbingshow:id/btnClear').click()
                time.sleep(2)
                print('清楚历史记录')
                OP.find_xpath('清除历史记录').click()
                time.sleep(2)
            except(NoSuchElementException,TimeoutError):
                pass
        except:
            print('推荐用户列表为空')
        time.sleep(2)
        print('素材搜索')
        OP.find_id('com.happyteam.dubbingshow:id/ll_source').click()
        time.sleep(2)
        '''热搜榜'''
        OP.find_id('com.happyteam.dubbingshow:id/hothead').click()
        time.sleep(2)
        list = OP.find_ids('com.happyteam.dubbingshow:id/name')
        name_list = []
        for  i in range(len(list)):
            name = OP.find_ids('com.happyteam.dubbingshow:id/name')[i].text
            name_list.append(name)
            time.sleep(0.5)
        print(name_list)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/name').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        except(NoSuchElementException,TimeoutError):
            print('素材详情加载失败')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnClear').click()
        time.sleep(1)
        print('搜索素材')
        OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys('配音')
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            title = OP.find_ids('com.happyteam.dubbingshow:id/title_tv')
            for i in range(len(title)):
                OP.find_ids('com.happyteam.dubbingshow:id/title_tv')[i].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tv_source_title')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutError):
                    print('素材详情列表跳转失败')
                time.sleep(2)
        except(NoSuchElementException,TimeoutError):
            print('搜索失败')
        time.sleep(2)
        OP.back()

def run():
    H = Home_Hot()
    H.Home_load()
    H.Home_List()
    H.Open_Video()
    H.Play_video()
    H.Comment()
    H.share()
    H.Gift_List()
    H.Dubbing()
    H.Swip()
    H.Search()
    # try:
    #
    # except:
    #     print('运行中断')
    #     os.system('adb -s  95SSG6DANNAQINEM shell am force-stop com.happyteam.dubbingshow')


if __name__=="__main__":
    run()
    devc.quit()