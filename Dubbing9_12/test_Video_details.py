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


    # 礼物榜
    @unittest.skip('9.12版本不再显示礼物榜信息')
    def test_f(self):
        gift_count = self.driver.find_id(soucred_id +'gift_tip').text
        print(gift_count)
        time.sleep(2)
        # #礼物规则弹窗,待开发增加识别ID
        # self.driver.find_id(soucred_id + 'guize').click()
        # time.sleep(2)
        while True:
            try:
                self.driver.find_id(soucred_id + 'gift_more')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
                self.driver.Background()
                time.sleep(2)
        time.sleep(2)
        video_title = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
        time.sleep(1)
        self.driver.find_id(soucred_id + 'gift_more').click()
        self.driver.wait_id(soucred_id + 'diamond_count')
        title_check = self.driver.find_ids(soucred_id + 'name')[0].text
        self.assertIn(title_check,video_title,msg='视频详情中的标题名称未包含礼物榜列表中标题名称')
        time.sleep(2)

    # 礼物榜详情列表-送礼按钮
    @unittest.skip('9.12版本不再显示礼物榜信息')
    def test_g(self):
        self.driver.find_id(soucred_id + 'send_gift').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'confirm')
        except:
            raise ('点击送礼按钮后未弹出礼物选择列表弹窗')
        time.sleep(2)
        gift_name = self.driver.find_ids(soucred_id + 'gift_name')
        list = []
        for i in range(len(gift_name)):
            name = self.driver.find_ids(soucred_id + 'gift_name')[i].text
            value = self.driver.find_ids(soucred_id + 'gift_value')[i].text
            list.append(name)
            list.append(value)
            time.sleep(1)
        time.sleep(2)
        if self.y ==1920:
            self.driver.swip_move(self.x*0.844,self.y*0.752,self.x*0.13,self.y*0.752)
        else:
            pass
        time.sleep(2)
        gift_name1 = self.driver.find_ids(soucred_id + 'gift_name')
        for i in range(len(gift_name1)):
            name = self.driver.find_ids(soucred_id + 'gift_name')[i].text
            value = self.driver.find_ids(soucred_id + 'gift_value')[i].text
            list.append(name)
            list.append(value)
            time.sleep(1)
        time.sleep(2)
        gift_check = ['鲜花', '10', '毛绒玩具', '188', '口红', '3980', '999朵玫瑰', '13140', '宝石', '1', '跑车', '5', '私人飞机', '20', '海岛', '200', '烟花', '880', '巧克力', '1880', '蓝色妖姬', '5200', '麦克风', '39999', '钻戒', '3', '游艇', '8', '别墅', '50', '城堡', '100']
        self.assertEqual(list,gift_check,msg='礼物列表校验失败，请检查')
        time.sleep(2)
        if self.y ==1920:
            self.driver.swip_move(self.x*0.13,self.y*0.752,self.x*0.844,self.y*0.752)
        else:
            pass
        time.sleep(2)

    # 赠送金币礼物后金币余额检查
    @unittest.skip('9.12版本不再显示礼物榜信息')
    def test_h(self):
        send_before = self.driver.find_id(soucred_id + 'gold_count').text
        self.driver.find_xpath('鲜花').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'add_view').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'confirm').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg="礼物赠送成功后的toast内容校验错误")
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'send_gift').click()
        time.sleep(2)
        send_later = self.driver.find_id(soucred_id + 'gold_count').text
        self.assertNotEqual(send_before,send_later,msg='送礼后的金币余额显示错误')
        time.sleep(2)

    # 钻石礼物
    @unittest.skip('9.12版本不再显示礼物信息')
    def test_i(self):
        try:
            self.driver.find_id(soucred_id + 'confirm')
        except:
            self.driver.find_id(soucred_id + 'send_gift')
        time.sleep(2)
        Diamond = self.driver.find_id(soucred_id + 'diamond_count').text
        F_Balance = float(Diamond)
        Balance = int(F_Balance)#得到钻石余额是字符串浮点型，因此需要先转换成浮点型再转换成整形
        if Balance < 200:
            self.driver.find_xpath('海岛').click()
            time.sleep(1)
            self.driver.find_id(soucred_id + 'confirm').click()
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '充值'
            self.assertIn(check,toast,msg='钻石不足toast提示文案错误')
            time.sleep(2)
        else:
            print('钻石余额大于200钻，不做钻石送礼测试')
        time.sleep(2)

    # 礼物列表跳转到钻石充值界面
    @unittest.skip('9.12版本不再显示礼物信息')
    def test_j(self):
        try:
            self.driver.find_id(soucred_id + 'confirm')
        except:
            self.driver.find_id(soucred_id + 'send_gift')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_vip').click()
        self.driver.wait_id(soucred_id + 'price_tv')
        #点击购买显示支付选项列表弹窗
        self.driver.find_id(soucred_id + 'price_tv').click()
        self.driver.wait_id(soucred_id + 'tv_pay')
        try:
            self.driver.find_id(soucred_id + 'pay_weixin_view')
            try:
                self.driver.find_id(soucred_id + 'pay_zhifu_view')
                try:
                    self.driver.find_id(soucred_id + 'pay_qq_view')
                    try:
                        self.driver.find_id(soucred_id + 'pay_balance_view')
                    except:
                        print('未显示余额支付选项')
                except:
                    print('未显示QQ钱包支付选项')
            except:
                print('未显示支付宝支付选项')
        except:
            print('未显示微信支付选项')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'close_icon').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    # 打榜信息
    @unittest.skip('9.12版本不再显示礼物信息')
    def test_k(self):
        try:
            self.driver.find_id(soucred_id + 'rl1')
        except:
            raise ('未显示打榜信息，不做此项测试')
        time.sleep(2)
        name = self.driver.find_id(soucred_id + 'tv_title1').text
        Ranking = self.driver.find_id(soucred_id + 'tv_rank1').text
        print(name,":",Ranking)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'img1_right').click()
        self.driver.wait_id(soucred_id + 'iv_source')
        list_name = self.driver.find_id(soucred_id + 'txtTitle').text
        self.assertEqual(name,list_name,msg='礼物列表中的上榜名称与榜单列表中的榜单标题名称不一致')
        video_count = self.driver.find_ids(soucred_id + 'iv_source')
        for i in range(len(video_count)):
            self.driver.find_ids(soucred_id + 'iv_source')[i].click()
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 作品送礼用户列表
    @unittest.skip('9.12版本不再显示礼物信息')
    def test_l(self):
        try:
            self.driver.find_id(soucred_id + 'iv_source')
            self.driver.find_id(soucred_id + 'btnBack')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'followcount')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'gift_img').click()
        time.sleep(2)
        send_kinds = self.driver.find_ids(soucred_id + 'text1')
        list = []
        for i in range(len(send_kinds)):
            gift_name = self.driver.find_ids(soucred_id + 'text1')[i].text
            gift_count = self.driver.find_ids(soucred_id + 'text2')[i].text
            list.append(gift_name)
            list.append(gift_count)
            time.sleep(1)
        print(list)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 礼物列表上滑加载
    @unittest.skip('9.12版本不再显示礼物信息')
    def test_m(self):
        while True:
            first = self.driver.find_ids(soucred_id + 'name')[-1].text
            time.sleep(1)
            self.driver.swip_up()
            time.sleep(2)
            second = self.driver.find_ids(soucred_id + 'name')[-1].text
            if first == second:
                self.driver.find_id(soucred_id + 'btnBack').click()
                break
            else:
                pass
            time.sleep(2)
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

    def test_o(self):
        #点击原声素材配音完成后保存草稿箱
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


    # 作品曝光
    @unittest.skip('9.11版本曝光逻辑，不做执行')
    def test_e(self):
        self.driver.find_id(soucred_id + 'gift').click()
        time.sleep(2)
        gold_before = self.driver.find_id(soucred_id + 'gold_count').text
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        while True:
            self.driver.find_id(soucred_id + 'exposure').click()
            try:
                self.driver.find_xpath('知道了')
                self.driver.find_xpath('知道了').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'film_img2').click()
                self.driver.wait_id(soucred_id + 'follow_ta')
                self.driver.Background()
                time.sleep(2)
            except:
                self.driver.find_id(soucred_id + 'btnCancel')
                break
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnCancel').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '曝光成功'
            self.assertEqual(toast, check_toast, msg='曝光toast内容校验不一致')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'gift').click()
        time.sleep(2)
        gold_after = self.driver.find_id(soucred_id + 'gold_count').text
        time.sleep(2)
        self.assertNotEqual(gold_before,gold_after,msg='5000金币曝光后金币余额没有更新')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 会员曝光
    @unittest.skip('9.11版本曝光逻辑，不做执行')
    def test_f(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        while True:
            self.driver.find_id(soucred_id + 'exposure').click()
            try:
                self.driver.find_xpath('知道了')
                self.driver.find_xpath('知道了').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'film_img2').click()
                self.driver.wait_id(soucred_id + 'follow_ta')
                self.driver.Background()
                time.sleep(2)
            except:
                self.driver.find_id(soucred_id + 'btnCancel')
                break
            time.sleep(2)
        exposure_before = self.driver.find_id(soucred_id + 'btnSubmit').text
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
            self.driver.find_id(soucred_id + 'exposure').click()
            time.sleep(2)
            exposure_after = self.driver.find_id(soucred_id + 'exposure').text
            self.assertNotEqual(exposure_before,exposure_after,msg= '曝光次数未减少')
        except:
            try:
                self.driver.find_id(soucred_id + 'renew')
                time.sleep(2)
                print('未购买会员，无法免费曝光')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 会员推荐
    @unittest.skip('9.11版本达人推荐逻辑，不做执行')
    def test_g(self):
        try:
            self.driver.find_id(soucred_id + 'recommend')
            self.driver.find_id(soucred_id + 'recommend').click()
            globals()["result"] = True
            return globals()['result']
        except:
            globals()['result'] = False
            return globals()['result']
        time.sleep(2)

    # 不输入内容直接提交
    @unittest.skip('9.11版本达人推荐逻辑，不做执行')
    def test_h(self):
        self.driver.find_id(soucred_id + 'sure').click()
        tip  = self.driver.wait_toast('//android.widget.Toast')
        check = '请输入推荐理由'
        self.assertEqual(tip,check,msg='不输入内容点击提价，toast提示内容校验失败')
        time.sleep(2)

    # 输入字符少于10个字符
    @unittest.skip('9.11版本达人推荐逻辑，不做执行')
    def test_i(self):
        self.driver.find_id(soucred_id + 'content').send_keys('功能测试，请忽略')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'sure').click()
        tip = self.driver.wait_toast('//android.widget.Toast')
        check = '推荐理由不得少于10字'
        self.assertEqual(tip,check,msg='输入小于10个字，toast提示内容校验不一致')
        time.sleep(2)

    # 输入10个字符后点击提交
    @unittest.skip('9.11版本达人推荐逻辑，不做执行')
    def test_j(self):
        self.driver.find_id(soucred_id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('进行功能测试，可忽略')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'sure').click()
        tip = self.driver.wait_toast('//android.widget.Toast')
        check = '推荐成功！若被小编审核通过将会私信通知你哦~'
        self.assertEqual(tip,check,msg='推荐提交成功后toast提示内容校验不一致')
        time.sleep(2)

    # 送礼
    @unittest.skip('9.11版本送礼逻辑，不做执行')
    def test_k(self):
        self.driver.find_id(soucred_id + 'gift').click()
        self.driver.wait_id(soucred_id + 'confirm')
        time.sleep(2)
        self.driver.find_xpath('鲜花').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'confirm').click()
        send_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        self.assertIn(check,send_toast,msg='送礼toast校验失败')
        time.sleep(2)
        self.driver.back()
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
