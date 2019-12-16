# author：Alvin
# Time  ：2019年03月26日
# coding = utf-8
import random
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
# 获取当前项目的根路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
import Peiyinxiu_Client.API
from pprint import pprint
from math import ceil
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()

'''个人空间'''
class My_Zoom():
    '''个人等级'''
    def __init__(self):
        self.API = Peiyinxiu_Client.API

    def Grade(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/task_box')
            print('===开始===')
        except:
            print('应用启动失败')
        OP.find_id('com.happyteam.dubbingshow:id/mineTab').click()
        time.sleep(2)
        name = OP.find_id('com.happyteam.dubbingshow:id/username').text
        check_name = "撸串"
        if name == check_name:
            pass
        else:
            print('测试账号错误，请切换！！')
            device().close_app()
        time.sleep(2)
        #获取关注、粉丝、作品、求合作、素材、更多tab中显示的数量
        Follows_count = OP.find_id('com.happyteam.dubbingshow:id/followed_count').text
        Follows_average = ceil(int(Follows_count))
        time.sleep(1)
        Fans_count = OP.find_id('com.happyteam.dubbingshow:id/fans_count').text
        Fans_average = ceil(int(Fans_count))
        time.sleep(1)
        production_count = OP.find_id('com.happyteam.dubbingshow:id/production_count').text
        Production_average = ceil(int(production_count))
        time.sleep(1)
        Cooperation_count = OP.find_id('com.happyteam.dubbingshow:id/invitation_count').text
        Cooperation_average = ceil(int(Cooperation_count))
        time.sleep(1)
        Sources_count = OP.find_id('com.happyteam.dubbingshow:id/source_count').text
        Sources_average = ceil(int(Sources_count))
        time.sleep(1)
        More_count = OP.find_id('com.happyteam.dubbingshow:id/transpond_count').text
        More_average = ceil(int(More_count))
        time.sleep(2)
        # print("点击头像进入个人空间")
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/content')
            # print("空间加载成功")
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btn_reload').click()
                OP.wait_id('com.happyteam.dubbingshow:id/content')
            except:
                pass
        time.sleep(2)
        Follow_list = []
        for i in range(1,Fans_average+1):
            count = self.API.Person_Follow('16685645',i)
            Follow_list.append(count)
        Follow_sum = 0
        for x in Follow_list:
            Follow_sum += x
        print(Follow_sum)
        # print("点击等级")
        OP.find_id('com.happyteam.dubbingshow:id/img_level').click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/tv_perform')
            yanyi = OP.find_id('com.happyteam.dubbingshow:id/tv_perform').text
            time.sleep(2)
            Y_Empirical_value = OP.find_id('com.happyteam.dubbingshow:id/tv_perform_max').text
            time.sleep(2)
            Y_My_experience = OP.find_id('com.happyteam.dubbingshow:id/tv_progress').text
            print(yanyi, "升级所需经验值:", Y_Empirical_value, "当前经验值:", Y_My_experience)
            zhizhuo = OP.find_id('com.happyteam.dubbingshow:id/tv_script').text
            time.sleep(2)
            Z_Empirical_value = OP.find_id('com.happyteam.dubbingshow:id/tv_script_max').text
            time.sleep(2)
            Z_My_experience = OP.find_id('com.happyteam.dubbingshow:id/tv_progress1').text
            print(zhizhuo, "升级所需经验值:", Z_Empirical_value, "当前经验值:", Z_My_experience)
            time.sleep(2)
            OP.back()
        except:
            OP.back()

    '''相册'''
    def photo(self):
        print("点击相册")
        OP.find_id('com.happyteam.dubbingshow:id/photo').click()
        time.sleep(5)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/img')
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.find_id('android:id/message')
                print("网络异常！")
                time.sleep(2)
                OP.back()
                time.sleep(2)
                OP.back()
            except:
                print("暂未添加照片")
                time.sleep(2)
                OP.back()
        time.sleep(4)

    '''个人资料'''
    def person_info(self):
        print("个人资料")
        OP.find_id('com.happyteam.dubbingshow:id/imgEdit').click()
        time.sleep(2)
        print("修改简介")
        area_num = random.randint(0, 8)
        OP.find_id('com.happyteam.dubbingshow:id/tv_sign').send_keys("不用看了！什么有没有写！", area_num)
        time.sleep(2)
        print("修改性别")
        OP.find_id('com.happyteam.dubbingshow:id/userinfo_gender').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.802 * y).release().perform()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/userinfo_gender').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.87 * y).release().perform()
        time.sleep(2)
        print("修改地区")
        OP.find_id('com.happyteam.dubbingshow:id/userinfo_area').click()
        time.sleep(2)
        OP.find_ids('com.happyteam.dubbingshow:id/name')[area_num].click()
        time.sleep(2)
        print("生日")
        OP.find_id('com.happyteam.dubbingshow:id/userinfo_time').click()
        time.sleep(3)
        OP.find_id('com.happyteam.dubbingshow:id/tv_ensure').click()
        time.sleep(2)
        username = OP.find_id('com.happyteam.dubbingshow:id/et_nickname').text
        time.sleep(2)
        userid = OP.find_id('com.happyteam.dubbingshow:id/tv_id').text
        time.sleep(2)
        usersign = OP.find_id('com.happyteam.dubbingshow:id/tv_sign').text
        time.sleep(2)
        Gender = OP.find_id('com.happyteam.dubbingshow:id/tv_gender').text
        time.sleep(2)
        Aera = OP.find_id('com.happyteam.dubbingshow:id/tv_area').text
        time.sleep(2)
        Birthday = OP.find_id('com.happyteam.dubbingshow:id/tv_time').text
        print(username, userid, usersign, Gender, Aera, Birthday)
        print("保存修改")
        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
        try:
            save_toast = OP.wait_toast('//android.widget.Toast')
            print(save_toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep((2))
        OP.back()
        time.sleep(2)
        identity = OP.find_id('com.happyteam.dubbingshow:id/vip_description').text
        print(identity)
        time.sleep(2)

    '''其它信息'''
    def other_info(self):
        fans = OP.find_id('com.happyteam.dubbingshow:id/fanscount').text
        time.sleep(2)
        print(fans)
        time.sleep(2)
        '''点击进入粉丝列表'''
        OP.find_id('com.happyteam.dubbingshow:id/fanscount').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            print('会员涨粉')
            OP.find_id('com.happyteam.dubbingshow:id/iwant').click()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit')
                content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                print(content)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/now_money_month')
                    print("未购买会员")
                    time.sleep(2)
                    OP.back()
                except:
                    pass
            time.sleep(2)
            fans_count = OP.find_ids('com.happyteam.dubbingshow:id/username')
            fans_list = []
            for fan in range(len(fans_count)):
                fans_user_name = OP.find_ids('com.happyteam.dubbingshow:id/username')[fan].text
                fans_list.append(fans_user_name)
                time.sleep(1)
            print(fans_list)
            fans_user_name = OP.find_ids('com.happyteam.dubbingshow:id/username')[1].text
            OP.find_ids('com.happyteam.dubbingshow:id/username')[1].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                print("空间加载成功")
                fans_zoom_user_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                if fans_user_name == fans_zoom_user_name:
                    pass
                else:
                    print("粉丝列表用户名与空间用户名不一致，请检查！")
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("点击关注")
            OP.find_id('com.happyteam.dubbingshow:id/status_icon').click()
            time.sleep(5)
            OP.back()
        except(TimeoutException, NoSuchElementException):
            print("粉丝列表加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(2)
        '''点击进入关注列表'''
        follows = OP.find_id('com.happyteam.dubbingshow:id/followcount').text
        time.sleep(2)
        print(follows)
        OP.find_id("com.happyteam.dubbingshow:id/followcount").click()
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            follow_count = OP.find_ids('com.happyteam.dubbingshow:id/username')
            '''获取关注用户信息'''
            Follow_list = []
            for follow in range(len(follow_count)):
                follow_user_name = OP.find_ids('com.happyteam.dubbingshow:id/username')[follow].text
                Follow_list.append(follow_user_name)
                time.sleep(1)
            print(Follow_list)
            time.sleep(2)
            Follow_user_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
            time.sleep(2)
            OP.find_ids('com.happyteam.dubbingshow:id/username')[0].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                print("空间加载成功")
                follow_zoom_user_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                if Follow_user_name == follow_zoom_user_name:
                    pass
                else:
                    print("关注列表用户名与空间用户名不一致，请检查！")
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("点击关注")
            OP.find_id('com.happyteam.dubbingshow:id/status_icon').click()
            time.sleep(5)
            OP.back()
        except(TimeoutException, NoSuchElementException):
            print("关注列表加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(2)
        societys = OP.find_id('com.happyteam.dubbingshow:id/societyCount').text
        time.sleep(2)
        print(societys)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/societyCount').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/user_image')
            socitey_count = OP.find_ids('com.happyteam.dubbingshow:id/userName')
            time.sleep(2)
            '''获取社团信息'''
            soc_list =[]
            for i in range(len(socitey_count)):
                socitey_name = OP.find_ids('com.happyteam.dubbingshow:id/userName')[i].text
                soc_list.append(socitey_name)
                time.sleep(1)
            print(soc_list)
            time.sleep(2)
            OP.find_ids('com.happyteam.dubbingshow:id/userName')[0].click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/membercount')
                print("空间加载成功")
                zoom_society_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
                print(zoom_society_name)
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("点击关注")
            OP.find_id('com.happyteam.dubbingshow:id/status_icon').click()
            try:
                OP.wait_toast('//android.widget.Toast')
                follow_toast = OP.find_xpath('//android.widget.Toast').text
                print(follow_toast)
            except(NoSuchElementException, TimeoutException):
                pass
            time.sleep(2)
            OP.back()
        except(TimeoutException, NoSuchElementException):
            print("社团列表加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(2)

    '''作品列表信息'''
    def works_info(self):
        print("全部作品")
        works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        print(works)
        time.sleep(2)
        title_name = OP.find_id('com.happyteam.dubbingshow:id/title').text
        work_look = OP.find_id('com.happyteam.dubbingshow:id/look').text
        work_gift = OP.find_id('com.happyteam.dubbingshow:id/like').text
        print('作品名称:',title_name,'作品播放量:',work_look,'作品礼物值:',work_gift)
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/privacytype')
            print('私密作品')
            OP.find_id('com.happyteam.dubbingshow:id/privacytype').click()
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            print("作品公开、私密")
            OP.find_id('com.happyteam.dubbingshow:id/setting').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.73 * y).release().perform()
            time.sleep(3)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except:
                pass
        except:
            OP.find_id('com.happyteam.dubbingshow:id/filmBg1').click()
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
        time.sleep(2)
        old_work_name = OP.find_id('com.happyteam.dubbingshow:id/tv_video_detail_title').text
        print(old_work_name)
        print("点击设置按钮")
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/setting').click()
        time.sleep(2)
        print("点击修改资料")
        TouchAction(devc).press(x=0.5 * x, y=0.74 * y).release().perform()
        time.sleep(4)
        try:
            OP.find_xpath('会员中心')
            print("未购买会员,无法修改作品名")
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.find_xpath('修改作品资料')
                time.sleep(2)
                print('更换封面')
                OP.find_id('com.happyteam.dubbingshow:id/btn_setting_cover_tip').click()
                time.sleep(2)
                TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/photo_wall_item_photo')
                    OP.find_id('com.happyteam.dubbingshow:id/photo_wall_item_photo').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                except(NoSuchElementException, TimeoutException):
                    OP.back()
                time.sleep(2)
                worker_name = OP.find_id('com.happyteam.dubbingshow:id/title').text
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/title').clear()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/title').send_keys(worker_name, "(修)")
                time.sleep(2)
                print('点击私密开关')
                OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
                time.sleep(3)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/tag_tv')
                    print('添加标签')
                    OP.find_id('com.happyteam.dubbingshow:id/tag_text').click()
                    time.sleep(5)
                    OP.find_id('com.happyteam.dubbingshow:id/tv').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                except(NoSuchElementException, TimeoutException):
                    pass
                time.sleep(2)
                print('保存修改')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/uploadbtn').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    new_works_name = OP.find_id('com.happyteam.dubbingshow:id/tv_video_detail_title').text
                    print(new_works_name)
                except(NoSuchElementException, TimeoutException):
                    OP.back()
            except(TimeoutException, NoSuchElementException):
                pass
        time.sleep(2)
        print("关闭、开启评论")
        OP.find_id('com.happyteam.dubbingshow:id/setting').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.81 * y).release().perform()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/txtContent')
            comment_tip = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
            print(comment_tip)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(5)
            OP.find_id('com.happyteam.dubbingshow:id/comment').click()
            time.sleep(5)
            try:
                OP.find_xpath('作者已关闭评论，当前评论隐藏')
                print("已关闭评论")
                time.sleep(2)
                OP.back()
            except:
                print("已开启评论")
                time.sleep(2)
                OP.back()
        except(TimeoutException, NoSuchElementException):
            time.sleep(2)
            OP.back()
        time.sleep(2)
        print('退出视频详情')
        OP.back()
        time.sleep(4)
        OP.swip_down()
        time.sleep(3)
        print("长按置顶")
        el = OP.find_id('com.happyteam.dubbingshow:id/filmBg1')
        TouchAction(devc).long_press(el).wait(2000).perform()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.81 * y).release().perform()
        try:
            Toast = OP.wait_toast('//android.widget.Toast')
            print(Toast)
            time.sleep(1)
            check1 = '配音秀：私密作品不可以置顶哦~'
            check2 = '私密作品不可以置顶哦~'
            if Toast == check1:
                OP.back()
            elif Toast == check2:
                OP.back()
            else:
                pass
        except(NoSuchElementException, TimeoutException):
            pass
        time.sleep(2)
        print("作品删除")
        Delete_Before = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        el = OP.find_id('com.happyteam.dubbingshow:id/filmBg1')
        TouchAction(devc).long_press(el).wait(2000).perform()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        except:
            pass
        time.sleep(5)
        OP.swip_down()
        time.sleep(4)
        Delete_After = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        time.sleep(2)
        print("删除前：", Delete_Before, "删除后：", Delete_After)
        time.sleep(2)

        print("单人作品")
        OP.find_id('com.happyteam.dubbingshow:id/head_single_film').click()
        OP.wait_id('com.happyteam.dubbingshow:id/filmBg1')
        single_works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        print(single_works)
        time.sleep(2)

        print("合作作品")
        OP.find_id('com.happyteam.dubbingshow:id/head_cooper_film').click()
        OP.wait_id('com.happyteam.dubbingshow:id/filmBg1')
        cooper_works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        print(cooper_works)
        time.sleep(2)

        print("创建合辑")
        OP.find_id('com.happyteam.dubbingshow:id/btnRight').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/content').send_keys("一个合辑")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/ok').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/choice')
            OP.find_id('com.happyteam.dubbingshow:id/choice').click()
            time.sleep(2)
            OP.find_xpath('完成').click()
            time.sleep(2)
        except:
            print("无可添加作品")
            OP.back()
        time.sleep(2)

        print("合辑列表")
        OP.find_id('com.happyteam.dubbingshow:id/head_reprint_film').click()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/noworks_prompt')
            print('暂无合辑')
        except:
            pass
        time.sleep(2)
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
            OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/img')
                OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/choice').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                    try:
                        add_works_toast = OP.wait_toast('//android.widget.Toast')
                        print(add_works_toast)
                    except:
                        pass
                    time.sleep(2)
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/tv_right')
                        print("合辑作品添加失败")
                        time.sleep(2)
                        OP.back()
                    except:
                        pass
                except(TimeoutException, NoSuchElementException):
                    print("无作品可添加")
                    time.sleep(2)
                    OP.back()
                workes = OP.find_ids('com.happyteam.dubbingshow:id/img')
                print("作品数量:",len(workes))
                time.sleep(2)
                long_press = OP.find_id('com.happyteam.dubbingshow:id/img')
                TouchAction(devc).long_press(long_press).wait(2000).perform()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/tv_zhiding').click()
                time.sleep(5)
                long_press = OP.find_id('com.happyteam.dubbingshow:id/img')
                TouchAction(devc).long_press(long_press).wait(2000).perform()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/tv_shanchu').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(2)
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except:
                    pass
                time.sleep(2)
                OP.back()
            except(TimeoutException, NoSuchElementException):
                print("合辑详情加载失败")
                time.sleep(2)
        except(TimeoutException, NoSuchElementException):
            print("合辑列表为空")
        time.sleep(2)
        print('个人空间界面合辑删除')
        time.sleep(1)
        try:
            Delete_reprint = OP.find_id('com.happyteam.dubbingshow:id/filmBg')
            TouchAction(devc).long_press(Delete_reprint).wait(2000).perform()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(3)
            OP.swip_right()
            time.sleep(4)
            reprint_works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
            print(reprint_works)
            time.sleep(2)
        except:
            pass

        print("社团作品")
        OP.find_id('com.happyteam.dubbingshow:id/head_coor_film').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/filmBg1')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/filmBg1').click()
            OP.wait_id('com.happyteam.dubbingshow:id/gift')
            time.sleep(2)
            OP.back()
        except:
            try:
                OP.find_xpath('你还没有参与制作社团作品喔~')
                print("社团作品为空")
            except:
                pass
        time.sleep(2)
        coor_works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
        print(coor_works)
        time.sleep(2)

        print("求合作")
        qiuhezuo = OP.find_id('com.happyteam.dubbingshow:id/coor_text').text
        print(qiuhezuo)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/coor_text').click()
        time.sleep(4)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/islook').click()
            print("预览视频")
            time.sleep(10)
            OP.back()
            time.sleep(2)
            print("点击配音按钮")
            OP.find_id('com.happyteam.dubbingshow:id/layout').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                time.sleep(2)
                OP.back()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            except(NoSuchElementException, TimeoutException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/layout')
                    print("素材下载失败！！")
                except:
                    pass
            time.sleep(2)
            qiuhezuo_Invitation = OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image')
            TouchAction(devc).long_press(qiuhezuo_Invitation).wait(2000).perform()
            time.sleep(2)
            print("邀请好友")
            TouchAction(devc).press(x=0.5 * x, y=0.656 * y).release().perform()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/socialstatus')
                OP.find_ids('com.happyteam.dubbingshow:id/socialstatus')[0].click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/reprint').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/layout')
                except(NoSuchElementException, TimeoutException):
                    print("转发失败")
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.back()
            except(TimeoutException, NoSuchElementException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("公开、私密求合作")
            qiuhezuo_open = OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image')
            TouchAction(devc).long_press(qiuhezuo_open).wait(2000).perform()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.729 * y).release().perform()
            try:
                open_toast = OP.wait_toast('//android.widget.Toast')
                print(open_toast)
            except(NoSuchElementException, TimeoutException):
                try:
                    OP.find_xpath('会员中心')
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.back()
                except:
                    pass
            time.sleep(2)

            print("作品置顶")
            qiuhezuo_zhiding = OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image')
            TouchAction(devc).long_press(qiuhezuo_zhiding).wait(2000).perform()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.809 * y).release().perform()
            try:
                zhiding_toast = OP.wait_toast('//android.widget.Toast')
                toast_check = "置顶成功"
                if zhiding_toast == toast_check:
                    print(zhiding_toast)
                else:
                    print(zhiding_toast)
                    time.sleep(2)
                    OP.back()
            except:
                pass
            time.sleep(2)

            print("求合作删除")
            qiuhezuo_delete = OP.find_id('com.happyteam.dubbingshow:id/item_sh_cooperate_article_image')
            TouchAction(devc).long_press(qiuhezuo_delete).wait(2000).perform()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.885 * y).release().perform()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)
        except:
            print("求和作列表为空")

        print("素材")
        time.sleep(2)
        '''素材tab'''
        source_count = OP.find_id('com.happyteam.dubbingshow:id/source_text').text
        print(source_count)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/source_text').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/imgSource')
            OP.find_id('com.happyteam.dubbingshow:id/imgSource').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/shouchang_tv_fake')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                try:
                    Reload = OP.find_id('com.happyteam.dubbingshow:id/Reload')
                    if Reload == True:
                        Reload.click()
                        time.sleep(10)
                        OP.back()
                    else:
                        pass
                except:
                    pass
            time.sleep(2)
            print("点击配音")
            OP.find_id('com.happyteam.dubbingshow:id/dubbing_container').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/roleall')
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                except:
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/action')
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    except:
                        pass
            except(NoSuchElementException, TimeoutException):
                pass
        except(NoSuchElementException, TimeoutException):
            '''素材列表为空，显示上传素材按钮'''
            Source_up = OP.find_id('com.happyteam.dubbingshow:id/noworks_submit')
            if Source_up == True:
                print("素材列表为空")
            else:
                pass
        time.sleep(2)
        print("更多")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/more_text').click()
        time.sleep(5)
        print("转发")
        Forward = OP.find_id('com.happyteam.dubbingshow:id/head_reprint_more')
        Forward.click()
        try:
            '''作品封面'''
            OP.wait_id('com.happyteam.dubbingshow:id/item_theme_bg')
            time.sleep(2)
            Works_cover = OP.find_id('com.happyteam.dubbingshow:id/item_theme_bg')
            Works_cover.click()
            try:
                Toast = OP.wait_toast('//android.widget.Toast')
                print(Toast)
                time.sleep(2)
            except:
                '''视频详情中的礼物按钮'''
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(5)
                OP.back()
                time.sleep(2)
                print("删除转发作品")
                TouchAction(devc).long_press(Works_cover).wait(2000).perform()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(2)
        except(NoSuchElementException, TimeoutException):
            try:
                OP.find_xpath('你还没有转发过作品~首页有很多大神哦~"')
                print("转发作品为空")
            except:
                pass
        OP.swip_down()
        time.sleep(4)
        Forwards = OP.find_id('com.happyteam.dubbingshow:id/more_text').text
        print(Forwards)
        time.sleep(2)

        '''帖子'''
        Post = OP.find_id('com.happyteam.dubbingshow:id/head_post_more')
        Post.click()
        try:
            OP.wait_download('com.happyteam.dubbingshow:id/action')
            OP.swip_up()
            time.sleep(2)
            '''帖子内容'''
            content = OP.find_id('com.happyteam.dubbingshow:id/content').text
            print(content)
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/comment').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tag')
            except(TimeoutException, NoSuchElementException):
                pass
            time.sleep(2)
            print("点击帖子话题标签")
            for i in range(3):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/tag').click()
                    break
                except:
                    OP.swip_up()
                time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                '''用户头像'''
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/userhead')
                    print("话题详情加载成功")
                    time.sleep(2)
                    OP.back()
                except:
                    print("话题详情加载失败")
                    time.sleep(2)
                    OP.back()
            except(TimeoutException, NoSuchElementException):
                pass
            time.sleep(2)
            OP.back()
            time.sleep(4)

            print("帖子转发")
            OP.swip_down()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/action').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5 * x, y=0.802 * y).release().perform()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                try:
                    OP.find_xpath('群聊')
                    OP.find_xpath('群聊').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                    OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                    time.sleep(5)
                    OP.back()
                except:
                    print("未显示群聊选项")
                    time.sleep(2)
                    OP.back()
            except(NoSuchElementException, TimeoutException):
                print("关注列表加载失败")
                time.sleep(2)
                OP.back()
            time.sleep(4)
        except(TimeoutException, NoSuchElementException):
            print("帖子列表为空")
        time.sleep(2)
        for i in range(3):
            OP.swip_up()
            time.sleep(2)
        time.sleep(4)
        Post_count = OP.find_id('com.happyteam.dubbingshow:id/more_text').text
        print(Post_count)
        time.sleep(2)

        print("语聊")
        Live = OP.find_id('com.happyteam.dubbingshow:id/head_live_more')
        Live.click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/item_image')
            '''保存的语聊封面'''
            Live_cover = OP.find_id('com.happyteam.dubbingshow:id/item_image')
            Live_cover.click()
            time.sleep(5)
            OP.back()
            time.sleep(2)
        except:
            try:
                OP.find_xpath('你还未保存过任何聊天室的音频哦~')
            except:
                pass
        time.sleep(2)
        Live_count = OP.find_id('com.happyteam.dubbingshow:id/more_text').text
        print(Live_count)
        time.sleep(2)
        print("退出个人空间")
        OP.back()

'''达人、CP、会员'''
class My_identity():
        '''会员'''
        def VIP(self):
            '''获取用户ID'''
            User_id = OP.find_id('com.happyteam.dubbingshow:id/tv_uid').text
            uid = User_id[4:]
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/img_vip').click()
            time.sleep(5)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/time')
                Vip_time = OP.find_id('com.happyteam.dubbingshow:id/time').text
                print(Vip_time)
            except:
                pass
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/money_month').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/money_season').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/money_year').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/renew').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/close_icon').click()
            time.sleep(2)
            print('赠送会员')
            OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/filter_edit')
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/send')
                    users_name = OP.find_ids('com.happyteam.dubbingshow:id/name')
                    user_list = []
                    for name in range(len(users_name)):
                        name = OP.find_ids('com.happyteam.dubbingshow:id/name')[name].text
                        user_list.append(name)
                        time.sleep(0.5)
                    pprint(user_list)
                    time.sleep(2)
                    print('点击进入个人空间')
                    OP.find_id('com.happyteam.dubbingshow:id/user_head').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                        time.sleep(2)
                        OP.back()
                    except:
                        print('空间加载失败')
                        time.sleep(1)
                        OP.back()
                    time.sleep(2)
                    print('选择我的关注列表用户赠送')
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/send').click()
                    time.sleep(2)
                    send_name = OP.find_id('com.happyteam.dubbingshow:id/user_name').text
                    print(send_name)
                    time.sleep(1)
                    month = OP.find_id('com.happyteam.dubbingshow:id/tv_money_month').text
                    money_month = OP.find_id('com.happyteam.dubbingshow:id/now_money_month').text
                    season = OP.find_id('com.happyteam.dubbingshow:id/now_money_season').text
                    season_Original_price = OP.find_id('com.happyteam.dubbingshow:id/original_money_season').text
                    season_money = OP.find_id('com.happyteam.dubbingshow:id/tv_money_season').text
                    year_money = OP.find_id('com.happyteam.dubbingshow:id/now_money_year').text
                    year = OP.find_id('com.happyteam.dubbingshow:id/tv_money_year').text
                    year_oroginal_price = OP.find_id('com.happyteam.dubbingshow:id/original_money_year').text
                    print(month,":",money_month,";",season_money,':',season_Original_price,season,year,':',year_oroginal_price,year_money)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/now_money_year').click()
                    time.sleep(2)
                    print('选择包年，点击赠送')
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/renew').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/money').click()
                    try:
                        toast = OP.wait_toast('//android.widget.Toast')
                        tip = "钻石不足，请在我的财富进行充值钻石"
                        if tip == toast:
                            print(tip)
                            time.sleep(1)
                            '''收起支付弹窗'''
                            OP.back()
                            time.sleep(2)
                            '''收起会员价格列表'''
                            OP.back()
                        else:
                            pass
                    except:
                        pass
                except:
                    print('我的关注列表为空')
                time.sleep(2)
                print('搜索用户')
                OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys(uid)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/name')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/send')
                        print('搜索当前账号依然显示有赠送按钮')
                    except:
                        pass
                except:
                    print('搜索失败')
                time.sleep(2)
                print('搜索其它用户')
                OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys('10251')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/name')
                    name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/send').click()
                    Send_name = OP.find_id('com.happyteam.dubbingshow:id/user_name').text
                    print(name,Send_name)
                    time.sleep(2)
                    OP.back()
                    '''退出赠送界面'''
                    time.sleep(2)
                    OP.back()
                except:
                    print('搜索失败')
                    time.sleep(1)
                    OP.back()
            except:
                print('赠送用户列表加载失败')
                time.sleep(2)
                OP.back()
            time.sleep(2)
            print("查看会员特权")
            OP.swip_up()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/photo_frame').click()
                tequan1 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan1)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/upgrade').click()
                tequan2 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan2)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/definition').click()
                tequan3 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan3)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            OP.swip_up()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/exposure').click()
                tequan4 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan4)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            OP.swip_up()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/effects').click()
                tequan5 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan5)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/transcoding').click()
                tequan6 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan6)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/film').click()
                tequan6 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan6)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/draft').click()
                tequan6 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan6)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            OP.swip_up()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/lianmai').click()
                tequan6 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan6)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/coor').click()
                tequan6 = OP.find_id('com.happyteam.dubbingshow:id/content').text
                print(tequan6)
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            print("退出会员中心")
            OP.back()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/right_huiyuan').click()
                print("此用户未购买会员，头像右侧显示有会员箭标")
                time.sleep(5)
                OP.back()
            except:
                pass
            time.sleep(2)

        '''CP'''
        def CP(self):
            OP.find_id('com.happyteam.dubbingshow:id/img_cp').click()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/search_id').send_keys("10251")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/submit').click()
                time.sleep(5)
                Cp_user_name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                print(Cp_user_name)
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/submit').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(2)
                CP_tip = OP.find_id('com.happyteam.dubbingshow:id/wait').text
                print(CP_tip)
                time.sleep(2)
                OP.back()
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/reset').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/search_id').send_keys("10251")
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/submit').click()
                    time.sleep(5)
                    Cp_user_name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                    print(Cp_user_name)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/submit').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                    CP_tip = OP.find_id('com.happyteam.dubbingshow:id/wait').text
                    print(CP_tip)
                    time.sleep(2)
                    OP.back()
                except:
                    pass
            time.sleep(2)

        '''我的界面中点击tab跳转'''

        def Jump(self):
            OP.find_xpath('作品').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                Zoom_works = OP.find_id('com.happyteam.dubbingshow:id/single_text').text
                print(Zoom_works)
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.find_xpath('求合作').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                Zoom_qiuhezuo = OP.find_id('com.happyteam.dubbingshow:id/coor_text').text
                print(Zoom_qiuhezuo)
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.find_xpath('素材').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                Zoom_source = OP.find_id('com.happyteam.dubbingshow:id/source_text').text
                print(Zoom_source)
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.find_xpath('更多').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/tv_level')
                Zoom_more = OP.find_id('com.happyteam.dubbingshow:id/more_text').text
                print(Zoom_more)
                time.sleep(2)
                OP.back()
            except(NoSuchElementException, TimeoutException):
                time.sleep(2)
                OP.back()
            time.sleep(2)

'''消息中心'''
class Notice_center():
    '''系统消息'''
    def Sys_notice(self):
        OP.find_id('com.happyteam.dubbingshow:id/system_notice').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/more')
            time.sleep(2)
            try:
                '''点击头像进入空间'''
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/gender')
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    print("空间加载失败")
                    time.sleep(2)
                    OP.back()
            except:
                pass
            '''获取当前界面中系统消息信息内容'''
            gift_content = OP.find_ids('com.happyteam.dubbingshow:id/invite_content')
            for i in range(len(gift_content)):
                Gift_content = OP.find_ids('com.happyteam.dubbingshow:id/invite_content')[i].text
                print(Gift_content)
                time.sleep(2)
            time.sleep(2)
            time.sleep(2)
            print("点击清空")
            OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
            time.sleep(2)

            print("点击更多按钮")
            OP.find_id('com.happyteam.dubbingshow:id/more').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5*x,y=0.87*y).release().perform()
            try:
                OP.wait_toast('//android.widget.Toast')
                Del = OP.find_id('//android.widget.Toast').text
                print(Del.text)
            except (TimeoutException, NoSuchElementException):
                pass
            time.sleep(2)
            OP.back()
        except(NoSuchElementException, TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/Reload')
                print('消息中心列表加载失败')
                time.sleep(2)
                OP.back()
            except:
                print("消息列表为空")
                time.sleep(2)
                OP.back()

    '''礼物消息'''
    def Gift_notice(self):
        OP.find_id('com.happyteam.dubbingshow:id/gift').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            '''获取顶部提示文案内容'''
            tips = OP.find_id('com.happyteam.dubbingshow:id/tip').text
            print(tips)
            time.sleep(2)
            try:
                '''点击头像进入空间'''
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(2)
                    OP.back()
                except(TimeoutException, NoSuchElementException):
                    print("空间加载失败")
                    time.sleep(2)
                    OP.back()
            except:
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/setPush')
                print("显示有消息开关按钮")
                OP.find_id('com.happyteam.dubbingshow:id/setPush').click()
                time.sleep(2)
                OP.back()
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            '''获取送礼信息'''
            gift_content = OP.find_ids('com.happyteam.dubbingshow:id/content')

            for i in range(len(gift_content)):
                Gold_gift = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                print(name,Gold_gift)
                time.sleep(2)
            time.sleep(2)
            '''点击内容跳转'''
            OP.find_id('com.happyteam.dubbingshow:id/content').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/gift')
                time.sleep(1)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                print("界面未跳转")
            time.sleep(2)
            '''点击关注'''
            try:
                OP.find_xpath('关注').click()
            except:
                pass
            time.sleep(2)
            '''点击发私信'''
            try:
                OP.find_xpath('发私信').click()
                OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            '''点击进入视频详情'''
            OP.find_id('com.happyteam.dubbingshow:id/content').click()
            try:
                '''判断是否跳转失败显示toast提示'''
                OP.wait_toast('//android.widget.Toast')
                tips = OP.find_xpath('//android.widget.Toast').text
                print(tips)
            except:
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    OP.back()
                except:
                    pass
            time.sleep(2)
            '''点击钻石礼物'''
            OP.find_id('com.happyteam.dubbingshow:id/rl_tag2').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                '''获取礼物信息'''
                Money_gift = OP.find_ids('com.happyteam.dubbingshow:id/content')
                for i in range(len(Money_gift)):
                    Gift = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                    name = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                    print(name, Gift)
                    time.sleep(2)
                '''点击关注'''
                try:
                    OP.find_xpath('关注').click()
                except:
                    pass
                time.sleep(2)
                '''点击发私信'''
                try:
                    OP.find_xpath('发私信').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                    time.sleep(2)
                    OP.back()
                except:
                    pass
            except(NoSuchElementException,TimeoutException):
                print("钻石礼物列表加载失败")
            time.sleep(2)
            '''退出礼物消息中心'''
            OP.back()
        except:
            try:
                OP.find_xpath('暂无礼物喔~')
                tips = OP.find_id('com.happyteam.dubbingshow:id/tip').text
                print(tips)
                print("金币礼物列表为空")
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/setPush')
                    print("显示有消息开关按钮")
                    OP.find_id('com.happyteam.dubbingshow:id/setPush').click()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                except:
                    pass
            except:
                pass
            time.sleep(2)
            '''退出礼物消息中心'''
            OP.back()


    '''合作消息'''
    def Cooperation_notice(self):
        print("点击合作")
        OP.find_id('com.happyteam.dubbingshow:id/coopera').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            print("点击进入用户空间")
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()
            except:
                print("空间加载失败")
                time.sleep(2)
                OP.back()
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/play')
                print('点击预览视频')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/play').click()
                time.sleep(10)
                OP.back()
            except:
                pass
            time.sleep(2)
            '''
            由于合作配音按钮与tab中的按钮文案相同，因此无法使用xpath定位，且配音按钮控件名称相同，但文案不同，
            折中方法是依次点击元素控件，不以文案为准

            '''
            Dubbing = OP.find_ids('com.happyteam.dubbingshow:id/btnAccept')
            for i in range(len(Dubbing)):
                OP.find_ids('com.happyteam.dubbingshow:id/btnAccept')[i].click()
                try:
                    OP.wait_not_id('com.happyteam.dubbingshow:id/btnAccept')
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/upload')
                        print("声漫配音邀请")
                        time.sleep(2)
                        OP.back()
                        break
                    except(NoSuchElementException,TimeoutException):
                        try:
                            OP.wait_download('com.happyteam.dubbingshow:id/action')
                            print("素材配音邀请")
                            time.sleep(2)
                            OP.back()
                            time.sleep(2)
                            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                            break
                        except(NoSuchElementException,TimeoutException):
                            pass
                except:
                    pass
                time.sleep(2)
                OP.swip_up()
                time.sleep(3)
            time.sleep(2)
            print("删除合作消息")
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/more').click()
            time.sleep(2)
            TouchAction(devc).press(x=0.5*x,y=0.87*y).release().perform()
            '''获取删除toast提示'''
            try:
                OP.wait_toast('//android.widget.Toast')
                Dele_toast = OP.find_xpath('//android.widget.Toast').text
                print(Dele_toast)
            except:
                pass
            time.sleep(2)
            '''上滑列表'''
            OP.swip_up()
            time.sleep(5)
            '''切换至生成作品tab'''
            OP.find_id('com.happyteam.dubbingshow:id/rl_tag2').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                time.sleep(2)
                '''点击进入视频详情'''
                OP.find_id('com.happyteam.dubbingshow:id/play').click()
                try:
                    tip = OP.wait_toast('//android.widget.Toast')
                    print(tip)
                except(NoSuchElementException, TimeoutException):
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/gift')
                        time.sleep(2)
                        '''左滑进入个人空间'''
                        OP.swip_left()
                        try:
                            OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                            time.sleep(2)
                            OP.back()
                        except(NoSuchElementException,TimeoutException):
                            print("用户空间加载失败")
                            time.sleep(2)
                            OP.back()
                        time.sleep(2)
                        '''退出视频详情'''
                        OP.back()
                        time.sleep(2)
                    except:
                        pass

                time.sleep(2)
                '''生成作品'''
                Dubbing = OP.find_ids('com.happyteam.dubbingshow:id/btnAccept')
                for i in range(len(Dubbing)):
                    zhizuo = OP.find_ids('com.happyteam.dubbingshow:id/btnAccept')[i].text
                    check1 = '生成作品'
                    if zhizuo == check1:
                        OP.find_ids('com.happyteam.dubbingshow:id/btnAccept')[i].click()
                        time.sleep(4)
                        '''设置封面'''
                        OP.find_id('com.happyteam.dubbingshow:id/head_name').click()
                        time.sleep(2)
                        '''选择相册'''
                        TouchAction(devc).press(x=0.5 * x, y=0.88 * y).release().perform()
                        time.sleep(2)
                        '''选择图片'''
                        OP.find_id('com.happyteam.dubbingshow:id/photo_wall_item_photo').click()
                        time.sleep(4)
                        try:
                            OP.find_id('com.happyteam.dubbingshow:id/confirm')
                            OP.find_id('com.happyteam.dubbingshow:id/confirm').click()
                        except:
                            OP.back()
                        time.sleep(3)
                        '''填写标题'''
                        OP.find_id('com.happyteam.dubbingshow:id/title').clear()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/title').send_keys("作品标题:无")
                        time.sleep(2)
                        '''选择标签'''
                        OP.find_ids('com.happyteam.dubbingshow:id/tv')[0].click()
                        time.sleep(2)
                        OP.find_ids('com.happyteam.dubbingshow:id/tv')[1].click()
                        time.sleep(2)
                        '''点击取消'''
                        OP.find_id('com.happyteam.dubbingshow:id/btn_close').click()
                        time.sleep(2)
                        break
                    else:
                        pass
                    time.sleep(2)
                time.sleep(2)
                '''点击设置'''
                OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
                time.sleep(2)
                '''点击修改权限'''
                OP.find_id('com.happyteam.dubbingshow:id/acceptAll').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/acceptFirends').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/acceptNone').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/acceptAll').click()
                time.sleep(2)
                '''点击清空'''
                OP.find_id('com.happyteam.dubbingshow:id/clearAllInviter').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
                time.sleep(2)
                '''退出设置界面'''
                OP.back()
                time.sleep(2)
                '''退出合作消息界面'''
                OP.back()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                print("生成合作列表加载失败")
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("合作消息列表加载失败")
            time.sleep(2)
            OP.back()


    '''评论消息'''
    def Comment_notices(self):
        print("点击评论消息")
        OP.find_id('com.happyteam.dubbingshow:id/comment').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            time.sleep(2)
            '''点击头像进入个人空间'''
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                time.sleep(2)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                print("空间加载失败")
                time.sleep(2)
                OP.back()
            time.sleep(2)
            '''评论内容及恢复内容'''
            replys = OP.find_ids('com.happyteam.dubbingshow:id/reply')
            for i in range(len(replys)):
                user = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                print(user)
                Reply = OP.find_ids('com.happyteam.dubbingshow:id/reply')[i].text
                print(Reply)
                Content = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                print(Content)
                time.sleep(2)
            time.sleep(2)
            '''点击关注'''
            try:
                OP.find_xpath('关注').click()
            except:
                pass
            time.sleep(2)
            '''点击发私信'''
            OP.find_xpath('发私信').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                time.sleep(2)
                OP.back()
            except:
                pass
            time.sleep(2)
            '''点击进入视频详情'''
            OP.find_id('com.happyteam.dubbingshow:id/reply').click()
            try:
                OP.wait_xpath('//android.widget.Toast')
                tips = OP.find_xpath('//android.widget.Toast').text
                print(tips)
            except(NoSuchElementException,TimeoutException):
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/gift')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    pass
            time.sleep(2)
            '''点击回复评论'''
            OP.find_id('com.happyteam.dubbingshow:id/reply_btn').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("😄")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
            try:
                com_tips = OP.wait_xpath('//android.widget.Toast')
                check = "作品已删除"
                if com_tips == check:
                    print(com_tips)
                    time.sleep(2)
                    OP.back()
                else:
                    print(com_tips)
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
            '''切换帖子消息tab'''
            OP.find_id('com.happyteam.dubbingshow:id/rl_tag2').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                '''点击进入个人空间'''
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    print("空间加载失败")
                    OP.back()
                time.sleep(2)
                '''评论内容及恢复内容'''
                tie_reps = OP.find_ids('com.happyteam.dubbingshow:id/reply')
                for i in range(len(tie_reps)):
                    user = OP.find_ids('com.happyteam.dubbingshow:id/textView')[i].text
                    print(user)
                    Reply = OP.find_ids('com.happyteam.dubbingshow:id/reply')[i].text
                    print(Reply)
                    Content = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                    print(Content)
                    time.sleep(2)
                time.sleep(2)
                '''点击进入帖子详情'''
                OP.find_id('com.happyteam.dubbingshow:id/reply').click()
                try:
                    tie_tips = OP.wait_xpath('//android.widget.Toast')
                    print(tie_tips)
                except(NoSuchElementException,TimeoutException):
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                        time.sleep(2)
                        OP.back()
                    except(NoSuchElementException,TimeoutException):
                        try:
                            OP.find_id('com.happyteam.dubbingshow:id/reply')
                            print('帖子跳转失败')
                        except:
                            OP.back()
                time.sleep(2)
                '''点击关注'''
                try:
                    OP.find_xpath('关注').click()
                except:
                    pass
                time.sleep(2)
                '''点击发私信'''
                try:
                    OP.find_xpath('发私信').click()
                    OP.wait_id('com.happyteam.dubbingshow:id/editContent')
                    time.sleep(2)
                    OP.back()
                except:
                    pass
                time.sleep(2)
                '''退出评论消息中心'''
                OP.back()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("评论消息列表加载失败")
            time.sleep(2)
            OP.back()


    '''聊天消息'''
    def Chat_notices(self):
        '''点击聊天消息'''
        OP.find_id('com.happyteam.dubbingshow:id/chat').click()
        time.sleep(4)
        '''点击进入聊天界面'''
        try:
            OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
            time.sleep(4)
            OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("😁")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
            time.sleep(2)
            OP.back()
        except:
            pass
        time.sleep(2)
        '''点击进入好友列表'''
        OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/name')
            '''获取关注列表用户信息'''
            name_list = []
            follow_user = OP.find_ids('com.happyteam.dubbingshow:id/name')
            for i in range(len(follow_user)):
                user_name = OP.find_ids('com.happyteam.dubbingshow:id/name')[i].text
                name_list.append(user_name)
                time.sleep(1)
            print(name_list)
            time.sleep(2)
            '''搜索用户'''
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys("16685645")
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                time.sleep(2)
                name = OP.find_id('com.happyteam.dubbingshow:id/name').text
                print(name)
                time.sleep(2)
                '''点击进入聊天界面'''
                OP.find_id('com.happyteam.dubbingshow:id/name').click()
                time.sleep(2)
                for i in range(3):
                    '''发送文字'''
                    word = random.choice(['蒹葭苍苍，白露为霜。所谓伊人，在水一方。溯洄从之，道阻且长；溯游从之，宛在水中央。蒹葭凄凄，白露未晞...',
                                          '关关雎鸠，在河之洲。窈窕淑女，君子好逑。参差荇菜，左右流之。窈窕淑女，寤寐求之。求之不得，寤寐思服。',
                                          '氓之蚩蚩，抱布贸丝。匪来贸丝，来即我谋。送子涉淇，至于顿丘。匪我愆期，子无良媒。将子无怒，秋以为期',
                                          '采薇采薇，薇亦作止。曰归曰归，岁亦莫止。靡家靡室，猃狁之故。不遑启居，猃狁之故。采薇采薇，薇亦柔止。',
                                          '静女其姝，俟我于城隅。爱而不见，搔首踟蹰。静女其娈，贻我彤管。彤管有炜，说怿女美。自牧归荑，洵美且异',
                                          '硕鼠硕鼠，无食我黍！三岁贯女，莫我肯顾。逝将去女，适彼乐土。乐土乐土，爰得我所？硕鼠硕鼠，无食我麦'])
                    OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys(word)
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
                    time.sleep(2)
                time.sleep(2)
                '''切换语音'''
                OP.find_id('com.happyteam.dubbingshow:id/btn_change_input_mode').click()
                time.sleep(2)
                '''发送语音'''
                Voice = OP.find_id('com.happyteam.dubbingshow:id/btn_record_voice')
                TouchAction(devc).long_press(Voice,duration=10000).wait(5000).perform()
                time.sleep(4)

                '''点击播放语音'''
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/btn_play_sound_content_layout').click()
                    time.sleep(5)
                except:
                    pass
                time.sleep(2)
                '''发送图片'''
                OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/photo').click()
                time.sleep(2)
                '''随机选择一张图片'''
                choice = OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')
                select_photo = random.randint(0,int(len(choice)))
                OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[select_photo].click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/next_step_tv').click()
                time.sleep(4)
                '''选择作品'''
                OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/film').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
                    '''显示作品名称'''
                    Name_list = []
                    title_name = OP.find_ids('com.happyteam.dubbingshow:id/title')
                    for i in range(len(title_name)):
                        Title = OP.find_ids('com.happyteam.dubbingshow:id/title')[i].text
                        Name_list.append(Title)
                        time.sleep(2)
                    print(Name_list)
                    time.sleep(2)
                    '''选择视频'''
                    OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSelect').click()
                    time.sleep(4)
                except(NoSuchElementException,TimeoutException):
                    print("作品列表加载失败")
                    time.sleep(2)
                    OP.back()
                time.sleep(2)
                '''发红包'''
                OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/redpacket').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/cash_num').send_keys("1")
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(6)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet')
                    OP.back()
                except:
                    pass
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/red_packet')
                    OP.find_id('com.happyteam.dubbingshow:id/red_packet').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/open_red_packet_btn').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/user_head')
                        time.sleep(2)
                        OP.back()
                    except(TimeoutException, NoSuchElementException):
                        print("红包领取失败")
                except(NoSuchElementException, TimeoutException):
                    print("无红包")
                time.sleep(2)
                print('社团邀请')
                OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/union_inviter').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/user_image')
                    '''显示社团名称'''
                    Society_list = []
                    Society_name = OP.find_ids('com.happyteam.dubbingshow:id/userName')
                    for i in range(len(Society_name)):
                        name = OP.find_ids('com.happyteam.dubbingshow:id/userName')[i].text
                        Society_list.append(name)
                        time.sleep(1)
                    print(Society_list)
                    time.sleep(2)
                    '''选择社团'''
                    OP.find_id('com.happyteam.dubbingshow:id/userName').click()
                    time.sleep(3)
                except(NoSuchElementException,TimeoutException):
                    print("社团列表未显示有社团")
                    time.sleep(2)
                    OP.back()
            except(NoSuchElementException,TimeoutException):
                print("未搜索到指定用户")
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("好友列表加载失败")
        time.sleep(2)
        '''退出聊天详情界面'''
        OP.back()
        '''返回聊天列表主界面'''
        time.sleep(2)
        OP.back()
        '''删除聊天用户'''
        Delete_user = OP.find_id('com.happyteam.dubbingshow:id/userhead')
        TouchAction(devc).long_press(Delete_user).wait(2000).perform()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/delete').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)
        '''拉黑用户'''
        Delete_user = OP.find_id('com.happyteam.dubbingshow:id/userhead')
        TouchAction(devc).long_press(Delete_user).wait(2000).perform()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/addBlack').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)
        '''退出聊天消息中心'''
        OP.back()


'''创作中心'''
class Creative_center():
    '''草稿箱'''
    def Drafts(self):
        '''点击草稿箱'''
        OP.find_id('com.happyteam.dubbingshow:id/draft').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/upload')
            '''显示作品时间及作品名称'''
            Names = OP.find_ids('com.happyteam.dubbingshow:id/from')
            for i in range(len(Names)):
                Date = OP.find_ids('com.happyteam.dubbingshow:id/date')[i].text
                Names = OP.find_ids('com.happyteam.dubbingshow:id/from')[i].text
                print(Date,Names)
                time.sleep(1)
            time.sleep(2)
            '''点击预览视频'''
            OP.find_id('com.happyteam.dubbingshow:id/imgSource').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/upload')
                time.sleep(5)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(4)
            '''点击上传按钮'''
            OP.find_id('com.happyteam.dubbingshow:id/upload').click()
            time.sleep(3)
            Title = OP.find_id('com.happyteam.dubbingshow:id/txtTitle').text
            banchengpin = "生成求合作"
            Upload = "上传作品"
            if Title == banchengpin:
                print(Title)
                '''填写标题'''
                OP.find_id('com.happyteam.dubbingshow:id/title').send_keys("脚本测试")
                time.sleep(2)
                '''点击重配'''
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/reDubbing').click()
                    OP.wait_download('com.happyteam.dubbingshow:id/roleall')
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
                    time.sleep(2)
                    OP.back()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/upload').click()
                except(NoSuchElementException,TimeoutError):
                    pass
                time.sleep(2)
                '''点击私密'''
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/private_top_tv')
                    print("已开启私密")
                except:
                    OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
                time.sleep(2)
                '''点击生成求合作'''
                OP.find_id('com.happyteam.dubbingshow:id/uploadbtn').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/myself')
                    '''选择邀请好友'''
                    OP.find_id('com.happyteam.dubbingshow:id/inviteFriend').click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
                        OP.find_ids('com.happyteam.dubbingshow:id/socialstatus')[0].click()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/content').send_keys('邀请合作')
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/reprint').click()
                        time.sleep(10)
                    except(NoSuchElementException,TimeoutError):
                        time.sleep(2)
                        Invite = "邀请合作"
                        Title = OP.find_id('com.happyteam.dubbingshow:id/txtTitle').text
                        if Title ==Invite:
                            OP.back()
                        else:
                            pass
                except(NoSuchElementException,TimeoutError):
                    pass
                try:
                    OP.find_xpath('给钱也不要').click()
                except:
                    pass
                time.sleep(2)
            elif Title == Upload:
                print(Title)
                '''填写标题'''
                OP.find_id('com.happyteam.dubbingshow:id/title').send_keys("脚本测试")
                time.sleep(2)
                '''选择标签'''
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/tag_text').click()
                    time.sleep(2)
                except:
                    print("未显示标签选项，点击私密按钮开启标签选择入口")
                    OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
                    time.sleep(2)
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/tv')
                    try:
                        OP.find_id('com.happyteam.dubbingshow:id/close')
                        print('取消已选标签')
                        OP.find_id('com.happyteam.dubbingshow:id/close').click()
                    except:
                        pass
                    time.sleep(2)
                    '''获取热门标签'''
                    Tv_list = []
                    Tv = OP.find_ids('com.happyteam.dubbingshow:id/tv')
                    for i in range(len(Tv)):
                        Tv_name = OP.find_ids('com.happyteam.dubbingshow:id/tv')[i].text
                        Tv_list.append(Tv_name)
                        time.sleep(1)
                    print(Tv_list)
                    time.sleep(2)
                    Select_tv = random.randint(0,int(len(Tv_list)))
                    OP.find_ids('com.happyteam.dubbingshow:id/tv')[Select_tv].click()
                    time.sleep(2)
                    OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                    time.sleep(2)
                    try:
                        OP.find_xpath('生成求合作')
                        '''点击合作开关'''
                        OP.find_id('com.happyteam.dubbingshow:id/check_box_add_square').click()
                        time.sleep(2)
                        '''点击私密'''
                        OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
                    except:
                        pass
                    time.sleep(2)
                    '''点击保存作品'''
                    OP.find_id('com.happyteam.dubbingshow:id/savebtn').click()
                    time.sleep(2)
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/btnSubmit')
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutError):
                        pass
                except(NoSuchElementException, TimeoutException):
                    time.sleep(2)
                    OP.back()
            else:
                pass
            '''点击同步按钮'''
            OP.find_id('com.happyteam.dubbingshow:id/btnSync').click()
            time.sleep(2)
            try:
                OP.find_xpath('会员中心')
                print("未购买会员")
                time.sleep(2)
                OP.back()
            except:
                try:
                    OP.wait_download('同步')
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    time.sleep(2)
                    OP.back()
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_xpath('您暂时还没有保存过草稿')
                print("草稿箱为空")
                OP.back()
            except:
                pass

    '''已配素材'''
    def Sources(self):
        OP.find_id('com.happyteam.dubbingshow:id/source').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/dubbing')
            '''获取列表素材名称'''
            Source_names = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')
            Name_list = []
            for i in range(len(Source_names)):
                Title_name = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[i].text
                Name_list.append(Title_name)
                time.sleep(1)
            print(Name_list)
            '''收藏素材'''
            for collect in range(len(Source_names)):
                OP.find_ids('com.happyteam.dubbingshow:id/iv_source')[collect].click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/zhuanfa_fake')
                    OP.find_id('com.happyteam.dubbingshow:id/shouchang_tv_fake').click()
                    try:
                        toast = OP.wait_toast('//android.widget.Toast')
                        print(toast)
                        Shouchang = "收藏成功"
                        if toast ==Shouchang:
                            print(toast)
                        else:
                            print('重新收藏')
                            OP.find_id('com.happyteam.dubbingshow:id/shouchang_tv_fake').click()
                    except(NoSuchElementException,TimeoutException):
                        pass
                    time.sleep(2)
                    OP.back()
                except(NoSuchElementException,TimeoutError):
                    print('素材视频详情加载失败')
                    OP.back()
                time.sleep(2)
            time.sleep(2)
            '''点击进入素材详情'''
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/zhuanfa_fake')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/yinpin')
                    print("合作素材")
                    '''点击配音按钮'''
                    OP.find_xpath('立即配音').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/roleall')
                        OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutError):
                        print("素材下载失败")
                except:
                    print("单配作品")
                    OP.find_xpath('立即配音').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/action')
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException,TimeoutError):
                        print("素材下载失败")
                time.sleep(2)
                '''退出素材视频详情界面'''
                OP.back()
            except(NoSuchElementException,TimeoutError):
                print('素材详情界面加载失败')
                OP.back()
            time.sleep(2)
            '''长按删除'''
            source_el = OP.find_id('com.happyteam.dubbingshow:id/iv_source')
            TouchAction(devc).long_press(source_el).wait(2000).perform()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except(NoSuchElementException,TimeoutError):
                pass
            time.sleep(2)
            '''全部删除'''
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                OP.find_id('com.happyteam.dubbingshow:id/delete').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/choice').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/toDelete').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(10)
                OP.find_id('com.happyteam.dubbingshow:id/cancel').click()
            except(NoSuchElementException,TimeoutError):
                pass
            time.sleep(2)
            '''返回我的界面'''
            OP.back()
            time.sleep(2)
            print('已配界面功能测试结束')
        except(NoSuchElementException,TimeoutError):
            time.sleep(2)
            OP.back()


    '''收藏'''
    def Collect(self):
        OP.find_id('com.happyteam.dubbingshow:id/collect').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/zhuanfa_fake')
                time.sleep(5)
                OP.back()
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                print("素材视频详情加载失败")
                time.sleep(2)
                OP.back()
                time.sleep(2)
            time.sleep(2)
            '''点击进入素材详情'''
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/zhuanfa_fake')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/yinpin')
                    print("合作素材")
                    '''点击配音按钮'''
                    OP.find_xpath('立即配音').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/roleall')
                        OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException, TimeoutError):
                        print("素材下载失败")
                except:
                    print("单配作品")
                    OP.find_xpath('立即配音').click()
                    try:
                        OP.wait_download('com.happyteam.dubbingshow:id/action')
                        time.sleep(2)
                        OP.back()
                        time.sleep(2)
                        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                        time.sleep(2)
                    except(NoSuchElementException, TimeoutError):
                        print("素材下载失败")
                time.sleep(2)
                '''退出素材视频详情界面'''
                OP.back()
            except(NoSuchElementException, TimeoutError):
                print('素材详情界面加载失败')
                OP.back()
            time.sleep(2)
            print("长按删除")
            source_el = OP.find_id('com.happyteam.dubbingshow:id/iv_source')
            TouchAction(devc).long_press(source_el).wait(2000).perform()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/iv_source')
                print('全部删除')
                OP.find_id('com.happyteam.dubbingshow:id/delete').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/choice').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/toDelete').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                try:
                    toast = OP.wait_toast('//android.widget.Toast')
                    print(toast)
                except(NoSuchElementException,TimeoutException):
                    pass
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
        except(NoSuchElementException,TimeoutException):
            try:
                OP.find_xpath('您还没有收藏任何素材哦~')
                print("素材收藏列表为空")
                time.sleep(2)
                OP.back()
            except(NoSuchElementException,TimeoutException):
                Reload = OP.find_id('com.happyteam.dubbingshow:id/Reload')
                if Reload == True:
                    print("素材收藏列表加载失败")
                    time.sleep(2)
                    OP.back()
                else:
                    pass
        time.sleep(2)
        OP.back()
        time.sleep(2)
        '''返回我的界面'''
        OP.back()
        print('收藏列表功能测试结束')
        time.sleep(2)

    '''自制素材'''
    def Made_material(self):
        OP.find_id('com.happyteam.dubbingshow:id/upload_source').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
            '''获取素材名称'''
            Source_title = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')
            Title_list = []
            for i in range(len(Source_title)):
                Title_name = OP.find_ids('com.happyteam.dubbingshow:id/tv_source_title')[i].text
                Title_list.append(Title_name)
            print (Title_list)
            time.sleep(2)
        except(NoSuchElementException,TimeoutException):
            print('未显示有素材作品')
        time.sleep(2)
        '''退出自制素材列表界面'''
        OP.back()
        time.sleep(2)

'''个人中心'''
class Personal_center():
    '''我的财富'''
    def My_wealth(self):
        '''上滑屏幕'''
        OP.swip_up()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/money').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            Gold_balance = OP.find_id('com.happyteam.dubbingshow:id/gold_count_tv').text
            print("金币余额:", Gold_balance)
            time.sleep(2)
            Diamond_balance = OP.find_id('com.happyteam.dubbingshow:id/diamond_count_tv').text
            print("钻石余额:", Diamond_balance)
            time.sleep(2)
            '''获取价格列表'''
            els = OP.find_ids('com.happyteam.dubbingshow:id/count_tv')
            for i in range(len(els)):
                content = OP.find_ids('com.happyteam.dubbingshow:id/count_tv')[i].text
                price = OP.find_ids('com.happyteam.dubbingshow:id/price_tv')[i].text
                print(content, price)
                time.sleep(1)

            '''账单'''
            OP.find_id('com.happyteam.dubbingshow:id/toBill').click()
            time.sleep(5)
            OP.back()
            time.sleep(2)
            '''点击购买'''
            OP.find_id('com.happyteam.dubbingshow:id/price_tv').click()
            time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/money')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/close_icon').click()
            except(NoSuchElementException,TimeoutException):
                print("未显示支付选项弹窗")
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            print("我的财富界面加载失败")
        time.sleep(2)
        '''退出我的财富界面'''
        OP.back()

    '''我的收益'''
    def My_income(self):
        OP.find_id('com.happyteam.dubbingshow:id/gold').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/postal')
            Money = OP.find_id('com.happyteam.dubbingshow:id/gold_count').text
            print("余额为:", Money)
            if float(Money) < 100:
                print("额度不足100，无法提现")
            else:
                print("余额足够，可提现")
            time.sleep(2)
            try:
                check_binding = OP.find_id('com.happyteam.dubbingshow:id/alipay').text
                zhifubao_check = "未绑定支付宝账户"
                time.sleep(2)
                if check_binding == zhifubao_check:
                    print(check_binding)
                else:
                    zhifubao_account = OP.find_id('com.happyteam.dubbingshow:id/mobile').text
                    print("绑定支付宝账号为:", zhifubao_account)
                time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                pass
            '''账单'''
            try:
                OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    time.sleep(3)
                    OP.back()
                except(NoSuchElementException,TimeoutException):
                    time.sleep(2)
                    OP.back()
                time.sleep(2)
                Bill_record = OP.find_ids('com.happyteam.dubbingshow:id/content')
                for i in range(len(Bill_record)):
                    record = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                    money_record = OP.find_ids('com.happyteam.dubbingshow:id/gold')[i].text
                    print(record, money_record)
                    time.sleep(2)
            except(NoSuchElementException,TimeoutException):
                print("账单为空")
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        '''常见问题'''
        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
        time.sleep(5)
        OP.back()
        print("退出我的收益界面")
        OP.back()

    '''我的成就'''
    def My_achievements(self):
        OP.find_id('com.happyteam.dubbingshow:id/achievement').click()
        try:
            OP.wait_xpath('个人成就')
            time.sleep(2)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            time.sleep(2)
            OP.back()
        time.sleep(4)

    '''找好友'''
    def Add_friend(self):
        OP.find_id('com.happyteam.dubbingshow:id/addfriend').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/inviteWeiboFriend')
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/filter_edit').send_keys('10251')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSearch').click()
            try:
                OP.wait_xpath('配音秀官方号')
                OP.find_xpath('配音秀官方号').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/fanscount')
                    follow_check = "已关注"
                    follow_status = OP.find_id('com.happyteam.dubbingshow:id/follow_status').text
                    time.sleep(2)
                    if follow_status == follow_check:
                        print("已关注")
                        time.sleep(2)
                        OP.back()
                    else:
                        OP.find_ids('com.happyteam.dubbingshow:id/follow_status').click()
                        time.sleep(5)
                        OP.back()
                except(NoSuchElementException,TimeoutException):
                    print("加载失败")
                    time.sleep(2)
                    OP.back()
            except(NoSuchElementException,TimeoutException):
                print("未搜索到指定用户")
        except(NoSuchElementException,TimeoutException):
            print("找好友界面加载失败")
        time.sleep(2)
        print("退出找好友界面")
        OP.back()
        time.sleep(2)

    '''积分兑换'''
    def Exchange(self):
        OP.find_id('com.happyteam.dubbingshow:id/exchange').click()
        try:
            OP.wait_xpath('金币商城')
            time.sleep(2)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            print("金币商城加载失败")
            time.sleep(2)
            OP.back()
        time.sleep(4)

    '''日/夜模式'''
    def Pattern(self):
        Pattern1 = OP.find_id('com.happyteam.dubbingshow:id/tvChange').text
        print(Pattern1)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/change').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            OP.swip_up()
            time.sleep(2)
            Pattern2 = OP.find_id('com.happyteam.dubbingshow:id/tvChange').text
            print(Pattern2)
            time.sleep(2)
            if Pattern1 == Pattern2:
                print("模式切换失败")
            else:
                print("模式切换成功")
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)


'''应用设置按钮'''
class Setting():
    def App_Setting(self):
        OP.find_id('com.happyteam.dubbingshow:id/shezhi').click()
        time.sleep(4)
        '''手机号绑定'''
        OP.find_id('com.happyteam.dubbingshow:id/phone').click()
        time.sleep(2)
        try:
            Phone = OP.find_id('com.happyteam.dubbingshow:id/account').text
            null = "未绑定"
            if Phone == null:
                print("未绑定手机号")
                time.sleep(2)
                OP.back()
            else:
                print(Phone)
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        '''分享设置'''
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        time.sleep(2)
        try:
            Sina = OP.find_id('com.happyteam.dubbingshow:id/txtSinaName').text
            share_check = "未绑定"
            if Sina == share_check:
                print("未绑定新浪微博")
                time.sleep(2)
                OP.back()
            else:
                print(Sina)
                time.sleep(2)
                OP.back()
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        '''功能设置'''
        OP.find_id('com.happyteam.dubbingshow:id/viewMsgSetting').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushwificheck').click()
        print("设置WiFi自动播放")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushDraftcheck').click()
        print("设置草稿箱云端同步")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushpraisecheck').click()
        Gift_setting = OP.find_id('com.happyteam.dubbingshow:id/textPraise').text
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(Gift_setting,toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushcommentcheck').click()
        Comment_setting = OP.find_id('com.happyteam.dubbingshow:id/textComment').text
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(Comment_setting,toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushfanscheck').click()
        Fans_setting = OP.find_id('com.happyteam.dubbingshow:id/textFans').text
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(Fans_setting,toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushtiezicheck').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
            print('回帖',toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushfriendcheck').click()
        try:
            friend_toast = OP.wait_toast('//android.widget.Toast')
            print('好友动态',friend_toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/pushlivecheck').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print('语聊通知',toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.back()
        time.sleep(2)

        '''隐私'''
        OP.find_id('com.happyteam.dubbingshow:id/view_black_list').click()
        time.sleep(2)
        '''作品下载开关'''
        OP.find_id('com.happyteam.dubbingshow:id/receiveOnlyLoad').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print('允许他人下载我的作品',toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        '''私信开关'''
        OP.find_id('com.happyteam.dubbingshow:id/receiveOnlyMyfollow').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print('只接收我关注的人发来的私信',toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        '''黑名单'''
        OP.find_id('com.happyteam.dubbingshow:id/black').click()
        time.sleep(5)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/userhead')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/right_icon1').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/delete').click()
            try:
                toast = OP.wait_toast('//android.widget.Toast')
                print(toast)
            except(NoSuchElementException,TimeoutException):
                pass
            time.sleep(2)
            OP.back()
        except(NoSuchElementException,TimeoutException):
            print("黑名单为空")
            time.sleep(2)
            OP.back()
        time.sleep(2)
        '''声漫共享开关'''
        OP.find_id('com.happyteam.dubbingshow:id/share').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print('声漫共享开关',toast)
        except(NoSuchElementException,TimeoutException):
            pass
        time.sleep(2)
        OP.back()
        time.sleep(2)

        '''意见反馈'''
        OP.find_id('com.happyteam.dubbingshow:id/viewReport').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys("测试")
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/content')
            contents = OP.find_ids('com.happyteam.dubbingshow:id/content')
            for i in range(len(contents)):
                content = OP.find_ids('com.happyteam.dubbingshow:id/content')[i].text
                print(content)
        except(NoSuchElementException, TimeoutException):
            pass
        time.sleep(2)
        '''上传错误日志'''
        OP.find_id('com.happyteam.dubbingshow:id/upload_log').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        try:
            toast = OP.wait_toast('//android.widget.Toast')
            print(toast)
        except(NoSuchElementException, TimeoutException):
            pass
        time.sleep(2)
        '''发送图片'''
        OP.find_id('com.happyteam.dubbingshow:id/btn_open_photo').click()
        time.sleep(2)
        TouchAction(devc).press(x=0.5 * x,y=0.88 * y).release().perform()
        time.sleep(4)
        Photos = OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')
        Select_Photo = random.randint(0, int(len(Photos)))
        OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[Select_Photo].click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/next_step_tv').click()
        time.sleep(5)
        '''退出意见反馈界面'''
        OP.back()
        time.sleep(4)
        '''关于配音秀'''
        OP.find_id('com.happyteam.dubbingshow:id/viewAbout').click()
        time.sleep(2)
        Version = OP.find_id('com.happyteam.dubbingshow:id/txtVersion').text
        print(Version)
        time.sleep(2)
        OP.back()



if __name__=="__main__":
    Zoom = My_Zoom()
    ID   = My_identity()
    N    = Notice_center()
    C    = Creative_center()
    P    = Personal_center()
    S    = Setting()
    Zoom.Grade()
    Zoom.photo()
    Zoom.person_info()
    Zoom.other_info()
    Zoom.works_info()
    ID.VIP()
    ID.CP()
    ID.Jump()
    N.Sys_notice()
    N.Gift_notice()
    N.Cooperation_notice()
    N.Comment_notices()
    N.Chat_notices()
    C.Drafts()
    C.Sources()
    C.Collect()
    C.Made_material()
    P.My_wealth()
    P.My_income()
    P.My_achievements()
    P.Add_friend()
    P.Exchange()
    P.Pattern()
    S.App_Setting()

