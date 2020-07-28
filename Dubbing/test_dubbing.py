#coding=utf-8
'''
配音界面除角色选择外功能，其它文件可引用
'''
import time,unittest,random,datetime,sys,os
from Dubbing9_12.Front import Dubbing
sourced_id = 'com.happyteam.dubbingshow:id/'
class Test_Dub(Dubbing):

    # 配音界面背景音开关
    def test_a_Background_sound(self):
        self.driver.find_id(sourced_id + 'headset').click()
        time.sleep(2)
        try:
            tips = self.driver.find_id(sourced_id + 'txtContent').text
            check = '开启背景音需要插上耳机！'
            self.assertEqual(tips, check, msg='耳机提示文案不一致')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
        except:
            print('已连接耳机')

    # 实况功能测试
    def test_b_Camera(self):
        # 开启实况权限检查
        self.driver.find_id(sourced_id + 'living').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'next')
            tips = self.driver.find_id(sourced_id + 'txtTitle').text
            print(tips)
            self.driver.find_id(sourced_id + 'close').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'living').click()
            time.sleep(1)
            try:
                self.driver.wait_sys("始终允许")
            except:
                self.driver.wait_sys("允许")
        except:
            try:
                self.driver.wait_sys("始终允许")
            except:
                try:
                    self.driver.wait_sys("允许")
                except:
                    pass
        time.sleep(2)

    #关闭实况开关
    def tast_b_a_Camera(self):
        try:
            self.driver.find_id(sourced_id + 'cameraView2')
        except:
            self.driver.find_id(sourced_id + 'living').click()
        time.sleep(4)
        self.driver.find_id(sourced_id + 'living').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'cameraView2')
            self.driver.find_id(sourced_id +  'living').click()
        except:
            pass
        time.sleep(2)

    # 开启实况后退到后台再启动
    def test_b_b_Camera(self):
        self.driver.find_id(sourced_id + 'living').click()
        self.driver.wait_id(sourced_id + 'cameraView2')
        time.sleep(2)
        self.driver.Background()
        self.driver.wait_id(sourced_id + 'cameraView2')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'living').click()
        time.sleep(2)

        # 点击进入台词列表

    #配音界面台词列表
    def test0(self):
        self.driver.find_id(sourced_id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(sourced_id + 'titleTextView')
        count = self.driver.find_ids(sourced_id + 'titleTextView')
        num = len(count)
        if num > 4:
            self.driver.swip_up()
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'cancelBn').click()
        self.driver.wait_id(sourced_id + 'scirpt')
        time.sleep(2)

    # 台词列表切换台词
    def test1(self):
        script_cout = int(self.driver.find_id(sourced_id + 'scirpt_count').text)
        if script_cout > 1:
            self.driver.find_id(sourced_id + 'scirpt').click()
            self.driver.wait_id(sourced_id + 'titleTextView')
            count = self.driver.find_ids(sourced_id + 'titleTextView')
            for i  in range((script_cout)-1,-1,-1):
                self.driver.find_ids(sourced_id + 'titleTextView')[i].click()
                self.driver.wait_id(sourced_id + 'edit_subtitle')
                self.driver.find_id(sourced_id + 'scirpt').click()
                self.driver.wait_id(sourced_id + 'titleTextView')
                time.sleep(2)
            self.driver.find_id(sourced_id + 'cancelBn').click()
        time.sleep(2)


    # 修改台词后点击完成，再次进入编辑界面查看修改后的台词
    def test4(self):
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_ids(sourced_id + 'content_editor')[0].clear()
        time.sleep(2)
        self.driver.find_ids(sourced_id + 'content_editor')[0].send_keys("台词修改")
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(sourced_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip, tip_check, msg='台词修改保存文案对比不一致，请检查')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        content = self.driver.find_ids(sourced_id + 'content_editor')[0].text
        content_check = '台词修改'
        self.assertEqual(content, content_check, msg='首句台词中的“台词修改”文案对比不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)

    # 修改首句台词后不保存返回配音界面再进，查看台词首句显示
    def test5(self):
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_ids(sourced_id + 'content_editor')[0].send_keys('台词修改')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(sourced_id + 'txtContent').text
        tip_check = '真的要放弃本次台词编辑吗？'
        self.assertEqual(tip, tip_check, msg='真的要放弃本次台词编辑吗？提示文件校验失败，文案不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(3)


    # 切换系统默认台词
    def test_6(self):
        script_cout = int(self.driver.find_id(sourced_id + 'scirpt_count').text)
        if script_cout > 1:
            self.driver.find_id(sourced_id + 'scirpt').click()
            self.driver.wait_id(sourced_id + 'titleTextView')
            self.driver.find_id(sourced_id + 'titleTextView').click()
            time.sleep(3)
            try:
                self.driver.find_id(sourced_id + 'roleall')
                self.driver.find_id(sourced_id + 'roleall').click()
            except:
                pass
            time.sleep(2)
            self.driver.find_id(sourced_id + 'edit_subtitle').click()
            time.sleep(2)
            content = self.driver.find_ids(sourced_id + 'content_editor')[0].text
            content_check = '台词修改'
            self.assertNotEqual(content, content_check, msg="台词修改后不保存退出，再次检查台词，显示的是修改后的台词")
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)

    # 清空字幕所有内容
    def test6(self):
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.driver.hide_keyboard()
        time.sleep(2)
        for i in range(2):
            Subtitles = self.driver.find_ids(sourced_id + 'content_editor')
            for i in range(len(Subtitles)):
                self.driver.find_ids(sourced_id + 'content_editor')[i].clear()
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        toast_check = '台词不能为空，请输入至少一句台词'
        self.assertEqual(toast, toast_check, msg='台词不能为空，请输入至少一句台词,文案对比不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)

    # 编辑台词输入特殊符号后保存
    def test7(self):
        self.driver.find_id(sourced_id + 'scirpt').click()
        self.driver.wait_id(sourced_id + 'titleTextView')
        self.driver.find_id(sourced_id + 'titleTextView').click()
        time.sleep(3)
        try:
            self.driver.find_id(sourced_id + 'roleall')
            self.driver.find_id(sourced_id + 'roleall').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').send_keys('∯∰∱∲∳')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        self.driver.wait_id(sourced_id + 'edit_subtitle')
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        content = self.driver.find_id(sourced_id + 'content_editor').text
        content_check = '∯∰∱∲∳'
        self.assertIn(content, content_check, msg='\(^o^)/~,不在字幕内容中')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        self.driver.wait_id(sourced_id + 'edit_subtitle')
        self.driver.find_id(sourced_id + 'scirpt').click()
        self.driver.wait_id(sourced_id + 'titleTextView')
        self.driver.find_id(sourced_id + 'titleTextView').click()
        time.sleep(3)
        try:
            self.driver.find_id(sourced_id + 'roleall')
            self.driver.find_id(sourced_id + 'roleall').click()
        except:
            pass
        time.sleep(2)

    # 配音界面点击预览视频
    def test0(self):
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.wait_download(sourced_id + 'play')

    # 播放过程中暂停
    def test1(self):
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.find_id(sourced_id + 'fl_video').click()
        # self.driver.Background()
        self.driver.wait_download(sourced_id + 'play')
        time.sleep(2)

    # 播放过程中推到后台
    def test3(self):
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.Background()
        self.driver.wait_id(sourced_id + 'play')
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'living')
        except Exception as e:
            raise e

    # 录音权限
    def test_a(self):
        self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'next')
            self.driver.find_id(sourced_id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            pass
        time.sleep(2)

    # 手动点击提交进入配音预览界面
    def test_c(self):
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 在完整录制后的基础上点击原声试听，查看视频播放是否从头开始播放
    def test_d(self):
        time1 = datetime.datetime.now()
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.wait_download(sourced_id + 'play')
        time2 = datetime.datetime.now()
        time_result = time2 - time1
        time_video = self.driver.find_id(sourced_id + 'video_time').text
        print('视频时间：',time_video,'实际播放时间：',time_result)
        time.sleep(2)

    # 配音试听
    def test_e(self):
        self.driver.find_id(sourced_id + 'review')
        self.driver.find_id(sourced_id + 'review').click()
        self.driver.wait_download(sourced_id + 'play')
        time.sleep(2)

    # 试听过程中点击提交进入预览界面
    def test_f(self):
        self.driver.find_id(sourced_id + 'review').click()
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(1)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'clear_voice')
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
        except:
            self.driver.find_id(sourced_id + 'uploadbtn')
            #返回配音界面
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)

    # 试听过程中应用退到后台再启动
    def test_g(self):
        self.driver.find_id(sourced_id + 'review').click()
        self.driver.Background()
        self.driver.wait_id(sourced_id + 'review')
        time.sleep(2)

    # 试听过程中，点击退出配音界面
    def test_h(self):
        self.driver.find_id(sourced_id + 'review').click()
        time.sleep(1)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(sourced_id + 'txtContent').text
        tip_check = '确定放弃吗？'
        self.assertEqual(tip,tip_check,msg="退出配音界面弹窗提示文案错误")
        self.driver.find_id(sourced_id + 'btnCancel').click()
        time.sleep(2)

    # 点击回撤按钮
    def test_i(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'withdraw')
                self.driver.find_id(sourced_id + 'withdraw').click()
            except:
                break
        time.sleep(2)

    # 录制过程中暂停
    def test_j(self):
        self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'dubbingWaveform')
        except:
            print('没有显示音轨，未录制进人声')
        time.sleep(2)

    # 录制完成后自动跳转再返回配音界面
    def test_k(self):
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 手动拖音轨
    def test_l(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.185,self.y *0.65,self.x *0.787,self.y *0.65)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.24, self.y * 0.71, self.x * 0.81, self.y * 0.71)
        else:
            pass
        time.sleep(2)
        # 点击预览视频
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.wait_download(sourced_id + 'play')
        self.driver.find_id(sourced_id + 'complete').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 重新录制
    def test_m(self):
        self.driver.find_id(sourced_id + 'review').click()
        self.driver.wait_id(sourced_id + 'play')
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(4)

    # 回撤重录
    def test_n(self):
        el = self.driver.find_id(sourced_id + 'withdraw')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'scirpt')
        self.driver.find_id(sourced_id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(sourced_id + 'titleTextView')
        self.driver.find_id(sourced_id + 'titleTextView').click()
        time.sleep(3)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 编辑字幕
    def test_o(self):
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').send_keys('台词编辑')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(sourced_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip_check, tip, msg="提示文案错误")
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'withdraw')
            print('台词编辑保存失败')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 实况录制
    def test_p(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'living')
                break
            except:
                self.driver.find_id(sourced_id + 'withdraw').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'living').click()
        time.sleep(4)
        try:
            self.driver.find_id(sourced_id + 'cameraView2')
        except:
            print("实况开启失败")
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 实况录制后返回预览界面，点击预览原声
    def test_q(self):
        self.driver.find_id(sourced_id + 'play').click()
        self.driver.wait_download(sourced_id + 'play')
        time.sleep(2)

    # 编辑台词后重新录制实况
    def test_r(self):
        self.driver.find_id(sourced_id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content_editor').send_keys('台词编辑')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(sourced_id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        self.assertEqual(tip_check, tip, msg="提示文案错误")
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(4)
        try:
            self.driver.find_id(sourced_id + 'withdraw')
            print('台词编辑保存失败')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

    # 点击配音按钮直接重录实况
    def test_s(self):
        self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(4)

    # 点击录制普通作品
    def test_t(self):
        try:
            self.driver.find_id(sourced_id + 'living')
        except:
            self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'living').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'script_container').click()
        time.sleep(4)
        self.driver.find_id(sourced_id +'titleTextView').click()
        time.sleep(4)
        self.driver.find_id(sourced_id + 'action').click()
        self.driver.wait_download(sourced_id + 'title')
        self.driver.Background()
        time.sleep(2)