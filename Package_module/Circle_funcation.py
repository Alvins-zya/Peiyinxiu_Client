#coding=utf-8
'''
圈子功能模块

'''

from Public.Driver_Operate import BaseOperate,resource_id
import time

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
        self.driver.find_id(soucred_id + 'history').click()
        time.sleep(2)

    #进入帖子详情
    def Circle_post_detail(self):
        try:
            self.driver.find_id(soucred_id + 'title')
            self.driver.find_id(soucred_id + 'title').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                self.driver.wait_id(soucred_id + 'userhead')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        except Exception as  e:
            print(e)

    #历史记录帖子删除
    def Circle_history_post_delete(self):
        delete_before = self.driver.find_id(soucred_id + 'title').text
        el = self.driver.find_id(soucred_id + 'title')
        self.driver.Long_Touche(el, 3000)
        time.sleep(1)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
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
            self.driver.find_id(soucred_id + 'empty_text')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            self.driver.find_id(soucred_id + 'tv_right').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
                self.driver.find_id(soucred_id + 'btnBack').click()
            except:
                self.driver.find_id(soucred_id + 'btnSubmit').click()
                time.sleep(2)
                try:
                    self.driver.find_id(soucred_id + 'title')
                    raise ('帖子清空失败')
                except:
                    pass
                self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    # 圈子主界面帖子转发
    def Circle_Post_forward(self):
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.802)
        self.driver.wait_id(soucred_id + 'group_chat')
        self.driver.find_id(soucred_id + 'group_chat').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'name')
        self.driver.find_id(soucred_id + 'name').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)


    #圈子列表界面点击圈子标签
    def Cricle_tag(self):
        tag_name = self.driver.find_id(soucred_id + 'tag').text
        self.driver.find_id(soucred_id + 'tag').click()
        self.driver.wait_id(soucred_id + 'img_subscribe')
        tag_detail_name = self.driver.find_id(soucred_id + 'topic_name').text
        assert tag_detail_name == tag_name
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    #圈子热门帖子列表界面点击评论按钮进入帖子详情
    def test_c_c(self):
        self.driver.find_id(soucred_id + 'comment').click()
        self.driver.wait_id(soucred_id + 'guanzhu')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #圈子热门帖子列表界面点赞
    def test_c_d(self):
        touche_good_before = self.driver.find_id(soucred_id + 'good').text
        self.driver.find_id(soucred_id + 'good').click()
        time.sleep(2)
        touche_good_later = self.driver.find_id(soucred_id + 'good').text
        if int(touche_good_later) > int(touche_good_before):
            pass
        else:
            raise ('点赞数量未变化',touche_good_before,touche_good_later)
        time.sleep(2)

    #圈子热门列表刷新
    def test_c_e(self):
        for i in range(5):
            self.driver.swip_up()
            time.sleep(1)
        #一键返回列表顶部
        self.driver.find_id(soucred_id + 'ivNewsTab').click()
        self.driver.wait_id(soucred_id + 'tv_key_word_help')
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)

    #圈子搜索
    def test_d(self):
        i = 0
        while True:
            self.driver.find_id(soucred_id + 'tv_key_word_help').click()
            try:
                self.driver.wait_id(soucred_id + 'tv')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
            if i == 10:
                break
            else:
                pass
            time.sleep(2)

    #热门话题点击跳转
    def test_d_a(self):
        tvs = self.driver.find_ids(soucred_id + 'tv')
        for i in range(len(tvs)):
            tv_name = self.driver.find_ids(soucred_id + 'tv')[i].text
            self.driver.find_ids(soucred_id + 'tv')[i].click()
            self.driver.wait_id(soucred_id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(soucred_id + 'topic_name').text
            self.assertEqual(tv_detail_name, tv_name, msg='标签名称校验不一致')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)

    #订阅话题
    def test_d_b(self):
        try:
            self.driver.find_id(soucred_id + 'title')
            name = self.driver.find_id(soucred_id + 'title').text
            self.driver.find_id(soucred_id +'title').click()
            self.driver.wait_id(soucred_id + 'img_subscribe')
            tv_detail_name = self.driver.find_id(soucred_id + 'topic_name').text
            self.assertEqual(tv_detail_name, name, msg='标签名称校验不一致')
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)
        except:
            pass

    #话题搜索
    def test_d_c(self):
        self.driver.find_id(soucred_id + 'et_key_word').clear()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'et_key_word').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'title')
        self.driver.find_id(soucred_id + 'title').click()
        self.driver.wait_id(soucred_id + 'img_subscribe')
        check = '测试'
        tv_detail_name = self.driver.find_id(soucred_id + 'topic_name').text
        self.assertIn(check, tv_detail_name, msg='标签名称校验不一致')
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #圈子主界面发帖-图文贴
    def test_e(self):
        self.driver.find_id(soucred_id + 'send').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'image_tie').click()
        time.sleep(2)

    #图文贴内容
    def test_e_a(self):
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了！”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了！”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)

    #添加图片
    def test_e_b(self):
        self.driver.find_id(soucred_id + 'add_img').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_photo').click()
        self.driver.wait_id(soucred_id + 'imgQueue')
        num = self.driver.find_ids(soucred_id + 'cb_select_tag')
        for i in range(len(num)):
            self.driver.find_ids(soucred_id + 'cb_select_tag')[i].click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
                break
            except:
                pass
            time.sleep(1)
        self.driver.find_id(soucred_id + 'next_step_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'del').click()
        time.sleep(2)
        #拍照
        self.driver.find_id(soucred_id + 'add_img').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_take_photo').click()
        time.sleep(5)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id('com.oppo.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.oppo.camera:id/done_button').click()
            self.driver.wait_id(soucred_id + 'right_icon1')
        except:
            self.driver.back()
        time.sleep(2)

    #添加话题
    def test_e_c(self):
        self.driver.find_id(soucred_id + 'add_topic').click()
        self.driver.wait_id(soucred_id + 'tv')
        self.driver.find_id(soucred_id + 'et_key_word').send_keys('一个人的话题')
        time.sleep(1)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'title')
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)

    #艾特好友
    def test_e_d(self):
        self.driver.find_id(soucred_id + 'at').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'filter_edit').send_keys('16461675')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'no_data_msg')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            self.driver.find_id(soucred_id + 'name').click()
        time.sleep(2)

    #发布图文帖
    def test_e_e(self):
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            self.driver.wait_id(soucred_id + 'img_subscribe')
            self.driver.swip_down()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'content').click()
            self.driver.wait_id(soucred_id + 'editContent')
        except:
            self.driver.find_id(soucred_id + 'btnBack').click()
            raise ('帖子发布失败')
        time.sleep(2)


    #删除图文帖
    def test_e_f(self):
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.885)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        self.assertEqual(del_toast, check)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    #发布语音帖
    def test_f(self):
        self.driver.find_id(soucred_id + 'send').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'voice_tie').click()
        time.sleep(2)

    #语音帖内容
    def test_f_a(self):
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了！”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)

    #录制语音
    def test_f_b(self):
        self.driver.find_id(soucred_id + 'dubbing').click()
        time.sleep(10)
        self.driver.find_id(soucred_id + 'dubbing').click()
        time.sleep(2)
        #试听
        self.driver.find_id(soucred_id + 'review').click()
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        #重录
        self.driver.find_id(soucred_id + 'reDo').click()
        time.sleep(2)
        date_check = '00:00'
        el = self.driver.find_id(soucred_id + 'time').text
        if el == date_check:
            pass
        else:
            raise ('点击重录按钮音轨没有恢复默认状态')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dubbing').click()
        time.sleep(10)
        self.driver.find_id(soucred_id + 'dubbing').click()
        time.sleep(2)

    #语音帖发布界面
    def test_f_c(self):
        self.driver.find_id(soucred_id + 'tv_right').click()
        self.driver.wait_id(soucred_id + 'play')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('有什么好说的呢？么有哦~')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        time.sleep(10)
        self.driver.find_id(soucred_id + 'change_cover').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_photo').click()
        self.driver.wait_id(soucred_id + 'photo_wall_item_photo')
        self.driver.find_id(soucred_id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'add_topic').click()
        self.driver.wait_id(soucred_id + 'tv')
        self.driver.find_id(soucred_id + 'et_key_word').send_keys('一个人的话题')
        time.sleep(1)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'title')
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'at').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'filter_edit').send_keys('16461675')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'no_data_msg')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            self.driver.find_id(soucred_id + 'name').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            self.driver.wait_id(soucred_id + 'img_subscribe')
        except:
            self.driver.find_id(soucred_id + 'btnBack').click()
            raise ('帖子发布失败')
        time.sleep(2)


    # 删除语音帖
    def test_f_d(self):
        self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').click()
        self.driver.wait_id(soucred_id + 'editContent')
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.885)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        self.assertEqual(del_toast, check)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    #圈子主页发布听评帖
    def test_g(self):
        self.driver.find_id(soucred_id + 'send').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'film_tie').click()
        time.sleep(2)

    #听评帖内容
    def test_g_a(self):
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('迷蒙中睁开眼睛，面前是一群陌生人。'
                                                              '“快看啊！孩子睁眼睛了！”一个中年妇女的声音。'
                                                              '“真是啊，眼珠还一直转，好像能看见什么似的。”一个男人附和着说。'
                                                              '“胡说什么？刚出生的孩子什么也看不见的，没有常识。”中年妇女训斥着一脸笑意的男人。'
                                                              '张明费了很大的劲才把一双手举起来，这个小手都盖不住中年妇女的鼻子，小胳膊瞬间被中年妇女牵在手里，柔弱的好像一用劲就会被弄断。'
                                                              '这时人群中有人说：“这孩子一定是饿了，赶快喂孩子点奶吃。”'
                                                              '就这样自己被送到一个年轻女人的怀里。'
                                                              '张明心里一下子明白了，我重新投胎了，我不是以前的张明了。'
                                                              '一、有秘密的孩子'
                                                              '张家三代单传，还真盼来了一个胖小子，孩子的爷爷奶奶整天高兴的合不拢嘴，又查字典又查笔画的给大孙子起了一个比较雅静的名字张浩思。'
                                                              '小浩思身体健康、好玩好动，从出生到三岁从来都没有生过什么病，给大人减少了很多的麻烦，浩思的爸爸妈妈一直从事个体货物运输，'
                                                              '从没有因为孩子的事耽误过一天生意，生了这样一个省心的孩子该有多福气啊？可就是有一点让浩思的爷爷奶奶犯了合计。'
                                                              '夏季的一天中午，小浩思沉沉的睡着午觉，爷爷奶奶悄悄的去外面忙些园子里的农活，回来后蹑手蹑脚的怕惊醒他。'
                                                              '“我就这样来这了？秀秀去了哪里？我怎么才能找到她啊！”一个压抑的童音在自言自语，声音中透露着一种极度的悲伤和难过。'
                                                              '爷爷和奶奶好奇的顺着声音看去，原来是小浩思独自在卫生间自说自话，小肩膀竟不停的耸动着，明明就是在哭泣，'
                                                              '小手还不停的在镜子上写着什么，要是按笔划来看，就是他口中的秀秀这两个字。'
                                                              '两个老人一看之下有点发蒙，一个三岁的孩子怎么像有什么心事一样，谁也没有教过他写字啊？谁是秀秀啊？'
                                                              '两个老人看孩子发现了自己，爷爷索性就直接开了口：“浩思啊，谁惹你了？谁是秀秀啊？你刚才写什么字呢？”'
                                                              '“我没有写什么啊，我在画着玩。我不认识什么秀秀啊！”小浩思忽闪着大眼睛奶声奶气的说着，一脸的纯真无邪。'
                                                              '回想自己孙儿真的是乖巧的可爱，可细一想就会发现他超越同龄孩子的聪明。小浩思的父母没有时间照顾他，'
                                                              '他一直被爷爷奶奶带着，农村的男孩子不怎么娇惯，磕着碰着是家常便饭，'
                                                              '可是小浩思没有摔过跟头、没有被烫着烧着过、没有被同龄小孩子打过、没有被什么猫呀狗呀的咬过、没有发生过任何足以弄伤自己的事。')
        time.sleep(2)

    #听评帖添加作品
    def test_g_b(self):
        self.driver.find_id(soucred_id + 'add_img').click()
        self.driver.wait_id(soucred_id + 'filmBg')
        self.driver.find_id(soucred_id + 'myLike').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'filmBg')
        self.driver.find_id(soucred_id + 'filmBg').click()
        self.driver.wait_id(soucred_id + 'playbtn')
        self.driver.find_id(soucred_id + 'btnSelect').click()
        time.sleep(2)

    #发布听评帖
    def test_g_c(self):
        self.driver.find_id(soucred_id + 'add_topic').click()
        self.driver.wait_id(soucred_id + 'tv')
        self.driver.find_id(soucred_id + 'et_key_word').send_keys('一个人的话题')
        time.sleep(1)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'title')
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'at').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'filter_edit').send_keys('16461675')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'no_data_msg')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            self.driver.find_id(soucred_id + 'name').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            self.driver.wait_id(soucred_id + 'img_subscribe')
        except:
            self.driver.find_id(soucred_id + 'btnBack').click()
            raise ('帖子发布失败')
        time.sleep(2)

    # 删除听评帖
    def test_g_d(self):
        self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').click()
        self.driver.wait_id(soucred_id + 'editContent')
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.885)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '帖子已被删除'
        self.assertEqual(del_toast, check)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)


