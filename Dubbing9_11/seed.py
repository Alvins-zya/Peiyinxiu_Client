#coding = utf-8
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction

from Dubbing9_11.parent import Dubbing


soucred_id = 'com.happyteam.dubbingshow:id/'

class Dub(Dubbing):

    def test1_touche_dubbing(self):
        try:
            self.driver.find_id(soucred_id + 'yinpin')
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_id(soucred_id + 'roleall')
            self.driver.find_id(soucred_id + 'roleall').click()
        except:
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_id(soucred_id + 'living')

    def test2_guidance(self):
        # 引导页面
        try:
            self.driver.find_id(soucred_id + 'subtitleView').click()
        except:
            pass
    def test3_headset(self):
        #背景音
        self.driver.find_id(soucred_id + 'headset').click()
        time.sleep(2)
        try:
            tips = self.driver.find_id(soucred_id + 'txtContent').text
            print(tips)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
        except:
            print('已连接耳机')

    def test4_living(self):
        #实况
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
        try:
           self.driver.find_id(soucred_id + 'txtTitle')
           tips = self.driver.find_id(soucred_id + 'txtTitle').text
           print(tips)
           self.driver.find_id(soucred_id + 'close').click()
           time.sleep(2)
           self.driver.find_id(soucred_id + 'living').click()
           time.sleep(2)
           self.driver.find_id(soucred_id + 'next').click()
           time.sleep(2)
           try:
               self.driver.wait_sys("始终允许")
           except:
               self.driver.wait_sys("允许")

        except:
            pass
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'cameraView2')
        except:
            self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'living')
        time.sleep(2)

    def test5_subtitle_change(self):
        #台词
        self.driver.find_id(soucred_id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'titleTextView')
        count = self.driver.find_ids(soucred_id + 'titleTextView')
        for i in range(len(count)):
            self.driver.find_ids(soucred_id + 'titleTextView')[i].click()
            self.driver.wait_id(soucred_id + 'edit_subtitle')
            self.driver.find_id(soucred_id + 'scirpt').click()
            self.driver.wait_id(soucred_id + 'titleTextView')
            time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def test6_subtitle_edit(self):
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        count1 = self.driver.find_ids(soucred_id + 'content_editor')
        script = []
        for i in range(len(count1)):
            sub = self.driver.find_ids(soucred_id + 'content_editor')[i].text
            script.append(sub)
            time.sleep(1)
        print(script)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)

    def test7_HD(self):
        HD_check = self.driver.find_id(soucred_id + 'swtich_hd').text
        check = '切换高清画质'
        if HD_check == check:
            self.driver.find_id(soucred_id + 'swtich_hd').click()
            time.sleep(2)
            tips = self.driver.find_id(soucred_id + 'txtContent').text
            tips_check = '购买会员专享高清素材，可生成高清配音作品'
            self.assertEqual(tips,tips_check,msg='文案错误')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            self.driver.wait_id(soucred_id + 'renew')
            time.sleep(2)
            self.driver.back()
        else:
            pass

    def test8_play(self):
        self.driver.find_id(soucred_id + 'play').click()
        time.sleep(8)
        self.driver.Background()
        self.driver.wait_download(soucred_id + 'play')

    def test9_jurisdiction(self):
        # 录音权限
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            self.driver.find_id(soucred_id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            pass
        time.sleep(2)

    def test10_action(self):
        try:
            self.driver.find_id(soucred_id + 'play')
            self.driver.find_id(soucred_id + 'action').click()
        except:
            pass
    def test11(self):
        #手动点击提交进入配音预览界面
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
    def test12(self):
        #原声试听
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
    def test13(self):
        #配音秀试听
        self.driver.find_id(soucred_id + 'review').click()
        self.driver.wait_download(soucred_id + 'play')
    def test14(self):
        #手动拖音轨
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        TouchAction(self.driver).press(x=self.x*0.24,y=self.y*0.71).move_to(x=self.x*0.81,y=self.y*0.71).release().perform()
        time.sleep(2)
        #点击预览视频
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
    def test15(self):






class Dub_preview(Dubbing):
    def test1_preview(self):
        # 配音预览界面
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)




class Dub_upload(Dubbing):
    def test2_complete(self):
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)

    def test3_privacy(self):
        # 私密开关
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)

    def test8_upload(self):
        self.driver.find_id(soucred_id + 'uploadbtn').click()
        time.sleep(2)
    def test9_over(self):
        self.driver.wait_id(soucred_id + 'down')
        print('上传成功')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Dub))
    runner = unittest.TextTestRunner()
    runner.run(suite)