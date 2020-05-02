import unittest
import time
import pytest

from Dubbing9_11.Front import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Source_search(Dubbing):
    def test_a(self):
        #点击素材搜索进入搜索界面
        self.driver.wait_id(soucred_id + 'tv_search')
        self.driver.find_id(soucred_id + 'tv_search').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'tv_search').click()
        time.sleep(2)

    def test_b(self):
        #推荐搜索标签
        tv_name = self.driver.find_ids(soucred_id + 'tv')
        tv_list = []
        print(len(tv_name))
        for i in range(len(tv_name)):
            name = self.driver.find_ids(soucred_id + 'tv')[i].text
            tv_list.append(name)
            time.sleep(1)
        print(tv_list)
        time.sleep(2)
        for i in range(len(tv_name)):
            self.driver.find_ids(soucred_id + 'tv')[i].click()
            self.driver.wait_id(soucred_id + 'rl_left2')
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'no_data')
                tip = self.driver.find_id(soucred_id + 'no_data').text
                print(tip)
                time.sleep(2)
                self.driver.find_xpath('全部').click()
                try:
                    self.driver.wait_id(soucred_id + 'iv_source')
                except:
                    print('全部选项中素材信息也为空')
            except:
                pass
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnClear').click()
            time.sleep(2)


    def test_c(self):
        #历史搜索记录
        try:
            self.driver.find_id(soucred_id + 'item')
            searche = self.driver.find_ids(soucred_id + 'item')
            for i in range(len(searche)):
                item_name = self.driver.find_ids(soucred_id + 'item')[i].click()
                try:
                    self.driver.wait_id(soucred_id + 'iv_source')
                    time.sleep(2)
                    self.driver.find_id(soucred_id + 'btnClear').click()
                    time.sleep(2)
                except:
                    pass
                time.sleep(1)
            time.sleep(2)
            #清空搜索记录
            self.driver.find_id(soucred_id + 'clear').click()
            time.sleep(2)
        except:
            raise ('未显示有历史搜索记录')
        time.sleep(2)

    def test_d(self):
        #推荐搜索-更多热点
        self.driver.find_id(soucred_id + 'tv1').click()
        self.driver.wait_id(soucred_id + 'rank_name')
        time.sleep(2)
        label = self.driver.find_ids(soucred_id + 'rank_name')
        for i in range(len(label)):
            self.driver.find_ids(soucred_id + 'rank_name')[i].click()
            try:
                self.driver.wait_id(soucred_id + 'iv_source')
                time.sleep(1)
                self.driver.back()
            except:
                raise ('素材标签详情界面未显示素材信息',i)
            time.sleep(2)
        #上滑加载标签列表
        while True:
            self.driver.swip_up()
            time.sleep(2)
            label_name = self.driver.find_ids(soucred_id + 'rank_name')[-1].text
            self.driver.swip_up()
            label_name1 = self.driver.find_ids(soucred_id + 'rank_name')[-1].text
            if label_name == label_name1:
                self.driver.find_id(soucred_id + 'btnBack').click()
                break
            else:
                pass
        time.sleep(2)
    def test_e(self):
        #进入标签详情界面
        self.driver.find_id(soucred_id + 'tv1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'rank_name').click()
        self.driver.wait_id(soucred_id + 'iv_source')
        time.sleep(2)
        #依次点击切换标签，且点击标签后进入素材预览界面再返回
        label_touche = self.driver.find_ids(soucred_id + 'types_name')
        for i in reversed(label_touche):
            i.click()
            self.driver.wait_id(soucred_id + 'iv_source')
            self.driver.find_id(soucred_id + 'iv_source').click()
            self.driver.wait_id(soucred_id + 'userhead')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        #上滑加载素材列表
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        #退出标签详情界面返回素材搜索界面
        while True:
            try:
                self.driver.find_id(soucred_id + 'tag_name')
                self.driver.find_id(soucred_id + 'btnBack').click()
            except:
                break
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)


    def test_f(self):
        #搜索素材
        self.driver.find_id(soucred_id + 'txtKeyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        self.driver.wait_id(soucred_id + 'iv_source')
        try:
            self.driver.find_xpath('配音')
        except:
            raise ('搜索结果中未发现配音关键字')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        el = self.driver.find_ids(soucred_id + 'types_name')
        for i in reversed(el):
            i.click()
            time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_b_Classification(Dubbing):
    def test_a(self):
        #素材库主界面8个标签
        tv_Main = self.driver.find_ids(soucred_id + 'tv')
        for i in range(len(tv_Main)):
            self.driver.find_ids(soucred_id + 'tv')[i].click()
            self.driver.wait_id(soucred_id + 'iv_source')
            #热门推荐标签
            tv_Branch = self.driver.find_ids(soucred_id + 'tv')
            for x in range(len(tv_Branch)):
                self.driver.find_ids(soucred_id + 'tv')[x].click()
                self.driver.wait_id(soucred_id + 'img_url')
                time.sleep(1)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            #更多热门标签
            self.driver.find_id(soucred_id + 'tv1').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            Screening = self.driver.find_ids(soucred_id + 'types_name')
            for j in range(len(Screening)-1,-1,-1):
                self.driver.find_ids(soucred_id + 'types_name')[j].click()
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'iv_source').click()
            self.driver.wait_id(soucred_id + 'userhead')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    def test_b(self):
        #合作广场-预览视频后点击进入配音界面
        self.driver.find_id(soucred_id + 'rl_coor').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)
        #点击视频预览界面的合作按钮进入配音界面
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        #点击广场列表中的配音按钮进入配音界面
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')

    def test_c(self):
        #获取广场中的求合作剩余时间
        times = self.driver.find_ids(soucred_id + 'item_sh_clock_time')
        #获取求和作数量
        Coopers = self.driver.find_ids(soucred_id + 'item_sh_cooperate_article_title')
        time.sleep(2)
        self.assertEqual(len(times),len(Coopers),msg='求合作的数量与时间的的数量不一致')
        time.sleep(2)
        #点击用户头像进入个人空间
        Use = self.driver.find_id(soucred_id + 'item_sh_user_name').text
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'followcount')
        Zoom_user = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(Use,Zoom_user,msg='广场点击的用户名称与空间中显示的用户名称不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(4)
        #加载列表
        for i in range(5):
            self.driver.swip_down()
            time.sleep(2)
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'top_img')
            self.driver.find_id(soucred_id +'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)

    def test_d(self):
        #广场tab筛选项切换
        self.driver.find_id(soucred_id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_female').click()
        time.sleep(2)

    def test_e(self):
        #选择求合作后配音完成保存草稿箱
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        self.driver.find_id(soucred_id +'title').send_keys('合作广场接合作')
        time.sleep(2)
        self.driver.swip_up()
        try:
            self.driver.find_id(soucred_id + 'add_square_container')
        except:
            raise ('合作广场接受的合作上传界面未显示生成求合作开关')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            pass
        time.sleep(2)

    def test_f(self):
        #合作广场-热门列表
        el = self.driver.find_xpath('热门')
        time.sleep(2)
        #显示合作次数
        Cooper_count = self.driver.find_ids(soucred_id + 'count')
        list = []
        for i in range(len(Cooper_count)):
            name = self.driver.find_ids(soucred_id + 'item_sh_cooperate_article_title')[i].text
            Counts = self.driver.find_ids(soucred_id + 'count')[i].text
            list.append(name)
            list.append(Counts)
            time.sleep(2)
        print(list)
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
            self.driver.find_id(soucred_id + 'top_img')
            self.driver.find_id(soucred_id + 'top_img').click()
            time.sleep(5)
        except:
            pass
        time.sleep(2)

    def test_g(self):
        #广场热门-配音完成保存草稿箱
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        self.driver.find_id(soucred_id + 'title').send_keys('合作广场-热门列表接合作')
        time.sleep(2)
        self.driver.swip_up()
        try:
            self.driver.find_id(soucred_id + 'add_square_container')
        except:
            print ('合作广场-热门接受的合作上传界面未显示生成求合作开关')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            print(toast)
        except:
            pass
        time.sleep(2)

    def test_h(self):
        # 热门tab筛选项切换
        self.driver.find_id(soucred_id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_female').click()
        time.sleep(2)

    def test_i(self):
        time.sleep(2)
        #合作广场-我的
        self.driver.find_xpath('我的').click()
        time.sleep(2)

    def test_j():
        try:
            self.driver.find_id(soucred_id + 'item_sh_cooperate_article_title')
            return False
        except:
            return True


    @pytest.mark.skipIf(test_j,'合作广场我的界面中求和作信息为空，跳过此项')
    def test_k(self):
        #置顶按钮
        try:
            self.driver.find_id(soucred_id + 'btnSetTop').click()
        except:
            try:
                self.driver.find_id(soucred_id + 'item_sh_clock_time')
            except:
                print('暂无已置顶求和作')
        time.sleep(2)
        #删除求合作
        el = self.driver.find_id(soucred_id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el)
        self.driver.wait_id(soucred_id + 'txtContent')
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除成功'
            self.assertEqual(toast,check,msg='toast内容不一致')
        except:
            pass
        time.sleep(1)

    def test_l(self):
        #合作广场-搜索
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'et_search_keyword').send_keys('配音')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        self.driver.find_id(soucred_id +'item_sh_cooperate_article_image').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'item_sh_cooperate_article_image')
        #滑动加载列表
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'et_search_keyword').send_keys('槛花笼鹤')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSearch').click()
        time.sleep(5)
        try:
            self.driver.find_xpath('没有搜索到任何内容')
        except:
            raise ('检查搜索无结果显示失败')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

class Test_c_Voicetest(Dubbing):
    #声音鉴定
    def test_a(self):
        self.driver.find_id(soucred_id + 'sj').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'boy').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'girl').click()
        time.sleep(2)
        conten = self.driver.find_id(soucred_id + 'text').text
        self.driver.find_id(soucred_id + 'change').click()
        conten_new = self.driver.find_id(soucred_id + 'text').text
        self.assertNotEqual(conten,conten_new,msg='切换朗读的前后内容对比一致，切换失败')
        time.sleep(2)

    def test_b():
        #录音
        i=1
        while True:
            i = i + 1
            try:
                self.driver.find_id(soucred_id + 'dubbing').click()
                time.sleep(15)
                self.driver.find_id(soucred_id + 'dubbing').click()
                time.sleep(10)
                self.driver.find_id(soucred_id + 'preview').click()
                break
                return False
            except:
                pass
            if i == 10:
                break
            else:
                pass
        time.sleep(2)
    @pytest.mark.skipIf(test_b(),'声鉴结果界面跳转失败，跳过此测试步骤')
    def test_c(self):
        #声鉴报告界面
        voice_style = self.driver.find_id(soucred_id + 'voice_type').text
        print(voice_style)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'title').click()
        self.driver.wait_id(soucred_id + 'userhead')
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        for i in range(3):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    @pytest.mark.skipIf(test_b(), '声鉴结果界面跳转失败，跳过此测试步骤')
    def test_d(self):
        #点击配音，保存草稿箱
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        self.driver.wait_download(soucred_id + 'action')
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id +'title')
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
        time.sleep(2)
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        for i in range(6):
            self.driver.swip_down()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'reIndetify').click()
        time.sleep(2)
        #返回素材库
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

class Test_d_source_list(Dubbing):
    #素材列表
    def test_a_list(self):
        self.driver.find_id(soucred_id + 'unlimited').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        for i in range(15):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'top_img')
            self.driver.find_id(soucred_id + 'top_img').click()
        except:
            pass
        time.sleep(4)

    #切换角色筛选项
    def test_b_select_role(self):
        self.driver.find_id(soucred_id + 'boy').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv_girl')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'coor').click()
        time.sleep(2)
        num = self.driver.find_ids(soucred_id + 'tv_source_from')
        for i in range(len(num)):
            try:
                self.driver.find_ids(soucred_id + 'tv_boy')[i]
            except:
                name = self.driver.find_ids(soucred_id + 'tv_source_title')[i].text
                raise ("合作素材列表中未显示双人角色:%s"%name)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'unlimited').click()
        time.sleep(4)


class Test_e_Preview(Dubbing):
    #点击进入素材预览界面
    def test_a_touch_source(self):
        source_num = self.driver.find_ids(soucred_id + 'iv_source')
        for i in range(len(source_num)):
            self.driver.find_ids(soucred_id + 'iv_source')[i].click()
            try:
                self.driver.wait_id(soucred_id + 'userhead')
                self.driver.Background()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            except:
                self.driver.find_id(soucred_id + 'btnReload')
                self.driver.find_id(soucred_id +'btnReload').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            time.sleep(2)
        time.sleep(2)
    #素材预览详情界面查看视频是否循环播放
    def test_b_play(self):
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(50)
        try:
            self.driver.find_id(soucred_id + 'play')
            raise ('素材视频未循环播放')
        except:
            self.driver.Background()
            time.sleep(2)
            self.driver.wait_id(soucred_id + 'play')
            time.sleep(2)

    #视频暂停情况下拖动进度条
    def test_e(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.202,self.y * 0.471,self.x * 0.566,self.y * 0.471)
        elif self.y > 2250:
            pass
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play').click()
        time.sleep(20)
        self.driver.Background()
        time.sleep(2)

    #进入素材作者个人空间
    def test_f(self):
        name1 = self.driver.find_id(soucred_id + 'user_name').text
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'fanscount')
        name2 = self.driver.find_id(soucred_id + 'username').text
        self.assertEqual(name1,name2,msg='素材视频详情界面的用户名称与空间中的用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #关注按钮
    def test_g(self):
        try:
            self.driver.find_id(soucred_id + 'userhead')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_video_detail_follow').click()
        try:
            follow_toast = self.driver.wait_toast('//android.widget.Toast')
            check = '关注成功'
            self.assertEqual(follow_toast,check,msg='关注toast内容校验不一致')
        except:
            try:
                self.driver.find_id(soucred_id + 'editContent')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnBack').click()
            except:
                pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'fanscount')
        self.driver.find_id(soucred_id + 'follow_status').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #点击素材标签
    def test_h(self):
        lables = self.driver.find_ids(soucred_id + 'types_name')
        for i in range(len(lables)):
            name = self.driver.find_ids(soucred_id + 'types_name')[i].text
            self.driver.find_ids(soucred_id + 'types_name')[i].click()
            self.driver.wait_id(soucred_id + 'iv_source')
            name1 = self.driver.find_id(soucred_id + 'tag_name').text
            self.assertEqual(name,name1,msg='素材预览界面点击的标签与跳转后显示的标签校验不一致')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    #配音列表
    def test_i(self):
        self.driver.swip_up()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'userHead')
        except:
            raise ('暂无更多配音列表用户')
        time.sleep(2)
        user_name = self.driver.find_ids(soucred_id + 'nickname')
        for i in range(len(user_name)):
            name = self.driver.find_ids(soucred_id + 'nickname')[i].text
            self.driver.find_ids(soucred_id + 'userHead')[i].click()
            self.driver.wait_id(soucred_id + 'follow_ta')
            self.driver.Background()
            time.sleep(2)
            name1 = self.driver.find_id(soucred_id + 'textView').text
            self.assertEqual(name1,name,msg='素材配音列表用户名称与视频详情作者用户名称校验不一致')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(3)
        time.sleep(2)
    #素材举报
    def test_g(self):
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_action_one').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='举报toast校验失败')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'txtKeyword').send_keys('功能测试，可忽略此信息')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='举报toast校验失败')
        except:
            try:
                self.driver.find_id(soucred_id + 'txtKeyword')
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    #素材收藏
    def test_h(self):
        self.driver.find_id(soucred_id + 'shouchang_tv_fake').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '收藏成功'
            self.assertEqual(toast, check, msg='素材收藏提示信息校验不一致')
        except:
            pass
        time.sleep(4)
        self.driver.find_id(soucred_id + 'shouchang_tv_fake').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '取消收藏成功'
            self.assertEqual(toast, check, msg='素材取消收藏提示信息校验不一致')
        except:
            pass
        time.sleep(2)

    #素材分享
    def test_i(self):
        self.driver.find_id(soucred_id + 'zhuanfa_fake').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'group_chat').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'userhead').click()
        self.driver.wait_id(soucred_id + 'btn_change_input_mode')
        time.sleep(2)
        source_name = self.driver.find_ids(soucred_id + 'chat_film_title')[-1].text
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        soucer_name1 = self.driver.find_id(soucred_id + 'source_title').text
        self.assertIn(soucer_name1,source_name,msg='分享素材内容显示错误')
        time.sleep(2)

    #素材界面点击配音按钮
    def test_j(self):
        try:
            self.driver.find_id(soucred_id + 'btn_change_input_mode')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack')
        except:
            pass
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'yinpin')
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_download(soucred_id + 'roleall')
            self.driver.find_id(soucred_id + 'roleall').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
        except:
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_download(soucred_id + 'action')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'dubbing_fake')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #合作素材预览界面合作信息列表
    def test_k(self):
        self.driver.find_id(soucred_id + 'coor').click()
        self.driver.wait_id(soucred_id + 'tv_boy')
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_rank_tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'left_name').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_name').click()
        time.sleep(2)
        role_name = self.driver.find_id(soucred_id + 'right_name').text
        self.driver.swip_up()
        time.sleep(2)
        check = self.driver.find_id(soucred_id + 'item_sh_cooperate_article_cooperate_gender').text
        self.assertIn(role_name,check,msg='选择的待配角色名称与待配作品列表中的角色名称校验不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'item_sh_cooperate_article_image').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'btnCooperate').click()
        self.driver.wait_download(soucred_id + 'action')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)







if __name__ == '__main__':
    unittest.main()
