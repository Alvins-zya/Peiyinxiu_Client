#coding=utf-8
'''
视频详情界面功能模块方法封装
'''
from Public.Driver_Operate import BaseOperate,resource_id
import time

class Video_detail_function():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    # 首页点击作品封面进入视频详情
    def Home_into_video(self):
        self.driver.find_id(self.id + 'film_img2').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)

    # 点击用户头像进入个人空间
    def Head_into_zoom_back(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(4)

    # 关注
    def Video_follow(self):
        self.driver.find_id(self.id + 'follow_ta').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.find_id(self.id + 'right_icon1')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    # 视频-弹幕开关
    def Video_danmu(self):
        self.driver.find_id(self.id + 'media_danmu_img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(20)
        self.driver.Background()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)

    # 全屏播放
    def test_e(self):
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_fullscreen_open').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)

    # 作品信息
    def Video_title(self):
        video_name = self.driver.find_id(self.id + 'tv_video_detail_title').text
        play_count_inside = self.driver.find_id(self.id + 'tv_video_play_num_in').text
        play_count_out = self.driver.find_id(self.id + 'tv_good').text
        # print('作品名称：',video_name,
        #       '站内播放量:',play_count_inside,
        #       '点赞量:',play_count_out)
        time.sleep(2)

    # 点赞
    def Video_good(self):
        num = self.driver.find_id(self.id + 'tv_good').text
        try:
            self.driver.find_id(self.id + + 'good_svga').click()
            tip = self.driver.wait_toast('//android.widget.Toast')
            check = '恭喜你获得300金币'
            assert tip == check
        except:
            self.driver.find_id(self.id + 'tv_good').click()
        self.driver.wait_id(self.id + 'svgaImageView')
        num1 = self.driver.find_id(self.id + 'tv_good').text
        try:
            assert num != num1
        except Exception as e:
            print(e)
        time.sleep(2)

    # 曝光
    def Video_exposure(self):
        tv_title = self.driver.find_id(self.id + 'tv_video_detail_title').text
        self.driver.find_id(self.id + 'tv_exposure').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        tv_title1 = self.driver.find_id(self.id + 'tv_source_title').text
        try:
            assert tv_title1 == tv_title
        except Exception as e:
            print(e)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_preview').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'img_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'price_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        prices = self.driver.find_ids(self.id + 'rl')
        # peoples = ['40','80','300','500','1000','5000','10000','30000']
        for i in range(len(prices) - 1):
            self.driver.find_ids(self.id + 'rl')[i].click()
            # people = self.driver.find_id(self.id + 'tv_personal_count').text
            # new = re.findall(r'(.*)人',people)
            # str_new = ''.join(new)
            # self.assertIn(str_new,peoples)
            # time.sleep(1)
        time.sleep(2)
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('200')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        Peo_num = self.driver.find_id(self.id + 'tv_personal_count').text
        new1 = re.findall(r'(.*)人', Peo_num)
        str_new1 = ''.join(new1)
        check1 = '24000'
        time.sleep(2)

    # 金币曝光
    def test_g_a(self):
        self.driver.find_id(self.id + 'rl').click()
        golds = self.driver.find_id(self.id + 'tv_gold').text
        if int(golds) >= 5000:
            self.driver.find_id(self.id + 'gold_count').click()
        else:
            self.driver.find_id(self.id + 'gold_count').click()
            gold_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '金币余额不足'
            self.assertIn(check, gold_toast)
        time.sleep(2)

    # 会员曝光
    def test_g_b(self):
        try:
            self.driver.find_id(self.id + 'free_count')
            count = self.driver.find_id(self.id + 'free_count').text
            if count == '当前剩余0次':
                self.driver.find_id(self.id + 'free_count').click()
                exp_toast = self.driver.wait_toast('//android.widget.Toast')
                check = '曝光机会用完'
                self.assertIn(check, exp_toast)
                return None
            self.driver.find_id(self.id + 'free_count').click()
            time.sleep(2)
            try:
                self.driver.find_xpath('会员中心')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        except Exception as e:
            print(e)

    # 自定义钻石曝光
    def test_g_c(self):
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('200')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        Peo_num = self.driver.find_id(self.id + 'tv_personal_count').text
        new = re.findall(r'(.*)人', Peo_num)
        str_new = ''.join(new)
        check = '24000'
        self.assertIn(check, str_new)
        time.sleep(2)
        self.driver.find_id(self.id + 'bottom').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_xpath('钻石余额不足')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'price_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 视频评论
    def Video_comments(self):
        while True:
            try:
                self.driver.find_id(self.id + 'tv_hide')
                self.driver.swip_up()
                time.sleep(2)
                self.driver.Background()
                time.sleep(2)
            except:
                try:
                    self.driver.find_id(self.id + 'tv_shafa')
                    self.driver.swip_up()
                    time.sleep(2)
                    self.driver.Background()
                    time.sleep(2)
                except:
                    try:
                        self.driver.find_id(self.id + 'comment_count')
                        break
                    except:
                        pass
        time.sleep(2)

    # 评论排序
    def Video_comment_sort(self):
        comments = self.driver.find_id(self.id + 'comment_count').text
        num = re.findall(r'共(.*)条评论', comments)
        str_num = ''.join(num)
        if str_num != '1':
            self.driver.find_id(self.id + 'tv_comment').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'editContent').send_keys('暖一个！')
            time.sleep(2)
            self.driver.find_id(self.id + 'btn_send').click()
            self.driver.wait_id(self.id + 'item_comment_video_more')
            time.sleep(2)
            try:
                self.driver.find_xpath('以上为置顶评论')
                Comment = self.driver.find_ids(self.id + 'item_video_common_time')[1].text
                time.sleep(1)
                self.driver.find_id(self.id + 'shunxu').click()
                time.sleep(2)
                Comment1 = self.driver.find_ids(self.id + 'item_video_common_time')[1].text
                assert Comment != Comment1
                time.sleep(2)
            except:
                Comment = self.driver.find_id(self.id + 'item_video_common_time').text
                time.sleep(1)
                self.driver.find_id(self.id + 'shunxu').click()
                time.sleep(2)
                Comment1 = self.driver.find_id(self.id + 'item_video_common_time').text
                assert Comment != Comment1
                time.sleep(2)
        time.sleep(2)

    # 评论举报
    def Video_comment_report(self):
        self.driver.find_id(self.id + 'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_one').click()
        time.sleep(2)
        reason = self.driver.find_id(self.id + 'txtTitle').text
        check = '政治'
        self.assertIn(check, reason, msg='选择的举报理由中未包含政治关键字')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '举报成功'
            self.assertEqual(toast, check_toast, msg='举报toast内容校验不一致')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('举报功能测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check_toast = '举报成功'
            self.assertEqual(toast, check_toast, msg='举报toast内容校验不一致')
        except:
            pass
        time.sleep(2)

    # 评论列表上滑加载
    def Video_comments_load(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'follow_ta').click()
        time.sleep(2)

    # 点击合作配音完成后保存草稿箱
    def Video_Coor_dubbing(self):
        while True:
            try:
                self.driver.find_xpath('配音/合作')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_down()
                time.sleep(2)
                self.driver.find_id(self.id + 'film_img2').click()
                self.driver.Background()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_xpath('配音/合作').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'coor')
            self.driver.find_id(self.id + 'coor').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'action')
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'btnSubmit')
                        self.driver.find_id(self.id + 'btnSubmit').click()
                        break
                    except:
                        pass
            time.sleep(2)
            self.driver.find_id(self.id + 'action').click()
            self.driver.wait_download(self.id + 'title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'complete').click()
            self.driver.wait_id(self.id + 'txtTitle')
            time.sleep(2)
            self.driver.find_id(self.id + 'pri_switch_tv').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'saveToDraft').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'coor')
            self.driver.find_id(self.id + 'close').click()
            time.sleep(2)
        except Exception as e:
            print(e)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'close')
            self.driver.find_id(self.id + 'close').click()
        except:
            pass
        time.sleep(2)

    # 点击原声素材配音完成后保存草稿箱
    def test_i_a(self):
        self.driver.find_id(self.id + 'tvSource').click()
        self.driver.wait_id(self.id + 'source_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'dubbing_fake').click()
        while True:
            try:
                self.driver.find_id(self.id + 'roleall')
                break
            except:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    tip = self.driver.find_id(self.id + 'txtTitle').text
                    print(tip)
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    break
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(self.id + 'roleall').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(self.id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(4)

    # 配音完成后保存草稿箱
    def test_i_b(self):
        while True:
            try:
                self.driver.find_id(self.id + 'tvSource')
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
                self.driver.find_id(self.id + 'film_img2').click()
                self.driver.wait_id(self.id + 'follow_ta')
                self.driver.Background()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'tvSource').click()
        self.driver.wait_id(self.id + 'types_name')
        self.driver.Background()
        time.sleep(2)

    # 素材预览界面配音
    def Video_source_dub(self):
        self.driver.find_id(self.id + 'dubbing_fake').click()
        while True:
            try:
                self.driver.find_id(self.id + 'action')
                break
            except:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                    except:
                        pass
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        pass
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(self.id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'saveToDraft').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'btnCancel')
        try:
            self.driver.find_xpath('退出配音')
            self.driver.find_xpath('退出配音').click()
        except:
            pass
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 作品分享
    def Video_share(self):
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)
        # QQ空间
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)

        # 点击新浪
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        self.driver.wait_xpath('发送')
        time.sleep(2)
        self.driver.find_id('com.sina.weibo:id/titleBack').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('不保存')
            self.driver.find_xpath('不保存').click()
        except:
            pass
        time.sleep(2)

        # 点击私信
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        self.driver.wait_id(self.id + 'filter_edit')
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys("15697802")
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_id(self.id + 'userhead')
            name = self.driver.find_id(self.id + 'name').text
            name2 = '米爱'
            if name == name2:
                self.driver.find_id(self.id + 'name').click()
                self.driver.wait_id(self.id + 'right_icon1')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            else:
                print("未搜索到指定用户")
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
        except(TimeoutException, NoSuchElementException):
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 点击复制链接
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            try:
                self.driver.wait_id(self.id + 'txtContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                pass
        time.sleep(2)

        # 点击转发
        self.driver.find_id(self.id + 'tv_share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.88, self.y * 0.83)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'reprint')
            self.driver.find_id(self.id + 'content').send_keys("不错，转发了！")
            time.sleep(2)
            self.driver.find_id(self.id + 'reprint').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                try:
                    self.driver.find_id(self.id + 'reprint')
                    self.driver.find_id(self.id + 'reprint').click()
                    self.driver.wait_toast('//android.widget.Toast')
                except Exception as  e:
                    print(e)
        except:
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.937)
        time.sleep(2)

    # 切换视频
    def Video_switch(self):
        for i in range(10):
            self.driver.swip_up()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.Background()
            time.sleep(2)
            self.driver.swip_left()
            self.driver.wait_id(self.id + 'followcount')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
