#coding = utf-8
#防止中文显示乱码
#coding = gb18030
import random
import os
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
# #获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
from pprint import pprint
# from Interface.USER import API
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()
class Dubbin():
    # def start_app(self):
    #     try:
    #         OP.wait_id('com.happyteam.dubbingshow:id/task_box')
    #         print('===开始===')
    #     except:
    #         print('应用启动失败')
    #     OP.find_id('com.happyteam.dubbingshow:id/btn_more').click()
    #     try:
    #         OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
    #     except(NoSuchElementException, TimeoutException):
    #         try:
    #             OP.find_id('com.happyteam.dubbingshow:id/Reload').click()
    #             try:
    #                 OP.wait_id('com.happyteam.dubbingshow:id/iv_source')
    #             except(NoSuchElementException, TimeoutException):
    #                 pass
    #         except(NoSuchElementException, TimeoutException):
    #             pass
    #     time.sleep(4)

    def Dubbing_again(self):
        while True:
            OP.find_id('com.happyteam.dubbingshow:id/iv_source').click()
            try:
                OP.wait_xpath('素材预览')
            except(NoSuchElementException, TimeoutException):
                pass
            time.sleep(2)
            T1 = '01:00'
            T2 = OP.find_id('com.happyteam.dubbingshow:id/video_total_time').text
            # l2 = T2.replace(':', '')
            if T2 < T1:
                print(T2)
                break
            else:
                print(T2)
                time.sleep(2)
                OP.back()
            time.sleep(2)
            OP.swip_down()
            time.sleep(3)
        time.sleep(2)
        try:
            OP.find_id('com.happyteam.dubbingshow:id/yinpin')
            OP.find_id('com.happyteam.dubbingshow:id/dubbing_fake').click()
            OP.wait_id('com.happyteam.dubbingshow:id/roleall')
            OP.find_id('com.happyteam.dubbingshow:id/roleall').click()
        except(NoSuchElementException, TimeoutException):
            try:
                OP.find_id('com.happyteam.dubbingshow:id/dubbing_fake').click()
                OP.wait_id('com.happyteam.dubbingshow:id/action')
            except(NoSuchElementException, TimeoutException):
                pass
        time.sleep(2)

        OP.find_id('com.happyteam.dubbingshow:id/action').click()
        try:
            OP.wait_download('com.happyteam.dubbingshow:id/clear_voice')
        except(NoSuchElementException, TimeoutException):
            device().quit()
        devc.keyevent(3)
        time.sleep(4)
        devc.launch_app()
        time.sleep(4)

        OP.find_id('com.happyteam.dubbingshow:id/complete').click()
        OP.wait_download('com.happyteam.dubbingshow:id/saveToDraft')
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/saveToDraft').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnCancel').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/rl_coor')
        except:
            pass
        time.sleep(2)
        OP.swip_down()
        time.sleep(3)


if __name__=="__main__":
    # Dubbin().start_app()
    i = 1
    while i == True:
        Dubbin().Dubbing_again()
    device().quit()

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
