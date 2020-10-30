#coding=utf-8
'''
配音界面功能模块，其它文件可引用
'''
import time, datetime
from Public.Driver_Operate import BaseOperate,resource_id


class Dubb_funcation():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #合作素材
    def Material_library_dubble(self):
        self.driver.wait_id(self.id + 'task_box')
        self.driver.find_id(self.id + 'btn_more').click()
        self.driver.wait_id(self.id + 'coor')
        self.driver.find_id(self.id + 'coor').click()
        time.sleep(2)
        self.driver.find_xpath('热门').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)

    # 双配素材-进入配音界面
    def Into_Dubbing_double(self):
        self.driver.find_id(self.id + 'dubbing_fake').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'close').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'dubbing_fake')
                self.driver.find_id(self.id + 'dubbing_fake').click()
                time.sleep(3)
                self.driver.find_id(self.id + 'next')
                self.driver.find_id(self.id + 'next').click()
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
        self.driver.wait_id(self.id + 'roleall')
        self.driver.find_id(self.id + 'roleall').click()
        time.sleep(2)

    #首次进入配音节目引导界面
    def Dub_Guidance(self):
        try:
            self.driver.find_id(self.id + 'subtitleView').click()
        except:
            pass
        time.sleep(2)

    #退出配音界面
    def Dub_Exit_dubbing(self):
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(3)

    # 双配素材配音界面配音角色切换
    def Dub_Exchange_roles(self):
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'role1_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'role2_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'coopera').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'roleall').click()
        time.sleep(2)

    # 配音界面背景音开关
    def Dub_Background_sound(self):
        self.driver.find_id(self.id + 'headset').click()
        time.sleep(2)
        try:
            tips = self.driver.find_id(self.id + 'txtContent').text
            check = '开启背景音需要插上耳机！'
            self.assertEqual(tips, check, msg='耳机提示文案不一致')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
        except:
            pass

    # 开启实况
    def Dub_Start_Camera(self):
        # 开启实况权限检查
        self.driver.find_id(self.id + 'living').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            time.sleep(2)
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
        try:
            self.driver.find_id(self.id + 'cameraView2')
        except:
            self.driver.find_id(self.id +  'living').click()
            time.sleep(4)

    #关闭实况开关
    def Dub_Close_Camera(self):
        self.driver.find_id(self.id + 'living').click()
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'cameraView2')
            self.driver.find_id(self.id +  'living').click()
        except:
            pass
        time.sleep(2)

    #配音界面台词列表
    def Dub_Script_list_swip(self):
        self.driver.find_id(self.id + 'scirpt').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'titleTextView')
        count = self.driver.find_ids(self.id + 'titleTextView')
        num = len(count)
        if num > 4:
            self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'cancelBn').click()
        self.driver.wait_id(self.id + 'scirpt')
        time.sleep(2)

    # 台词列表切换台词
    def Dub_Script_change(self):
        script_cout = int(self.driver.find_id(self.id + 'scirpt_count').text)
        if script_cout > 1:
            self.driver.find_id(self.id + 'scirpt').click()
            self.driver.wait_id(self.id + 'titleTextView')
            count = self.driver.find_ids(self.id + 'titleTextView')
            for i  in range((script_cout)-1,-1,-1):
                self.driver.find_ids(self.id + 'titleTextView')[i].click()
                self.driver.wait_id(self.id + 'edit_subtitle')
                self.driver.find_id(self.id + 'scirpt').click()
                self.driver.wait_id(self.id + 'titleTextView')
                time.sleep(2)
            self.driver.find_id(self.id + 'cancelBn').click()
        time.sleep(2)


    # 修改台词后点击完成，再次进入编辑界面查看修改后的台词
    def Dub_Script_edit(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_ids(self.id + 'content_editor')[0].clear()
        time.sleep(2)
        self.driver.find_ids(self.id + 'content_editor')[0].send_keys("台词修改")
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '修改台词将移除当前的配音进度'
        assert tip == tip_check
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        content = self.driver.find_ids(self.id + 'content_editor')[0].text
        content_check = '台词修改'
        assert content == content_check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

    # 修改首句台词后不保存返回配音界面再进，查看台词首句显示
    def Dub_Script_edit_nosave(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_ids(self.id + 'content_editor')[0].send_keys('台词修改')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '真的要放弃本次台词编辑吗？'
        assert  tip_check == tip
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(3)


    # 切换系统默认台词
    def Dub_Script_default(self):
        self.driver.find_id(self.id + 'scirpt').click()
        self.driver.wait_id(self.id + 'titleTextView')
        self.driver.find_id(self.id + 'titleTextView').click()
        time.sleep(3)
        try:
            self.driver.find_id(self.id + 'roleall')
            self.driver.find_id(self.id + 'roleall').click()
        except:
            pass
        time.sleep(2)

    # 清空字幕所有内容
    def Dub_Script_clearall(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.driver.hide_keyboard()
        time.sleep(2)
        for i in range(2):
            Subtitles = self.driver.find_ids(self.id + 'content_editor')
            for i in range(len(Subtitles)):
                self.driver.find_ids(self.id + 'content_editor')[i].clear()
            time.sleep(2)
            self.driver.swip_up()
            time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        toast = self.driver.wait_toast('//android.widget.Toast')
        toast_check = '台词不能为空，请输入至少一句台词'
        assert toast == toast_check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

    # 编辑台词输入特殊符号后保存
    def Dub_Script_special_char(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_id(self.id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content_editor').send_keys('∯∰∱∲∳')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'edit_subtitle')
        except:
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            self.driver.wait_id(self.id + 'edit_subtitle')

    #单行台词输入超过30个字符
    def Dub_Script_char_lenth(self):
        self.driver.find_id(self.id + 'edit_subtitle').click()
        time.sleep(2)
        self.driver.hide_Keyboard()
        self.driver.find_id(self.id + 'content_editor').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'content_editor').send_keys('123456789012345678901234567890123456789')
        tip = self.driver.wait_toast('//android.widget.Toast')
        check = '单行台词不能超过30个字符'
        assert tip == check
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'edit_subtitle')

    # 配音界面点击预览视频
    def Dub_Video_play(self):
        self.driver.find_id(self.id + 'play').click()
        try:
            self.driver.find_id(self.id + 'video_time')
        except Exception as e :
            raise e
        self.driver.wait_download(self.id + 'play')

    # 播放过程中暂停
    def Dub_Video_pause(self):
        self.driver.find_id(self.id + 'play').click()
        self.driver.find_id(self.id + 'fl_video').click()
        # self.driver.Background()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

    # 播放过程中推到后台
    def Dub_Video_background(self):
        self.driver.find_id(self.id + 'play').click()
        time.sleep(2)
        self.driver.Background()
        self.driver.wait_id(self.id + 'play')
        time.sleep(2)

    # 录音权限
    def Dub_Record_permissions(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            pass
        time.sleep(2)

    # 手动点击提交进入配音预览界面
    def Dub_Dub_into_preview(self):
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)

    # 在完整录制后的基础上点击原声试听，查看视频播放是否从头开始播放
    def Dub_Video_play_time(self):
        time1 = datetime.datetime.now()
        self.driver.find_id(self.id + 'play').click()
        self.driver.wait_download(self.id + 'play')
        time2 = datetime.datetime.now()
        time_result = time2 - time1
        time_video = self.driver.find_id(self.id + 'video_time').text
        print('视频时间：',time_video,'实际播放时间：',time_result)
        time.sleep(2)

    # 配音试听
    def Dub_Video_review(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)

    # 试听过程中点击提交进入预览界面
    def Dub_review_into_preview(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)


    # 试听过程中，点击退出配音界面
    def Dub_Video_review_quit(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        tip = self.driver.find_id(self.id + 'txtContent').text
        tip_check = '确定放弃吗？'
        self.assertEqual(tip,tip_check,msg="退出配音界面弹窗提示文案错误")
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)

    # 点击回撤按钮
    def Dub_Video_withdraw(self):
        while True:
            try:
                self.driver.find_id(self.id + 'withdraw')
                self.driver.find_id(self.id + 'withdraw').click()
            except:
                break
        time.sleep(2)

    # 录制过程中暂停
    def Dub_Record_pause(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'dubbingWaveform')
        except Exception as e:
            raise (e,'没有显示音轨，未录制进人声')
        time.sleep(2)

    # 录制完成后自动跳转再返回配音界面
    def Preview_back_dubbing(self):
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    # 手动拖音轨
    def Dub_Audio_track_move(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.185,self.y *0.65,self.x *0.787,self.y *0.65)
        elif self.y == 2280:
            self.driver.swip_move(self.x * 0.24, self.y * 0.71, self.x * 0.81, self.y * 0.71)
        else:
            pass
        time.sleep(2)

    # 重新录制
    def Dub_Restart_record_dubbing(self):
        self.driver.find_id(self.id + 'review').click()
        self.driver.wait_id(self.id + 'play')
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(4)

    # 长按回撤按钮
    def Dub_Long_withdraw(self):
        el = self.driver.find_id(self.id + 'withdraw')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)

    # 播放完整的视频
    def Preview_video_play(self):
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)

    # 字幕开关
    def Preview_subtitle_onoff(self):
        el = self.driver.find_id(self.id + 'add_subtitle_cb').get_attribute('checked')
        check = 'true'
        if el == check:
            print('字幕默认开启')
        else:
            print('字幕默认关闭')
        time.sleep(2)
        self.driver.find_id(self.id + 'add_subtitle_cb').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id(self.id + 'add_subtitle_cb').get_attribute('checked')
        assert el != el1
        self.driver.find_id(self.id + 'add_subtitle_cb').click()
        time.sleep(2)

    #降噪开关
    def Preview_voice_onoff(self):
        el = self.driver.find_id(self.id + 'clear_voice').get_attribute('checked')
        self.driver.find_id(self.id + 'clear_voice').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        el1 = self.driver.find_id(self.id + 'clear_voice').get_attribute('checked')
        assert el != el1
        self.driver.find_id(self.id + 'clear_voice').click()
        time.sleep(2)

    # 预览界面人声
    def Preview_voice_volume(self):
        #调节人声音量
        if self.y ==1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592,self.x * 0.37, self.y * 0.718)#调大音量
            time.sleep(4)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718,self.x * 0.115,self.y * 0.628)  # 调小音量
        elif self.y >2250:
            self.driver.swip_move(self.x*0.245, self.y*0.535,self.x*0.376, self.y*0.633)#调大音量
            time.sleep(4)
            self.driver.swip_move(self.x*0.364,self.y*0.627,self.x*0.107,self.y*0.627)# 调小音量
        else:
            pass
        time.sleep(4)

    # 声音校准
    def Preview_voice_calibration(self):
        self.driver.find_id(self.id + 'trim').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37,self.y * 0.718)  # 提前播放人声进度
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37,self.y * 0.718, self.x * 0.115,self.y * 0.628)  # 延后播放人声进度
        elif self.y >2250:
            self.driver.swip_move(self.x * 0.245,self.y * 0.535, self.x * 0.376, self.y * 0.633)  # 提前播放人声进度
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107,self.y * 0.627)  # 延后播放人声进度
        else:
            pass
        time.sleep(2)

    # 人声变声调节
    def Preview_Voice_Changer(self):
        self.driver.find_id(self.id + 'pitch').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37,self.y * 0.718)  # #人声声线加粗
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.718,self.x * 0.115,self.y * 0.628)  #人声声线变细
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.245, self.y * 0.535, self.x * 0.376,self.y * 0.633)  #人声声线加粗
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.364, self.y * 0.627, self.x * 0.107,self.y * 0.627)  #人声声线变细
        else:
            pass
        time.sleep(2)

    #人声混响调节
    def Preview_reverberation(self):
        self.driver.find_id(self.id + 'fx').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.093, self.y * 0.8, self.x * 0.093, self.y * 0.59)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.8, self.x * 0.254, self.y * 0.59)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.8, self.x * 0.419, self.y * 0.59)  # 增加回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.093, self.y * 0.59, self.x * 0.093, self.y * 0.8)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.59, self.x * 0.254, self.y * 0.8)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.59, self.x * 0.419, self.y * 0.8)  # 减小回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.098, self.y * 0.7, self.x * 0.098, self.y * 0.553)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.7, self.x * 0.252, self.y * 0.553)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.7, self.x * 0.413, self.y * 0.553)  # 增加回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.098, self.y * 0.553, self.x * 0.098, self.y * 0.7)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.553, self.x * 0.252, self.y * 0.7)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.553, self.x * 0.413, self.y * 0.7)  # 减小回声效果值
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
        else:
            pass
        # try:
        #     self.driver.find_xpath('确定')
        #     self.driver.find_xpath('确定').click()
        #     print("服务端关闭人声混响功能，不做混响调节测试")
        # except:

    # 背景音音量调节
    def Preview_background_music(self):
        if self.y == 1920:
            self.driver.swip_move(self.x*0.632,self.y*0.62,self.x*0.893,self.y*0.67)#增大背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.893,self.y*0.67,self.x*0.632,self.y*0.62)#减小背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x * 0.632, self.y * 0.62, self.x * 0.893, self.y * 0.67)  # 增大背景音音量
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.607,self.y*0.591,self.x*0.884,self.y*0.571)#增大背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.884,self.y*0.571,self.x*0.607,self.y*0.591)#减小背景音音量
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            self.driver.swip_move(self.x*0.607,self.y*0.591,self.x*0.884,self.y*0.571)#增大背景音音量
        else:
            pass
        time.sleep(2)

    #关闭背景音音量
    def Preview_close_background_music(self):
        self.driver.find_id(self.id + 'voice_open').click()
        # el = self.driver.find_id(self.id + 'voice_open').get_attribute('checked')
        # self.assertTrue(el,msg='状态点击背景音关闭按钮后，状态没有显示关闭')
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)

    # 背景音音乐列表中选择其它音乐
    def Preview_chage_music(self):
        count = self.driver.find_id(self.id + 'tvBgCount').text
        if int(count) > 1:
            self.driver.find_id(self.id + 'imgBgCount').click()
            time.sleep(4)
            if self.y==1920:
                self.driver.tap(self.x*0.5,self.y*0.469)
            elif self.y > 2250:
                self.driver.tap(self.x*0.5,self.y*0.464)
            else:
                pass
        time.sleep(4)

    # 背景音混响调节
    def Preview_background_reverberation(self):
        self.driver.find_id(self.id + 'bgfx').click()
        time.sleep(2)
        # try:
        #     self.driver.find_xpath('确定')
        #     self.driver.find_xpath('确定').click()
        #     print("服务端关闭人声混响功能，不做混响调节测试")
        # except:
        #     el = self.driver.find_id(self.id + 'bgfx').get_attribute('checked')
        #     self.assertTrue(el,msg='状态点击背景音混响按钮后，状态没有显示选中')
        #     time.sleep(2)
        if self.y == 1920:
            #增加混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.8, self.x*0.588, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.8, self.x*0.75, self.y*0.59)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.8, self.x*0.91, self.y*0.59)
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
            time.sleep(2)
            #减小背景音混响效果
            self.driver.swip_move(self.x*0.588, self.y*0.59, self.x*0.588, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.75, self.y*0.59, self.x*0.75, self.y*0.8)
            time.sleep(2)
            self.driver.swip_move(self.x*0.91, self.y*0.59, self.x*0.91, self.y*0.8)
            time.sleep(2)
        elif self.y > 2250:
            #增加混响效果
            TouchAction(self.driver).press(x=640, y=1636).move_to(x=643, y=1261).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=808, y=1648).move_to(x=815, y=1255).release().perform()
            time.sleep(2)
            TouchAction(self.driver).press(x=986, y=1642).move_to(x=980, y=1258).release().perform()
            time.sleep(2)
            self.driver.find_id(self.id + 'play_button').click()
            self.driver.wait_download(self.id + 'play_button')
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

    # 下载系统推荐背景音音乐
    def Preview_download_music(self):
        self.driver.find_id(self.id + 'bgvol').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'imgBgCount').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.955)
        elif self.y > 2250:
            self.driver.tap(self.x*0.5, self.y*0.96)
        else:
            pass
        self.driver.wait_id(self.id + 'btnRight')
        while True:
            try:
                self.driver.find_id(self.id + 'btnDownload')
                self.driver.find_id(self.id + 'btnDownload').click()
            except:
                break

    # 随机选中背景音音乐
    def Preview_select_music(self):
        count = self.driver.find_ids(self.id + 'title')
        select = random.randint(0,len(count)-1)
        self.driver.find_ids(self.id + 'title')[select].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)
        #选中音乐后进入音乐试听界面，拖动视频进度条
        if self.y ==1920:
            self.driver.swip_move(self.x*0.052,self.y*0.487,self.x*0.704,self.y*0.487)
        elif self.y > 2250:
            self.driver.swip_move(self.x*0.052,self.y*0.448,self.x*0.633,self.y*0.448)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'play_button').click()
        self.driver.wait_download(self.id + 'play_button')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'clear_voice')
        time.sleep(2)

    # 上滑加载背景音音乐列表并点击下载按钮
    def Preview_load_music_list(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)

    #预览界面点击完成
    def Preview_into_upload(self):
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)

    # 修改作品封面-视频截图
    def Upload_screenshot(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x*0.5,self.y*0.708)
            time.sleep(2)
            self.driver.swip_move(self.x*0.37,self.y*0.422,self.x*0.74,self.y*0.422)
        elif self.y > 2250:
            self.driver.tap(self.x*0.5,self.y*0.752)
            time.sleep(2)
            self.driver.swip_move(self.x*0.33,self.y*0.361,self.x*0.441,self.y*0.361)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
        time.sleep(2)
        # 选择视频截图
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.708)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.37, self.y * 0.422, self.x * 0.74, self.y * 0.422)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.752)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.33, self.y * 0.361, self.x * 0.441, self.y * 0.361)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    # 修改作品封面-拍照
    def Upload_photograph(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
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
            time.sleep(2)
        except:
            #VivoX21
            try:
                self.driver.find_id('com.android.camera:id/shutter_button')
                self.driver.find_id('com.android.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.android.camera:id/done_button').click()
                time.sleep(4)
            except:
                try:
                    # oppor11/oppor15
                    self.driver.find_id('com.oppo.camera:id/shutter_button')
                    self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.oppo.camera:id/done_button').click()
                    time.sleep(3)
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(2)

    # 修改作品封面-拍照-拍照以后点击取消
    def Upload_photograph(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
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
            time.sleep(2)
        except:
            # VivoX21
            try:
                self.driver.find_id('com.android.camera:id/shutter_button')
                self.driver.find_id('com.android.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.android.camera:id/done_button').click()
                time.sleep(4)
            except:
                try:
                    # oppor11
                    self.driver.find_id('com.oppo.camera:id/shutter_button')
                    self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.oppo.camera:id/done_button').click()
                    time.sleep(3)
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id('android:id/button1').click()
        time.sleep(4)

    # 修改作品封面-相册
    def Upload_picture(self):
        self.driver.find_id(self.id + 'btn_setting_cover_tip').click()
        time.sleep(3)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.856)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.875)
        else:
            pass
        time.sleep(2)
        photo_count = self.driver.find_ids(self.id + 'photo_wall_item_photo')
        select = random.randint(0,len(photo_count)-1)
        self.driver.find_ids(self.id + 'photo_wall_item_photo')[select].click()
        time.sleep(3)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(4)

    # 标题名称-输入30个字符
    def Upload_title(self):
        self.driver.find_id(self.id + 'title').send_keys('123456789012345678901234567890')
        time.sleep(2)
        char = self.driver.find_id(self.id + 'title').text
        char_check = '123456789012345678901234567890'
        assert char == char_check
        time.sleep(2)

    # 标题名称-清空标题
    def Upload_title_clear(self):
        self.driver.find_id(self.id + 'title').clear()
        num = self.driver.find_id(self.id + 'title_count').text
        check = '0/30'
        assert num == check
        time.sleep(2)

    # 上传界面标签显示检查
    def Upload_channel_select(self):
        try:
            self.driver.find_xpath('添加')
        except:
            self.driver.find_id(self.id + 'tv1').click()
        time.sleep(2)
        self.driver.find_xpath('添加').click()
        self.driver.wait_id(self.id + 'edit_text')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv')
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_xpath('添加').click()
            self.driver.wait_id(self.id + 'edit_text')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv1')
            self.driver.find_id(self.id + 'tv1').click()
            time.sleep(2)
            hot_lable = self.driver.find_ids(self.id + 'tv')
            select = random.randint(0, len(hot_lable))
            self.driver.find_ids(self.id + 'tv')[select].click()
            time.sleep(2)
            label_name = self.driver.find_id(self.id + 'tv1').text
            self.driver.find_id(self.id + 'tv_right').click()
            time.sleep(2)
            label_check = self.driver.find_id(self.id + 'tv1').text
            assert  label_name == label_check
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #上传界面设置私密
    def Upload_privacy(self):
        self.driver.find_id(self.id + 'pri_switch_tv').click()
        try:
            self.driver.find_id(self.id + 'private_top_tv2')
        except:
            raise ('点击私密后未显示私密提示文案')
        time.sleep(2)

    # 点击上传按钮
    def Upload(self):
        self.driver.find_id(self.id + 'uploadbtn').click()
        self.driver.wait_id(self.id + 'close')
        time.sleep(2)

    #上传成功后点击查看视频详情
    def Upload_video_detial(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #点击查看视频详情
            self.driver.find_id(self.id + 'img_url').click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            print('视频上传失败，不执行视频查看用例')

    #上传成功后下载视频到本地
    def Video_download(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #视频下载
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.922, self.y * 0.232, self.x * 0.57, self.y * 0.232)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.786, self.y * 0.186, self.x * 0.54, self.y * 0.186)
            time.sleep(2)
            self.driver.find_id(self.id + 'down').click()
            time.sleep(2)
            try:
                self.driver.find_xpath('直接下载')
                self.driver.find_xpath('直接下载').click()
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            except:
                self.driver.wait_id(self.id + 'btnSubmit')
                self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.507, self.y * 0.24, self.x * 0.897, self.y * 0.24)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.509, self.y * 0.186, self.x * 0.753, self.y * 0.186)
        except:
            pass
        time.sleep(2)

    #上传成功后视频站外分享
    def Upload_video_share(self):
        try:
            self.driver.find_id(self.id + 'wx')
            #微信分享
            self.driver.find_id(self.id + 'wx').click()
            time.sleep(4)
            self.driver.wait_id('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            self.driver.wait_id(self.id + 'wx')
            time.sleep(2)

            #朋友圈分享
            self.driver.find_id(self.id + 'wxf').click()
            self.driver.wait_id('com.tencent.mm:id/ch')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            self.driver.wait_id(self.id + 'wx')
            time.sleep(2)

            #QQ分享
            self.driver.find_id(self.id + 'qq').click()
            self.driver.wait_id('com.tencent.mobileqq:id/ivTitleBtnRightText')
            time.sleep(2)
            self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
            time.sleep(2)

            #QQ空间分享
            self.driver.find_id(self.id + 'qqz').click()
            self.driver.wait_id('com.tencent.mobileqq:id/ivTitleBtnRightText')
            self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
            time.sleep(2)

            #微博分享
            self.driver.find_id(self.id + 'wb').click()
            self.driver.wait_id('com.sina.weibo:id/titleSave')
            self.driver.find_id('com.sina.weibo:id/titleBack').click()
            time.sleep(2)
            self.driver.find_xpath('不保存').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.507,self.y*0.24,self.x*0.897,self.y *0.24)
            elif self.y == 2280:
                self.driver.swip_move(self.x * 0.786, self.y * 0.186, self.x * 0.54, self.y * 0.186)
            time.sleep(2)
        except Exception as  e:
            print(e)

    #上传成功进入视频详情删除视频
    def Upload_video_delete(self):
        try:
            self.driver.find_id(self.id + 'wx')
            self.driver.find_id(self.id + 'img_url').click()
            self.driver.wait_id(self.id + 'btnBack')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'setting').click()
            time.sleep(2)
            self.driver.tap(self.x * 0.5,self.y * 0.854)
            time.sleep(2)
            tip = self.driver.find_id(self.id + 'txtContent').text
            check = '删除作品'
            self.assertIn(check,tip,msg='作品删除提示内容校验不一致')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except Exception as e:
            print(e)

    #上传失败保存草稿箱
    def Upload_fail_save(self):
        try:
            self.driver.find_id(self.id + 're_update')
            self.driver.find_id(self.id + 'saveToDraft').click()
            time.sleep(3)
            self.driver.find_xpath('保存草稿').click()
            self.driver.wait_id(self.id + 'btnSubmit')
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except Exception as e:
            print(e)

    # 上传失败查看失败原因
    def Upload_fail_reason(self):
        try:
           self.driver.find_id(self.id + 're_update')
           self.driver.find_id(self.id + 'rl_bg').click()
           try:
               toast = self.driver.wait_toast('//android.widget.Toast')
               print('上传失败的情况下，点击作品封面：', toast)
           except:
               pass
           time.sleep(2)
           reason = self.driver.find_id(self.id + 're_update').text
           reason_state1 = '修改标题'
           reason_state2 = '重新上传'
           if reason == reason_state1:
               self.driver.find_id(self.id + 're_update').click()
               time.sleep(2)
               self.driver.find_id(self.id + 'edit').clear()
               time.sleep(2)
               self.driver.find_id(self.id + 'edit').send_keys('标题修改')
               self.driver.find_id(self.id + 'btnSubmit').click()
               time.sleep(2)
               try:
                   self.driver.wait_id(self.id + 'wx')
               except:
                   raise ('修改标题后重新上传失败')
           elif reason_state2 == reason_state2:
               self.driver.find_id(self.id + 're_update').click()
               try:
                   self.driver.wait_id(self.id + 'wx')
               except:
                   raise ('点击重新上传按钮后，作品依然上传失败')
           else:
               raise ('未知错误')
           time.sleep(2)
        except Exception as  e:
           print(e)