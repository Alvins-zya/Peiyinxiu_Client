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
        Heads = self.driver.find_ids(self.id + 'userhead')
        for i in range(len(Heads)):
            self.driver.find_ids(self.id + 'userhead')[i].click()
            self.driver.wait_id(self.id + 'fanscount')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(3)

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
    def Video_fullscreen(self):
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
            self.driver.find_id(self.id + 'good_svga').click()
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

    # 曝光界面功能按钮点击
    def Video_exposure_touch(self):
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
        #曝光券
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(1)
        self.driver.find_id(self.id + 'tab1').click()
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        #评论推荐人预览
        self.driver.find_id(self.id + 'tv_preview').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        #充值界面跳转
        self.driver.find_id(self.id + 'img_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'price_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        #曝光价格列表
        prices = self.driver.find_ids(self.id + 'rl')
        for i in range(len(prices) - 1):
            self.driver.find_ids(self.id + 'rl')[i].click()
        time.sleep(2)
        #曝光服务协议
        self.driver.find_id(self.id + 'tv_xieyi').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        #作品曝光要求
        self.driver.find_id(self.id + 'tv_yaoqiu').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        #自定义钻石价格
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('200')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 金币曝光
    def Video_exposure_gold(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'rl').click()
        golds = self.driver.find_id(self.id + 'tv_gold').text
        if int(golds) >= 5000:
            self.driver.find_id(self.id + 'gold_count').click()
        else:
            self.driver.find_id(self.id + 'gold_count').click()
            gold_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '金币余额不足'
            assert check == gold_toast
        self.driver.wait_id(self.id + 'btnBack')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 会员曝光
    def Video_exposure_freevip(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        count = self.driver.find_id(self.id + 'free_count').text
        if count == '当前剩余0次':
            self.driver.find_id(self.id + 'free_count').click()
            exp_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '曝光机会用完'
            assert check == exp_toast
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
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 自定义钻石曝光
    def Video_exposure_diamond(self):
        self.driver.find_id(self.id + 'tv_exposure').click()
        time.sleep(2)
        self.driver.find_ids(self.id + 'rl')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit').send_keys('200')
        time.sleep(1)
        self.driver.find_id(self.id + 'sure').click()
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
                self.driver.find_id(self.id + 'comment_count')
                break
            except:
                self.driver.swip_up()
                self.driver.Background()
                time.sleep(2)
            time.sleep(2)

    # 发送评论
    def Video_comment_send(self):
        self.driver.find_id(self.id + 'tv_comment').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('暖一个！')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'item_comment_video_more')
        time.sleep(2)
        self.driver.find_id(self.id + 'shunxu').click()
        time.sleep(2)


    # 评论举报
    def Video_comment_report(self):
        self.driver.find_ids(self.id + 'item_comment_video_more')[-1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_one').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        check_toast = '举报成功'
        assert toast == check_toast
        time.sleep(2)
        self.driver.find_id(self.id + 'item_comment_video_more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('举报功能测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        toast1 = self.driver.wait_toast('//android.widget.Toast')
        assert toast1 == check_toast
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
                    #素材下载失败/素材已被删除
                    self.driver.wait_toast('//android.widget.Toast')
                    break
                except:
                    try:
                        self.driver.find_id(self.id + 'action')
                        break
                    except:
                        #限制素材进入配音界面显示限制弹窗
                        try:
                            self.driver.find_id(self.id + 'btnSubmit')
                            self.driver.find_id(self.id + 'btnSubmit').click()
                            break
                        except:
                            pass
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(3)
        except Exception as e:
            raise e
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    # 视频详情界面进入素材预览界面
    def Video_source(self):
        self.driver.find_id(self.id + 'tvSource').click()
        self.driver.wait_id(self.id + 'source_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(4)

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
