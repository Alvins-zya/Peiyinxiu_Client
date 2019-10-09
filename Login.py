#coding = UTf-8
'''
author:zya
time:2019年6月3日
function:Login

New:
time:2019年9月29日
function:新增接口返回数据结果与UI界面获取数据结果对比功能

'''
import os
import time
from appium.webdriver.common.touch_action import TouchAction
from Peiyinxiu_Client.devices import device,dev
from Peiyinxiu_Client.Operate import BaseOperate
import Interface.USER.API

OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
touch = device()
D = dev

class Login():
    def __init__(self):
        self.API = Interface.USER.API
    def Main_interface(self):
        OP.wait_download('com.happyteam.dubbingshow:id/btnSubmit')
        print('显示温馨提示弹窗')
        content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
        print(content)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
        time.sleep(4)
        touch.launch_app()
        OP.wait_id('com.happyteam.dubbingshow:id/btnCancel')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)
        print('手机号登录')
        OP.find_id('com.happyteam.dubbingshow:id/phone').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/zone_tv').click()
        OP.wait_xpath('地区')
        country = OP.find_ids('com.happyteam.dubbingshow:id/username')
        country_name = []
        country_code = []
        for i in range(len(country)):
            name = OP.find_ids('com.happyteam.dubbingshow:id/username')[i].text
            code = OP.find_ids('com.happyteam.dubbingshow:id/code')[i].text
            country_name.append(name)
            country_code.append(code)
            time.sleep(0.5)
        time.sleep(3)
        '''
        APP界面中获取的国家信息与接口返回的国家信息进行对比
        '''
        #获取UI界面中的国家count
        country_number = len(country_name)
        #截取接口返回国家数量，与UI界面中的country_number一直，进行对比
        country_list = self.API.get_country('', 0)
        Interface_country_name = country_list[0]#国家列表
        # Interface_country_code = country_list[1]#区号列表
        # print(Interface_country_name)
        # print(Interface_country_code)
        Interface_country_number = Interface_country_name[0:country_number]     #以UI获取国家列表长度为准，截取接口返回数据中相等长度的国家信息
        if country_name == Interface_country_number:
            print("APP界面获取国家列表数据信息与接口返回列表数据信息一致")
        else:
            print("====列表对比不一致，请检查====")
            print("APP界面获取的国家列表信息：",country_name)
            print("接口返回的国家列表信息：",Interface_country_number)
        time.sleep(3)
        OP.find_id('com.happyteam.dubbingshow:id/edit_text').send_keys('zg')
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/btn_search').click()
        time.sleep(2)
        Interface_search_country = self.API.Search_country('zg')
        OP.wait_xpath('中国')
        UI_country_name = OP.find_id('com.happyteam.dubbingshow:id/username').text
        if Interface_search_country == UI_country_name:
            print('接口返回国家名称与UI界面获取国家名称信息一致')
        else:
            print("对比界面不一致,","接口返回结果：",Interface_search_country,"UI界面获取结果：",UI_country_name)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/username').click()
        time.sleep(4)
        print("用户注册")
        OP.find_id('com.happyteam.dubbingshow:id/to_register').click()

    def register(self):
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/et_number').send_keys('12345678956')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/et_password').send_keys('123456')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/send_code').click()
        try:
            get_toast = OP.wait_toast('//android.widget.Toast')
            print(get_toast)
            check1 = '手机号输入错误'
            if get_toast == check1:
                OP.find_id('com.happyteam.dubbingshow:id/et_number').clear()
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/et_number').send_keys('18072702677')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/et_password').send_keys('123456')
                OP.wait_load('发送验证码')
                OP.find_id('com.happyteam.dubbingshow:id/send_code').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/et_code').send_keys('888888')
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/tv_login').click()
                try:
                    get_toast = OP.wait_toast('//android.widget.Toast')
                    print(get_toast)
                except:
                    print('未检测到toast')
            else:
                pass
        except:
            print('未监测到toast')
        time.sleep(2)
        OP.back()
        time.sleep(2)

    def forget_pw(self):
        print('忘记密码')
        OP.find_id('com.happyteam.dubbingshow:id/forget_psw').click()
        time.sleep(3)
        Login().register()

    def login(self):
        print('验证码登录')
        OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
        OP.wait_xpath('发送验证码')
        OP.find_id('com.happyteam.dubbingshow:id/et_number').send_keys('123456789123')
        time.sleep(1)
        OP.find_id('com.happyteam.dubbingshow:id/send_code').click()
        try:
            get_toast = OP.wait_toast('//android.widget.Toast')
            check3 = '手机号输入错误'
            if get_toast == check3:
                OP.find_id('com.happyteam.dubbingshow:id/tv_right').click()
                time.sleep(2)
                OP.find_id('com.happyteam.dubbingshow:id/et_number').send_keys('18072702677')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/et_password').send_keys('123456')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/tv_login').click()
                time.sleep(4)
                login_info = self.API.Phone_login('18072702677','123456')
                print(login_info)
                time.sleep(2)
                TouchAction(touch).press(x = 0.5*x,y= 0.3*y).release().perform()
                # OP.wait_id('com.happyteam.dubbingshow:id/btnSubmit')
                # OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                time.sleep(2)
            else:
                pass
        except:
            print('未检测到toast信息')
    def change_login(self):
        OP.find_id('com.happyteam.dubbingshow:id/ivMineTab').click()
        time.sleep(2)
        print('点击设置')
        OP.find_id('com.happyteam.dubbingshow:id/shezhi').click()
        time.sleep(2)
        OP.swip_up()
        time.sleep(2)
        print('退出登录')
        OP.find_id('com.happyteam.dubbingshow:id/quitlogin').click()
        time.sleep(1)
        OP.find_xpath('确定').click()
        try:
            quit_toast = OP.wait_toast('//android.widget.Toast')
            check = '退出登录成功'
            if check == quit_toast:
                print(quit_toast)
            else:
                print('退出登录失败')
        except:
            pass
        time.sleep(2)
        print('点击登录')
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        print('其它方式登录')
        TouchAction(touch).press(x=0.5*x,y=0.44*y).release().perform()
        time.sleep(2)
        print('微信登录')
        TouchAction(touch).press(x=0.28*x,y=0.42*y).release().perform()
        try:
            login_toast = OP.wait_toast('//android.widget.Toast')
            check = '登录成功'
            if login_toast == check:
                print(login_toast)
            else:
                print('微信登录失败，请检查！')
        except:
            try:
                OP.find_xpath('确认登录')
                OP.find_xpath('确认登录').click()
            except:
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/women')
                    print('用户信息填写')
                    OP.find_id('com.happyteam.dubbingshow:id/man').click()
                    OP.find_id('com.happyteam.dubbingshow:id/women').click()
                    time.sleep(2)
                    # 日期:年/月/日
                    touch.swipe(0.28 * x, 0.78 * x, 0.28 * x, 0.65 * y, 300)
                    time.sleep(1)
                    touch.swipe(0.5 * x, 0.78 * x, 0.5 * x, 0.65 * y, 300)
                    time.sleep(1)
                    touch.swipe(0.71 * x, 0.78 * x, 0.71 * x, 0.65 * y, 300)
                    time.sleep(1)
                    print('下一步')
                    OP.find_id('com.happyteam.dubbingshow:id/sava').click()
                    toast = OP.wait_toast('//android.widget.Toast')
                    check = '保存成功'
                    if toast == check:
                        print(toast)
                    else:
                        print('用户信息填写失败，请检查！')
                except:
                    try:
                        OP.find_xpath('帐号')
                        print('微信未登录')
                        OP.back()
                    except:
                        try:
                            OP.find_id('com.tencent.mm:com.tencent.mm:id/ec7')
                            OP.find_id('com.tencent.mm:com.tencent.mm:id/ec7').click()
                        except:
                            OP.back()

        time.sleep(2)
        username = OP.find_id('com.happyteam.dubbingshow:id/username').text
        print(username)
        time.sleep(1)
        print('点击设置')
        OP.find_id('com.happyteam.dubbingshow:id/shezhi').click()
        time.sleep(2)
        OP.swip_up()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/quitlogin')
            print('退出登录')
            OP.find_id('com.happyteam.dubbingshow:id/quitlogin').click()
            time.sleep(1)
            OP.find_xpath('确定').click()
            try:
                quit_toast = OP.wait_toast('//andorid.widget.Toast')
                check = '退出登录成功'
                if check == quit_toast:
                    print(quit_toast)
                else:
                    print('退出登录失败')
            except:
                pass
        except:
            OP.back()
        time.sleep(2)
        print('点击登录')
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        print('其它方式登录')
        time.sleep(2)
        TouchAction(touch).press(x=0.5 * x, y=0.57 * y).release().perform()
        time.sleep(4)
        print('微博登录')
        TouchAction(touch).press(x=0.5 * x, y=0.42 * y).release().perform()
        try:
            login_toast = OP.wait_toast('//android.widget.Toast')
            check = '登录成功'
            if login_toast == check:
                print(login_toast)
            else:
                print('微博登录失败，请检查！')
                OP.back()
        except:
            try:
                OP.find_xpath('手机号或者邮箱')
                print('微博未登录')
                time.sleep(1)
                OP.back()
            except:
                pass
        time.sleep(2)
        username = OP.find_id('com.happyteam.dubbingshow:id/username').text
        print(username)
        time.sleep(1)
        print('点击设置')
        OP.find_id('com.happyteam.dubbingshow:id/shezhi').click()
        time.sleep(2)
        OP.swip_up()
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/quitlogin')
            print('退出登录')
            OP.find_id('com.happyteam.dubbingshow:id/quitlogin').click()
            time.sleep(1)
            OP.find_xpath('确定').click()
            try:
                quit_toast = OP.wait_toast('//andorid.widget.Toast')
                check = '退出登录成功'
                if check == quit_toast:
                    print(quit_toast)
                else:
                    print('退出登录失败')
            except:
                pass
        except:
            OP.back()
        time.sleep(2)
        print('点击登录')
        OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
        time.sleep(2)
        print('其它方式登录')
        TouchAction(touch).press(x=0.5 * x, y=0.714 * y).release().perform()
        time.sleep(2)
        print('QQ登录')
        TouchAction(touch).press(x=0.72 * x, y=0.42 * y).release().perform()
        try:
            OP.wait_xpath('登录')
            OP.find_xpath('登录').click()
        except:
            OP.find_xpath('授权并登录').click()
        try:
            login_toast = OP.wait_toast('//android.widget.Toast')
            check = '登录成功'
            if login_toast == check:
                print(login_toast)
            else:
                print('QQ登录失败，请检查！')
        except:
            pass
        time.sleep(2)
        username = OP.find_id('com.happyteam.dubbingshow:id/username').text
        print(username)









def main():
    L = Login()
    L.Main_interface()
    L.register()
    L.forget_pw()
    L.login()
    L.change_login()
    print('====结束=====')
    time.sleep(5)
    # 清除应用数据
    os.system('adb -s %s shell pm clear com.happyteam.dubbingshow' % D)


if __name__=="__main__":
    main()