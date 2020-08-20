#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import random
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from Peiyinxiu_Client.dubbbingshow_99550.Operate import BaseOperate
from Peiyinxiu_Client.dubbbingshow_99550.devices import device
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()


'''社团'''
class Corporation():
    '''社团主界面'''
    def Corp_Home(self):
        print("点击社团")
        OP.find_id('com.happyteam.dubbingshow:id/society').click()
        try:
            OP.wait_xpath('我的社团')

        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_xpath('我的社团')
                    pass
                except(TimeoutException, NoSuchElementException):
                    print("社团主界面加载失败")
            except:
                pass
        time.sleep(2)

    '''社团搜索'''
    def Corp_Search(self):
        print("搜索社团搜索框")
        OP.find_id('com.happyteam.dubbingshow:id/search').click()
        time.sleep(2)
        print("输入社团ID")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys("145834196")
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            time.sleep(5)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                OP.back()
                print("网络异常")
            except:
                pass
        except:

        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_xpath('人间惨剧')
        except(TimeoutException,NoSuchElementException):
            pass
        Corp_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
        check_name = "人间惨剧"
        if Corp_name == check_name:
            pass
        else:

            time.sleep(1)
            OP.back()
            print("未搜索到指定社团")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/username').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')

            time.sleep(2)
            OP.back()
        except(TimeoutException,NoSuchElementException):

            time.sleep(2)
            OP.back()
        time.sleep(2)
        OP.back()

    '''我的社团'''
    def Corp_My(self):
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/read')
        except:
            print("暂未加入社团")
        time.sleep(2)
        num = [0,1,2]
        for i in num:
            try:
                OP.find_ids('com.happyteam.dubbingshow:id/rl_all')[i].click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("测试一下")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                    time.sleep(2)
                    print("消息发送成功")
                    OP.back()
                except(TimeoutException,NoSuchElementException):
                    time.sleep(1)
                    OP.back()
            except:
                pass
        time.sleep(2)
        print("点击全部已读")
        OP.find_id('com.happyteam.dubbingshow:id/read').click()
        time.sleep(2)
        print("点击进入社团")
        OP.find_ids('com.happyteam.dubbingshow:id/rl_all')[0].click()
        time.sleep(2)
        print("发送语音")
        OP.find_id('com.happyteam.dubbingshow:id/btn_change_input_mode').click()
        time.sleep(1)
        voice = OP.find_id('com.happyteam.dubbingshow:id/btn_record_voice')
        TouchAction(devc).long_press(voice,duration=10000).wait(5000).perform()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/btn_play_sound')
            print('点击播放语音')
            OP.find_id('com.happyteam.dubbingshow:id/btn_play_sound').click()
            time.sleep(3)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        print('发送图片')
        Action = OP.find_id('com.happyteam.dubbingshow:id/show_action')
        Action.click()
        time.sleep(2)
        print("点击相册")
        OP.find_id('com.happyteam.dubbingshow:id/photo').click()
        time.sleep(2)
        '''随机选择图片'''
        Photos = OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')
        Select_photo = random.randint(0,int(len(Photos)-1))
        time.sleep(2)

        time.sleep(1)
        OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[Select_photo].click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/next_step_tv').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/btn_record_voice')
        except:
            print('未返回到聊天详情界面')

        time.sleep(2)
        print('发送作品')
        Action.click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/film').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')

            time.sleep(2)
            '''随机选择作品'''
            Films = OP.find_ids('com.happyteam.dubbingshow:id/filmBg')
            Select_film = random.randint(0,int(len(Films)-2))
            OP.find_ids('com.happyteam.dubbingshow:id/filmBg')[Select_film].click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSelect').click()
            OP.wait_id('com.happyteam.dubbingshow:id/btn_record_voice')
        except(NoSuchElementException,TimeoutException):
            print("作品列表加载失败")
            time.sleep(1)
            OP.back()
        time.sleep(3)
        print('发红包')
        Action.click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/redpacket').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/cash_num').send_keys("1")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/people_num').send_keys("1")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet').click()
        time.sleep(2)

        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        try:
            OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet')
            time.sleep(2)
            print("钻石不足")
            time.sleep(2)
            OP.back()
        except:
            pass
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/red_packet')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/red_packet').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/open_red_packet_btn').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/user_head')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/red_packet_detail_close_btn').click()
            except(TimeoutException,NoSuchElementException):
                print("红包领取失败")

        except(NoSuchElementException,TimeoutException):
            print("无红包")

        time.sleep(2)
        OP.back()
        time.sleep(2)
        OP.find_ids('com.happyteam.dubbingshow:id/rl_all')[0].click()
        time.sleep(2)
        try:
            el3 = OP.find_id('com.happyteam.dubbingshow:id/btn_space_manager_jump')
            el3.click()
            print("点击社团管理")
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userHead')
            except(TimeoutException,NoSuchElementException):

            time.sleep(2)
            try:
                OP.find_xpath('可以分配权限给其他成员啦！')
                print("显示有成员引导")
                OP.find_xpath('可以分配权限给其他成员啦！').click()
            except:
                pass
            time.sleep(2)
            print('点击编辑资料')
            OP.find_id('com.happyteam.dubbingshow:id/edit_profile').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/society_name')

                Society_name = random.randint(0x4E00, 0x9FBF)
                OP.find_id('com.happyteam.dubbingshow:id/society_name').send_keys(Society_name)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/brief_content').send_keys("暂时没有写简介哦~")
                time.sleep(2)
                OP.find_xpath('更多频道').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tv')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/close')
                        OP.find_id('com.happyteam.dubbingshow:id/close').click()
                    except:
                        pass
                    time.sleep(2)

                    time.sleep(2)
                    Tv_num = random.randint(1,20)
                    name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[Tv_num].text
                    print(name)
                    time.sleep(1)
                    OP.find_ids('com.happyteam.dubbingshow:id/tv')[Tv_num].click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                    time.sleep(2)
                except:
                    print('更多频道界面加载失败')
                    time.sleep(1)

                    time.sleep(1)
                    OP.back()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except:
                    try:
                        OP.find_xpath('更多频道')
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        print("社团资料修改失败")

                    except:
                        pass
                time.sleep(2)
            except(TimeoutException,NoSuchElementException):
                print("社团编辑资料界面加载失败")
                time.sleep(1)

                OP.back()
            time.sleep(2)
            Member_count = OP.find_id('com.happyteam.dubbingshow:id/member').text
            print(Member_count)
            print("点击添加社团成员")
            OP.find_id('com.happyteam.dubbingshow:id/addfriend').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    OP.wait_xpath('配音秀官方号')
                    OP.find_xpath('配音秀官方号').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                    try:
                        toast = OP.wait_toast('//android.widget.Toast')
                        print(toast)
                    except(TimeoutException,NoSuchElementException):
                        pass
                except(TimeoutException,NoSuchElementException):
                    print("搜索失败")
                    time.sleep(1)
                    OP.back()
            except(TimeoutException,NoSuchElementException):
                print("关注列表加载失败")
                time.sleep(1)
                OP.back()
            time.sleep(2)
            print("进入社团成员列表")
            OP.find_id('com.happyteam.dubbingshow:id/member').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/shezhang')
                time.sleep(1)
                print("添加成员")
                OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
                    try:
                        OP.wait_xpath('配音秀官方号')
                        OP.find_xpath('配音秀官方号').click()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                        try:
                            OP.wait_id('com.happyteam.dubbingshow:id/shezhang')
                        except(TimeoutException, NoSuchElementException):
                            print("添加失败")
                            time.sleep(1)
                            OP.back()
                        time.sleep(2)
                        try:
                            OP.find_id('com.happyteam.dubbingshow:id/more')
                            print('设置成员权限')
                            OP.find_id('com.happyteam.dubbingshow:id/more').click()
                            time.sleep(2)
                            OP.find_id('com.happyteam.dubbingshow:id/check_box1').click()
                            time.sleep(1)
                            OP.find_id('com.happyteam.dubbingshow:id/check_box2').click()
                            time.sleep(1)
                            OP.find_id('com.happyteam.dubbingshow:id/save').click()
                            try:
                                toast = OP.wait_toast('//android.widget.Toast')
                                print(toast)
                            except:
                                pass
                            time.sleep(2)
                        except:
                            print('非社长，成员未显示权限设置')
                    except(TimeoutException, NoSuchElementException):
                        print("搜索失败")
                        time.sleep(1)
                        OP.back()
                    time.sleep(2)
                except(TimeoutException, NoSuchElementException):
                    print("成员列表加载失败")
            except(TimeoutException,NoSuchElementException):
                pass
            time.sleep(2)
            OP.back()
            time.sleep(2)
            print("点击编辑公告")
            OP.find_id('com.happyteam.dubbingshow:id/edit_gonggao').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/content').send_keys('此社团无公告~')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(4)
            print("点击作品管理")
            OP.find_id('com.happyteam.dubbingshow:id/film_manage').click()
            time.sleep(2)
            try:
                OP.find_xpath('你还没有社团空间作品哦')
                print("暂无社团作品")
            except:
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/item_theme_bg')
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/item_theme_bg').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/gift')
                        time.sleep(2)
                        OP.back()
                    except(TimeoutException,NoSuchElementException):
                        print("社团作品详情加载失败")
                    time.sleep(2)
                    print("作品置顶")
                    touch_film = OP.find_id('com.happyteam.dubbingshow:id/item_theme_bg')
                    TouchAction(devc).long_press(touch_film,2000).release().perform()
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/zhiding').click()
                    except(TimeoutException,NoSuchElementException):
                        pass
                    time.sleep(2)

                    print("创建合辑")
                    OP.find_id('com.happyteam.dubbingshow:id/addfilm').click()
                    time.sleep(2)
                    TouchAction(devc).press(x=0.5*x,y=0.802*y).release().perform()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("合辑1")
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/ok').click()
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/choice').click()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                        time.sleep(2)
                        OP.find_xpath('合辑').click()
                        time.sleep(2)
                        OP.find_xpath('合辑1').click()
                        time.sleep(2)
                        long_touch = OP.find_id('com.happyteam.dubbingshow:id/img')
                        TouchAction(devc).long_press(long_touch,3000).release().perform()
                        OP.find_id('com.happyteam.dubbingshow:id/tv_zhiding').click()
                        try:
                            shangyi_toast = OP.wait_toast('//android.widget.Toast')
                            print(shangyi_toast)
                        except:
                            pass
                        time.sleep(2)
                        TouchAction(devc).long_press(long_touch, 2500).release().perform()
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/tv_shanchu').click()
                        time.sleep(1)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        try:
                            OP.wait_xpath('合辑')
                        except:
                            print("移除失败")
                            time.sleep(1)
                            OP.back()
                        time.sleep(2)
                        print("退出作品管理界面")
                        OP.back()
                    except:
                        print("暂无作品可添加~")
                        time.sleep(2)
                        OP.back()
                        print("退出社团作品列表界面")
                        OP.back()
                except(TimeoutException,NoSuchElementException):
                    print("作品列表加载失败")
                    time.sleep(1)
                    OP.back()
            time.sleep(2)

            print("申请蓝V")
            try:
                OP.find_id('com.happyteam.dubbingshow:id/apply_lv').click()
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/apply_lv')
                    print("蓝v界面跳转失败")
                except:
                    time.sleep(2)
                    OP.back()
            except:
                print("未显示蓝V申请入口")
            time.sleep(2)

            print("入社权限设置")
            OP.find_id('com.happyteam.dubbingshow:id/society_apply_jurisdiction').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/modify').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("闲人免进！")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/addFilm').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/addSource').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/all').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/apply').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/none').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
            try:
                OP.wait_xpath('社团管理')
            except(TimeoutException,NoSuchElementException):
                time.sleep(1)
                OP.back()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)
            print("社团消息免打扰")
            OP.find_id('com.happyteam.dubbingshow:id/btn_push').click()
            time.sleep(6)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/gold_match')
                print("点击社团财富")
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/gold_match').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/distribution_diamond')
                    print("分配钻石")
                    OP.find_id('com.happyteam.dubbingshow:id/distribution_diamond').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/username').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/gold_count').send_keys("1")
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/remark').send_keys("测试")
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/sure').click()
                    try:
                        OP.wait_xpath('社团财富')
                    except(NoSuchElementException, TimeoutException):
                        print("钻石分配失败")
                        time.sleep(1)
                        OP.back()
                    time.sleep(2)
                    print("分配金币")
                    OP.find_id('com.happyteam.dubbingshow:id/distribution_gold').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/username').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/gold_count').send_keys("1")
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/remark').send_keys("测试")
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/sure').click()
                    try:
                        OP.wait_xpath('社团财富')
                        pass
                    except(NoSuchElementException, TimeoutException):
                        print("金币分配失败")
                        time.sleep(1)
                        OP.back()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                except(NoSuchElementException, TimeoutException):
                    print("社团财富界面加载失败")
                    time.sleep(1)
                    OP.back()
                time.sleep(2)
                OP.swip_up()
                print("社团钱包")
                OP.find_id('com.happyteam.dubbingshow:id/meney').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/distribution_gold')
                    OP.find_id('com.happyteam.dubbingshow:id/distribution_gold').click()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    print("社团钱包界面加载失败")
                    time.sleep(1)
                    OP.back()
                time.sleep(2)
                print("作品下载设置开关")
                OP.find_id('com.happyteam.dubbingshow:id/btn_load').click()
                time.sleep(5)
            except(TimeoutException,NoSuchElementException):
                print("非社长身份，未显示社团财富、社团钱包、社团消息设置入口")
            time.sleep(2)
            print("退出社团管理界面")
            OP.back()
            time.sleep(2)
        except(NoSuchElementException,TimeoutException):
            print("未显示社团管理按钮")
        time.sleep(2)

        print("点击空间按钮")
        Zoom = OP.find_id('com.happyteam.dubbingshow:id/btn_space_jump')
        Zoom.click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')
            OP.find_id('com.happyteam.dubbingshow:id/fanscount').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/username')
                time.sleep(2)
                OP.back()
            except(TimeoutException,NoSuchElementException):
                print("粉丝列表加载失败")
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/membercount').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/name')
                time.sleep(2)
                OP.back()
            except(TimeoutException,NoSuchElementException):
                print("成员列表加载失败")
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnMember').click()#素材列表
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnCollect').click()#合集列表
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnFilm').click()#作品列表
            time.sleep(2)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            print("空间加载失败")
            time.sleep(1)
            OP.back()
        time.sleep(2)

        print("点击活动")
        OP.find_xpath('活动').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/task_box')
            OP.find_ids('com.happyteam.dubbingshow:id/task_box')[0].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/gift')
                    devc.keyevent(3)
                    time.sleep(2)
                    devc.launch_app()
                    time.sleep(2)
                    print("送礼两次")
                    OP.find_id('com.happyteam.dubbingshow:id/gift').click()
                    time.sleep(2)
                    for i in range(2):
                        OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                        time.sleep(4)
                    time.sleep(2)
                    for i in range(3):
                        OP.back()
                        time.sleep(2)
                except(TimeoutException,NoSuchElementException):
                    print("视频详情加载失败")
                    time.sleep(2)
                    OP.back()
                print("下拉刷新")
                OP.swip_down()
                time.sleep(4)
            except(TimeoutException,NoSuchElementException):
                try:
                    OP.find_xpath('还没有任何作品哦~')
                    time.sleep(1)
                    print('还没有任何作品哦~')
                    time.sleep(1)
                    OP.back()
                except:
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/bg_view')
                        print("开启宝箱")
                        time.sleep(1)
                        OP.back()
                    except:
                        try:
                            OP.find_xpath('给社团成员的作品送礼2次')
                            print('宝箱以领取')
                        except:
                            pass
            time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            print("活动列表界面加载失败")

        print("点击榜单")
        OP.find_xpath('榜单').click()
        time.sleep(3)
        bangdan = OP.find_ids('com.happyteam.dubbingshow:id/look_rank')
        for i in range(len(bangdan)):
            OP.find_ids('com.happyteam.dubbingshow:id/look_rank')[i].click()
            try:
                OP.wait_xpath('贡献榜')
                OP.find_xpath('活动榜').click()
                time.sleep(2)
                OP.swip_up()
                time.sleep(4)
                OP.find_xpath('作品榜').click()
                time.sleep(2)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
        OP.back()
        time.sleep(2)


        print("点击社团更多")
        try:
            OP.find_id('com.happyteam.dubbingshow:id/more_img')
            OP.find_id('com.happyteam.dubbingshow:id/more_img').click()
            time.sleep(2)
            print("上滑列表")
            for i in range(5):
                OP.swip_up()
                time.sleep(4)
        except:
            pass

    '''推荐社团'''
    def Corp_Recommend(self):
        print("上滑列表")
        OP.swip_up()
        time.sleep(4)
        print("点击进入社团空间")
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/membercount')

            time.sleep(2)
            OP.back()
        except(TimeoutException, NoSuchElementException):
            print("空间加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(2)
        print("点击加入按钮")
        OP.find_id('com.happyteam.dubbingshow:id/join').click()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            print("申请入社界面加载失败")
            time.sleep(2)
            OP.back()
        except:
            time.sleep(2)
            OP.back()
        time.sleep(2)
        print("上滑列表")
        for i in range(5):
            OP.swip_up()
            time.sleep(4)

            time.sleep(2)


