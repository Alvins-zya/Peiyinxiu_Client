# coding = utf-8
import time
import unittest
import random
import datetime
import sys
import os,re
from collections import Counter
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Dubbing9_11.Front import Dubbing

soucred_id = 'com.happyteam.dubbingshow:id/'

class Test_Circle(Dubbing):

    #首页进入圈子主界面
    def test_a(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(soucred_id + 'ivNewsTab')
        self.driver.find_id(soucred_id + 'ivNewsTab').click()
        time.sleep(2)

    #帖子浏览历史记录-单个删除
    def test_b(self):
        self.driver.find_id(soucred_id + 'history').click()
        time.sleep(2)
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
            delete_before = self.driver.find_id(soucred_id + 'title').text
            el = self.driver.find_id(soucred_id + 'title')
            self.driver.Long_Touche(el,3000)
            time.sleep(1)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            time.sleep(2)
            try:
                self.driver.find_xpath(delete_before)
                raise ('帖子长按删除失败')
            except:
                pass
        except Exception as  e:
            print(e)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #帖子浏览历史记录-清空
    def test_b_a(self):
        self.driver.find_id(soucred_id + 'history').click()
        time.sleep(2)
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

    #圈子主页热门帖子列表
    def test_c(self):
        hot_user = self.driver.find_id(soucred_id + 'textView').text
        self.driver.find_id(soucred_id + 'textView').click()
        self.driver.wait_id(soucred_id + 'guanzhu')
        detail_user = self.driver.find_id(soucred_id + 'textView').text
        self.assertEqual(hot_user,detail_user,msg='圈子热门列表用户名与帖子详情用户名不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #圈子主界面帖子转发
    def test_c_a(self):
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        self.driver.tap(self.x * 0.5 , self.y * 0.802)
        self.driver.wait_id(soucred_id + 'group_chat')
        self.driver.find_id(soucred_id + 'group_chat').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'name')
        self.driver.find_id(soucred_id + 'name').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #圈子列表界面点击圈子标签
    def test_c_b(self):
        tag_name = self.driver.find_id(soucred_id + 'tag').text
        self.driver.find_id(soucred_id + 'tag').click()
        self.driver.wait_id(soucred_id + 'img_subscribe')
        tag_detail_name = self.driver.find_id(soucred_id + 'topic_name').text
        self.assertEqual(tag_detail_name,tag_name,msg='圈子标签名称校验不一致')
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


class Test_Society(Dubbing):

    #点击进入社团主界面
    def test_a(self):
        self.driver.find_id(soucred_id + 'society').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)

    #我的社团-检查是否拥有社团
    def test_b(self):
        self.driver.find_id(soucred_id + 'ivMineTab').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'll_fan')
        num = self.driver.find_id(soucred_id + 'societyCount').text
        check = '0'
        if num == check:
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'ivNewsTab').click()
            time.sleep(2)
            return False
        else:
            self.driver.find_id(soucred_id + 'll_society').click()
            time.sleep(2)
            self.driver.wait_id(soucred_id + 'status_icon')
            societys = self.driver.find_ids(soucred_id + 'userName')
            list_society = []
            for i in range(len(societys)):
                title = self.driver.find_ids(soucred_id + 'userName')[i].text
                list_society.append(title)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'ivNewsTab').click()
            time.sleep(2)
            return list_society

    #我的社团点击查看
    def test_b_a(self):
        state = Test_Society().test_b()
        if state == False:
            pass
        else:
            try:
                self.driver.find_id(soucred_id + 'more_img')
                self.driver.find_id(soucred_id + 'more_img').click()
            except:
                pass
            time.sleep(2)
            for item in state:
                self.driver.find_xpath(item).click()
                self.driver.wait_id(soucred_id + 'btn_change_input_mode')
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)

    #我的社团聊天-文字
    def test_b_b(self):
        self.driver.find_id(soucred_id + 'time').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        select = random.choice('社团聊天文字测试')
        self.driver.find_id(soucred_id + 'editContent').send_keys(select)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_send').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            raise (toast)
        except:
            self.driver.wait_id(soucred_id + 'content')
            check = self.driver.find_ids(soucred_id + 'content')[-1].text
            self.assertEqual(select, check, msg='发送文字校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团聊天-语音
    def test_b_c(self):
        self.driver.find_id(soucred_id + 'time').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_id(soucred_id + 'btn_change_input_mode').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'btn_record_voice')
        self.driver.Long_Touche(el,10000)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            raise (toast)
        except:
            self.driver.wait_id(soucred_id + 'btn_play_sound_content_layout')
            self.driver.find_ids(soucred_id + 'btn_play_sound_content_layout')[-1].click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                raise (toast)
            except:
                pass
        time.sleep(2)
        #发送60s语音
        self.driver.Long_Touche(el, 60000)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            raise (toast)
        except:
            self.driver.wait_id(soucred_id + 'btn_play_sound_content_layout')
            self.driver.find_ids(soucred_id + 'btn_play_sound_content_layout')[-1].click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                raise (toast)
            except:
                pass
        time.sleep(2)
        #录制语音过程中上滑取消
        self.driver.Long_press_move(el, self.x * 0.5, self.y * 0.5)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团聊天-发送表情
    def test_b_d(self):
        self.driver.find_id(soucred_id + 'time').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_id(soucred_id + 'btn_send_smile').click()
        time.sleep(2)
        emoji = self.driver.find_ids(soucred_id + 'emojicon_icon')
        for i in range(len(emoji)):
            self.driver.find_ids(soucred_id + 'emojicon_icon')[i].click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_send').click()
        self.driver.wait_id(soucred_id + 'content')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团聊天-其它按钮
    def test_b_e(self):
        self.driver.find_id(soucred_id + 'time').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_id(soucred_id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'photo').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'cb_select_tag').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'next_step_tv').click()
        self.driver.wait_id(soucred_id + 'chat_image')
        time.sleep(2)
        # 拍照发送私信信息
        self.driver.find_id(soucred_id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'camera').click()
        time.sleep(4)
        try:
            self.driver.find_id('com.oppo.camera:id/shutter_button')
            self.driver.find_id('com.oppo.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.oppo.camera:id/done_button').click()
        except:
            try:
                self.driver.find_id('com.android.camera:id/shutter_button').click()
                time.sleep(3)
                self.driver.find_id('com.android.camera:id/done_button').click()
            except:
                pass
        self.driver.wait_id(soucred_id + 'chat_image')
        time.sleep(2)
        # 发送作品
        self.driver.find_id(soucred_id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'film').click()
        self.driver.wait_id(soucred_id + 'filmBg')
        self.driver.find_id(soucred_id + 'myLike').click()
        self.driver.wait_id(soucred_id + 'filmBg')
        self.driver.find_id('filmBg').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'btnSelect').click()
        self.driver.wait_id(soucred_id + 'chat_film_title')
        time.sleep(2)
        # 发送红包
        self.driver.find_id(soucred_id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'redpacket').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'cash_num').send_keys('0.1')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'people_num').send_keys('1')
        time.sleep(3)
        self.driver.find_id(soucred_id + 'generate_red_packet').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'red_packet')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'red_packet').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'open_red_packet_btn').click()
        self.driver.wait_id(soucred_id + 'diamond')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团-活动-每日活动
    def test_c(self):
        self.driver.find_id(soucred_id + 'time').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        self.driver.find_xpath('活动').click()
        time.sleep(2)
        title = self.driver.find_id(soucred_id + 'desc').text
        if title == '给社团成员的作品送礼2次':
            # 点赞两次
            self.driver.find_id(soucred_id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'btn_close')
                self.driver.find_id(soucred_id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('给社团成员的作品送礼2次')
            except:
                self.driver.wait_id(soucred_id + 'filmBg')
                self.driver.find_ids(soucred_id + 'filmBg')[0].click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'gift').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_ids(soucred_id + 'filmBg')[1].click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'gift').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '评论社团成员的作品2次':
            # 社团作品评论两次
            self.driver.find_id(soucred_id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'btn_close')
                self.driver.find_id(soucred_id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('评论社团成员的作品2次')
            except:
                self.driver.wait_id(soucred_id + 'filmBg')
                self.driver.find_ids(soucred_id + 'filmBg')[0].click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'comment').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'editContent').send_keys('作品评论')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btn_send').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    self.assertIn(check_toast, toast, msg='评论发送失败')
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_ids(soucred_id + 'filmBg')[1].click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'comment').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'editContent').send_keys('作品评论')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btn_send').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    check_toast = '发送成功'
                    self.assertIn(check_toast, toast, msg='评论发送失败')
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.swip_up()
                time.sleep(2)
        elif title == '与社团成员完成合作作品':
            # 完成社团合作
            self.driver.find_id(soucred_id + 'task_box').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'btn_close')
                self.driver.find_id(soucred_id + 'btn_close').click()
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_xpath('与社团成员完成合作作品')
            except:
                self.driver.wait_id(soucred_id + 'filmBg')
                self.driver.find_xpath('求合作').click()
                self.driver.wait_id(soucred_id + 'btnCooperate')
                self.driver.find_id(soucred_id + 'btnCooperate').click()
                while True:
                    try:
                        self.driver.find_id(soucred_id + 'btnSubmit')
                        self.driver.find_id(soucred_id + 'btnSubmit').click()
                        break
                    except:
                        try:
                            self.driver.find_id(soucred_id + 'action')
                            break
                        except:
                            pass
                self.driver.find_id(soucred_id + 'action').click()
                self.driver.wait_download(soucred_id + 'title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'complete').click()
                self.driver.wait_id(soucred_id + 'pri_switch_tv')
                self.driver.swip_up()
                self.driver.find_id(soucred_id + 'check_box_add_square').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'uploadbtn').click()
                self.driver.wait_download(soucred_id + 'down')
                self.driver.find_id(soucred_id + 'ivNewsTab').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'society').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'time').click()
                self.driver.wait_id(soucred_id + 'btn_change_input_mode')
                self.driver.find_xpath('活动').click()
                time.sleep(2)

    #我的社团-活动-历时活动
    def test_d(self):
        self.driver.swip_up()
        time.sleep(2)

        # 社团活动查看历时素材
        try:
            self.driver.find_id(soucred_id + 'film_look')
            self.driver.find_id(soucred_id + 'film_look').click()
            self.driver.wait_id(soucred_id + 'userhead')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'playBtn').click()
            self.driver.wait_download(soucred_id + 'playbtn')
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

        # 社团活动社长添加活动素材
        try:
            self.driver.find_id(soucred_id + 'choice_source')
            self.driver.find_id(soucred_id + 'choice_source').click()
            self.driver.wait_id(soucred_id + 'txtKeyword')
            self.driver.find_id(soucred_id + 'txtKeyword').send_keys('配音')
            self.driver.find_id(soucred_id + 'btnSearch').click()
            self.driver.wait_id(soucred_id + 'iv_source')
            self.driver.find_id(soucred_id + 'iv_source').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '创建成功'
            check1 = '配音秀:创建成功'
            if toast != check or toast != check1:
                self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            pass
        time.sleep(2)

        # 社团活动素材配音
        try:
            self.driver.find_id(soucred_id + 'dubbing')
            self.driver.find_id(soucred_id + 'dubbing').click()
            try:
                self.driver.find_id(soucred_id + 'btn_close')
                self.driver.find_id(soucred_id + 'btn_close').click()
            except:
                while True:
                    try:
                        self.driver.find_id(soucred_id + 'btnSubmit')
                        self.driver.find_id(soucred_id + 'btnSubmit').click()
                        try:
                            self.driver.find_id(soucred_id + 'roleall')
                            self.driver.find_id(soucred_id + 'roleall').click()
                        except:
                            pass
                        break
                    except:
                        try:
                            self.driver.find_id(soucred_id + 'action')
                            break
                        except:
                            try:
                                self.driver.find_id(soucred_id + 'roleall')
                                self.driver.find_id(soucred_id + 'roleall').click()
                                break
                            except:
                                pass
                time.sleep(2)
                self.driver.find_id(soucred_id + 'action').click()
                self.driver.wait_download(soucred_id + 'title')
                self.driver.Background()
                self.driver.find_id(soucred_id + 'complete').click()
                self.driver.wait_id(soucred_id + 'pri_switch_tv')
                self.driver.swip_up()
                try:
                    self.driver.find_id(soucred_id + 'check_box_add_square')
                    self.driver.find_id(soucred_id + 'check_box_add_square').click()
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(soucred_id + 'uploadbtn').click()
                self.driver.wait_download(soucred_id + 'down')
                self.driver.find_id(soucred_id + 'ivNewsTab').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'society').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'time').click()
                self.driver.wait_id(soucred_id + 'btn_change_input_mode')
                self.driver.find_xpath('活动').click()
                time.sleep(2)
        except:
            pass

    #我的社团-榜单
    def test_e(self):
        self.driver.find_xpath('榜单').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'username')
            self.driver.find_id(soucred_id + 'username').click()
            self.driver.wait_id(soucred_id + 'll_fan')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'look_rank').click()
        self.driver.wait_id(soucred_id + 'tv_right')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'username1')
            self.driver.find_id(soucred_id + 'userHead1').click()
            self.driver.wait_id(soucred_id + 'll_fan')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        ranks = self.driver.find_ids(soucred_id + 'img_rank')
        for i in range(len(ranks)):
            self.driver.find_ids(soucred_id + 'img_rank')[i].click()
            self.driver.wait_id(soucred_id + 'tv_right')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(1)
        time.sleep(2)

    #我的社团-社团空间
    def test_f(self):
        while True:
            i = 0
            try:
                self.driver.find_id(soucred_id + 'btn_space_jump').click()
                self.driver.wait_id(soucred_id + 'll_fan')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            if i == 5:
                break
            else:
                pass
            i = i+1
        time.sleep(2)

    #社团空间-头像
    def test_f_a(self):
        self.driver.find_id(soucred_id + 'userhead').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv_id')
        except:
            raise ('社团id信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv_nickname')
        except:
            raise ('社团昵称信息未显示')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv_sign')
        except:
            raise ('社团简介信息未显示')
        time.sleep(2)
        #举报
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'txtKeyword').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            Report_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,Report_toast,msg='举报失败')
        except:
            pass
        time.sleep(2)

    #社团空间-社团财富
    def test_f_b(self):
        self.driver.find_id(soucred_id + 'gold_match').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv_gold')
            try:
                self.driver.find_id(soucred_id + 'tv_diamond')
            except:
                raise ('社团财富界面未显示余额信息')
        except:
            raise ('社团财富界面未显示余额信息')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-聊天
    def test_f_c(self):
        self.driver.find_id(soucred_id + 'photo').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'editContent')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-功能列表
    def test_f_d(self):
        # 设置关注区权限
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.573)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'check').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            raise ('动态开关设置后没有toast提示')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

        #特别关注
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.685)
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                raise ('特别关注没有toast提示')
        else:
            pass
        time.sleep(2)

        #消息免打扰
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.729)
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                raise ('消息免打扰没有toast提示')
        else:
            pass
        time.sleep(2)

        #添加社团素材
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.802)
        else:
            pass
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'iv_source')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'iv_source').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSelect').click()
        insert_toast = self.driver.wait_toast('//android.widget.Toast')
        if insert_toast == '该素材存在':
            self.driver.find_id(soucred_id + 'btnCancelSelect').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

        #管理/退出社团
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.875)
        else:
            pass
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'btnSubmit')
            self.driver.find_id(soucred_id + 'btnCancel').click()
        except:
            self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-粉丝
    def test_f_e(self):
        self.driver.find_id(soucred_id + 'll_fan').click()
        self.driver.wait_id(soucred_id + 'status_icon')
        status = self.driver.find_ids(soucred_id + 'status_icon')
        for i in range(len(status)):
            self.driver.find_ids(soucred_id + 'status_icon')[i].click()
            time.sleep(1)
        user_name = self.driver.find_ids(soucred_id + 'username')[-1].text
        self.driver.find_ids(soucred_id + 'username')[-1].click()
        self.driver.wait_id(soucred_id + 'll_fan')
        user_name1 = self.driver.find_id(soucred_id + 'username').text
        self.driver.find_id(soucred_id + 'btnBack').click()
        self.assertEqual(user_name,user_name1,msg='粉丝列表用户名与空间用户名校验失败')
        time.sleep(2)
        user_list = self.driver.find_ids(soucred_id + 'username')
        new_user_list =[]
        for i in range(len(new_user_list)):
            name = self.driver.find_ids(soucred_id + 'username')[i].text
            new_user_list.append(name)
        time.sleep(1)
        D_user_list = dict(Counter(new_user_list))
        for key,value in D_user_list:
            if value >1:
                raise (key,'粉丝列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-成员
    def test_f_f(self):
        self.driver.find_id(soucred_id + 'll_member').click()
        self.driver.wait_id(soucred_id + 'manager')
        user_name = self.driver.find_ids(soucred_id + 'name')[-1].text
        self.driver.find_ids(soucred_id + 'userhead')[-1].click()
        self.driver.wait_id(soucred_id + 'll_fan')
        user_name1 = self.driver.find_id(soucred_id + 'username').text
        self.driver.find_id(soucred_id + 'btnBack').click()
        self.assertEqual(user_name, user_name1, msg='成员列表用户名与空间用户名校验失败')
        time.sleep(2)
        user_list = self.driver.find_ids(soucred_id + 'username')
        new_user_list = []
        for i in range(len(new_user_list)):
            name = self.driver.find_ids(soucred_id + 'name')[i].text
            new_user_list.append(name)
        time.sleep(1)
        D_user_list = dict(Counter(new_user_list))
        for key, value in D_user_list:
            if value > 1:
                raise (key, '成员列表用户信息显示重复')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-社团作品
    def test_f_g(self):
        self.driver.find_id(soucred_id + 'filmBg').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团空间-社团素材
    def test_f_h(self):
        self.driver.find_id(soucred_id + 'btnMember').click()
        time.sleep(2)
        count = self.driver.find_id(soucred_id + 'film_all_count').text
        num = re.findall(r'素材(.*)',count)
        new = "".join(num)
        if new == '0':
            return
        time.sleep(2)
        self.driver.find_id(soucred_id + 'imgSource').click()
        self.driver.wait_id(soucred_id + 'shouchang_tv_fake')
        self.driver.Background()
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'imgTip').click()
        while True:
            try:
                self.driver.find_id(soucred_id + 'btnSubmit')
                self.driver.find_id(soucred_id + 'btnSubmit').click()
                try:
                    self.driver.find_id(soucred_id + 'roleall')
                    self.driver.find_id(soucred_id + 'roleall').click()
                except:
                    pass
                break
            except:
                try:
                    self.driver.find_id(soucred_id + 'roleall')
                    self.driver.find_id(soucred_id + 'roleall').click()
                    break
                except:
                    try:
                        self.driver.find_id(soucred_id + 'action')
                        break
                    except:
                        pass
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)

    #社团空间-合辑
    def test_f_i(self):
        self.driver.find_id(soucred_id + 'btnCollect').click()
        time.sleep(2)
        count = self.driver.find_id(soucred_id + 'film_all_count').text
        num = re.findall(r'合辑(.*)', count)
        new = ''.join(num)
        if new != '0':
            self.driver.find_id(soucred_id + 'filmBg').click()
            try:
                self.driver.wait_id(soucred_id + 'userName')
                self.driver.find_id(soucred_id + 'filmBg').click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
                self.driver.Background()
                try:
                    self.driver.find_id(soucred_id + 'follow_ta')
                    self.driver.find_id(soucred_id + 'follow_ta').click()
                    try:
                        follow_toast = self.driver.wait_toast('//android.widget.Toast')
                        check = '社团成员不可取消关注'
                        self.assertEqual(follow_toast,check)
                    except:
                        pass
                except:
                    pass
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
            except Exception as e:
                print(e)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #社团管理
    def test_g(self):
        state = Test_Society().test_b()
        for item in state:
            self.driver.find_xpath(item).click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'btn_space_manager_jump')
                break
            except:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_space_manager_jump').click()
        time.sleep(2)

    #社团管理-编辑资料
    def test_g_a(self):
        self.driver.find_id(soucred_id + 'edit_profile').click()
        time.sleep(2)
        #修改头像
        self.driver.find_id(soucred_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.796)
        time.sleep(4)
        self.driver.find_id('com.oppo.camera:id/shutter_button').click()
        time.sleep(4)
        self.driver.find_id('com.oppo.camera:id/done_button').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'confirm').click()
        time.sleep(3)

        #修改社团名称
        self.driver.find_id(soucred_id + 'society_name').send_keys('属于我自己的社团哦~')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        fail_toast = self.driver.wait_toast('//android.widget.Toast')
        fail_check = '社团名称只支持空格、中英文、数字'
        self.assertEqual(fail_check,fail_toast)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'society_name').send_keys('属于我自己的社团哦')
        time.sleep(2)

        #社团简介
        self.driver.find_id(soucred_id + 'brief_content').send_keys('这是一个严肃的社团简介~')
        time.sleep(2)

        #社团频道
        self.driver.find_ids(soucred_id + 'tv')[-1].click()
        self.driver.wait_id(soucred_id + 'edit_text')
        try:
            self.driver.find_id(soucred_id + 'tv1')
            self.driver.find_id(soucred_id + 'tv1').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(soucred_id + 'edit_text').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_search').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)

        #完成社团资料修改
        self.driver.find_id(soucred_id + 'tv_right').click()
        edit_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '修改成功'
        self.assertEqual(edit_toast,check)
        time.sleep(2)

    #社团管理-社团成员
    def test_g_b(self):
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'shezhang')
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        #添加成员
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'isCheck')
        #搜索用户
        self.driver.find_id(soucred_id + 'filter_edit').send_keys('16685645')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        self.driver.wait_xpath('撸串')
        self.driver.find_id(soucred_id + 'isCheck').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        Invited_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        try:
            self.driver.find_id(soucred_id + 'isCheck')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            pass
        self.assertIn(check, Invited_toast, msg='社团成员邀请发送失败')
        time.sleep(2)

    #社团管理-成员权限
    def test_g_c(self):
        try:
            self.driver.find_id(soucred_id + 'more')
            self.driver.find_id(soucred_id + 'more').click()
            time.sleep(2)
            # 社团管理权限
            self.driver.find_id(soucred_id + 'check_box1').click()
            time.sleep(1)
            state1 = self.driver.find_id(soucred_id + 'check_box1').get_attribute('checked')
            time.sleep(1)
            self.driver.find_id(soucred_id + 'check_box2').click()
            time.sleep(1)
            state2 = self.driver.find_id(soucred_id + 'check_box2').get_attribute('checked')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'save').click()
            save_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '保存成功'
            self.assertEqual(save_toast, check)
            time.sleep(2)
            if state1 == 'true':
                try:
                    self.driver.find_id(soucred_id + 'power')
                except:
                    raise ('开启社团管理权限后，成员一栏中未显示管理图标')
            elif state1 == 'false':
                try:
                    self.driver.find_id(soucred_id + 'power')
                    raise ('关闭社团管理权限后，成员一栏中依然显示管理图标')
                except:
                    pass
            time.sleep(2)
            if state2 == 'true':
                try:
                    self.driver.find_id(soucred_id + 'power')
                except:
                    raise ('开启社团声漫权限后，成员一栏中未显示声漫制作图标')
            elif state2 == 'false':
                try:
                    self.driver.find_id(soucred_id + 'power')
                    raise ('关闭社团声漫权限后，成员一栏中依然显示声漫制作图标')
                except:
                    pass
            time.sleep(2)
        except Exception as e:
            print(e)

    #社团管理-移除成员
    def test_g_d(self):
        Members = self.driver.find_ids(soucred_id + 'username')[-1]
        self.driver.Long_Touche(Members,2000)
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'txtContent')
            content = self.driver.find_id(soucred_id + 'txtContent').text
            check = '移出属于'
            self.assertIn(check,content)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnCancel').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except:
            print('非社长身份，无法移除社团成员')
            try:
                self.driver.find_id(soucred_id + 'll_fan')
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            except:
                pass

    #社团管理-社团公告
    def test_g_e(self):
        self.driver.find_id(soucred_id + 'edit_gonggao').click()
        time.sleep(2)
        choice = random.choice('这是一个严肃的社团公告')
        self.driver.find_id(soucred_id + 'content').send_keys(choice)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        gonggao_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '成功'
        self.assertIn(check,gonggao_toast)
        check_content = self.driver.find_id(soucred_id + 'tv_gonggao').text
        if check_content != choice:
            raise ('社团公告修改后文案显示不正确',choice)
        time.sleep(2)

    #社团作品-作品管理
    def test_g_f(self):
        self.driver.find_id(soucred_id + 'film_manage').click()
        self.driver.wait_id(soucred_id + 'filmBg')
        #审核标准协议
        self.driver.find_id(soucred_id + 'middle').click()
        self.driver.wait_id(soucred_id + 'btnClose')
        self.driver.find_id(soucred_id + 'btnClose').click()
        time.sleep(2)

    #社团作品-添加作品
    def test_g_g(self):
        self.driver.find_id(soucred_id + 'addfilm').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x * 0.5,self.y * 0.875)
        time.sleep(2)
        try:
            self.driver.find_xpath('视频').click()
        except:
            try:
                self.driver.find_desc('显示根目录').click()
                time.sleep(2)
                self.driver.find_xpath('视频').click()
            except:
                pass
        time.sleep(4)
        self.driver.find_xpath('Camera').click()
        time.sleep(4)
        self.driver.find_id('com.android.documentsui:id/icon_thumb').click()
        time.sleep(3)
        #作品标题
        self.driver.find_id(soucred_id + 'title').send_keys('随便传个社团原创作品')
        time.sleep(2)
        #作品封面
        self.driver.find_id(soucred_id + 'upload_cover').click()
        self.driver.wait_id(soucred_id + 'photo_wall_item_photo')
        self.driver.find_id(soucred_id + 'photo_wall_item_photo').click()
        self.driver.wait_id(soucred_id + 'confirm')
        self.driver.find_id(soucred_id + 'confirm').click()
        time.sleep(2)
        #添加配音表用户
        self.driver.find_id(soucred_id + 'mem').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'role').send_keys('我')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'add_mem').click()
        self.driver.wait_id(soucred_id + 'userhead')
        self.driver.find_id(soucred_id + 'userhead').click()
        time.sleep(2)
        #添加作品频道
        self.driver.find_id(soucred_id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        while True:
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                if self.y == 1920:
                    self.driver.tap(self.x * 0.5, self.y * 0.542)
                    time.sleep(6)
                else:
                    pass
            try:
                self.driver.find_id(soucred_id + 'filmBg')
                break
            except:
                pass
            time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath('随便传个社团原创作品')
        except:
            raise ('未获取到上传的作品信息')
        time.sleep(2)

    #社团作品-删除作品
    def test_g_h(self):
        self.driver.find_id(soucred_id + 'filmBg').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'setting').click()
            try:
                time.sleep(2)
                if self.y == 1920:
                    self.driver.tap(self.x * 0.5, self.y * 0.875)
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnSubmit').click()
                delet_toast = self.driver.wait_toast('//android.widget.Toast')
                check = '删除作品成功'
                self.assertEqual(delet_toast, check)
                time.sleep(2)
                self.driver.swip_down()
                time.sleep(2)
            except Exception as e:
                print(e)
        except Exception as e:
            print('非社长身份，无法删除社团作品')

    #社团作品-创建合辑
    def test_h(self):
        self.driver.find_id(soucred_id + 'tab2').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'addfilm').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.802)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('测试合辑')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'ok').click()
        self.driver.wait_id(soucred_id + 'choice')
        time.sleep(2)
        select = self.driver.find_ids(soucred_id + 'choice')
        for i in range(len(select)):
            self.driver.find_ids(soucred_id + 'choice')[i].click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        create_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '创建成功'
        self.assertEqual(create_toast,check)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath('测试合辑')
        except:
            raise ('未显示创建的合辑')
        time.sleep(2)

    #我的社团-编辑合辑作品
    def test_h_a(self):
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)
        #点击合辑作品
        self.driver.find_id(soucred_id + 'img').click()
        self.driver.wait_id(soucred_id + 'tv_video_detail_title')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

        #长按调节作品列表
        el = self.driver.find_id(soucred_id + 'img')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_zhiding').click()
        ZD_toast = self.driver.wait_toast('//android.widget.Toast')
        check = '第一个位置'
        self.assertIn(check,ZD_toast)
        time.sleep(2)
        el2 = self.driver.find_ids(soucred_id + 'img')[-1]
        self.driver.Long_Touche(el2, 2000)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_zhiding').click()
        SY_toast = self.driver.wait_toast('//android.widget.Toast')
        check1 = '上移成功'
        self.assertIn(check1, SY_toast)
        time.sleep(2)

        #移除作品
        el3 = self.driver.find_id(soucred_id + 'img')
        self.driver.Long_Touche(el3, 2000)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_shanchu').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast == '无权操作' or del_toast == '删除成功':
            pass
        else:
            raise ('合辑作品移除失败')

        #添加合辑作品
        self.driver.find_id(soucred_id + 'right_icon1').click()
        self.driver.wait_id(soucred_id + 'choice')
        title_before = self.driver.find_id(soucred_id + 'title').text
        self.driver.find_id(soucred_id + 'choice').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        add_toast = self.driver.wait_toast('//android.widget.Toast')
        check3 = '添加成功'
        self.assertEqual(check3, add_toast)
        time.sleep(2)
        try:
            self.driver.find_xpath(title_before)
        except:
            raise ('合辑作品列表未显示添加的新作品')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团-编辑合辑
    def test_h_b(self):
        el = self.driver.find_id(soucred_id + 'filmBg')
        self.driver.Long_Touche(el,2000)
        time.sleep(2)
        #合辑置顶
        if self.y ==1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.807)
        zhiding_toast = self.driver.wait_toast('//android.widget.Toast')
        zhiding_check = '成功'
        self.assertIn(zhiding_check,zhiding_toast)
        time.sleep(2)

        #删除合辑
        self.driver.Long_Touche(el, 2000)
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.885)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        del_toast = self.driver.wait_toast('//android.widget.Toast')
        if del_toast == '无权操作' or del_toast == '删除成功':
            pass
        else:
            raise ('合辑删除失败')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团-申请蓝V
    def test_i(self):
        self.driver.find_id(soucred_id + 'apply_lv').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('立即申请')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except:
            pass

    #我的社团-入社权限
    def test_j(self):
        self.driver.find_id(soucred_id + 'society_apply_jurisdiction').click()
        time.sleep(2)
        #招募内容
        self.driver.find_id(soucred_id + 'modify').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content').send_keys('本社团并不招人')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)
        #申请要求
        self.driver.find_id(soucred_id + 'addFilm').click()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'addSource').click()
        time.sleep(1)
        #入社申请开关
        self.driver.find_id(soucred_id + 'choice').click()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'choice1').click()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'choice2').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)

    #我的社团-社团消息通知开关
    def test_k(self):
        self.driver.find_id(soucred_id + 'btn_push').click()
        time.sleep(2)

    #我的社团-社团财富、社团钱包
    def test_l(self):
        self.driver.swip_up()
        try:
            self.driver.find_id(soucred_id + 'gold_match')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'gold_match').click()
            time.sleep(2)
            # 分配钻石
            self.driver.find_id(soucred_id + 'distribution_diamond').click()
            self.driver.wait_id(soucred_id + 'userhead')
            self.driver.find_id(soucred_id + 'userhead').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'gold_count').send_keys('100')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'remark').send_keys('分配钻石')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'sure').click()
            Diamond_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '钻石'
            self.assertIn(check, Diamond_toast)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            # 分配金币
            self.driver.find_id(soucred_id + 'distribution_gold').click()
            self.driver.wait_id(soucred_id + 'userhead')
            self.driver.find_id(soucred_id + 'userhead').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'gold_count').send_keys('10000')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'remark').send_keys('分配金币')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'sure').click()
            gold_toast = self.driver.wait_toast('//android.widget.Toast')
            check1 = '金币'
            self.assertIn(check1, gold_toast)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        except Exception as e:
            print(e)


    #我的社团-允许他人下载社团作品
    def test_m(self):
        try:
            self.driver.find_id(soucred_id + 'btn_load')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btn_load').click()
            time.sleep(2)
        except Exception as e:
            print(e)



    #我的社团-社团管理须知
    def test_n(self):
        self.driver.find_xpath('《社团管理须知》').click()
        self.driver.wait_id(soucred_id + 'webview')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #我的社团-转让社团/解散社团
    def test_o(self):
        try:
            self.driver.find_id(soucred_id + 'right_icon1')
            self.driver.find_id(soucred_id + 'right_icon1').click()
            time.sleep(2)
            if self.y ==1920:
                self.driver.tap(self.x * 0.5,self.y *0.807)
            self.driver.wait_xpath('转让社团')
            self.driver.find_ids(soucred_id + 'username')[-1].click()
            time.sleep(2)
            Transfer_content = self.driver.find_id(soucred_id + 'txtContent').text
            check = '您确定要将社团转让给'
            self.assertIn(check,Transfer_content)
            self.driver.find_id(soucred_id + 'btnCancel').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.885)
            time.sleep(2)
            Dissolved_content = self.driver.find_id(soucred_id + 'txtContent').text
            check1 = '你真的要解散社团吗？请提前处理好社团钱包中的收益，解散后无法恢复社团'
            self.assertEqual(check1, Dissolved_content)
            self.driver.find_id(soucred_id + 'btnCancel').click()
            time.sleep(2)
        except Exception as e:
            print(e)

    #返回社团主界面
    def test_p(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(soucred_id + 'task_box')
        self.driver.find_id(soucred_id + 'ivNewsTab').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'society').click()
        time.sleep(2)






















if __name__ == "__main__":
    unittest.main()









