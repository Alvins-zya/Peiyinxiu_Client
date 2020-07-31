import unittest
import time
from Front import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'
class Test_a_Source_search(Dubbing):

    # 点击素材搜索进入搜索界面
    def test_a(self):
        self.driver.wait_id(soucred_id + 'task_box')
        self.driver.find_id(soucred_id + 'btn_more').click()
        self.driver.wait_id(soucred_id + 'tv_search')
        self.driver.find_id(soucred_id + 'tv_search').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'tv_search').click()
        time.sleep(2)

    # 推荐搜索标签
    def test_b(self):
        tv_name = self.driver.find_ids(soucred_id + 'tv')
        tv_list = []
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
                time.sleep(5)
                try:
                    self.driver.find_id(soucred_id + 'iv_source')
                except:
                    print('全部选项中素材信息也为空')
            except:
                pass
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnClear').click()
            time.sleep(2)

    # 历史搜索记录
    def test_c(self):
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

    # 推荐搜索-更多热点
    def test_d(self):
        self.driver.find_id(soucred_id + 'tv1').click()
        self.driver.wait_id(soucred_id + 'rank_name')
        time.sleep(2)
        label = self.driver.find_ids(soucred_id + 'rank_name')
        for i in range(len(label)-1):
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

    # 进入标签详情界面
    def test_e(self):
        self.driver.find_id(soucred_id + 'tv1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'rank_name').click()
        self.driver.wait_id(soucred_id + 'iv_source')
        time.sleep(2)
        #依次点击切换标签，且点击标签后进入素材预览界面再返回
        label_touche = self.driver.find_ids(soucred_id + 'types_name')
        for i in range(len(label_touche)-1,-1,-1):
            self.driver.find_ids(soucred_id + 'types_name')[i].click()
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
        self.driver.find_id(soucred_id + 'btnBack').click()
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

    # 搜索素材
    def test_f(self):
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

    # 素材库主界面8个标签
    def test_a(self):
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

    # 合作广场-预览视频后点击进入配音界面
    def test_b(self):
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

    # 获取广场中的求合作剩余时间
    def test_c(self):
        times = self.driver.find_ids(soucred_id + 'item_sh_clock_time')
        #获取求和作数量
        Coopers = self.driver.find_ids(soucred_id + 'userhead')
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

    # 广场tab筛选项切换
    def test_d(self):
        self.driver.find_id(soucred_id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_female').click()
        time.sleep(2)

    # 选择求合作后配音完成保存草稿箱
    def test_e(self):
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

    # 合作广场-热门列表
    def test_f(self):
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

    # 广场热门-配音完成保存草稿箱
    def test_g(self):
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

    # 热门tab筛选项切换
    def test_h(self):
        self.driver.find_id(soucred_id + 'fq_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'fq_female').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_male').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'dp_female').click()
        time.sleep(2)

    # 合作广场-我的
    def test_i(self):
        time.sleep(2)
        self.driver.find_xpath('我的').click()
        time.sleep(2)

    def test_j(self):
        try:
            self.driver.find_id(soucred_id + 'item_sh_cooperate_article_title')
            return True
        except:
            return False

    # 置顶按钮
    def test_k(self):
        state = Test_b_Classification.test_j(self=None)
        if state == True:
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
            self.driver.Long_Touche(el,3000)
            self.driver.wait_id(soucred_id + 'txtContent')
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '删除成功'
                self.assertEqual(toast,check,msg='toast内容不一致')
            except:
                pass
            time.sleep(1)
        else:
            pass

    # 合作广场-搜索
    def test_l(self):
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
        try:
            self.driver.find_id(soucred_id + 'reIndetify')
            self.driver.find_id(soucred_id +'reIndetify').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(soucred_id + 'boy').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'girl').click()
        time.sleep(2)
        conten = self.driver.find_id(soucred_id + 'text').text
        self.driver.find_id(soucred_id + 'change').click()
        time.sleep(2)
        conten_new = self.driver.find_id(soucred_id + 'text').text
        self.assertNotEqual(conten,conten_new,msg='切换朗读的前后内容对比一致，切换失败')
        time.sleep(2)

    # 录音
    def test_b(self):
        i=1
        while True:
            i = i + 1
            try:
                self.driver.find_id(soucred_id + 'dubbing').click()
                time.sleep(15)
                self.driver.find_id(soucred_id + 'dubbing').click()
                self.driver.wait_id(soucred_id + 'preview')
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
            self.driver.find_id(soucred_id + 'play')
            return True
        except:
            return False

    # 声鉴报告界面
    def test_c(self):
        state = Test_c_Voicetest().test_b_a()
        print(state)
        if state == True:
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
        else:
            print('声鉴结果界面跳转失败，跳过此测试步骤')

    # 点击配音，保存草稿箱
    def test_d(self):
        state = Test_c_Voicetest().test_b_a()
        if state == True:
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
        else:
            print('声鉴结果界面跳转失败，跳过此测试步骤')
            self.driver.back()

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
            self.driver.find_id(soucred_id + 'll_follow')
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

    #素材预览界面点击素材标签
    def test_h(self):
        lable_name = self.driver.find_ids(soucred_id  + 'types_name')
        for i in range(len(lable_name)):
            name = self.driver.find_ids(soucred_id + 'types_name')[i].text
            self.driver.find_ids(soucred_id + 'types_name')[i].click()
            self.driver.wait_id(soucred_id + 'tag_name')
            name1 = self.driver.find_id(soucred_id + 'tag_name').text
            self.assertEqual(name1,name,msg='素材预览界面点击的标签与标签详情界面的标签校验不一致')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    #退出素材预览界面
    def test_i(self):
        try:
            self.driver.find_id(soucred_id + 'tag_name')
            self.driver.find_id(soucred_id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        self.driver.wait_id(soucred_id + 'iv_source')
        time.sleep(2)

class Test_f_upload_source(Dubbing):

    #素材库界面素材上传按钮
    def test_a(self):
        self.driver.find_id(soucred_id + 'upload').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id +'tv_upload')
        time.sleep(2)

    #上传本地视频素材
    def test_b(self):
        self.driver.find_id(soucred_id + 'tv_upload').click()
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

    #素材上传详情界面视频播放
    def test_c(self):
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play_button').click()
        time.sleep(5)
        self.driver.Background()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'play_button')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.124,self.y * 0.385,self.x * 0.688,self.y * 0.385)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id +'play_button').click()
        self.driver.wait_id(soucred_id + 'play_button')
        time.sleep(2)

    #不输入任何内容点击上传
    def test_d(self):
        self.driver.find_id(soucred_id + 'complete').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '请填写素材标题'
            self.assertEqual(toast,check,msg='未输入任何内容点击上传toast提示校验不一致')
        except:
            raise ("点击素材上传按钮，未检测到toast提示")
        time.sleep(2)

    #输入素材标题检测
    def test_e(self):
        self.driver.find_id(soucred_id + 'title').send_keys('上传本地素材')
        time.sleep(2)
        title = self.driver.find_id(soucred_id + 'title').text
        check = '上传本地素材'
        self.assertEqual(title,check,msg='输入标题内容检测结果不一致')
        time.sleep(2)

    #素材标题长度检测
    def test_f(self):
        self.driver.find_id(soucred_id + 'title').clear()
        time.sleep(2)
        #中文字符长度检测
        self.driver.find_id(soucred_id + 'title').send_keys('一二三四五六七八九十一二')
        time.sleep(2)
        Chinese_char = self.driver.find_id(soucred_id + 'title').text
        check = 10
        self.assertEqual(len(Chinese_char),check,msg='素材标题允许输入的最大中文字符数不为10')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'title').clear()
        time.sleep(2)
        #英文字符数检测
        self.driver.find_id(soucred_id + 'title').send_keys('abcdefghijhijk')
        time.sleep(2)
        English_char =self.driver.find_id(soucred_id + 'title').text
        self.assertEqual(len(English_char),check,msg='素材标题允许输入的最大英文字符长度不为10')
        time.sleep(2)

    #输入标题不添加添加字幕，点击上传按钮
    def test_g(self):
        self.driver.find_id(soucred_id + 'complete').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '请添加素材标签'
            self.assertEqual(toast,check,msg='不添加字幕点击上传按钮toast提示校验不一致')
        except:
            raise ('不添加字幕上传，未检测到toast提示')
        time.sleep(2)

    #添加字幕文件
    def test_h(self):
        '''
        以下测试步骤只适用于vivoX9机型
        '''
        self.driver.find_id(soucred_id + 'addsrt').click()
        time.sleep(4)
        self.driver.find_desc("显示根目录").click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_xpath('文件管理').click()
        time.sleep(2)
        self.driver.find_xpath('a_test').click()
        time.sleep(2)
        self.driver.find_id('com.coloros.filemanager:id/mark_radio_button').click()
        time.sleep(2)
        self.driver.find_desc('确定').click()
        time.sleep(5)
        try:
            self.driver.find_id(soucred_id + 'et_role_2')
        except:
            raise ('双人素材，未显示两个角色信息')
        time.sleep(2)
        self.driver.find_id(soucred_id +'role_female_img_2').click()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'role_female_img_1').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_sure').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'role_text')
        self.assertTrue(el, msg='字幕角色信息显示错误')
        time.sleep(2)


    #不添加素材标签点击上传
    def test_j(self):
        self.driver.find_id(soucred_id + 'complete').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '请添加素材标签'
            self.assertEqual(toast,check,msg='不添加素材标签上传toast提示校验不一致')
        except:
            raise ('不添加素材标签上传，未检测到toast提示')
        time.sleep(2)

    #进入素材标签选择界面
    def test_k(self):
        self.driver.find_id(soucred_id + 'tv1').click()
        self.driver.wait_id(soucred_id + 'tv')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #素材标签选择界面搜索标签
    def test_l(self):
        self.driver.find_id(soucred_id + 'tv1').click()
        self.driver.wait_id(soucred_id + 'tv')
        self.driver.find_id(soucred_id + 'edit_text').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'edit_text').send_keys('测试')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_search').click()
        self.driver.wait_id(soucred_id + 'tv')
        check = '测试'
        tv_name = self.driver.find_id(soucred_id + 'tv').text
        self.assertIn(check,tv_name,msg='标签搜索结果中未包含有“测试”关键词')
        time.sleep(2)

    #创建素材标签
    def test_m(self):
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_create').click()
        self.driver.wait_id(soucred_id + 'tv1')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_create').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '不能重复添加该标签哦~'
            self.assertEqual(toast,check,msg='重复创建素材标签toast提示内容校验不一致')
        except:
            raise ('重复创建素材标签，未检测到toast提示')
        time.sleep(2)

    #添加搜索结果标签
    def test_n(self):
        self.driver.find_id(soucred_id + 'tv1').click()
        time.sleep(2)
        for i in range(4):
            self.driver.find_ids(soucred_id + 'tv')[i].click()
            time.sleep(1)
        time.sleep(2)
        self.driver.find_ids(soucred_id + 'tv')[6].click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '最多添加4个标签哦~'
            self.assertEqual(toast,check,msg='添加素材标签超过四个后的toast提示内容校验不一致')
        except:
            raise ('添加第五个素材标签未显示toast提示')
        time.sleep(2)

    #更换已添加的素材标签
    def test_o(self):
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)
        list = []
        tv_name = self.driver.find_ids(soucred_id + 'tv1')
        for i in range(len(tv_name)):
            name = self.driver.find_ids(soucred_id + 'tv1')[i].text
            list.append(name)
            time.sleep(1)
        self.driver.find_id(soucred_id + 'tv1').click()
        time.sleep(2)
        self.driver.find_ids(soucred_id + 'tv1')[-1].click()
        self.driver.wait_id(soucred_id + 'tv')
        self.driver.find_id(soucred_id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)
        list1 = []
        tv_name1 = self.driver.find_ids(soucred_id + 'tv1')
        for i in range(len(tv_name1)):
            name = self.driver.find_ids(soucred_id + 'tv1')[i].text
            list1.append(name)
            time.sleep(1)
        self.assertNotEqual(list,list1,msg='素材标签修改后校验内容未变化')
        time.sleep(2)

    # 输入标题，添加字幕，添加标签，不添加背景音，点击素材上传按钮
    def test_p(self):
        self.driver.find_id(soucred_id + 'complete').click()
        check = '请先上传背景音文件'
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            self.assertEqual(check,toast,msg='不添加背景音上传素材toast提示内容检验不一致')
        except:
            raise ('不添加背景音上传，未检测到toast提示信息')
        time.sleep(2)

    #添加素材背景音
    def test_q(self):
        self.driver.find_id(soucred_id + 'addMusic').click()
        time.sleep(3)
        while True:
            try:
                self.driver.find_id(soucred_id + 'btnDownload')
                self.driver.find_id(soucred_id + 'btnDownload').click()
            except:
                break
            time.sleep(1)
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)
        music_name = self.driver.find_id(soucred_id + 'title').text
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        music_name1 = self.driver.find_id(soucred_id + 'fileName').text
        self.assertEqual(music_name,music_name1,msg='选择的背景音名称校验不一致')
        time.sleep(2)

    #播放选择的素材背景音
    def test_r(self):
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.104,self.y * 0.488,self.x * 0.626,self.y *0.488)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    #拖动背景音音轨
    def test_s(self):
        if self.y == 1920:
            self.driver.swip_move(self.x *0.844,self.y * 0.641,self.x *0.189,self.y *0.641)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(4)

    #上传素材
    def test_t(self):
        self.driver.find_id(soucred_id + 'complete').click()
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
                self.driver.find_xpath('我知道了')
                break
            except:
                pass
            time.sleep(2)

    #上传成功后素自制素材列表界面
    def test_u(self):
        self.driver.wait_id(soucred_id + 'btnSubmit')
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)
        tv = self.driver.find_id(soucred_id +'tv_source_from').text
        check = '测试'
        self.assertIn(check,tv,msg='素材标签中未包含“测试”关键字')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

    #删除已上传的素材
    def test_v(self):
        tv = self.driver.find_id(soucred_id + 'tv_source_from').text
        check = '测试'
        self.assertIn(check, tv, msg='素材标签中未包含“测试”关键字')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'tv_source_from').click()
        self.driver.wait_id(soucred_id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(0.5 * self.x, 0.867 * self.y)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            try:
                self.driver.wait_toast('//android.widget.Toast')
            except:
                raise ('未检测到素材删除toast')
            time.sleep(2)
        else:
            self.driver.back()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
