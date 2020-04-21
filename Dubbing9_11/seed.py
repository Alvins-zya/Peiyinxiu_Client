# coding = utf-8
import time
import unittest
import random
import datetime



from Dubbing9_11.parent import Dubbing

soucred_id = 'com.happyteam.dubbingshow:id/'


class Test_a_Dub(Dubbing):
    # 点击进入配音界面
    def test0(self):
        #进入素材库
        self.driver.wait_id(soucred_id + 'task_box')
        self.driver.find_id(soucred_id + 'btn_more').click()
        self.driver.wait_id(soucred_id + 'unlimited')
        self.driver.find_id(soucred_id + 'unlimited').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.wait_id(soucred_id + 'iv_source')
        except:
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)

    def test1(self):
        try:
            self.driver.find_id(soucred_id + 'yinpin')
            return False
        except:
            return True

    source_result_style  = test1(self= None)
    @unittest.skipIf(source_result_style,u'结果为False时，判断是双配素材,执行此条用例')
    def test2(self):
        self.driver.find_id(soucred_id + 'dubbing_fake').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            tip = self.driver.find_id(soucred_id + 'txtTitle').text
            check = '为了您正常使用配音秀 需获得以下权限'
            self.assertEqual(tip, check, msg='内存权限文案不一致')
            self.driver.find_id(soucred_id + 'close').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'dubbing_fake')
                self.driver.find_id(soucred_id + 'dubbing_fake').click()
                time.sleep(3)
                self.driver.find_id(soucred_id + 'next')
                self.driver.find_id(soucred_id + 'next').click()
                time.sleep(2)
                try:
                    self.driver.wait_sys('始终允许')
                except:
                    self.driver.wait_sys('允许')
            except:
                print('未返回到素材预览界面')
                self.driver.Quit()
        except:
            pass
        self.driver.wait_id(soucred_id + 'roleall')
        self.driver.find_id(soucred_id + 'roleall').click()
        time.sleep(2)

    @unittest.skipUnless(source_result_style,u'结果为True时，判断是单人素材，执行此条用例')
    def test3(self):
        #点击配音内存检查
        self.driver.find_id(soucred_id + 'dubbing_fake').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            tip = self.driver.find_id(soucred_id + 'txtTitle').text
            check = '为了您正常使用配音秀 需获得以下权限'
            self.assertEqual(tip,check,msg='内存权限文案不一致')
            self.driver.find_id(soucred_id + 'close').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'dubbing_fake')
                self.driver.find_id(soucred_id + 'dubbing_fake').click()
                time.sleep(3)
                self.driver.find_id(soucred_id + 'next')
                self.driver.find_id(soucred_id + 'next').click()
                time.sleep(2)
                try:
                    self.driver.wait_sys('始终允许')
                except:
                    self.driver.wait_sys('允许')
            except:
                print('未返回到素材预览界面')
                self.driver.Quit()
        except:
            pass
        self.driver.wait_id(soucred_id + 'living')
        time.sleep(2)

    def test4(self):
        # 配音引导页
        try:
            self.driver.find_id(soucred_id + 'subtitleView').click()
            time.sleep(2)

        except:
            pass
    @unittest.skipIf(source_result_style,u'结果为False时，双配素材退出配音界面再进')
    def test5(self):
        #退出配音界面再进
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            self.driver.wait_id(soucred_id + 'dubbing_fake')
            time.sleep(2)
            self.driver.wait_id(soucred_id + 'roleall')
            self.driver.find_id(soucred_id + 'roleall').click()
            time.sleep(2)
        except:
            print('配音界面返回跳转错误')
            self.driver.Quit()
    @unittest.skipUnless(source_result_style,u'结果为True时，单配素材退出再进')
    def test6(self):
        # 退出配音界面再进
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        try:
            self.driver.wait_id(soucred_id + 'dubbing_fake')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_id(soucred_id + 'living')
            time.sleep(2)
        except:
            print('配音界面返回跳转错误')
            self.driver.Quit()



    @unittest.skipIf(source_result_style,u'结果为False时，合作素材，执行切换角色')
    def test7(self):
        #合作配音角色切换
        try:
            self.driver.find_id(soucred_id + 'coopera')
            self.driver.find_id(soucred_id + 'coopera').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'role1_tv').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'coopera').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'role2_tv').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'coopera').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'roleall').click()
        except:
            pass



class Test_b_Music(Dubbing):
    # 配音界面背景音开关
    def test0(self):
        self.driver.find_id(soucred_id + 'headset').click()
        time.sleep(2)
        try:
            tips = self.driver.find_id(soucred_id + 'txtContent').text
            check = '开启背景音需要插上耳机！'
            self.assertEqual(tips,check,msg='耳机提示文案不一致')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
        except:
            print('已连接耳机')

class Test_c_living(Dubbing):
    #实况功能测试
    def test0(self):
        # 开启实况权限检查
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'name')
            tips = self.driver.find_id(soucred_id + 'txtTitle').text
            print(tips)
            self.driver.find_id(soucred_id + 'close').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'living').click()
            time.sleep(1)
            try:
                self.driver.wait_sys("始终允许")
            except:
                self.driver.wait_sys("允许")
        except:
            try:
                self.driver.wait_sys("始终允许")
            except:
                self.driver.wait_sys("允许")
        else:
            pass
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'cameraView2')
        except:
            self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
    def test1(self):
        #开启实况后退到后台再启动
        self.driver.find_id(soucred_id + 'living').click()
        self.driver.wait_id(soucred_id + 'cameraView2')
        time.sleep(2)
        self.driver.Background()
        self.driver.wait_id(soucred_id + 'cameraView2')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)



class Test_d_script(Dubbing):
    #台词功能测试
    def test0(self):
        # 点击进入台词列表
        self.driver.find_id(soucred_id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'titleTextView')
        count = self.driver.find_ids(soucred_id + 'titleTextView')
        num = len(count)
        if num>4:
            self.driver.swip_up()
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id +'cancelBn').click()
        self.driver.wait_id(soucred_id + 'scirpt')

    def test1(self):
        #切换台词
        self.driver.find_id(soucred_id + 'scirpt').click()
        self.driver.wait_id(soucred_id + 'titleTextView')
        count = self.driver.find_ids(soucred_id + 'titleTextView')
        num = len(count)
        if num > 1:
            for i in range(num):
                self.driver.find_ids(soucred_id + 'titleTextView')[i].click()
                self.driver.wait_id(soucred_id + 'edit_subtitle')
                self.driver.find_id(soucred_id + 'scirpt').click()
                self.driver.wait_id(soucred_id + 'titleTextView')
                time.sleep(2)
        else:
            print('台词数量小于2，不做切换')
            self.driver.find_id(soucred_id + 'cancelBn').click()
            self.driver.wait_id(soucred_id + 'scirpt')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'titleTextView')
            self.driver.find_id(soucred_id + 'cancelBn').click()
        except:
            pass
        time.sleep(2)

    def test3(self):
        #台词内容
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        count1 = self.driver.find_ids(soucred_id + 'content_editor')
        script = []
        for i in range(len(count1)):
            sub = self.driver.find_ids(soucred_id + 'content_editor')[i].text
            script.append(sub)
            time.sleep(1)
        print(script)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)

    def test4(self):
        #修改台词后点击完成，再次进入编辑界面查看修改后的台词
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_ids(soucred_id +'content_editor')[0].clear()
        time.sleep(2)
        self.driver.find_ids(soucred_id + 'content_editor')[0].send_keys("台词修改")
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip,tip_check,msg='台词修改保存文案对比不一致，请检查')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        content = self.driver.find_ids(soucred_id + 'content_editor')[0].text
        content_check = '台词修改'
        self.assertEqual(content,content_check,msg='首句台词中的“台词修改”文案对比不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)

    def test5(self):
        #修改首句台词后不保存返回配音界面再进，查看台词首句显示
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_ids(soucred_id + 'content_editor')[0].send_keys('台词修改')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'txtContent').text
        tip_check = '真的要放弃本次台词编辑吗？'
        self.assertEqual(tip,tip_check,msg='真的要放弃本次台词编辑吗？提示文件校验失败，文案不一致')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(3)
        #切换系统默认台词
        self.driver.find_id(soucred_id + 'scirpt').click()
        self.driver.wait_id(soucred_id + 'titleTextView')
        self.driver.find_id(soucred_id + 'titleTextView').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        content  = self.driver.find_ids(soucred_id + 'content_editor')[0].text
        content_check = '台词修改'
        self.assertNotEqual(content,content_check,msg="台词修改后不保存退出，再次检查台词，显示的是修改后的台词")
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)

    def test6(self):
        #清空字幕所有内容
        while True:
            self.driver.find_id(soucred_id + 'edit_subtitle').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'content_editor').clear()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'complete').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                toast_check = '台词不能为空，请输入至少一句台词'
                self.assertEqual(toast,toast_check,msg='台词不能为空，请输入至少一句台词,文案对比不一致')
                time.sleep(2)
                self.driver.find_id(soucred_id + 'back').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'btnSubmit').click()
                time.sleep(2)
                break
            except:
                self.driver.find_id(soucred_id + 'btnSubmit').click()
            time.sleep(2)

    def test7(self):
        #编辑台词输入特殊符号后保存
        self.driver.find_id(soucred_id + 'scirpt').click()
        self.driver.wait_id(soucred_id + 'titleTextView')
        self.driver.find_id(soucred_id + 'titleTextView').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').send_keys('\(^o^)/~')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'edit_subtitle')
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        content = self.driver.find_id(soucred_id + 'content_editor').text
        content_check = '\(^o^)/~'
        self.assertIn(content,content_check,msg='\(^o^)/~,不在字幕内容中')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        self.driver.wait_id(soucred_id + 'edit_subtitle')
        self.driver.find_id(soucred_id + 'scirpt').click()
        self.driver.wait_id(soucred_id + 'titleTextView')
        self.driver.find_id(soucred_id + 'titleTextView').click()
        time.sleep(3)

class Test_e_video_HD(Dubbing):
    def test0(self):
        #非高清素材
        HD_check = self.driver.find_id(soucred_id + 'swtich_hd').text
        check = '切换高清画质'
        if HD_check == check:
            self.driver.find_id(soucred_id + 'swtich_hd').click()
            time.sleep(2)
            tips = self.driver.find_id(soucred_id + 'txtContent').text
            tips_check = '购买会员专享高清素材，可生成高清配音作品'
            self.assertEqual(tips, tips_check, msg='文案错误')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnSubmit').click()
            self.driver.wait_id(soucred_id + 'renew')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
        else:
            pass

class Test_f_Play_vido(Dubbing):
    def test0(self):
        #完整的预览视频
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')

    def test1(self):
        #播放过程中暂停
        self.driver.find_id(soucred_id + 'play').click()
        try:
            self.driver.find_id(soucred_id + 'play')
            pass
        except:
            self.driver.Background()
            self.driver.wait_download(soucred_id + 'play')
            T =self.driver.find_id(soucred_id + 'video_time').text
            T_check = '00:00'
            self.assertIn(T_check,T,msg='时间进度没有走')
        time.sleep(2)

    def test3(self):
        #播放过程中推到后台
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.Background()
        self.driver.wait_id(soucred_id + 'play')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'living')
        except:
            print('未恢复到默认状态')
            self.driver.Quit()

class Test_g_Record(Dubbing):
    def test_a(self):
        # 录音权限
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            self.driver.find_id(soucred_id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            pass
        time.sleep(2)

    def test_b(self):
        #点击录音按钮配音
        try:
            self.driver.find_id(soucred_id + 'play')
            self.driver.find_id(soucred_id + 'action').click()
        except:
            pass

    def test_c(self):
        # 手动点击提交进入配音预览界面
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_d(self):
        # 在完整录制后的基础上点击原声试听，查看视频播放是否从头开始播放
        time1 = datetime.datetime.now()
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        time2 = datetime.datetime.now()
        time_result = time2 - time1
        time_video = self.driver.find_id(soucred_id + 'video_time').text
        print('视频时间：',time_video,'实际播放时间：',time_result)
        time.sleep(2)


    def test_e(self):
        # 配音秀试听
        self.driver.find_id(soucred_id + 'review')
        self.driver.find_id(soucred_id + 'review').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)

    def test_f(self):
        #试听过程中点击提交进入预览界面
        self.driver.find_id(soucred_id + 'review').click()
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(1)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'clear_voice')
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)
        except:
            self.driver.find_id(soucred_id + 'uploadbtn')
            #返回配音界面
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'back').click()
            time.sleep(2)

    def test_g(self):
        #试听过程中应用退到后台再启动
        self.driver.find_id(soucred_id + 'review').click()
        self.driver.Background()
        self.driver.wait_id(soucred_id + 'review')
        time.sleep(2)

    def test_h(self):
        #试听过程中，点击退出配音界面
        self.driver.find_id(soucred_id + 'review').click()
        time.sleep(1)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'txtContent').text
        tip_check = '确定放弃吗？'
        self.assertEqual(tip,tip_check,msg="退出配音界面弹窗提示文案错误")
        self.driver.find_id(soucred_id + 'btnCancel').click()
        time.sleep(2)

    def test_i(self):
        #点击回撤按钮
        count = self.driver.find_id(soucred_id + 'withdrawcount').text
        for i in range(len(count)):
            self.driver.find_id(soucred_id + 'withdraw').click()
            self.driver.wait_not_id(soucred_id + 'withdraw')
            break
        time.sleep(2)

    def test_j(self):
        #录制过程中暂停
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(3)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'dubbingWaveform')
        except:
            print('没有显示音轨，未录制进人声')
        time.sleep(2)
    def test_k(self):
        #录制完成后自动跳转后再返回配音界面
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_l(self):
        # 手动拖音轨
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        time.sleep(2)
        self.driver.swip_move(int(self.x*0.24),int(self.y*0.71),int(self.x*0.81),int(self.y*0.71))
        time.sleep(2)
        # 点击预览视频
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_m(self):
        # 重新录制
        self.driver.find_id(soucred_id + 'review').click()
        self.driver.wait_id(soucred_id + 'play')
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back')
        time.sleep(2)

    def test_n(self):
        # 回撤重录
        el = self.driver.find_id(soucred_id + 'withdraw')
        self.driver.Long_Touche(el)
        time.sleep(2)
        self.driver.find_id(soucred_id + 'scirpt')
        self.driver.find_id(soucred_id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'titleTextView')
        self.driver.find_id(soucred_id + 'titleTextView').click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_o(self):
        # 编辑字幕
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').send_keys('台词编辑')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip_check, tip, msg="提示文案错误")
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'withdraw')
            print('台词编辑保存失败')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_p(self):
        # 实况录制
        while True:
            try:
                self.driver.find_id(soucred_id + 'living')
                break
            except:
                self.driver.find_id(soucred_id + 'withdraw').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(4)
        try:
            self.driver.find_id(soucred_id + 'cameraView2')
        except:
            print("实况开启失败")
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_q(self):
        # 实况录制后返回预览界面，点击预览原声
        self.driver.find_id(soucred_id + 'play').click()
        self.driver.wait_download(soucred_id + 'play')
        time.sleep(2)

    def test_r(self):
        # 编辑台词后重新录制实况
        self.driver.find_id(soucred_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'content_editor').send_keys('台词编辑')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(soucred_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip_check, tip, msg="提示文案错误")
        self.driver.find_id(soucred_id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'withdraw')
            print('台词编辑保存失败')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_s(self):
        # 点击配音按钮直接重录实况
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_t(self):
        #点击录制普通作品
        try:
            self.driver.find_id(soucred_id + 'living')
        except:
            self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'living').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)




class Test_h_preview_video(Dubbing):
    def test1(self):
        #播放完整的视频
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        #播放过程中推到后台再打开
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.Background()
        self.driver.wait_id(soucred_id + 'play_button')
        #播放过程中返回配音界面再进预览界面
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(4)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test2(self):
        #字幕开关
        el = self.driver.find_id(soucred_id + 'add_subtitle_cb').get_attribute('checked')
        if el == True:
            print('字幕默认开启')
        else:
            print('字幕默认关闭')
        time.sleep(2)
        if el == False:
            self.driver.find_id(soucred_id + 'add_subtitle_cb').click()
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.assertTrue(el,msg='开启字幕开关后，返回配音界面再进预览界面，没有保留开关状态')
        time.sleep(2)

    def test3(self):
        #降噪开关
        el = self.driver.find_id(soucred_id + 'clear_voice').get_attribute('checked')
        state_check = 'true'
        if el == state_check:
            print('降噪默认开启')
        else:
            print('降噪默认关闭')
        time.sleep(2)
        if el == state_check:
            self.driver.find_id(soucred_id + 'clear_voice').click()
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id(soucred_id + 'clear_voice').get_attribute('checked')
        if el1 ==state_check:
            self.assertFalse(el1, msg='降噪开关关闭后，返回配音界面再进预览界面，没有保留开关状态')
        else:
            pass
        time.sleep(2)

class Test_i_preview(Dubbing):
    # 预览界面人声
    def test_a(self):
        #调节人声音量
        el = self.driver.find_id(soucred_id + 'vol').get_attribute('checked')
        self.assertTrue(el,msg='进入配音预览界面后未默认选中人声选项')
        time.sleep(2)
        if self.y ==1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592,self.x * 0.37, self.y * 0.718)#调大音量
            time.sleep(4)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718,self.x * 0.115,self.y * 0.628)  # 调大音量
        elif self.y >2250:
            self.driver.swip_move(self.x*0.245, self.y*0.535,self.x*0.376, self.y*0.633)#调大音量
            time.sleep(4)
            self.driver.swip_move(self.x*0.364,self.y*0.627,self.x*0.107,self.y*0.627)# 调小音量
        else:
            pass
        time.sleep(4)
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test_b(self):
        #声音校准
        self.driver.find_id(soucred_id + 'trim').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'trim').get_attribute('checked')
        self.assertTrue(el,msg='点击校准后未显示选中状态')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37,self.y * 0.718)  # 提前播放人声进度
            self.driver.wait_download(soucred_id + 'play_button')
            self.driver.swip_move(self.x * 0.37,self.y * 0.718, self.x * 0.115,self.y * 0.628)  # 延后播放人声进度
        elif self.y >2250:
            self.driver.swip_move(self.x * 0.245,self.y * 0.535, self.x * 0.376, self.y * 0.633)  # 提前播放人声进度
            self.driver.wait_download(soucred_id + 'play_button')
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107,self.y * 0.627)  # 延后播放人声进度
        else:
            pass
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test_c(self):
        #人声变声调节
        self.driver.find_id(soucred_id + 'pitch').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'pitch').get_attribute('checked')
        self.assertTrue(el,msg='点击变声后未显示选中状态')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37,self.y * 0.718)  # #人声声线加粗
            self.driver.wait_download(soucred_id + 'play_button')
            self.driver.swip_move(self.x * 0.37, self.y * 0.718,self.x * 0.115,self.y * 0.628)  #人声声线变细
        elif self.y >2250:
            self.driver.swip_move(self.x * 0.245, self.y * 0.535, int(self.x * 0.376,self.y * 0.633)  #人声声线加粗
            self.driver.wait_download(soucred_id + 'play_button')
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107,self.y * 0.627)  #人声声线变细
        else:
            pass
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test_d(self):
        #人声混响调节
        self.driver.find_id(soucred_id + 'fx').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'fx').get_attribute('checked')
        self.assertTrue(el,msg='点击人声混响后未显示选中状态')
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x*0.093,self.y*0.8,self.x*0.093,self.y*0.59)#增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.254,self.y*0.8,self.x*0.254,self.y*0.59)#增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.419,self.y*0.8,self.x*0.419,self.y*0.59)#增加回声效果值
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.093,self.y*0.59,self.x*0.093,self.y*0.8)#减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.254,self.y*0.59,self.x*0.254,self.y*0.8)#减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.419,self.y*0.59,self.x*0.419,self.y*0.8)#减小回声效果值
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
        elif self.y >2250:
            self.driver.swip_move(self.x*0.098,self.y*0.7,self.x*0.098,self.y*0.553)#增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.252,self.y*0.7,self.x*0.252,self.y*0.553)#增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.413,self.y*0.7,self.x*0.413,self.y*0.553)#增加回声效果值
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.098,self.y*0.553,self.x*0.098,self.y*0.7)#减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.252,self.y*0.553,self.x*0.252,self.y*0.7)#减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x*0.413,self.y*0.553,self.x*0.413,self.y*0.7)#减小回声效果值
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
        else:
            pass

    def test_e(self):
        #返回配音界面后再进入配音预览界面，查看人声选项默认状态
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'vol').get_attribute('checked')
        self.assertTrue(el,msg='返回配音界面再进预览界面，人声选项没有恢复默认状态')

    def test_f(self):
        #背景音音量调节
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x*0.632,self.y*0.62,self.x*0.893,self.y*0.67)#增大背景音音量
            time.sleep(2)
            self.driver.swip_move(self.x*0.893,self.y*0.67,self.x*0.632,self.y*0.62)#减小背景音音量
            time.sleep(2)
            self.driver.swip_move(self.x * 0.632, self.y * 0.62, self.x * 0.893, self.y * 0.67)  # 增大背景音音量
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.607,self.y*0.591,self.x*0.884,self.y*0.571)#增大背景音音量
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.884,self.y*0.571,self.x*0.607,self.y*0.591)#减小背景音音量
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.607,self.y*0.591,self.x*0.884,self.y*0.571)#增大背景音音量
        else:
            pass
        time.sleep(2)
        #关闭背景音音量
        self.driver.find_id(soucred_id + 'voice_open').click()
        el = self.driver.find_id(soucred_id + 'voice_open').get_attribute('checked')
        self.assertTrue(el,msg='状态点击背景音关闭按钮后，状态没有显示关闭')
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test_g(self):
        #背景音音乐列表中选择其它音乐
        count = self.driver.find_id(soucred_id + 'tvBgCount').text
        if count >1:
            self.driver.find_id(soucred_id + 'imgBgCount').click()
            if self.y==1920:
                self.driver.tap(self.x*0.5,self.y*0.469)
            elif self.y > 2250:
                self.driver.tap(self.x*0.5,self.y*0.464)
            else:
                pass
        else:
            print('背景音数量少于2，不做切换')
        time.sleep(4)
    def test_h(self):
        #背景音混响调节
        self.driver.find_id(soucred_id + 'bgfx').click()
        time.sleep(2)
        el = self.driver.find_id(soucred_id + 'bgfx').get_attribute('chedked')
        self.assertTrue(el,msg='状态点击背景音混响按钮后，状态没有显示选中')
        time.sleep(2)
        if self.y == 1920:
            #增加混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.8, self.x*0.588, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.8, self.x*0.75, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.8, self.x*0.91, self.y*0.59)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            #减小背景音混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.59, self.x*0.588, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.59, self.x*0.75, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.59, self.x*0.91, self.y*0.8)
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
        elif self.y > 2250:
            #增加混响效果
            TouchAction(self.driver).press(x=640, y=1636).move_to(x=643, y=1261).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=808, y=1648).move_to(x=815, y=1255).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=986, y=1642).move_to(x=980, y=1258).release().perform()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'play_button').click()
            self.driver.wait_download(soucred_id + 'play_button')
            time.sleep(2)
            #减小混响效果
            TouchAction(self.driver).press(x=640, y=1161).move_to(x=637, y=1645).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=805, y=1180).move_to(x=805, y=1639).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=986, y=1177).move_to(x=980, y=1636).release().perform()
            time.sleep(2)
        else:
            pass
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)

    def test_i(self):
        #下载系统推荐背景音音乐
        self.driver.find_id(soucred_id + 'bgvol').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'imgBgCount').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.519, self.y * 0.803)
        elif self.y > 2250:
            self.driver.tap(self.x*0.51, self.y*0.96)
        else:
            pass
        self.driver.wait_id(soucred_id + 'btnRight')
        while True:
            try:
                self.driver.find_id(soucred_id + 'btnDownload')
                self.driver.find_id(soucred_id + 'btnDownload').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    print(toast)
                    break
                except:
                    pass
            except:
                break
            time.sleep(2)
    def test_j(self):
        #随机选中背景音音乐
        count = self.driver.find_ids(soucred_id + 'title')
        select = randint(0,len(count))
        self.driver.find_ids(soucred_id + 'title')[select].click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnRight').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)
        #选中音乐后进入音乐试听界面，拖动视频进度条
        if self.y ==1920:
            self.driver.swip_move(self.x*0.052,self.y*0.487,self.x*0.704,self.y*0.487)
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.052,self.y*0.448,self.x*0.633,self.y*0.448)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'play_button').click()
        self.driver.wait_download(soucred_id + 'play_button')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)

    def test_k(self):
        #上滑加载背景音音乐列表并点击下载按钮
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        while True:
            try:
                self.driver.find_id(soucred_id + 'btnDownload')
                self.driver.find_id(soucred_id + 'btnDownload').click()
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    print(toast)
                    break
                except:
                    pass
            except:
                break
            time.sleep(2)
    def test_l(self):
        #选择任意音乐后返回预览界面
        self.driver.find_id(soucred_id + 'title').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnRight').click()
        self.driver.wait_id(soucred_id + 'play_button')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'complete').click()
        self.driver.wait_id(soucred_id + 'clear_voice')
        time.sleep(2)

    def test_m(self):
        #预览界面返回配音界面后重新录制
        self.driver.find_id(soucred_id + 'back').click()
        self.driver.wait_id(soucred_id + 'review')
        if self.y == 1920:
            self.driver.swip_move(self.x*0.204,self.y*0.651,self.x*0.741,self.y*0.651)
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.215,self.y*0.707,self.x*0.709,self.y*0.707)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'action').click()
        self.driver.wait_download(soucred_id + 'title')
        time.sleep(2)


class Test_j_upload(Dubbing):
    def test_a(self):
        #预览界面点击完成
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)

    def test_b(self):
        #修改作品封面-视频截图
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x*0.5,self.y*0.708)
            time.sleep(2)
            self.driver.swip_move(self.x*0.37,self.y*0.422,self.x*0.74,self.y*0.422)
        elif self.y > 2250:
            self.driver.tap(self.x*0.5,self.y*0.752)
            time.sleep(2)
            self.driver.swip_move(self.x*0.033,self.y*0.361,self.x*0.441,self.y*0.361)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(soucred_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        # 选择视频截图
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.708)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.422, self.x * 0.74, self.y * 0.422)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.752)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.033, self.y * 0.361, self.x * 0.441, self.y * 0.361)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)

    def test_c(self):
        #切换封面后返回预览界面再进入上传界面选择视频封面更换
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(soucred_id + 'btn_setting_cover_tip')
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        # 选择视频截图
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.708)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.422, self.x * 0.74, self.y * 0.422)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.752)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.033, self.y * 0.361, self.x * 0.441, self.y * 0.361)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(soucred_id + 'complete').click()
        time.sleep(2)

    def test_d(self):
        #修改作品封面-拍照
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.755)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.82)
        else:
            pass
        time.sleep(5)
        try:
            #米5
            self.driver.find_id('com.android.camera:id/v9_camera_picker')
            self.driver.find_id('com.android.camera:id/v9_camera_picker').click()
            time.sleep(5)
            self.driver.find_id('com.android.camera:id/inten_done_apply').click()
        except:
            #VivoX21
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
            time.sleep(4)
        except:
            pass
        self.driver.find_id(soucred_id + 'confirm').click()
        time.sleep(2)

    def test_e(self):
        #修改作品封面-拍照-拍照以后点击取消
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.755)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.82)
        else:
            pass
        time.sleep(5)
        try:
            # 米5
            self.driver.find_id('com.android.camera:id/v9_camera_picker')
            self.driver.find_id('com.android.camera:id/v9_camera_picker').click()
            time.sleep(5)
            self.driver.find_id('com.android.camera:id/inten_done_apply').click()
        except:
            # VivoX21
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
            time.sleep(4)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(soucred_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id('android:id/button1').click()
        time.sleep(4)

    def test_f(self):
        #修改作品封面-相册
        self.driver.find_id(soucred_id + 'btn_setting_cover_tip').click()
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.856)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.875)
        else:
            pass
        time.sleep(2)
        photo_count = self.driver.find_ids(soucred_id + 'photo_wall_item_photo')
        select = randint(0,len(photo_count))
        self.driver.find_ids(soucred_id + 'photo_wall_item_photo')[select].click()
        time.sleep(3)
        self.driver.find_id(soucred_id + 'confirm').click()
        time.sleep(2)

    def test_g(self):
        #标题名称-输入30个字符
        self.driver.find_id(soucred_id + 'title').send_keys('123456789012345678901234567890')
        time.sleep(2)
        char = self.driver.find_id(soucred_id + 'title').text
        char_check = '123456789012345678901234567890'
        count_check = '30'
        self.assertEqual(char,char_check,msg='标题内容与“123456789012345678901234567890”对比不一致')
        time.sleep(2)

    def test_h(self):
        #标题名称-清空标题
        self.driver.find_id(soucred_id + 'title').clear()
        num = self.driver.find_id(soucred_id + 'title_count').text
        check = '0/30'
        self.assertEqual(num,check,msg='标题未清空')
        time.sleep(2)

    def test_i(self):
        # 上传界面标签显示检查
        try:
            self.driver.find_xpath('添加')
        except:
            self.driver.find_id(soucred_id + 'tv1').click()
        time.sleep(2)
        self.driver.find_xpath('添加').click()
        self.driver.wait_id(soucred_id + 'edit_text')
        try:
            self.driver.find_id(soucred_id + 'tv')
        except:
            print('未显示热门标签')
            self.driver.find_id(soucred_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_xpath('添加').click()
            self.driver.wait_id(soucred_id + 'edit_text')
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'tv1')
            self.driver.find_id(soucred_id + 'tv1').click()
        except:
            pass
        time.sleep(2)
        hot_lable = self.driver.find_ids(soucred_id + 'tv')
        select =random.randint(0,len(hot_lable))
        self.driver.find_ids(soucred_id + 'tv')[select].click()
        time.sleep(2)
        label_name = self.driver.find_id(soucred_id + 'tv1').text
        self.driver.find_id(soucred_id + 'tv_right').click()
        time.sleep(2)
        label_check = self.driver.find_id(soucred_id + 'tv1').text
        self.assertEqual(label_name,label_check,msg='标签对比不一致，%s,%s'%(label_name,label_check))
        time.sleep(2)
class Test_k_Upload(Dubbing):
    def test_a(self):
        #点击上传按钮
        self.driver.find_id(soucred_id + 'uploadbtn').click()
        time.sleep(2)
        self.driver.wait_id(soucred_id + 'down')
        print('上传成功')



if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(Dub))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
