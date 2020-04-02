#coding = utf-8
from Dubbing_910.operate.Driver_Operate import BaseOperate
from Dubbing_910.Public.devices import appium_desired
from appium.webdriver.common.touch_action import TouchAction

import time
id = 'com.happyteam.dubbingshow:id/'
class Dub():
    def __init__(self,udid,port,sp):
        self.D = BaseOperate(udid,port,sp)
        self.driver = appium_desired(udid,port,sp)
        self.X = BaseOperate(udid,port,sp).touch()[0]
        self.Y = BaseOperate(udid,port,sp).touch()[1]
        self.dev = udid
    def Dub_start(self):
        self.D.wait_id(id+'task_box')
        print('==开始==')
        time.sleep(2)
        try:
            for i in range(100):
                self.D.find_id(id + 'btn_more').click()
                time.sleep(2)
                self.D.wait_id(id + 'unlimited')
                self.D.find_id(id + 'unlimited').click()
                time.sleep(2)
                self.D.find_xpath('推荐').click()
                time.sleep(2)
                print(i)
                self.D.swip_down()
                time.sleep(2)
                try:
                    self.D.wait_id(id + 'iv_source')
                except:
                    self.D.swip_down()
                time.sleep(2)
                self.D.find_id(id+'iv_source').click()
                self.D.wait_id(id+'shouchang_tv_fake')
                time.sleep(2)
                try:
                    self.D.find_id(id + 'yinpin')
                    self.D.find_id(id + 'dubbing_fake').click()
                    self.D.wait_id(id +'roleall')
                    time.sleep(2)
                    self.D.find_id(id + 'roleall').click()
                except:
                    self.D.find_id(id +'dubbing_fake').click()
                    self.D.wait_download(id + 'living')
                time.sleep(2)
                try:
                    #首次进入配音界面引导遮罩
                    self.D.find_id(id +'subtitleView')
                    self.D.find_id(id+ 'subtitleView').click()
                except:
                    pass
                # self.D.wait_id(id + 'btnSubmit')
                # self.D.find_id(id+'btnSubmit').click()
                # time.sleep(2)
                # try:
                #     self.D.find_id(id+'roleall')
                #     time.sleep(1)
                #     self.D.find_id(id+'roleall').click()
                # except:
                #     pass
                # time.sleep(2)
                time.sleep(2)
                self.D.find_id(id+'action').click()
                time.sleep(2)
                try:
                    self.D.find_id(id +'next')
                    self.D.find_id(id + 'next').click()
                    time.sleep(2)
                    try:
                        self.D.wait_sys("始终允许")
                        self.D.find_id(id + 'action').click()
                        time.sleep(2)
                    except:
                        self.D.wait_sys("允许")
                        self.D.find_id(id + 'action').click()
                        time.sleep(2)
                except:
                    pass
                time.sleep(2)
                self.D.wait_download(id+'title')
                self.D.Background()
                time.sleep(2)
                self.D.find_xpath('完成').click()
                self.D.wait_id(id+'txtTitle')
                time.sleep(2)
                self.D.find_id(id +'btn_setting_cover_tip').click()
                time.sleep(2)
                if self.Y == 1920:
                    TouchAction(self.driver).press(x=int(self.X * 0.5), y=int(self.Y * 0.7)).release().perform()
                elif self.Y > 1920:
                    TouchAction(self.driver).press(x=int(self.X * 0.5), y=int(self.Y * 0.76)).release().perform()
                elif self.Y < 1281:
                    TouchAction(self.driver).press(x=int(self.X * 0.5), y=int(self.Y * 0.7)).release().perform()
                elif self.Y < 1920:
                    TouchAction(self.driver).press(x=int(self.X * 0.5), y=int(self.Y * 0.75)).release().perform()
                else:
                    pass
                time.sleep(2)
                self.D.find_id(id + 'complete').click()
                time.sleep(2)
                self.D.find_id(id + 'pri_switch_tv').click()
                time.sleep(2)
                # self.D.find_id(id + 'title').click()
                # time.sleep(2)
                # self.D.find_id(id+'title').send_keys("1")
                # time.sleep(2)
                # self.D.find_id(id+'saveToDraft').click()
                # time.sleep(2)
                # self.D.find_id(id+'btnSubmit').click()
                # self.D.wait_id(id+'btn_more')
                # time.sleep(2)
                self.D.find_id(id+'uploadbtn').click()
                time.sleep(2)
                try:
                    self.D.find_id(id+'btnSubmit')
                    self.D.find_id(id+'btnSubmit').click()
                except:
                    pass
                time.sleep(2)
                try:
                    self.D.wait_id(id+'down')
                    print('上传成功！')
                except:
                    element = self.D.find_id(id+'film_title').text
                    print(element)
                    self.D.Quit()
        except:
            print(self.dev)
        time.sleep(2)
        self.D.Quit()







