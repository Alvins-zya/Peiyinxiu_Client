#coding = utf-8
#防止中文显示乱码
#coding = gb18030
# from appium import webdriver
import time
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#获取当前项目的根路径
# PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from dubbbingshow_99550.operate.Driver_Operate import BaseOperate
#
# OP = BaseOperate

class Dubbin():

    def __init__(self,udid,port,systemport):
        self.D = BaseOperate(udid,port,systemport)

    def start_app(self):
        try:
            self.D.wait_id('com.happyteam.dubbingshow:id/task_box')
            print('===开始===')
        except:
            print('应用启动失败')
    def start_dub(self):
        self.D.find_id('com.happyteam.dubbingshow:id/btn_more').click()
        try:
            self.D.wait_id('com.happyteam.dubbingshow:id/iv_source')
        except(NoSuchElementException, TimeoutException):
            try:
                self.D.find_id('com.happyteam.dubbingshow:id/Reload').click()
                try:
                    self.D.wait_id('com.happyteam.dubbingshow:id/iv_source')
                except(NoSuchElementException, TimeoutException):
                    pass
            except(NoSuchElementException, TimeoutException):
                pass
        time.sleep(4)

    def Dubbing_again(self):
            self.D.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                self.D.wait_xpath('素材预览')
            except(NoSuchElementException, TimeoutException):
                try:
                    self.D.find_id('com.happyteam.dubbingshow:id/Reload').click()
                    try:
                        self.D.wait_xpath("立即配音")
                    except(NoSuchElementException, TimeoutException):
                        pass
                except(NoSuchElementException, TimeoutException):
                    pass
            time.sleep(2)
            try:
                self.D.find_id('com.happyteam.dubbingshow:id/yinpin')
                self.D.find_xpath("立即配音").click()
                self.D.wait_id('com.happyteam.dubbingshow:id/roleall')
                time.sleep(2)
                self.D.find_id('com.happyteam.dubbingshow:id/roleall').click()
            except(NoSuchElementException, TimeoutException):
                try:
                    self.D.find_xpath("立即配音").click()
                    self.D.wait_id('com.happyteam.dubbingshow:id/action')
                except(NoSuchElementException, TimeoutException):
                    pass
            time.sleep(2)
            print('台词编辑')
            self.D.find_id('com.happyteam.dubbingshow:id/edit_subtitle').click()
            time.sleep(2)
            content = self.D.find_id('com.happyteam.dubbingshow:id/content_editor').text
            time.sleep(1)
            self.D.find_id('com.happyteam.dubbingshow:id/content_editor').clear()
            time.sleep(1)
            self.D.find_id('com.happyteam.dubbingshow:id/content_editor').send_keys(content+'。')
            time.sleep(2)
            self.D.find_id('com.happyteam.dubbingshow:id/complete').click()
            time.sleep(4)
            print('开启实况')
            self.D.find_id('com.happyteam.dubbingshow:id/living').click()
            time.sleep(2)
            try:
                self.D.find_xpath('始终允许')
                self.D.find_xpath('始终允许').click()
            except:
                try:
                    self.D.find_xpath('允许')
                    self.D.find_xpath('允许').click()
                except:
                    pass
            time.sleep(2)
            try:
                self.D.wait_id('com.happyteam.dubbingshow:id/cameraView2')
                print('实况开启成功')
                time.sleep(1)
                print('关闭实况')
                self.D.find_id('com.happyteam.dubbingshow:id/living').click()
            except:
                print('实况开启失败')
            time.sleep(2)

            try:
                self.D.find_id('com.happyteam.dubbingshow:id/script_container')
                print('点击台词列表')
                time.sleep(1)
                self.D.find_id('com.happyteam.dubbingshow:id/script_container').click()
                time.sleep(2)
                try:
                    self.D.find_id('com.happyteam.dubbingshow:id/txtContent')
                    content = self.D.find_id('com.happyteam.dubbingshow:id/txtContent').text
                    print(content)
                    time.sleep(1)
                    self.D.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
                except:
                    pass
                time.sleep(2)
                srt = self.D.find_ids('com.happyteam.dubbingshow:id/titleTextView')
                self.D.back()
                time.sleep(1)
                for i in range(len(srt)):
                    self.D.find_id('com.happyteam.dubbingshow:id/script_container').click()
                    time.sleep(2)
                    self.D.find_ids('com.happyteam.dubbingshow:id/titleTextView')[i].click()
                    try:
                        self.D.wait_id('com.happyteam.dubbingshow:id/action')
                    except:
                        print('未返回到配音界面')
                    time.sleep(2)

            except:
                pass

            '''循环'''
            for i in range(1):
                print("循环第", i + 1, "次")
                self.D.find_id('com.happyteam.dubbingshow:id/action').click()
                time.sleep(2)
                try:
                    self.D.find_id('com.happyteam.dubbingshow:id/next')
                    time.sleep(1)
                    self.D.find_id('com.happyteam.dubbingshow:id/next').click()
                    time.sleep(2)
                    self.D.find_id('com.android.packageinstaller:id/permission_allow_button').click()
                    time.sleep(2)
                    self.D.find_id('com.happyteam.dubbingshow:id/action').click()
                except:
                    pass
                try:
                    self.D.wait_download('com.happyteam.dubbingshow:id/vol')
                except(NoSuchElementException, TimeoutException):
                    print('跳转失败')
                self.D.wait_download('com.happyteam.dubbingshow:id/play_button')
                time.sleep(4)
                self.D.back()
                time.sleep(4)
                self.D.find_id('com.happyteam.dubbingshow:id/withdraw').click()
                time.sleep(4)
                try:
                    self.D.find_id('com.happyteam.dubbingshow:id/review')
                    self.D.find_id('com.happyteam.dubbingshow:id/review').click()
                except:
                    pass
            try:
                self.D.wait_download('com.happyteam.dubbingshow:id/action')
                self.D.find_id('com.happyteam.dubbingshow:id/action').click()
                self.D.wait_download('com.happyteam.dubbingshow:id/vol')
            except:
                pass
            time.sleep(2)
            print('点击字幕开关')
            self.D.find_id('com.happyteam.dubbingshow:id/add_subtitle_cb').click()
            time.sleep(4)
            self.D.find_id('com.happyteam.dubbingshow:id/complete').click()
            try:
                self.D.wait_download('com.happyteam.dubbingshow:id/uploadbtn')
                try:
                    self.D.find_id('com.happyteam.dubbingshow:id/private_top_tv')
                except:
                    self.D.find_id('com.happyteam.dubbingshow:id/pri_switch_tv').click()
            except:
                pass
            time.sleep(2)
            self.D.find_id('com.happyteam.dubbingshow:id/uploadbtn').click()
            time.sleep(2)
            try:
                self.D.wait_load('上传作品成功！')
                self.D.find_id('com.happyteam.dubbingshow:id/close').click()
            except:
                pass
            time.sleep(2)
            self.D.swip_down()
            time.sleep(3)
            print("=======结束========")

    def start(self):
        self.start_app()
        self.start_dub()
        self.Dubbing_again()


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
