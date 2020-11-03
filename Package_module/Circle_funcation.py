#coding=utf-8
'''
圈子功能模块

'''

from Public.Driver_Operate import BaseOperate,resource_id
import time
file = open('topic_words.txt','r',encoding='UTF-8')
class Circle():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id
    #进入圈子界面
    def Circle_into(self):
        self.driver.find_id(self.id + 'ivNewsTab').click()
        time.sleep(2)

    #帖子浏览历史
    def Circle_post_history(self):
        self.driver.find_id(self.id + 'history').click()
        time.sleep(2)

    #进入帖子详情
    def Circle_post_detail(self):
        try:
            self.driver.find_id(self.id + 'title').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.wait_id(self.id + 'userhead')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        except Exception as  e:
            print(e)

    #历史记录帖子删除
    def Circle_post_history_delete(self):
        delete_before = self.driver.find_id(self.id + 'title').text
        el = self.driver.find_id(self.id + 'title')
        self.driver.Long_Touche(el, 3000)
        time.sleep(1)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_xpath(delete_before)
            raise ('帖子长按删除失败')
        except:
            pass
        time.sleep(2)

    #清空帖子浏览记录
    def Circle_history_clear(self):
        try:
            self.driver.find_id(self.id + 'empty_text')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'tv_right').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
                self.driver.find_id(self.id + 'btnBack').click()
            except:
                self.driver.find_id(self.id + 'btnSubmit').click()
                time.sleep(2)
                try:
                    self.driver.find_id(self.id + 'title')
                    raise ('帖子清空失败')
                except:
                    pass
                self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 圈子主界面帖子转发
    def Circle_Post_forward(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.802)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.829)
        self.driver.wait_id(self.id + 'group_chat')
        self.driver.find_id(self.id + 'group_chat').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'name')
        self.driver.find_id(self.id + 'name').click()
        self.driver.wait_id(self.id + 'btn_change_input_mode')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子列表界面点击圈子标签
    def Circle_tag(self):
        tag_name = self.driver.find_id(self.id + 'tag').text
        self.driver.find_id(self.id + 'tag').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        tag_detail_name = self.driver.find_id(self.id + 'topic_name').text
        assert tag_detail_name == tag_name
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #圈子热门帖子列表界面点击评论按钮进入帖子详情
    def Circle_comment_detail(self):
        self.driver.find_id(self.id + 'comment').click()
        self.driver.wait_id(self.id + 'guanzhu')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子热门帖子列表界面点赞
    def Circle_good(self):
        touche_good_before = self.driver.find_id(self.id + 'good').text
        self.driver.find_id(self.id + 'good').click()
        time.sleep(2)
        touche_good_later = self.driver.find_id(self.id + 'good').text
        if int(touche_good_later) > int(touche_good_before):
            pass
        else:
            raise ('点赞数量未变化',touche_good_before,touche_good_later)
        time.sleep(2)

    # 点击帖子内容进入帖子详情
    def Circle_content(self):
        self.driver.find_id(sourced_id + 'content').click()
        self.driver.wait_id(sourced_id + 'right_icon1')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #圈子热门列表刷新
    def Circle_refresh(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(1)
        #一键返回列表顶部
        self.driver.find_id(self.id + 'ivNewsTab').click()
        self.driver.wait_id(self.id + 'tv_key_word_help')
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)

    #圈子搜索界面显示
    def Circle_search(self):
        i = 0
        while True:
            self.driver.find_id(self.id + 'tv_key_word_help').click()
            try:
                self.driver.wait_id(self.id + 'tv')
                break
            except:
                #界面显示失败时返回上一界面再进
                self.driver.find_id(self.id + 'btnBack').click()
            #尝试10次后停止以上操作
            if i == 10:
                break
            else:
                pass
            time.sleep(2)

    #帖子搜索界面热门话题点击跳转
    def Circle_hot_tv_jump(self):
        tvs = self.driver.find_ids(self.id + 'tv')
        for i in range(len(tvs)):
            tv_name = self.driver.find_ids(self.id + 'tv')[i].text
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
            self.assertEqual(tv_detail_name, tv_name, msg='标签名称校验不一致')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)

    #已订阅的话题
    def Circle_topic_Subscribes(self):
        try:
            self.driver.find_id(self.id + 'title')
            name = self.driver.find_id(self.id + 'title').text
            self.driver.find_id(soucred_id +'title').click()
            self.driver.wait_id(self.id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
            self.assertEqual(tv_detail_name, name, msg='标签名称校验不一致')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
        except:
            pass

    #话题搜索
    def Circle_topic_search(self):
        self.driver.find_id(self.id + 'et_key_word').clear()
        time.sleep(1)
        self.driver.find_id(self.id + 'et_key_word').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'title')
        self.driver.find_id(self.id + 'title').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        check = '测试'
        tv_detail_name = self.driver.find_id(self.id + 'topic_name').text
        self.assertIn(check, tv_detail_name, msg='标签名称校验不一致')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #圈子主界面发帖-图文贴
    def Circle_Home_word_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'image_tie').click()
        time.sleep(2)

    #图文贴内容
    def Circle_word_topic_content(self):
        topic_read = file.read()
        self.driver.find_id(self.id + 'content').send_keys(topic_read,'\n')
        time.sleep(2)
        self.driver.find_id(self.id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys(topic_read,'\n')
        time.sleep(2)

    #添加图片
    def Circle_word_topic_add_image(self):
        self.driver.find_id(self.id + 'add_img').click()
        time.sleep(2)

    #选择图片
    def Circle_word_topic_select_image(self):
        self.driver.find_id(self.id + 'tv_photo').click()
        self.driver.wait_id(self.id + 'imgQueue')
        num = self.driver.find_ids(self.id + 'cb_select_tag')
        for i in range(len(num)):
            self.driver.find_ids(self.id + 'cb_select_tag')[i].click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
                break
            except:
                pass
            time.sleep(1)
        self.driver.find_id(self.id + 'next_step_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'del').click()
        time.sleep(2)

    # 拍照
    def Circle_word_topic_photo(self):
        self.driver.find_id(self.id + 'tv_take_photo').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
        except:
            pass
        time.sleep(2)
        try:
            self.driver.wait_sys('始终允许')
        except:
            pass
        time.sleep(5)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id('com.oppo.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.oppo.camera:id/done_button').click()
            self.driver.wait_id(self.id + 'right_icon1')
        except:
            try:
                self.driver.find_id('com.huawei.camera:id/shutter_button')
                self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.huawei.camera:id/done_button').click()
            except:
                self.driver.back()
        time.sleep(2)

    #添加话题
    def Circle_word_topic_insert_topic(self):
        self.driver.find_id(self.id + 'add_topic').click()
        self.driver.wait_id(self.id + 'tv')
        self.driver.find_id(self.id + 'et_key_word').send_keys('一个人的话题')
        time.sleep(1)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'title')
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)

    #添加好友
    def Circle_word_topic_at(self):
        self.driver.find_id(self.id + 'at').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys('16461675')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'no_data_msg')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

    #发布图文帖
    def Circle_word_topic_release(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            self.driver.wait_id(self.id + 'img_subscribe')
            self.driver.swip_down()
            time.sleep(2)
            self.driver.find_id(self.id + 'content').click()
            self.driver.wait_id(self.id + 'editContent')
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            raise ('帖子发布失败')
        time.sleep(2)

    #删除图文帖
    def Circle_word_topic_delete(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.885)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.829)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        assert del_toast == check
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #发布语音帖
    def Circle_Home_Voice_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'voice_tie').click()
        time.sleep(2)

    #语音帖内容
    def Circle_voice_topic(self):
        self.Circle_word_topic_content()

    #录制语音
    def Circle_voice_topic_record(self):
        self.driver.find_id(self.id + 'dubbing').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #试听
        self.driver.find_id(self.id + 'review').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

        #重录
        self.driver.find_id(self.id + 'reDo').click()
        time.sleep(2)
        date_check = '00:00'
        el = self.driver.find_id(self.id + 'time').text
        if el != date_check:
            raise ('点击重录按钮音轨没有恢复默认状态')
        time.sleep(2)
        self.driver.find_id(self.id + 'dubbing').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)

    #语音帖发布界面
    def Circle_voice_topic_next(self):
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('有什么好说的呢？么有哦~')
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'change_cover').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        self.driver.wait_id(self.id + 'photo_wall_item_photo')
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.Circle_word_topic_insert_topic()
        self.Circle_word_topic_at()

    #圈子主页发布听评帖
    def Circle_Home_listen_topic(self):
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film_tie').click()
        time.sleep(2)

    #听评帖添加作品
    def Circle_listen_insert_work(self):
        self.driver.find_id(self.id + 'add_img').click()
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id(self.id + 'myLike').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'filmBg')
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'playbtn')
        self.driver.find_id(self.id + 'btnSelect').click()
        time.sleep(2)



