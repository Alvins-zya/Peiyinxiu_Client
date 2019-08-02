from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
from pprint import pprint
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()

'''圈子'''
class Home_Circle():
    '''浏览历史'''
    def History(self):
        OP.find_id('com.happyteam.dubbingshow:id/newsTab').click()
        time.sleep(5)
        print("点击浏览历史")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/history').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/title')
            time.sleep(2)
            titles = OP.find_ids('com.happyteam.dubbingshow:id/title')
            print("当前页帖子数量:", len(titles))
            try:
                OP.find_id('com.happyteam.dubbingshow:id/title').click()
                print("点击进入帖子详情")
                time.sleep(2)
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                        time.sleep(1)
                        print("帖子详情加载失败")
                        OP.back()
                    except:
                        pass
                time.sleep(2)
                print("长按删除")
                el = OP.find_id('com.happyteam.dubbingshow:id/title')
                TouchAction(devc).long_press(el, 2000).release().perform()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right')
                    print("点击历史清空按钮")
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                except:
                    pass
                time.sleep(2)
                OP.back()
            except:
                time.sleep(1)
                OP.back()
        except(TimeoutException, NoSuchElementException):
            try:
                Tip = OP.find_id('com.happyteam.dubbingshow:id/empty_text').text
                print(Tip)
                time.sleep(2)
                OP.back()
            except:
                time.sleep(2)
                OP.back()

    '''话题搜索'''
    def Topic_search(self):
        OP.find_id('com.happyteam.dubbingshow:id/tv_key_word_help').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv')
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/tv')
            except:
                pass
        time.sleep(2)
        Tvs = OP.find_ids('com.happyteam.dubbingshow:id/tv')
        print("点击进入热门话题详情")
        for i in range(len(Tvs)):
            Topic_name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].text
            print(Topic_name)
            time.sleep(1)
            OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/title')
            Titles = OP.find_ids('com.happyteam.dubbingshow:id/title')
            for i in range(len(Titles)):
                Topic_name = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
                print(Topic_name)
                time.sleep(1)
                OP.find_ids('com.happyteam.dubbingshow:id/title')[i].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException, TimeoutException):
                    time.sleep(2)
                    OP.back()
                time.sleep(2)
        except:
            pass
        time.sleep(2)

        print("搜索话题")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("秀友圈")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_xpath('搜索结果')
            try:
                Topics_name = OP.find_id('com.happyteam.dubbingshow:id/title').text
                print(Topics_name)
                time.sleep(1)
                OP.back()
            except:
                time.sleep(1)
                OP.back()
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_xpath('热门话题')
                print("搜索失败")
                time.sleep(1)
                OP.back()
            except:
                pass
        time.sleep(2)

    '''圈子主页'''
    def Circle_home(self):
        print("点击帖子发布按钮")
        OP.find_id('com.happyteam.dubbingshow:id/send').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/image_tie')
            time.sleep(1)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            pass

        print("点击头像进入个人空间")
        name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[0].text
        print("圈子首页用户名称：",name)
        OP.find_ids('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
            Zoom_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
            print("个人空间用户名称：", Zoom_name)
            time.sleep(2)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                Zoom_name = OP.find_id('com.happyteam.dubbingshow:id/textView').text
                print("个人空间用户名称：", Zoom_name)
                time.sleep(2)
                OP.back()
            except(TimeoutException, NoSuchElementException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                    print('个人空间重载失败')
                    time.sleep(1)
                    OP.back()
                except:
                    pass
        time.sleep(2)
        print("获取帖子文字内容")
        Text = OP.find_ids('com.happyteam.dubbingshow:id/content')[0].text
        print("帖子内容：",Text)
        print("点击进入帖子详情")
        OP.find_ids('com.happyteam.dubbingshow:id/content')[0].click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/editContent')
            detail_Text = OP.find_id('com.happyteam.dubbingshow:id/content').text
            print("帖子内容：", detail_Text)
            time.sleep(2)
            OP.back()
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                    Text = OP.find_id('com.happyteam.dubbingshow:id/content').text
                    print("帖子内容：", Text)
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                        print('帖子详情重载失败')
                        time.sleep(1)
                        OP.back()
                    except:
                        pass
            except:
                pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/action').click()
        time.sleep(1)
        OP.back()
        time.sleep(2)

        print("查找图文帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/img3').click()
                time.sleep(2)
                print("左滑切换图片")
                OP.swip_left()
                time.sleep(1)
                OP.swip_left()
                time.sleep(1)
                OP.back()
                break
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/img1').click()
                    time.sleep(2)
                    OP.back()
                    break
                except:
                    pass
            time.sleep(1)
            OP.swip_up()
            time.sleep(1)
            while i ==9:
                print("未找到图文帖")
                break
        time.sleep(2)
        print("查找听评帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/playBtn').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/gift')
                    OP.find_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    devc.keyevent(3)
                    time.sleep(3)
                    devc.launch_app()
                    time.sleep(2)
                    OP.back()
                    break
                except(TimeoutException,NoSuchElementException):
                    pass
            except:
                pass
            OP.swip_up()
            time.sleep(2)
            while i==9:
                print("未找到听评帖")
                break


        time.sleep(2)
        print("查找语音帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/play').click()
                time.sleep(5)
                devc.keyevent(3)
                time.sleep(3)
                devc.launch_app()
                time.sleep(2)
                break
            except:
                pass
            OP.swip_up()
            time.sleep(1)
            while i ==9:
                print("未找到语音帖")
                break
        time.sleep(2)
        print("返回圈子顶部")
        OP.find_id('com.happyteam.dubbingshow:id/newsTab').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_key_word_help')
        except(TimeoutException,NoSuchElementException):
            print("未回到圈子首页顶部")
            OP.find_id('com.happyteam.dubbingshow:id/newsTab').click()
        time.sleep(2)

    '''话题详情'''
    def Topic_detail(self):
        print("进入话题详情")
        OP.find_id('com.happyteam.dubbingshow:id/tv_key_word_help').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv')
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/tv')
            except:
                pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("秀友圈")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_xpath('搜索结果')
            titles = OP.find_ids('com.happyteam.dubbingshow:id/title')
            list = []
            for i in range(len(titles)):
                name = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
                list.append(name)
                time.sleep(1)
            print(list)
            time.sleep(2)
            title = '秀友圈'
            check = list.index(title)
            OP.find_ids('com.happyteam.dubbingshow:id/title')[check].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
            except:
                pass
            time.sleep(2)
        except(TimeoutException, NoSuchElementException):
            try:
                OP.find_xpath('热门话题')
                print("搜索失败")
                time.sleep(1)
                OP.back()
                devc.close_app()
            except:
                pass
        time.sleep(2)
        print("点击订阅按钮")
        OP.find_id('com.happyteam.dubbingshow:id/img_subscribe').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            pass
        time.sleep(2)
        print("切换tab")
        time.sleep(10)
        OP.find_xpath('热门').click()
        time.sleep(4)

        print("查找图文帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/img3').click()
                time.sleep(2)
                print("左滑切换图片")
                OP.swip_left()
                time.sleep(1)
                OP.swip_left()
                time.sleep(1)
                OP.back()
                break
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/img1').click()
                    time.sleep(2)
                    OP.back()
                    break
                except:
                    pass
            time.sleep(1)
            OP.swip_up()
            time.sleep(1)
            if i == 9:
                print("未找到图文帖")
            else:
                pass

        time.sleep(2)
        print("查找听评帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/playBtn').click()
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    devc.keyevent(3)
                    time.sleep(3)
                    devc.launch_app()
                    time.sleep(2)
                    OP.back()
                    break
                except:
                    time.sleep(1)
                    break
            except:
                pass
            OP.swip_up()
            time.sleep(1)
            if i == 9:
                print("未找到听评帖")
            else:
                pass

        time.sleep(2)
        print("查找语音帖")
        for i in range(10):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/play').click()
                time.sleep(5)
                devc.keyevent(3)
                time.sleep(3)
                devc.launch_app()
                time.sleep(2)
                break
            except:
                pass
            OP.swip_up()
            time.sleep(1)
            if i == 9:
                print("未找到语音帖")
            else:
                pass
        time.sleep(2)
        print("上滑列表")
        for i in range(10):
            OP.swip_up()
            time.sleep(1)
        time.sleep(2)
    '''发帖'''
    def Posting(self):
        print("发布帖子")
        OP.find_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        print("发布图文帖")
        OP.find_id('com.happyteam.dubbingshow:id/image_tie').click()
        time.sleep(4)
        OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("点击添加图片")
        OP.find_id('com.happyteam.dubbingshow:id/pic').click()
        time.sleep(2)
        print("选择相册")
        OP.find_id('com.happyteam.dubbingshow:id/tv_photo').click()
        time.sleep(3)
        print("选择图片")
        OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[0].click()
        time.sleep(2)
        OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[1].click()
        time.sleep(2)
        OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[2].click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/next_step_tv').click()
        time.sleep(2)
        print("删除已添加的图片")
        OP.find_id('com.happyteam.dubbingshow:id/del').click()
        time.sleep(2)
        print("添加话题")
        OP.find_id('com.happyteam.dubbingshow:id/add_topic').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/tv')
            except:
                pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/title')
            OP.find_id('com.happyteam.dubbingshow:id/title').click()
        except(TimeoutException,NoSuchElementException):
            time.sleep(1)
            OP.back()
            time.sleep(1)
            devc.close_app()
        time.sleep(2)
        print("添加@用户")
        OP.find_id('com.happyteam.dubbingshow:id/at').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        except(TimeoutException,NoSuchElementException):
            time.sleep(1)
            OP.back()
        time.sleep(2)
        print("点击发布")
        OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
        except(TimeoutException,NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/right_icon1')
                time.sleep(1)
                OP.back()
            except:
                pass
        time.sleep(8)
        print("删除帖子")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/textView').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/editContent')
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                print("未显示删除弹窗")
                OP.back()
        except(TimeoutException,NoSuchElementException):
            time.sleep(2)
            OP.back()
        time.sleep(2)

        print("发布语音帖")
        OP.find_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/voice_tie').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("点击录音")
        OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        time.sleep(5)
        devc.keyevent(3)
        time.sleep(2)
        devc.launch_app()
        time.sleep(4)
        print("点击试听")
        OP.find_id('com.happyteam.dubbingshow:id/review').click()
        time.sleep(3)
        devc.keyevent(3)
        time.sleep(2)
        devc.launch_app()
        time.sleep(2)
        print("点击重录")
        OP.find_id('com.happyteam.dubbingshow:id/reDo').click()
        time.sleep(2)
        print("点击录音")
        OP.find_id('com.happyteam.dubbingshow:id/dubbing').click()
        time.sleep(10)
        devc.keyevent(3)
        time.sleep(2)
        devc.launch_app()
        time.sleep(2)
        print("点击下一步")
        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/play')
            OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("就是发帖子了！")
            time.sleep(2)
            print("更换语音帖封面")
            OP.find_id('com.happyteam.dubbingshow:id/change_cover').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/tv_photo').click()
            time.sleep(3)
            OP.find_id('com.happyteam.dubbingshow:id/photo_wall_item_photo').click()
            time.sleep(5)
            print("点击播放语音")
            OP.find_id('com.happyteam.dubbingshow:id/play').click()
            time.sleep(3)
            devc.keyevent(3)
            time.sleep(2)
            devc.launch_app()
            time.sleep(2)
            print("添加话题")
            OP.find_id('com.happyteam.dubbingshow:id/add_top').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/title')
                    OP.find_id('com.happyteam.dubbingshow:id/title').click()
                    time.sleep(2)
                except(NoSuchElementException):
                    time.sleep(1)
                    OP.back()
            except(TimeoutException,NoSuchElementException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/tv')
                    OP.find_xpath('我自己的话题').click()
                    time.sleep(2)
                except(NoSuchElementException):
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                        print("话题列表加载失败")
                        devc.close_app()
                    except:
                        pass
        except(TimeoutException,NoSuchElementException):
            pass
        time.sleep(2)
        print("添加@用户")
        OP.find_id('com.happyteam.dubbingshow:id/at').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                print("搜索失败")
                time.sleep(1)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("关注列表加载失败")
            time.sleep(1)
            OP.back()
        time.sleep(2)
        print("点击发布")
        OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbbingshow:id/btn_send').click()
                time.sleep(2)
                OP.back()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                pass
        time.sleep(2)
        print("删除帖子")
        OP.find_id('com.happyteam.dubbingshow:id/content').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/editContent')
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print("未显示删除弹窗")
                OP.back()
                time.sleep(1)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            OP.back()
        time.sleep(2)
        print("发布听评帖")
        OP.find_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/film_tie').click()
        time.sleep(3)
        print("输入内容")
        OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("添加作品")
        OP.find_id('com.happyteam.dubbingshow:id/add_img').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("配音")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
                OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSelect').click()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                time.sleep(1)
                OP.back()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            OP.back()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnBack').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)

        print("添加话题")
        OP.find_id('com.happyteam.dubbingshow:id/add_topic').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv')
            OP.find_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/title')
                OP.find_id('com.happyteam.dubbingshow:id/title').click()
            except(NoSuchElementException,TimeoutException):
                time.sleep(1)
                OP.back()
        except(NoSuchElementException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print("话题列表加载失败")
                devc.close_app()
            except:
                pass
        time.sleep(2)

        print("添加@用户")
        OP.find_id('com.happyteam.dubbingshow:id/at').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            OP.find_id(('com.happyteam.dubbingshow:id/btnSearch')).click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            except(NoSuchElementException,TimeoutException):
                print("搜索失败")
                time.sleep(1)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("关注列表加载失败")
            time.sleep(1)
            OP.back()
        time.sleep(2)

        print("点击发布")
        OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/img_subscribe')
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/right_icon1')
                time.sleep(1)
                OP.back()
            except:
                pass
        time.sleep(2)

        print("删除帖子")
        OP.find_id('com.happyteam.dubbingshow:id/content').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/editContent')
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print("未显示删除弹窗")
                time.sleep(2)
                OP.back()
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            OP.back()
        time.sleep(2)
        devc.close_app()
        time.sleep(3)
        devc.launch_app()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/newsTab')
        except(TimeoutException,NoSuchElementException):
            pass

