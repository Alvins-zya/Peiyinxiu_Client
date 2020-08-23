#coding=utf-8
from Public.Driver_Operate import BaseOperate,resource_id
import time
class Live_funcation():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入语聊间
    def Into_live_detail(self):
        self.driver.find_id(self.id + 'fram').click()
        self.driver.wait_id(self.id + 'gift_value')

    #切换语聊间
    def Switch_live(self):
        for i in range(3):
            self.driver.swip_left()
            self.driver.wait_id(self.id + 'gift_value')
            time.sleep(2)

    #语聊间创建界面编辑
    def Create_live_edit(self):
        self.driver.find_id(self.id +'create').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id +'confirm').click()
        time.sleep(2)
        self.driver.find_id(self.id +'title').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'title').send_keys('空')
        time.sleep(2)
        self.driver.find_id(self.id + 'tag_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv').click()
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id +'right').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #创建进入语聊间
    def Create_live(self):
        self.driver.find_id(self.id + 'create').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'check_box').click()
        self.driver.find_id(self.id +'start_live').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        self.driver.wait_id(self.id + 'name')

    #查看头像简介
    def Live_Head_Introduction(self):
        el = self.driver.find_id(self.id + 'userhead')
        self.driver.Long_Touche(el,3000)
        try:
            self.driver.find_id(self.id + 'user_id')
            self.driver.find_id(self.id + 'icon_close').click()
        except:
            print('长按麦位用户头像未显示简介弹窗')
        time.sleep(2)

    #礼物弹窗
    def Live_gift(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'gift_img')
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'function_send_gift').click()
        self.driver.wait_id(self.id + 'gift_img')
        self.driver.back()
        time.sleep(2)

    #点赞
    def Live_good(self):
        self.driver.find_id(self.id + 'periscope_view').click()
        time.sleep(2)

    #语聊间发送评论
    def Live_comments(self):
        self.driver.find_id(self.id + 'function_comment_layout').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('这是一个语聊间！')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'home_comment_comments')
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #长按用户名@用户
    def Live_at(self):
        el = self.driver.find_id(self.id + 'username')
        self.driver.Long_Touche(el,2500)
        try:
            self.driver.find_id(self.id + 'editContent')
            content = self.driver.find_id(self.id + 'editContent').text
            check ='@'
            assert check in content
            time.sleep(1)
            self.driver.find_id(self.id + 'btn_send')
            self.driver.wait_id(self.id + 'home_comment_comments')
            self.driver.find_id(self.id + 'name').click()
        except:
            print('长按用户名未出现@')
        time.sleep(2)

    #发红包
    def Live_red(self):
        self.driver.find_id(self.id +'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.097, self.y *0.814)
            time.sleep(2)
            self.driver.find_id(self.id + 'cash_num').send_keys('1')
            time.sleep(1)
            self.driver.find_id(self.id + 'people_num').send_keys('1')
            time.sleep(2)
            self.driver.find_id(self.id + 'generate_red_packet').click()
            time.sleep(2)
            self.driver.find_id(self.id +'btnSubmit').click()
            self.driver.wait_id(self.id +'rl_red')
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_more').click()
            self.driver.wait_id(self.id + 'open_red_packet_btn')
            self.driver.find_id(self.id + 'open_red_packet_btn').click()
            self.driver.wait_id(self.id + 'diamond')
            self.driver.back()
            time.sleep(2)

    #语聊间分享
    def Live_share(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.301, self.y * 0.814)
            time.sleep(2)
            #朋友圈
            self.driver.tap(self.x * 0.097, self.y * 0.814)
            self.driver.wait_xpath('发表')
            self.driver.find_id('com.tencent.mm:id/dn').click()
            time.sleep(3)

    #语聊间私信
    def Live_persion_information(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
            time.sleep(2)
            try:
                self.driver.find_id(self.id +'tab1')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    #语聊间黑名单
    def Live_blacklist(self):

















    #退出语聊间
    def out_live(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'fram')
        time.sleep(1)




