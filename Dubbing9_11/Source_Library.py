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
            Screening = self.driver.find_ids(soucred_id + 'types_name')
            for j in reversed(Screening):
                j.click()
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'iv_source').click()
            self.driver.wait_id(soucred_id + 'userhead')
            time.sleep(2)
            self.driver.find_id('btnBack').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)












if __name__ == '__main__':
    unittest.main()
