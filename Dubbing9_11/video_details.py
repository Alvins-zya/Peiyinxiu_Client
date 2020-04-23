import unittest
import time
from Dubbing9_11.parent import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'

class test_a_Video_detial(Dubbing):
    def test_a(self):
        #点击进入视频详情
        self.driver.find_id(soucred_id + 'film_img2').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)

    def test_b(self):
        #点击用户头像进入个人空间
        heads = self.driver.find_ids(soucred_id + 'userhead')
        for i in range(len(heads)):
            self.driver.find_ids(soucred_id + 'userhead')[i].click()
            self.driver.wait_id(soucred_id + 'followcount')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)

    def test_c(self):
        #关注-发私信
        self.driver.find_id(soucred_id + 'follow_ta').click()
        try:
            follow_toast = self.driver.wait_toast('//android.widget.Toast')
            toast = '关注成功'
            self.assertEqual(follow_toast,toast,msg='toast提示信息内容校验不一致')
        except:
            try:
                self.driver.find_id(soucred_id + 'right_icon1')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'follow_ta').click()
        self.driver.wait_id(soucred_id + 'right_icon1')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x*0.5,self.y*0.859)
        else:
            pass
        self.driver.wait_id(soucred_id + 'followcount')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'follow_status').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    def test_d(self):
        #视频-弹幕开关
        danmu  = self.driver.find_ids(soucred_id + 'danmaku')
        if len(danmu) ==2:
            self.driver.find_id(soucred_id + 'media_danmu_img').click()
        else:
            print("弹幕已关闭")
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()
