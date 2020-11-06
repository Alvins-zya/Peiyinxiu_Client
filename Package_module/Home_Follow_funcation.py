#coding=utf-8
'''
首页发现界面功能封装
'''
from Public.Driver_Operate import BaseOperate,resource_id
import time

class Follow():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #首页关注主界面
    def Follow_jump(self):
        self.driver.find_id(self.id + 'ivCirclesTab').click()
        self.driver.wait_id(self.id + 'musicPlayView')
        time.sleep(2)

    #语聊推荐列表
    def Follow_chat_list(self):
        self.driver.find_id(self.id + 'musicPlayView').click()
        self.driver.wait_id(self.id + 'item_theme_image')
        self.driver.find_id(self.id + 'item_theme_image').click()
        self.driver.wait_download(self.id + 'user_list')
        self.driver.find_id(self.id +'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'item_theme_image').click()
        time.sleep(2)


    #首页关注列表进入个人空间
    def Follow_person_zoom(self):
        name = self.driver.find_id(self.id + 'textView').text
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        Name = self.driver.find_id(self.id + 'username').text
        assert name == Name
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #视频播放
    def Follow_play_video(self):
        while True:
            try:
                self.driver.find_id(self.id + 'play')
                self.driver.find_id(self.id + 'play').click()
                self.driver.wait_download(self.id + 'play')
                time.sleep(2)
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        while True:
            try:
                self.driver.find_id(self.id + 'content').click()
                try:
                    self.driver.wait_id(self.id + 'tv_video_detail_title')
                    self.driver.find_id(self.id + 'btnBack').click()
                    time.sleep(2)
                    break
                except:
                    self.driver.find_id(self.id + 'btnBack').click()
                    time.sleep(2)
                    self.driver.swip_up()
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)

    #关注界面作品分享
    def Follow_work_share(self):
        count =  self.driver.find_id(self.id + 'item_attention_share_num').text
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)

        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)

        # QQ空间
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)

        # 点击新浪
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.323, self.y * 0.712)
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
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.833)
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

        # 点击下载视频到本地
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.807)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.311, self.y * 0.843)
        # 先判断点击是否为下载按钮，若是复制按钮则会toast提示，不是复制按钮则判断是否有非会员弹窗，不是则直接等待作品下载完成
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '存在'
            if check in toast:
                print(toast)
        except:
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                try:
                    self.driver.wait_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                except:
                    pass


        # 点击复制链接
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.493, self.y * 0.833)
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
        self.driver.find_id(self.id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.88, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.87, self.y * 0.833)
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
            # 点击取消分享弹窗按钮
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.937)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.947)
        time.sleep(2)


    #关注界面送礼9.12版本不再支持送礼
    # def test_h(self):
    #     while True:
    #         try:
    #             self.driver.find_id(self.id + 'item_attention_praise')
    #             self.driver.find_id(self.id + 'item_attention_praise').click()
    #             break
    #         except:
    #             self.driver.swip_up()
    #             time.sleep(2)
    #     time.sleep(4)
    #     self.driver.find_id(self.id + 'confirm').click()
    #     self.driver.wait_toast('//android.widget.Toast')
    #     time.sleep(2)
    #     self.driver.swip_up()
    #     time.sleep(2)



    # 关注界面点赞
    def Follow_good(self):
        while True:
            try:
                self.driver.find_id(self.id + 'item_attention_praise')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        num = self.driver.find_id(self.id + 'item_attention_praise').text
        self.driver.find_id(self.id + 'item_attention_praise').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            pass
        new_Praise = self.driver.find_id(self.id + 'item_attention_praise').text
        assert new == new_Praise
        time.sleep(2)

    #关注界面评论作品
    def Follow_comment(self):
        while True:
            try:
                self.driver.find_id(self.id + 'item_attention_comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'item_attention_comment_count').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('日常评论下！^.^')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        try:
            toast =  self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='关注界面发送评论提示校验不一致')
        except:
            raise ('未检测到评论发送toast提示')
        time.sleep(2)

    #关注界面素材预览-配音
    def Follow_source(self):
        while True:
            try:
                self.driver.find_id(self.id + 'action')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        while True:
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
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

    #设置特别关注
    def Follow_special_focus_setting(self):
        while True:
            try:
                self.driver.find_id(self.id + 'more')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        #用户动态开关
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x *0.5,self.y *0.794)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.829)
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #特别关注
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='特别关注toast提示检验失败')
        except:
            raise ('未检测到特别关注toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'ivCirclesTab').click()
        self.driver.wait_id(self.id + 'rl')
        self.driver.find_id(self.id + 'rl').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        name = self.driver.find_id(self.id +'textView').text
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '取消'
            self.assertIn(check, toast, msg='取消特别关注toast提示检验失败')
        except:
            raise ('未检测到特别关注toast提示')
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath(name)
            raise ('特别关注取消特别关注后刷新界面依然显示用户信息')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)