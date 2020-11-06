#encoding: utf-8
'''
@author:alvin.zhu
@file:Source_list.py
@time:2020/10/30 11:32
@Description:

'''
import time, datetime
from Public.Driver_Operate import BaseOperate,resource_id


class Source():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入素材库
    def Source_into_List(self):
        self.driver.find_id(self.id + 'btn_more').click()
        self.driver.wait_id(self.id + 'coor')

    # 素材库搜索素材
    def Source_searchs(self):
        self.driver.wait_id(self.id + 'tv_search')
        self.driver.find_id(self.id + 'tv_search').click()
        time.sleep(4)

        #点击热门素材标签
        tv_name = self.driver.find_ids(self.id + 'tv')
        time.sleep(2)
        for i in range(len(tv_name)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'rl_left2')
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)

        # 历史搜索记录
        try:
            self.driver.find_id(self.id + 'item').click()
            self.driver.wait_id(self.id + 'iv_source')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnClear').click()
            time.sleep(2)
        except:
            raise ('未显示有历史搜索记录')
        time.sleep(2)
        # 清空搜索记录
        self.driver.find_id(self.id + 'clear').click()
        time.sleep(2)

        # 推荐搜索-更多热点
        self.driver.find_id(self.id + 'tv1').click()
        self.driver.wait_id(self.id + 'rank_name')
        time.sleep(2)
        self.driver.find_id(self.id + 'rank_name').click()
        try:
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            raise ('素材标签详情界面未显示素材信息')

        # 上滑加载标签列表
        while True:
            self.driver.swip_up()
            time.sleep(2)
            label_name = self.driver.find_ids(self.id + 'rank_name')[-1].text
            self.driver.swip_up()
            label_name1 = self.driver.find_ids(self.id + 'rank_name')[-1].text
            if label_name == label_name1:
                self.driver.find_id(self.id + 'btnBack').click()
                break
            else:
                pass
        time.sleep(2)

    # 进入标签详情界面
    def Source_tv_detail(self):
        self.driver.find_id(self.id + 'tv1').click()
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)
        # 依次点击切换标签，且点击标签后进入素材预览界面再返回
        label_touche = self.driver.find_ids(self.id + 'types_name')
        for i in range(len(label_touche) - 1, -1, -1):
            self.driver.find_ids(self.id + 'types_name')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            try:
                self.driver.find_id(self.id + 'iv_source').click()
                self.driver.wait_id(self.id + 'userhead')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

        # 上滑加载素材搜索结果列表
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnClear').click()
        time.sleep(2)

    # 搜索素材
    def Source_search(self):
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'iv_source')
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        el = self.driver.find_ids(self.id + 'types_name')
        for i in reversed(el):
            i.click()
            time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 素材库主界面8个大分类
    def Source_Classification(self):
        tv_Main = self.driver.find_ids(self.id + 'tv')
        for i in range(len(tv_Main)):
            self.driver.find_ids(self.id + 'tv')[i].click()
            self.driver.wait_id(self.id + 'iv_source')
            # 热门推荐标签
            tv_Branch = self.driver.find_ids(self.id + 'tv')
            for x in range(len(tv_Branch)):
                self.driver.find_ids(self.id + 'tv')[x].click()
                self.driver.wait_id(self.id + 'img_url')
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            # 更多热门标签
            self.driver.find_id(self.id + 'tv1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            Screening = self.driver.find_ids(self.id + 'types_name')
            for j in range(len(Screening) - 1, -1, -1):
                self.driver.find_ids(self.id + 'types_name')[j].click()
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(self.id + 'iv_source').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 合作广场-广场列表
    def Source_Coor(self):
        self.driver.find_id(self.id + 'rl_coor').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

        # 点击视频预览界面的合作按钮进入配音界面
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')

        # 点击广场列表中的配音按钮进入配音界面
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        time.sleep(2)

        # 获取广场中的求合作剩余时间
        try:
            self.driver.find_id(self.id + 'item_sh_clock_time')
        except:
            raise ('未显示时间')
        time.sleep(2)

        # 加载列表
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)

    # 合作广场角色tab筛选项切换
    def Source_role_change(self):
        self.driver.find_id(self.id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'dp_female').click()
        time.sleep(2)

    # 合作广场-热门列表
    def Source_coor_hot(self):
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        # 显示合作次数
        try:
            self.driver.find_id(self.id + 'count')
        except:
            raise ('合作广场热门列表未显示合作次数')
        time.sleep(2)
        # 加载列表
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)


    # 合作广场-我的
    def test_i(self):
        time.sleep(2)
        self.driver.find_xpath('我的').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 合作广场-搜索
    def Source_coor_search(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_search_keyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.find_id(self.id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(self.id + 'play')
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'item_sh_cooperate_article_image')
        # 滑动加载列表
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_search_keyword').send_keys('槛花笼鹤')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(5)
        try:
            self.driver.find_xpath('没有搜索到任何内容')
        except:
            raise ('检查搜索无结果显示失败')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    # 声音鉴定
    def test_a(self):
        self.driver.find_id(self.id + 'sj').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'reIndetify')
            self.driver.find_id(self.id + 'reIndetify').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'boy').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'girl').click()
        time.sleep(2)
        conten = self.driver.find_id(self.id + 'text').text
        self.driver.find_id(self.id + 'change').click()
        time.sleep(2)
        conten_new = self.driver.find_id(self.id + 'text').text
        self.assertNotEqual(conten, conten_new, msg='切换朗读的前后内容对比一致，切换失败')
        time.sleep(2)

    # 录音
    def test_b(self):
        i = 1
        while True:
            i = i + 1
            try:
                self.driver.find_id(self.id + 'dubbing').click()
                time.sleep(15)
                self.driver.find_id(self.id + 'dubbing').click()
                self.driver.wait_id(self.id + 'preview')
                break
            except:
                pass
            if i == 10:
                break
            else:
                pass
        time.sleep(2)

    def test_b_a(self):
        try:
            self.driver.find_id(self.id + 'play')
            return True
        except:
            return False

    # 声鉴报告界面
    def test_c(self):
        state = Test_c_Voicetest().test_b_a()
        print(state)
        if state == True:
            voice_style = self.driver.find_id(self.id + 'voice_type').text
            print(voice_style)
            time.sleep(2)
            self.driver.find_id(self.id + 'play').click()
            self.driver.wait_download(self.id + 'play')
            time.sleep(2)
            self.driver.find_id(self.id + 'title').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            for i in range(3):
                self.driver.swip_up()
                time.sleep(2)
            time.sleep(2)
        else:
            print('声鉴结果界面跳转失败，跳过此测试步骤')

    # 点击配音，保存草稿箱
    def test_d(self):
        state = Test_c_Voicetest().test_b_a()
        if state == True:
            self.driver.find_id(self.id + 'action').click()
            time.sleep(2)
            self.driver.wait_download(self.id + 'action')
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
            time.sleep(2)
            self.driver.wait_xpath('退出配音')
            self.driver.find_xpath('退出配音').click()
            time.sleep(2)
            for i in range(6):
                self.driver.swip_down()
                time.sleep(2)
            self.driver.find_id(self.id + 'reIndetify').click()
            time.sleep(2)
            # 返回素材库
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
        else:
            print('声鉴结果界面跳转失败，跳过此测试步骤')
            self.driver.back()

    # 素材列表
    def Source_list(self):
        self.driver.find_id(self.id + 'unlimited').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        for i in range(15):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'top_img')
            self.driver.find_id(self.id + 'top_img').click()
        except:
            pass
        time.sleep(4)

    #素材列表预览模式
    def Source_preview(self):
        try:
            self.driver.find_id(self.id + 'tv_title')
        except:
            self.driver.find_id(self.id + 'change_type').click()
        time.sleep(2)
        self.driver.swip_up()
        self.driver.find_id(self.id + 'bg_view').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'subtitleView').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'change_type').click()
        time.sleep(2)

        # 点击进入素材预览界面
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        # 切换角色筛选项
        self.driver.find_id(self.id + 'boy').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_girl')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'coor').click()
        time.sleep(2)
        num = self.driver.find_ids(self.id + 'tv_source_from')
        for i in range(len(num)):
            try:
                self.driver.find_ids(self.id + 'tv_boy')[i]
            except:
                name = self.driver.find_ids(self.id + 'tv_source_title')[i].text
                raise ("合作素材列表中未显示双人角色:%s" % name)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'unlimited').click()
        time.sleep(4)

    # 素材预览详情界面查看视频是否循环播放
    def Source_detail(self):
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')

        # 进入素材作者个人空间
        name1 = self.driver.find_id(self.id + 'user_name').text
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        name2 = self.driver.find_id(self.id + 'username').text
        self.assertEqual(name1, name2, msg='素材视频详情界面的用户名称与空间中的用户名称校验不一致')
        time.sleep(2)

    # 关注按钮
    def Source_detail_follow(self):
        self.driver.find_id(self.id + 'btn_video_detail_follow').click()
        try:
            follow_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '关注成功'
            self.assertEqual(follow_toast, check, msg='关注toast内容校验不一致')
        except:
            try:
                self.driver.find_id(self.id + 'editContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
            except:
                pass
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'fanscount')
        self.driver.find_id(self.id + 'follow_status').click()
        time.sleep(4)

    # 素材预览界面点击素材标签
    def Source_detail_types(self):
        lable_name = self.driver.find_ids(self.id + 'types_name')
        for i in range(len(lable_name)):
            name = self.driver.find_ids(self.id + 'types_name')[i].text
            self.driver.find_ids(self.id + 'types_name')[i].click()
            self.driver.wait_id(self.id + 'tag_name')
            name1 = self.driver.find_id(self.id + 'tag_name').text
            self.assertEqual(name1, name, msg='素材预览界面点击的标签与标签详情界面的标签校验不一致')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    # 退出素材预览界面
    def Source_detail_exit(self):
        try:
            self.driver.find_id(self.id + 'tag_name')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        self.driver.wait_id(self.id + 'iv_source')
        time.sleep(2)


    # 素材库界面素材上传按钮
    def test_a(self):
        self.driver.find_id(self.id + 'upload').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'tv_upload')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)




