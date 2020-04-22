import unittest
import time
from Dubbing9_11.parent import Dubbing
soucred_id = 'com.happyteam.dubbingshow:id/'
class Source_search(Dubbing):
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

class Classification(Dubbing):
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
        self.driver.find_xpath('热门').click()
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
        #合作广场-我的
        self.driver.find_xpath('我的').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'item_sh_cooperate_article_title')
            return True
        except:
            print('合作广场-我的tab界面为空')
            return False
    result = test_i(self=None)
    @unittest.skipUnless(result,u'合作广场我的界面中求和作信息为空，跳过此项')
    def test_j(self):
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
        time.sleep(2)































if __name__ == '__main__':
    unittest.main()
