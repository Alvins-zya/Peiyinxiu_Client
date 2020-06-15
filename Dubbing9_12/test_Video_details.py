import unittest
import time
import pytest
from Dubbing9_11.Front import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Video_detial(Dubbing):
    # 点击进入视频详情
    def test_a(self):
        self.driver.find_id(soucred_id + 'film_img2').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)

    # 点击用户头像进入个人空间
    def test_b(self):
        heads = self.driver.find_ids(soucred_id + 'userhead')
        for i in range(len(heads)):
            self.driver.find_ids(soucred_id + 'userhead')[i].click()
            self.driver.wait_id(soucred_id + 'fanscount')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(4)

    # 关注-发私信
    def test_c(self):
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

    # 视频-弹幕开关
    def test_d(self):
        self.driver.find_id(soucred_id + 'media_danmu_img').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        time.sleep(20)
        self.driver.Background()
        self.driver.wait_id(soucred_id + 'play')
        time.sleep(2)

    # 全屏播放
    def test_e(self):
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'film_img2').click()
        self.driver.wait_id(soucred_id + 'follow_ta')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'iv_fullscreen_open').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)

    # 作品信息
    def test_e_a(self):
        video_name = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
        play_count_inside =  self.driver.find_id(soucred_id + 'tv_video_play_num_in').text
        play_count_out = self.driver.find_id(soucred_id + 'tv_good').text
        print('作品名称：',video_name,
              '站内播放量:',play_count_inside,
              '点赞量:',tv_video_play_num_out,)
        time.sleep(2)



class Test_b_Function(Dubbing):


    # 视频评论
    def test_a(self):
        while True:
            try:
                self.driver.find_id(soucred_id + 'tv_hide')
                self.driver.swip_up()
                time.sleep(2)
                self.driver.Background()
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'tv_shafa')
                self.driver.swip_up()
                time.sleep(2)
                self.driver.Background()
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'comment_count')
                break
            except:
                pass
        time.sleep(2)

    # 评论排序
    def test_b(self):
        self.driver.find_id(soucred_id + 'tv_comment').click()
        self.driver.wait_id(soucred_id + 'item_comment_video_more')
        time.sleep(2)
        try:
            self.driver.find_xpath('以上为置顶评论')
            Comment = self.driver.find_ids(soucred_id + 'item_video_common_time')[1].text
            time.sleep(1)
            self.driver.find_id(soucred_id + 'shunxu').click()
            time.sleep(2)
            Comment1 = self.driver.find_ids(soucred_id + 'item_video_common_time')[1].text
            self.assertNotEqual(Comment, Comment1, msg='评论切换顺序后评论内容校验错误')
            time.sleep(2)
        except:
            Comment = self.driver.find_id(soucred_id + 'item_video_common_time').text
            time.sleep(1)
            self.driver.find_id(soucred_id + 'shunxu').click()
            time.sleep(2)
            Comment1 = self.driver.find_id(soucred_id + 'item_video_common_time').text
            self.assertNotEqual(Comment,Comment1,msg='评论切换顺序后评论时间校验错误')
            time.sleep(2)

    # 评论举报
    def test_c(self):
        self.driver.find_id(soucred_id +'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_action_one').click()
        time.sleep(2)
        reason = self.driver.find_id(soucred_id + 'txtTitle').text
        check = '政治'
        self.assertIn(check,reason,msg='选择的举报理由中未包含政治关键字')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '举报成功'
            self.assertEqual(toast,check_toast,msg='举报toast内容校验不一致')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'txtKeyword').send_keys('举报功能测试')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '举报成功'
            self.assertEqual(toast,check_toast,msg='举报toast内容校验不一致')
        except:
            pass
        time.sleep(2)

    # 评论列表上滑加载
    def test_d(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'follow_ta').click()
        time.sleep(2)

    # 点击合作配音完成后保存草稿箱
    def test_n(self):
        while True:
            try:
                self.driver.find_xpath('配音/合作')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
                self.driver.Background()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('配音/合作').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'coor')
            self.driver.find_id(soucred_id + 'coor').click()
            while True:
                try:
                    self.driver.find_id(soucred_id + 'action')
                    break
                except:
                    try:
                        self.driver.find_id(soucred_id + 'btnSubmit')
                        tip = self.driver.find_id(soucred_id + 'txtTitle').text
                        print(tip)
                        self.driver.find_id(soucred_id + 'btnSubmit').click()
                        break
                    except:
                        pass
            time.sleep(2)
            self.driver.find_id(soucred_id + 'action').click()
            self.driver.wait_download(soucred_id + 'title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'complete').click()
            self.driver.wait_id(soucred_id + 'txtTitle')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'pri_switch_tv').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'saveToDraft').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            self.driver.wait_id(soucred_id + 'userhead')
            time.sleep(4)
        except Exception as e:
            print(e)
        try:
            self.driver.wait_download(soucred_id + 'action')
        except:
            self.driver.find_id(soucred_id + 'btnSubmit')
            tip = self.driver.find_id(soucred_id + 'txtTitle').text
            print(tip)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'coor')
        self.driver.find_id(soucred_id + 'close').click()
        time.sleep(2)

    # 点击原声素材配音完成后保存草稿箱
    def test_o(self):
        self.driver.find_id(soucred_id + 'tvSource').click()
        self.driver.wait_id(soucred_id + 'source_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dubbing_fake').click()
        while True:
            try:
                self.driver.find_id(soucred_id + 'roleall')
                break
            except:
                try:
                    self.driver.find_id(soucred_id + 'btnSubmit')
                    tip = self.driver.find_id(soucred_id + 'txtTitle').text
                    print(tip)
                    self.driver.find_id(soucred_id + 'btnSubmit').click()
                    break
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'roleall').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 配音完成后保存草稿箱
    def test_l(self):
        while True:
            try:
                self.driver.find_xpath('原声素材')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'film_img2').click()
                self.driver.wait_id(soucred_id + 'follow_ta')
                self.driver.Background()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('原声素材').click()
        self.driver.wait_id(soucred_id + 'types_name')
        self.driver.Background()
        time.sleep(2)

    def test_m(self):
        try:
            self.driver.find_id(soucred_id + 'yinpin')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            globals()["result"] = True
            return globals()['result']
        except:
            globals()['result'] = False
            return globals()['result']

    @pytest.mark.skipif(test_m(self=None), u'结果为False时，判断是单配素材,不执行此条用例')
    def test_n(self):
        self.driver.find_id(soucred_id + 'dubbing').click()
        self.driver.wait_download(soucred_id + 'roleall')
        self.driver.find_id(soucred_id + 'roleall').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(4)
        try:
            self.driver.find_xpath('退出配音')
            self.driver.find_xpath('退出配音').click()
        except:
            pass
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)

    @unittest.skipIf(test_m(self=None), u'结果为True时，判断是双人素材，不执行此条用例')
    def test_o(self):
        self.driver.find_id(soucred_id + 'dubbing_fake').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(4)
        self.driver.wait_id(soucred_id + 'btnSubmit')
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)

    # 切换视频
    def test_p(self):
        for i in range(10):
            self.driver.swip_up()
            self.driver.wait_id(soucred_id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.swip_left()
            self.driver.wait_id(soucred_id + 'followcount')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()
