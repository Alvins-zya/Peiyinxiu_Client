#coding=utf-8
from Public.Driver_Operate import BaseOperate,resource_id
import time
class Live():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id
    def Live_list(self):
        while True:
            try:
                self.driver.find_xpath('频道')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854 ,self.y * 0.197,self.x * 0.249,self.y *0.197)
                    time.sleep(2)
                elif self.y >=2280:
                    self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
                    time.sleep(2)

        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        self.driver.find_id(self.id + 'create')

    #进入语聊间
    def Live_Into_live_detail(self):
        self.driver.find_id(self.id + 'fram').click()
        self.driver.wait_id(self.id + 'gift_value')

    #切换语聊间
    def Live_Switch_live(self):
        for i in range(3):
            self.driver.swip_left()
            self.driver.wait_id(self.id + 'gift_value')
            time.sleep(2)

    #语聊间创建界面编辑
    def LiveCreate_live_edit(self):
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
    def LiveCreate_Room(self):
        self.driver.find_id(self.id + 'create').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'check_box').click()
        self.driver.find_id(self.id +'start_live').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        self.driver.wait_id(self.id + 'name')

    #闭麦
    def Live_Close_mic(self):
        try:
            self.driver.find_id(self.id + 'mic_tag')
        except:
            self.driver.find_id(self.id + 'home_microphone1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'mic_own_control').click()
            self.driver.wait_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'mic_tag').click()
        time.sleep(2)

    #开麦
    def Live_Open_mic(self):
        try:
            self.driver.find_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'home_microphone1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'mic_own_control').click()
            self.driver.wait_not_id(self.id + 'mic_tag')
            self.driver.find_id(self.id + 'name').click()
        except:
            pass
        time.sleep(2)

    #查看头像简介
    def Live_Head_Introduction(self):
        el = self.driver.find_id(self.id + 'userhead')
        self.driver.Long_Touche(el,3000)
        try:
            self.driver.find_id(self.id + 'user_id')
            self.driver.find_id(self.id + 'icon_close').click()
        except:
            raise ('长按麦位用户头像未显示简介弹窗')
        time.sleep(2)

    #送礼
    def Live_gift(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'gift_img')
        time.sleep(2)
        self.driver.find_xpath(self.id + '鲜花').click()
        self.driver.find_id(self.id + 'right_view').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_view').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(2)
        self.driver.tap(self.x * 0.5 ,self.y * 0.5)
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
        self.driver.Long_Touche(el,3000)
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
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'cash_num').send_keys('0.1')
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
        elif self.y >=2280:
            self.driver.tap(self.x * 0.295, self.y * 0.812)
            time.sleep(2)
        #私信
        self.driver.tap(self.x * 0.122, self.y * 0.912)
        self.driver.wait_id(self.id + 'group_chat')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(3)

    #语聊间私信
    def Live_persion_notice(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.499, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)



    #语聊间黑名单
    def Live_blacklist(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.698, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    #设置房管
    def Live_Manager(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.894, self.y * 0.812)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    #随机抽选游戏
    def Live_Games(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_turntable').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'customize_back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_random').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'random_close').click()
        time.sleep(2)

    #麦位数量
    def Live_Mic_count(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.295, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'check2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    #pia戏
    def Live_Pia(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.496, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'iv_close').click()
        time.sleep(2)

    #组Cp
    def Live_Cp(self):
        self.driver.find_id(self.id + 'function_more').click()
        time.sleep(2)
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.704, self.y * 0.908)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_check').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #公告
    def Live_Notice(self):
        self.driver.find_id(self.id + 'marquee').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_sure').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_title').send_keys('哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'et_content').send_keys('哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_save').click()
        time.sleep(2)

    #房间成员列表
    def Live_Members(self):
        try:
            self.driver.find_id(self.id + 'pack_up').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'count').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'room_user').click()
        time.sleep(2)
        self.driver.find_id(self.id +'fast_room_check').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        self.driver.wait_xpath('移除')
        self.driver.find_xpath('申请').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'fast_room_check').click()
        time.sleep(2)
        self.driver.find_id(self.id +'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'close').click()
        time.sleep(2)

    #房间详情
    def Live_Room_detail(self):
        self.driver.find_id(self.id + 'user_list').click()
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

    #房间背景音音乐
    def Live_Music(self):
        self.driver.find_id(self.id + 'function_joke_articles').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'title')
        except:
            self.driver.find_id(self.id +'add_music').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'rl').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'previous').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'modify').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'music_list').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #语聊任务
    def Live_Tasks(self):
        self.driver.find_id(self.id + 'img').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)


    #退出语聊间
    def Live_Room_Exit(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'outLive')
            self.driver.find_id(self.id + 'outLive').click()
        except:
            pass
        time.sleep(2)




