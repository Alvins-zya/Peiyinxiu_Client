#coding = utf-8
#防止中文显示乱码
#coding = gb18030
import random
# from appium import webdriver
import time
# from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#获取当前项目的根路径
# PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from dubbbingshow_99550.Operate import BaseOperate
from devices import device
OP = BaseOperate()

class Dubbin():
    def start_app(self):
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/task_box')
            print('===开始===')
        except:
            print('应用启动失败')
    def start_dub(self):
        OP.find_id('com.happyteam.dubbingshow:id/btn_more').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
        except(NoSuchElementException, TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/Reload').click()
                try:
                    OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
                except(NoSuchElementException, TimeoutException):
                    pass
            except(NoSuchElementException, TimeoutException):
                pass
        time.sleep(4)

    def Dubbing_again(self):
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                OP.wait_xpath('素材预览')
            except(NoSuchElementException, TimeoutException):
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/Reload').click()
                    try:
                        OP.wait_xpath("立即配音")
                    except(NoSuchElementException, TimeoutException):
                        pass
                except(NoSuchElementException, TimeoutException):
                    pass
            time.sleep(2)
            try:
                OP.find_id('com.happyteam.dubbingshow:id/yinpin')
                OP.find_xpath("立即配音").click()
                OP.wait_id('com.happyteam.dubbingshow:id/roleall')
                OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
            except(NoSuchElementException, TimeoutException):
                try:
                    OP.find_xpath("立即配音").click()
                    OP.wait_id('com.happyteam.dubbingshow:id/action')
                except(NoSuchElementException, TimeoutException):
                    pass
            time.sleep(2)
            print('台词编辑')
            OP.find_id('com.happyteam.dubbingshow:id/edit_subtitle').click()
            time.sleep(2)
            content = OP.find_id('com.happyteam.dubbingshow:id/content_editor').text
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/content_editor').clear()
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/content_editor').send_keys(content+'。')
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(4)
            print('开启实况')
            OP.find_id('com.happyteam.dubbingshow:id/living').click()
            time.sleep(2)
            try:
                OP.find_xpath('始终允许')
                OP.find_xpath('始终允许').click()
            except:
                try:
                    OP.find_xpath('允许')
                    OP.find_xpath('允许').click()
                except:
                    pass
            time.sleep(2)
            try:
                OP.wait_id('com.happyteam.dubbingshow:id/cameraView2')
                print('实况开启成功')
                time.sleep(1)
                print('关闭实况')
                OP.find_id('com.happyteam.dubbingshow:id/living').click()
            except:
                print('实况开启失败')
            time.sleep(2)

            try:
                OP.find_id('com.happyteam.dubbingshow:id/script_container')
                print('点击台词列表')
                time.sleep(1)
                OP.find_id('com.happyteam.dubbingshow:id/script_container').click()
                time.sleep(2)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/txtContent')
                    content = OP.find_id('com.happyteam.dubbingshow:id/txtContent').text
                    print(content)
                    time.sleep(1)
                    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                except:
                    pass
                time.sleep(2)
                srt = OP.find_ids('com.happyteam.dubbingshow:id/titleTextView')
                OP.back()
                time.sleep(1)
                for i in range(len(srt)):
                    OP.find_id('com.happyteam.dubbingshow:id/script_container').click()
                    time.sleep(2)
                    OP.find_ids('com.happyteam.dubbingshow:id/titleTextView')[i].click()
                    try:
                        OP.wait_id('com.happyteam.dubbingshow:id/action')
                    except:
                        print('未返回到配音界面')
                    time.sleep(2)

            except:
                pass

            '''循环'''
            for i in range(1):
                print("循环第", i + 1, "次")
                OP.find_id('com.happyteam.dubbingshow:id/action').click()
                try:
                    OP.wait_download('com.happyteam.dubbingshow:id/vol')
                except(NoSuchElementException, TimeoutException):
                    print('跳转失败')
                OP.wait_download('com.happyteam.dubbingshow:id/play_button')
                time.sleep(4)
                OP.back()
                time.sleep(4)
                OP.find_id('com.happyteam.dubbingshow:id/withdraw').click()
                time.sleep(4)
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/review')
                    OP.find_id('com.happyteam.dubbingshow:id/review').click()
                except:
                    pass
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/action')
                OP.find_id('com.happyteam.dubbingshow:id/action').click()
                OP.wait_download('com.happyteam.dubbingshow:id/vol')
            except:
                pass
            time.sleep(2)
            print('点击字幕开关')
            OP.find_id('com.happyteam.dubbingshow:id/add_subtitle_cb').click()
            time.sleep(4)
            OP.find_id('com.happyteam.dubbingshow:id/complete').click()
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/uploadbtn')
                try:
                    OP.find_id('com.happyteam.dubbingshow:id/private_top_tv')
                except:
                    OP.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
            except:
                pass
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/uploadbtn').click()
            time.sleep(2)
            OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
            time.sleep(2)
            try:
                OP.wait_download('com.happyteam.dubbingshow:id/submit')
                OP.find_id('com.happyteam.dubbingshow:id/submit').click()
            except:
                pass
            time.sleep(2)
            OP.swip_down()
            time.sleep(3)
            print("=======结束========")


# if __name__=="__main__":
#     Dubbin().start_app()
#     Dubbin().start_dub()
#     i = 1
#     while i == True:
#         Dubbin().Dubbing_again()
#     device().quit()

        # mailserver = "smtp.qq.com"  # 邮箱服务器地址
        # username_send = '406096917@qq.com'  # 邮箱用户名
        # password = 'cmaciajztfmmbibh'  # 邮箱密码：需要使用授权码
        # username_recv = 'zya@show-mobi.com'  # 收件人，多个收件人用逗号隔开
        # mail = MIMEText('第%s轮配音测试完成'%(i+1))
        # mail['Subject'] = '第%s测试结束'%(i+1)
        # mail['From'] = username_send  # 发件人
        # mail['To'] = username_recv  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
        # # smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
        # smtp = smtplib.SMTP_SSL('smtp.qq.com', port=465)  # QQ邮箱的服务器和端口号
        # smtp.login(username_send, password)  # 登录邮箱
        # smtp.sendmail(username_send, username_recv, mail.as_string())  # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        # smtp.quit()  # 发送完毕后退出smtp
