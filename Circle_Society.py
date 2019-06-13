#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import random
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException



# 获取屏幕宽(x)/高(y)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
# # 打印屏幕高和宽
# print(driver.get_window_size())


# 判断是否成功进入首页（以每日任务按钮为标准）
WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/task_box'))


'''圈子'''
class Home_Circle():
    '''浏览历史'''
    def History(self):
        driver.find_element_by_id('com.happyteam.dubbingshow:id/newsTab').click()
        time.sleep(5)
        print("点击浏览历史")
        time.sleep(1)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/history').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/title'))
            time.sleep(2)
            titles = driver.find_elements_by_id('com.happyteam.dubbingshow:id/title')
            print("当前页帖子数量:", len(titles))
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/title').click()
                print("点击进入帖子详情")
                time.sleep(2)
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                    time.sleep(2)
                    driver.back()
                except(TimeoutException, NoSuchElementException):
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                        time.sleep(1)
                        print("帖子详情加载失败")
                        driver.back()
                    except:
                        pass
                time.sleep(2)
                print("长按删除")
                el = driver.find_element_by_id('com.happyteam.dubbingshow:id/title')
                TouchAction(driver).long_press(el, 2000).release().perform()
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(4)
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/clear')
                    print("点击历史清空按钮")
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/clear').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                except:
                    pass
                time.sleep(2)
                driver.back()
            except:
                time.sleep(1)
                driver.back()
        except(TimeoutException, NoSuchElementException):
            try:
                Tip = driver.find_element_by_id('com.happyteam.dubbingshow:id/empty_text').text
                print(Tip)
                time.sleep(2)
                driver.back()
            except:
                time.sleep(2)
                driver.back()

    '''话题搜索'''
    def Topic_search(self):
        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_key_word_help').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
        except(TimeoutException, NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
            except:
                pass
        time.sleep(2)
        Tvs = driver.find_elements_by_id('com.happyteam.dubbingshow:id/tv')
        print("点击进入热门话题详情")
        for i in range(len(Tvs)):
            Topic_name = driver.find_elements_by_id('com.happyteam.dubbingshow:id/tv')[i].text
            print(Topic_name)
            time.sleep(1)
            driver.find_elements_by_id('com.happyteam.dubbingshow:id/tv')[i].click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe'))
                time.sleep(2)
                driver.back()
            except(NoSuchElementException,TimeoutException):
                time.sleep(2)
                driver.back()
            time.sleep(2)
        time.sleep(2)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/title')
            Titles = driver.find_elements_by_id('com.happyteam.dubbingshow:id/title')
            for i in range(len(Titles)):
                Topic_name = driver.find_elements_by_id('com.happyteam.dubbingshow:id/title')[i].text
                print(Topic_name)
                time.sleep(1)
                driver.find_elements_by_id('com.happyteam.dubbingshow:id/title')[i].click()
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe'))
                    time.sleep(2)
                    driver.back()
                except(NoSuchElementException, TimeoutException):
                    time.sleep(2)
                    driver.back()
                time.sleep(2)
        except:
            pass
        time.sleep(2)

        print("搜索话题")
        time.sleep(1)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("秀友圈")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="搜索结果"]'))
            try:
                Topics_name = driver.find_element_by_id('com.happyteam.dubbingshow:id/title').text
                print(Topics_name)
                time.sleep(1)
                driver.back()
            except:
                time.sleep(1)
                driver.back()
        except(TimeoutException, NoSuchElementException):
            try:
                driver.find_element_by_xpath('//android.widget.TextView[@text="热门话题"]')
                print("搜索失败")
                time.sleep(1)
                driver.back()
            except:
                pass
        time.sleep(2)

    '''圈子主页'''
    def Circle_home(self):
        print("点击帖子发布按钮")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/send').click()
        try:
            WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/image_tie'))
            time.sleep(1)
            driver.back()
        except(TimeoutException,NoSuchElementException):
            pass

        print("点击头像进入个人空间")
        name = driver.find_elements_by_id('com.happyteam.dubbingshow:id/textView')[0].text
        print("圈子首页用户名称：",name)
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/userhead')[0].click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_level'))
            Zoom_name = driver.find_element_by_id('com.happyteam.dubbingshow:id/username').text
            print("个人空间用户名称：", Zoom_name)
            time.sleep(2)
            driver.back()
        except(TimeoutException,NoSuchElementException):
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
            try:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_level'))
                Zoom_name = driver.find_element_by_id('com.happyteam.dubbingshow:id/textView').text
                print("个人空间用户名称：", Zoom_name)
                time.sleep(2)
                driver.back()
            except(TimeoutException, NoSuchElementException):
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                    print('个人空间重载失败')
                    time.sleep(1)
                    driver.back()
                except:
                    pass
        time.sleep(2)
        print("获取帖子文字内容")
        Text = driver.find_elements_by_id('com.happyteam.dubbingshow:id/content')[0].text
        print("帖子内容：",Text)
        print("点击进入帖子详情")
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/content')[0].click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent'))
            detail_Text = driver.find_element_by_id('com.happyteam.dubbingshow:id/content').text
            print("帖子内容：", detail_Text)
            time.sleep(2)
            driver.back()
        except(TimeoutException,NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent'))
                    Text = driver.find_element_by_id('com.happyteam.dubbingshow:id/content').text
                    print("帖子内容：", Text)
                    time.sleep(2)
                    driver.back()
                except(TimeoutException, NoSuchElementException):
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                        print('帖子详情重载失败')
                        time.sleep(1)
                        driver.back()
                    except:
                        pass
            except:
                pass
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/action').click()
        time.sleep(1)
        driver.back()
        time.sleep(2)

        print("查找图文帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/img3').click()
                time.sleep(2)
                print("左滑切换图片")
                driver.swipe(0.8*x,0.5*y,0.3*x,0.5*y,300)
                time.sleep(1)
                driver.swipe(0.96 * x, 0.5 * y, 0.18 * x, 0.5 * y, 300)
                time.sleep(1)
                driver.back()
                break
            except:
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/img1').click()
                    time.sleep(2)
                    driver.back()
                    break
                except:
                    pass
            time.sleep(1)
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
            while i ==9:
                print("未找到图文帖")
                break
        time.sleep(2)
        print("查找听评帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/playBtn').click()
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/gift'))
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    driver.keyevent(3)
                    time.sleep(3)
                    driver.launch_app()
                    time.sleep(2)
                    driver.back()
                    break
                except(TimeoutException,NoSuchElementException):
                    pass
            except:
                pass
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(2)
            while i==9:
                print("未找到听评帖")
                break


        time.sleep(2)
        print("查找语音帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/play').click()
                time.sleep(5)
                driver.keyevent(3)
                time.sleep(3)
                driver.launch_app()
                time.sleep(2)
                break
            except:
                pass
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
            while i ==9:
                print("未找到语音帖")
                break
        time.sleep(2)
        print("返回圈子顶部")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/newsTab').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_key_word_help'))
        except(TimeoutException,NoSuchElementException):
            print("未回到圈子首页顶部")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/newsTab').click()
        time.sleep(2)

    '''话题详情'''
    def Topic_detail(self):
        print("进入话题详情")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_key_word_help').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
        except(TimeoutException, NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                WebDriverWait(driver, 15).until(
                    lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
            except:
                pass
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("秀友圈")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="搜索结果"]'))
            driver.find_element_by_xpath('//android.widget.TextView[@text="秀友圈"]').click()
        except(TimeoutException, NoSuchElementException):
            try:
                driver.find_element_by_xpath('//android.widget.TextView[@text="热门话题"]')
                print("搜索失败")
                time.sleep(1)
                driver.back()
                driver.close_app()
            except:
                pass
        time.sleep(2)
        print("点击订阅按钮")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe').click()
        time.sleep(4)
        print("切换tab")
        time.sleep(10)
        driver.find_element_by_xpath('//android.widget.TextView[@text="热门"]').click()
        time.sleep(4)

        print("查找图文帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/img3').click()
                time.sleep(2)
                print("左滑切换图片")
                driver.swipe(0.8 * x, 0.5 * y, 0.3 * x, 0.5 * y, 300)
                time.sleep(1)
                driver.swipe(0.8 * x, 0.5 * y, 0.3 * x, 0.5 * y, 300)
                time.sleep(1)
                driver.back()
                break
            except:
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/img1').click()
                    time.sleep(2)
                    driver.back()
                    break
                except:
                    pass
            time.sleep(1)
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
            if i == 9:
                print("未找到图文帖")
            else:
                pass

        time.sleep(2)
        print("查找听评帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/playBtn').click()
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/gift'))
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    driver.keyevent(3)
                    time.sleep(3)
                    driver.launch_app()
                    time.sleep(2)
                    driver.back()
                    break
                except:
                    time.sleep(1)
                    break
            except:
                pass
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
            if i == 9:
                print("未找到听评帖")
            else:
                pass

        time.sleep(2)
        print("查找语音帖")
        for i in range(10):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/play').click()
                time.sleep(5)
                driver.keyevent(3)
                time.sleep(3)
                driver.launch_app()
                time.sleep(2)
                break
            except:
                pass
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
            if i == 9:
                print("未找到语音帖")
            else:
                pass
        time.sleep(2)
        print("上滑列表")
        for i in range(10):
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(1)
        time.sleep(2)
    '''发帖'''
    def Posting(self):
        print("发布帖子")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        print("发布图文帖")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/image_tie').click()
        time.sleep(4)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("点击添加图片")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/pic').click()
        time.sleep(2)
        print("选择相册")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_photo').click()
        time.sleep(3)
        print("选择图片")
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/cb_select_tag')[0].click()
        time.sleep(2)
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/cb_select_tag')[1].click()
        time.sleep(2)
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/cb_select_tag')[2].click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/next_step_tv').click()
        time.sleep(2)
        print("删除已添加的图片")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/del').click()
        time.sleep(2)
        print("添加话题")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/add_topic').click()
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
        except(TimeoutException,NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
            except:
                pass
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/title'))
            driver.find_element_by_xpath('//android.widget.TextView[@text="我自己的话题"]').click()
        except(TimeoutException,NoSuchElementException):
            time.sleep(1)
            driver.back()
            time.sleep(1)
            driver.close_app()
        time.sleep(2)
        print("添加@用户")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/at').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead').click()
        except(TimeoutException,NoSuchElementException):
            time.sleep(1)
            driver.back()
        time.sleep(2)
        print("点击发布")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe'))
        except(TimeoutException,NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1')
                time.sleep(1)
                driver.back()
            except:
                pass
        time.sleep(8)
        print("删除帖子")
        time.sleep(1)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/textView').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(driver).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                print("未显示删除弹窗")
                driver.back()
        except(TimeoutException,NoSuchElementException):
            time.sleep(2)
            driver.back()
        time.sleep(2)

        print("发布语音帖")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/voice_tie').click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("点击录音")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/dubbing').click()
        time.sleep(5)
        driver.keyevent(3)
        time.sleep(2)
        driver.launch_app()
        time.sleep(4)
        print("点击试听")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/review').click()
        time.sleep(3)
        driver.keyevent(3)
        time.sleep(2)
        driver.launch_app()
        time.sleep(2)
        print("点击重录")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/reDo').click()
        time.sleep(2)
        print("点击录音")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/dubbing').click()
        time.sleep(10)
        driver.keyevent(3)
        time.sleep(2)
        driver.launch_app()
        time.sleep(2)
        print("点击下一步")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_right').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/play'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("就是发帖子了！")
            time.sleep(2)
            print("更换语音帖封面")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/change_cover').click()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_photo').click()
            time.sleep(3)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/photo_wall_item_photo').click()
            time.sleep(5)
            print("点击播放语音")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/play').click()
            time.sleep(3)
            driver.keyevent(3)
            time.sleep(2)
            driver.launch_app()
            time.sleep(2)
            print("添加话题")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/add_top').click()
            try:
                WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    WebDriverWait(driver,15).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="我自己的话题"]'))
                    driver.find_element_by_xpath('//android.widget.TextView[@text="我自己的话题"]').click()
                    time.sleep(2)
                except(NoSuchElementException):
                    time.sleep(1)
                    driver.back()
            except(TimeoutException,NoSuchElementException):
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
                    driver.find_element_by_xpath('//android.widget.TextView[@text="我自己的话题"]').click()
                    time.sleep(2)
                except(NoSuchElementException):
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                        print("话题列表加载失败")
                        driver.close_app()
                    except:
                        pass
        except(TimeoutException,NoSuchElementException):
            pass
        time.sleep(2)
        print("添加@用户")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/at').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead').click()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                print("搜索失败")
                time.sleep(1)
                driver.back()
        except(NoSuchElementException,TimeoutException):
            print("关注列表加载失败")
            time.sleep(1)
            driver.back()
        time.sleep(2)
        print("点击发布")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe'))
        except(NoSuchElementException,TimeoutException):
            try:
                driver.find_element_by_id('com.happyteam.dubbbingshow:id/btn_send').click()
                time.sleep(2)
                driver.back()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                pass
        time.sleep(2)
        print("删除帖子")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/content').click()
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(driver).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print("未显示删除弹窗")
                driver.back()
                time.sleep(1)
                driver.back()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            driver.back()
        time.sleep(2)
        print("发布听评帖")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/send').click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/film_tie').click()
        time.sleep(3)
        print("输入内容")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("就是想发个帖子！")
        time.sleep(2)
        print("添加作品")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/add_img').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("配音")
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg'))
                driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg').click()
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSelect').click()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                time.sleep(1)
                driver.back()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnBack').click()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            driver.back()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnBack').click()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)

        print("添加话题")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/add_topic').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/tv'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/et_key_word').send_keys("我自己的话题")
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/title'))
                driver.find_element_by_xpath('//android.widget.TextView[@text="我自己的话题"]').click()
            except(NoSuchElementException,TimeoutException):
                time.sleep(1)
                driver.back()
        except(NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                print("话题列表加载失败")
                driver.close_app()
            except:
                pass
        time.sleep(2)

        print("添加@用户")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/at').click()
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(1)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
            time.sleep(2)
            driver.find_element_by_id(('com.happyteam.dubbingshow:id/btnSearch')).click()
            try:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead').click()
            except(NoSuchElementException,TimeoutException):
                print("搜索失败")
                time.sleep(1)
                driver.back()
        except(NoSuchElementException,TimeoutException):
            print("关注列表加载失败")
            time.sleep(1)
            driver.back()
        time.sleep(2)

        print("点击发布")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/img_subscribe'))
        except(NoSuchElementException,TimeoutException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1')
                time.sleep(1)
                driver.back()
            except:
                pass
        time.sleep(2)

        print("删除帖子")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/content').click()
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            TouchAction(driver).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException,TimeoutException):
                print("未显示删除弹窗")
                time.sleep(2)
                driver.back()
                time.sleep(2)
                driver.back()
        except(NoSuchElementException,TimeoutException):
            time.sleep(1)
            driver.back()
        time.sleep(2)
        driver.close_app()
        time.sleep(3)
        driver.launch_app()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/newsTab'))
        except(TimeoutException,NoSuchElementException):
            pass


'''社区'''
class Community():
    def Communitys(self):
        print("点击首页-社区")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/newsTab').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
        except(TimeoutException,NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                WebDriverWait(driver, 15).until( lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                    print('圈子主界面重载失败')
                    driver.close_app()
                except:
                    pass
            except:
                pass
        time.sleep(2)


'''社团'''
class Corporation():
    '''社团主界面'''
    def Corp_Home(self):
        print("点击社团")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/society').click()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="我的社团"]'))
        except(TimeoutException,NoSuchElementException):
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="我的社团"]'))
                    pass
                except(TimeoutException, NoSuchElementException):
                    print("社团主界面加载失败")
            except:
                pass
        time.sleep(2)

    '''社团搜索'''
    def Corp_Search(self):
        print("搜索社团搜索框")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/search').click()
        time.sleep(2)
        print("输入社团ID")
        time.sleep(1)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/txtKeyword').send_keys("145834196")
        time.sleep(2)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload').click()
            time.sleep(5)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
                time.sleep(1)
                driver.back()
                print("网络异常")
            except:
                pass
        except:
            pass
        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
        try:
            WebDriverWait(driver,15).until(lambda driver:driver.find_element_by_id('//android.widget.TextView[@text="人间惨剧"]'))
        except(TimeoutException,NoSuchElementException):
            pass
        Corp_name = driver.find_element_by_id('com.happyteam.dubbingshow:id/username').text
        check_name = "人间惨剧"
        if Corp_name == check_name:
            pass
        else:
            time.sleep(1)
            driver.back()
            print("未搜索到指定社团")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/username').click()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/membercount'))
            time.sleep(2)
            driver.back()
        except(TimeoutException,NoSuchElementException):
            time.sleep(2)
            driver.back()
        time.sleep(2)
        driver.back()


    '''我的社团'''
    def Corp_My(self):
        time.sleep(2)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/read')
        except:
            print("暂未加入社团")
        time.sleep(2)
        num = [0,1,2]
        for i in num:
            try:
                driver.find_elements_by_id('com.happyteam.dubbingshow:id/rl_all')[i].click()
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/editContent').send_keys("测试一下")
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_send').click()
                try:
                    WebDriverWait(driver,20).until_not(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_send'))
                    time.sleep(2)
                    driver.back()
                except(TimeoutException,NoSuchElementException):
                    print("社团消息发送失败")
                    driver.back()
            except:
                pass
        time.sleep(2)
        print("点击全部已读")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/read').click()
        time.sleep(2)
        print("点击进入社团")
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/rl_all')[0].click()
        time.sleep(2)
        # print("发送语音")
        # driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_change_input_mode').click()
        # time.sleep(1)
        # voice = driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_record_voice')
        # TouchAction(driver).long_press(voice,duration=10000).wait(5000).perform()
        # time.sleep(2)
        # try:
        #     WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_play_sound'))
        #     print('点击播放语音')
        #     driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_play_sound').click()
        #     time.sleep(3)
        # except(NoSuchElementException,TimeoutException):
        #     pass
        time.sleep(2)
        print('发送图片')
        Action = driver.find_element_by_id('com.happyteam.dubbingshow:id/show_action')
        Action.click()
        time.sleep(2)
        print("点击相册")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/photo').click()
        time.sleep(2)
        '''随机选择图片'''
        Photos = driver.find_elements_by_id('com.happyteam.dubbingshow:id/cb_select_tag')
        Select_photo = random.randint(0,int(len(Photos)))
        time.sleep(2)
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/cb_select_tag')[Select_photo].click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/next_step_tv').click()
        time.sleep(2)
        print('发送作品')
        Action.click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/film').click()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg'))
            time.sleep(2)
            '''随机选择作品'''
            Films = driver.find_elements_by_id('com.happyteam.dubbingshow:id/filmBg')
            Select_film = random.randint(0,int(len(Films)-2))
            driver.find_elements_by_id('com.happyteam.dubbingshow:id/filmBg')[Select_film].click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSelect').click()
        except(NoSuchElementException,TimeoutException):
            print("作品列表加载失败")
            time.sleep(1)
            driver.back()
        time.sleep(2)
        print('发红包')
        Action.click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/redpacket').click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/cash_num').send_keys("1")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/people_num').send_keys("1")
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/generate_red_packet').click()
        time.sleep(2)
        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(6)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/generate_red_packet')
            time.sleep(2)
            print("钻石不足")
            time.sleep(2)
            driver.back()
        except:
            pass
        time.sleep(2)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/red_packet')
            Reds = driver.find_elements_by_id('com.happyteam.dubbingshow:id/red_packet')
            time.sleep(2)
            driver.find_elements_by_id('com.happyteam.dubbingshow:id/red_packet')[-1].click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/open_red_packet_btn').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/user_head'))
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/red_packet_detail_close_btn').click()
            except(TimeoutException,NoSuchElementException):
                print("红包领取失败")
        except(NoSuchElementException,TimeoutException):
            print("无红包")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.find_elements_by_id('com.happyteam.dubbingshow:id/rl_all')[0].click()
        time.sleep(2)
        try:
            el3 = driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_space_manager_jump')
            el3.click()
            print("点击社团管理")
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/userHead'))
            except(TimeoutException,NoSuchElementException):
                pass
            time.sleep(2)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/content').click()
                print("显示有成员引导")
            except:
                pass
            time.sleep(2)
            print('点击编辑资料')
            driver.find_element_by_id('com.happyteam.dubbingshow:id/edit_profile').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/society_name'))
                Society_name = random.randint(0x4E00, 0x9FBF)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/society_name').send_keys(Society_name)
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/brief_content').send_keys("暂时没有写简介哦~")
                time.sleep(2)
                Tv_num = random.randint(1,20)
                for i in range(2):
                    driver.find_elements_by_id('com.happyteam.dubbingshow:id/tv')[Tv_num].click()
                    time.sleep(1)
                time.sleep(2)
                driver.back()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                print("社团资料修改失败")
            except(TimeoutException,NoSuchElementException):
                print("社团编辑资料界面加载失败")
                time.sleep(1)
                driver.back()
            time.sleep(2)
            Member_count = driver.find_element_by_id('com.happyteam.dubbingshow:id/member').text
            print(Member_count)
            print("点击添加社团成员")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/addfriend').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="配音秀官方号"]'))
                    driver.find_element_by_xpath('//android.widget.TextView[@text="配音秀官方号"]').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/complete').click()
                    try:
                        WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="邀请好友"]'))
                    except(TimeoutException,NoSuchElementException):
                        pass
                except(TimeoutException,NoSuchElementException):
                    print("搜索失败")
                    time.sleep(1)
                    driver.back()
            except(TimeoutException,NoSuchElementException):
                print("关注列表加载失败")
                time.sleep(1)
                driver.back()
            time.sleep(2)
            print("进入社团成员列表")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/member').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/shezhang'))
                time.sleep(1)
                print("添加成员")
                driver.find_element_by_id('com.happyteam.dubbingshow:id/addmembers').click()
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead'))
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("10251")
                    time.sleep(1)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSearch').click()
                    try:
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="配音秀官方号"]'))
                        driver.find_element_by_xpath('//android.widget.TextView[@text="配音秀官方号"]').click()
                        time.sleep(2)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/complete').click()
                        try:
                            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/shezhang'))
                        except(TimeoutException, NoSuchElementException):
                            print("添加失败")
                            time.sleep(1)
                            driver.back()
                    except(TimeoutException, NoSuchElementException):
                        print("搜索失败")
                        time.sleep(1)
                        driver.back()
                    time.sleep(2)
                    print("设置成员权限")
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/more').click()
                        time.sleep(2)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/check_box1').click()
                        time.sleep(2)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/check_box2').click()
                        time.sleep(2)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/save').click()
                        try:
                            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/more'))
                        except:
                            try:
                                driver.find_element_by_id('com.happyteam.dubbingshow:id/save')
                                time.sleep(1)
                                driver.back()
                            except:
                                pass
                    except:
                        print("非社长身份，未显示设置权限按钮")
                    time.sleep(2)
                    print("删除成员")
                    member_name = driver.find_elements_by_id('com.happyteam.dubbingshow:id/username')[1]
                    TouchAction(driver).long_press(member_name,2000).release().perform()
                    time.sleep(1)
                    driver.back()
                except(TimeoutException, NoSuchElementException):
                    print("成员列表加载失败")
            except(TimeoutException,NoSuchElementException):
                pass
            time.sleep(2)
            driver.back()
            time.sleep(2)
            print("点击编辑公告")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/edit_gonggao').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys('此社团无公告~')
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(2)

            print("点击作品管理")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/film_manage').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//android.widget.TextView[@text="你还没有社团空间作品哦"]')
                print("暂无社团作品")
            except:
                try:
                    WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/item_theme_bg'))
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/item_theme_bg').click()
                    try:
                        WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/gift'))
                        time.sleep(2)
                        driver.back()
                    except(TimeoutException,NoSuchElementException):
                        print("社团作品详情加载失败")
                    time.sleep(2)
                    print("作品置顶")
                    touch_film = driver.find_element_by_id('com.happyteam.dubbingshow:id/item_theme_bg')
                    TouchAction(driver).long_press(touch_film,2000).release().perform()
                    time.sleep(2)
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/zhiding').click()
                    except(TimeoutException,NoSuchElementException):
                        pass
                    time.sleep(2)

                    print("创建合辑")
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/addfilm').click()
                    time.sleep(2)
                    TouchAction(driver).press(x=0.5*x,y=0.802*y).release().perform()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("合辑1")
                    time.sleep(1)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/ok').click()
                    time.sleep(2)
                    try:
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/choice').click()
                        time.sleep(2)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/ok').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('//android.widget.TextView[@text="合辑"]').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('//android.widget.TextView[@text="合辑1"]').click()
                        time.sleep(2)
                        long_touch = driver.find_element_by_id('com.happyteam.dubbingshow:id/img')
                        TouchAction(driver).long_press(long_touch,3000).release().perform()
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_zhiding').click()
                        time.sleep(1)
                        shangyi_toast = driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_zhiding').text
                        print(shangyi_toast)
                        time.sleep(2)
                        TouchAction(driver).long_press(long_touch, 2500).release().perform()
                        time.sleep(1)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/tv_shanchu').click()
                        time.sleep(1)
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(5)
                        try:
                            driver.find_element_by_xpath('//android.widget.TextView[@text="合辑"]')
                            pass
                        except:
                            print("移除失败")
                            time.sleep(1)
                            driver.back()
                        time.sleep(2)
                        print("退出作品管理界面")
                        driver.back()
                    except:
                        print("暂无作品可添加~")
                        time.sleep(2)
                        driver.back()
                        print("退出社团作品列表界面")
                        driver.back()
                except(TimeoutException,NoSuchElementException):
                    print("作品列表加载失败")
                    time.sleep(1)
                    driver.back()
            time.sleep(2)

            print("申请蓝V")
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/apply_lv').click()
                time.sleep(2)
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/apply_lv')
                    print("蓝v界面跳转失败")
                except:
                    time.sleep(2)
                    driver.back()
            except:
                print("未显示蓝V申请入口")
            time.sleep(2)

            print("入社权限设置")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/society_apply_jurisdiction').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/modify').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/content').send_keys("闲人免进！")
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/addFilm').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/addSource').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/all').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/apply').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/none').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/save').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="管理社团"]'))
            except(TimeoutException,NoSuchElementException):
                time.sleep(1)
                driver.back()
                time.sleep(1)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)

            print("社团消息免打扰")
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_push').click()
            time.sleep(6)
            try:
                driver.find_element_by_id('com.happyteam.dubbingshow:id/gold_match')
                print("点击社团财富")
                try:
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gold_match').click()
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/distribution_diamond'))
                    print("分配钻石")
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/distribution_diamond').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/username').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gold_count').send_keys("1")
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/remark').send_keys("测试")
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/sure').click()
                    try:
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="社团财富"]'))
                        pass
                    except(NoSuchElementException, TimeoutException):
                        print("钻石分配失败")
                        time.sleep(1)
                        driver.back()
                    time.sleep(2)
                    print("分配金币")
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/distribution_gold').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/username').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gold_count').send_keys("1")
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/remark').send_keys("测试")
                    time.sleep(2)
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/sure').click()
                    try:
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//android.widget.TextView[@text="社团财富"]'))
                        pass
                    except(NoSuchElementException, TimeoutException):
                        print("金币分配失败")
                        time.sleep(1)
                        driver.back()
                    time.sleep(2)
                    driver.back()
                    time.sleep(2)
                except(NoSuchElementException, TimeoutException):
                    print("社团财富界面加载失败")
                    time.sleep(1)
                    driver.back()
                time.sleep(2)
                driver.swipe(0.5*x,0.8*y,0.5*x,0.4*y,300)
                print("社团钱包")
                driver.find_element_by_id('com.happyteam.dubbingshow:id/meney').click()
                try:
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/distribution_gold'))
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/distribution_gold').click()
                    time.sleep(2)
                    driver.back()
                    time.sleep(2)
                    driver.back()
                except(TimeoutException, NoSuchElementException):
                    print("社团钱包界面加载失败")
                    time.sleep(1)
                    driver.back()
                time.sleep(2)

                print("作品下载设置开关")
                driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_load').click()
                time.sleep(5)
            except(TimeoutException,NoSuchElementException):
                print("非社长身份，未显示社团财富、社团钱包、社团消息设置入口")
            time.sleep(2)
            print("退出社团管理界面")
            driver.back()
            time.sleep(2)
        except(NoSuchElementException,TimeoutException):
            print("未显示社团管理按钮")
        time.sleep(2)

        print("点击空间按钮")
        Zoom = driver.find_element_by_id('com.happyteam.dubbingshow:id/btn_space_jump')
        Zoom.click()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/membercount'))
            driver.find_element_by_id('com.happyteam.dubbingshow:id/fanscount').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/username'))
                time.sleep(2)
                driver.back()
            except(TimeoutException,NoSuchElementException):
                print("粉丝列表加载失败")
                time.sleep(2)
                driver.back()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/membercount').click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/name'))
                time.sleep(2)
                driver.back()
            except(TimeoutException,NoSuchElementException):
                print("成员列表加载失败")
                time.sleep(2)
                driver.back()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnMember').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnCollect').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnFilm').click()
            time.sleep(2)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/photo')
            time.sleep(2)
            driver.back()
        except(NoSuchElementException,TimeoutException):
            print("空间加载失败")
            time.sleep(1)
            driver.back()
        time.sleep(2)

        print("点击活动")
        driver.find_element_by_xpath('//android.widget.TextView[@text="活动"]').click()
        try:
            WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/task_box'))
            driver.find_elements_by_id('com.happyteam.dubbingshow:id/task_box')[0].click()
            try:
                WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg'))
                time.sleep(2)
                driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg').click()
                try:
                    WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('com.happyteam.dubbingshow:id/gift'))
                    driver.keyevent(3)
                    time.sleep(2)
                    driver.launch_app()
                    time.sleep(2)
                    print("送礼两次")
                    driver.find_element_by_id('com.happyteam.dubbingshow:id/gift').click()
                    time.sleep(2)
                    for i in range(2):
                        driver.find_element_by_id('com.happyteam.dubbingshow:id/confirm').click()
                        time.sleep(4)
                    time.sleep(2)
                    for i in range(3):
                        driver.back()
                        time.sleep(2)
                except(TimeoutException,NoSuchElementException):
                    print("视频详情加载失败")
                    time.sleep(2)
                    driver.back()
                print("下拉刷新")
                driver.swipe(0.5 * x, 0.22 * y,0.5 * x, 0.83 * y,  300)
                time.sleep(2)
            except(TimeoutException,NoSuchElementException):
                try:
                    driver.find_element_by_xpath('//android.widget.TextView[@text="还没有任何作品哦~"]')
                    time.sleep(1)
                    tip_film = driver.find_element_by_xpath('//android.widget.TextView[@text="还没有任何作品哦~"]').text
                    print(tip_film)
                except:
                    pass
            time.sleep(2)
        except(TimeoutException,NoSuchElementException):
            print("活动列表界面加载失败")

        print("点击榜单")
        driver.find_element_by_xpath('//android.widget.TextView[@text="榜单"]').click()
        time.sleep(3)
        bangdan = driver.find_elements_by_id('com.happyteam.dubbingshow:id/look_rank')
        for i in range(len(bangdan)):
            driver.find_elements_by_id('com.happyteam.dubbingshow:id/look_rank')[i].click()
            try:
                WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//android.widget.TextView[@text="贡献榜"]'))
                driver.find_element_by_xpath('//android.widget.TextView[@text="活动榜"]').click()
                time.sleep(2)
                driver.swipe(0.5 * x, 0.8 * y, 0.5 * x, 0.4 * y, 300)
                driver.find_element_by_xpath('//android.widget.TextView[@text="作品榜"]').click()
                time.sleep(2)
                driver.back()
            except(NoSuchElementException,TimeoutException):
                time.sleep(2)
                driver.back()
            time.sleep(2)
        driver.back()
        time.sleep(2)


        print("点击社团更多")
        try:
            Corp_count = driver.find_element_by_id('com.happyteam.dubbingshow:id/society_count').text
            print(Corp_count)
            driver.find_element_by_id('com.happyteam.dubbingshow:id/society_count').click()
            time.sleep(2)
            print("上滑列表")
            for i in range(5):
                driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
                time.sleep(1)
        except:
            pass

    '''推荐社团'''
    def Corp_Recommend(self):
        print("上滑列表")
        driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
        time.sleep(2)
        print("点击进入社团空间")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/userhead').click()
        try:
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/membercount'))
            time.sleep(2)
            driver.back()
        except(TimeoutException, NoSuchElementException):
            print("空间加载失败")
            time.sleep(2)
            driver.back()
        time.sleep(2)
        print("点击加入按钮")
        driver.find_element_by_id('com.happyteam.dubbingshow:id/join').click()
        time.sleep(2)
        try:
            driver.find_element_by_id('com.happyteam.dubbingshow:id/btnReload')
            print("申请入社界面加载失败")
            time.sleep(2)
            driver.back()
        except:
            time.sleep(2)
            driver.back()
        time.sleep(2)
        print("上滑列表")
        for i in range(5):
            driver.swipe(0.5 * x, 0.83 * y, 0.5 * x, 0.22 * y, 300)
            time.sleep(2)


if __name__=="__main__":
    Tiezi_home = Home_Circle()
    Soc = Community()
    Corp = Corporation()
    Tiezi_home.History()
    Tiezi_home.Topic_search()
    Tiezi_home.Circle_home()
    Tiezi_home.Topic_detail()
    Tiezi_home.Posting()
    # Soc.Communitys()
    # Corp.Corp_Home()
    # Corp.Corp_Search()
    # Corp.Corp_My()
    # Corp.Corp_Recommend()
