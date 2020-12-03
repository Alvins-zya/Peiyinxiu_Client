# encoding = utf-8
'''
@author: alvin.zhu
@file :Location_list.py
@time :2020/12/3 9:43
@Description: 配音秀应用中坐标点击位置集合
'''
from Public.Driver_Operate import BaseOperate

class location():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = BaseOperate().touch_X()
        self.y = BaseOperate().touch_Y()

    #首页顶部功能列表入口查找
    def home_func(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.854, self.y * 0.197, self.x * 0.249, self.y * 0.197)
            time.sleep(2)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.85, self.y * 0.15, self.x * 0.18, self.y * 0.15)
            time.sleep(2)

    #声漫背景音界面裁剪添加背景音
    def carton_cut_music(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.045, self.y * 0.718, self.x * 0.891, self.y * 0.683)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.934, self.y * 0.785, self.x * 0.066, self.y * 0.785)

    #配音界面拖动音轨
    def dub_track(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.185, self.y * 0.65, self.x * 0.787, self.y * 0.65)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.24, self.y * 0.71, self.x * 0.81, self.y * 0.71)
        else:
            pass
        time.sleep(2)

    #配音预览界面音量增大
    def voice_increase(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.24, self.y * 0.592, self.x * 0.37, self.y * 0.718)  # 提前播放人声进度
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.245, self.y * 0.535, self.x * 0.376, self.y * 0.633)  # 提前播放人声进度

    #配音预览界面音量减小
    def voice_reduce(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.37, self.y * 0.718, self.x * 0.115, self.y * 0.628)  # 延后播放人声进度
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.38, self.y * 0.62, self.x * 0.17, self.y * 0.62)  # 延后播放人声进度

    # 配音界面人声混响增大
    def voice_reverberation_increase(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.093, self.y * 0.8, self.x * 0.093, self.y * 0.59)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.8, self.x * 0.254, self.y * 0.59)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.8, self.x * 0.419, self.y * 0.59)  # 增加回声效果值
            time.sleep(2)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.098, self.y * 0.7, self.x * 0.098, self.y * 0.553)  # 增加混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.7, self.x * 0.252, self.y * 0.553)  # 增加空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.7, self.x * 0.413, self.y * 0.553)  # 增加回声效果值
            time.sleep(2)

    # 配音界面人声混响减小
    def voice_reverberation_reduce(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.093, self.y * 0.59, self.x * 0.093, self.y * 0.8)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.254, self.y * 0.59, self.x * 0.254, self.y * 0.8)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.419, self.y * 0.59, self.x * 0.419, self.y * 0.8)  # 减小回声效果值
            time.sleep(2)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.098, self.y * 0.553, self.x * 0.098, self.y * 0.7)  # 减小混响效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.252, self.y * 0.553, self.x * 0.252, self.y * 0.7)  # 减小空间效果值
            time.sleep(2)
            self.driver.swip_move(self.x * 0.413, self.y * 0.553, self.x * 0.413, self.y * 0.7)  # 减小回声效果值
            time.sleep(2)

    #配音界面背景音音量增大
    def back_music_increase(self):
        if self.y == 1920:
            # 增大背景音音量
            self.driver.swip_move(self.x * 0.632, self.y * 0.62, self.x * 0.893, self.y * 0.67)
        elif self.y > 2250:
            # 增大背景音音量
            self.driver.swip_move(self.x * 0.607, self.y * 0.591, self.x * 0.884, self.y * 0.571)

    # 配音界面背景音音量减小
    def back_music_reduce(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.893, self.y * 0.67, self.x * 0.632, self.y * 0.62)  # 减小背景音音量
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.884, self.y * 0.571, self.x * 0.607, self.y * 0.591)  # 减小背景音音量

    # 配音界面背景音混响增大
    def back_music_reverberation_increase(self):
        if self.y == 1920:
            # 增加混响效果
            self.driver.swip_move(self.x * 0.588, self.y * 0.8, self.x * 0.588, self.y * 0.59)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.75, self.y * 0.8, self.x * 0.75, self.y * 0.59)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.91, self.y * 0.8, self.x * 0.91, self.y * 0.59)
            time.sleep(2)
        elif self.y > 2250:
            # 增加混响效果
            self.driver.swip_move(self.x * 0.593, self.y * 0.699, self.x * 0.595, self.y * 0.539)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.748, self.y * 0.704, self.x * 0.755, self.y * 0.536)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.913, self.y * 0.702, self.x * 0.907, self.y * 0.538)
            time.sleep(2)

    # 配音界面背景音混响减小
    def back_music_reverberation_reduce(self):
        if self.y == 1920:
            # 减小背景音混响效果
            self.driver.swip_move(self.x * 0.588, self.y * 0.59, self.x * 0.588, self.y * 0.8)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.75, self.y * 0.59, self.x * 0.75, self.y * 0.8)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.91, self.y * 0.59, self.x * 0.91, self.y * 0.8)
            time.sleep(2)
        elif self.y > 2250:
            self.driver.swip_move(self.x * 0.595, self.y * 0.539, self.x * 0.593, self.y * 0.699)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.755, self.y * 0.536, self.x * 0.748, self.y * 0.704)
            time.sleep(2)
            self.driver.swip_move(self.x * 0.907, self.y * 0.538, self.x * 0.913, self.y * 0.702)
            time.sleep(2)

    #点击倒数第一个按钮
    def one_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.94)
        elif self.y > 2250:
            self.driver.tap(self.x*0.5, self.y*0.94)

    # 点击倒数第二个按钮
    def two_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.755)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.89)

    # 点击倒数第三个按钮
    def three_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.856)
        elif self.y > 2250:
            self.driver.tap(self.x * 0.5, self.y * 0.83)

    # 点击倒数第四个按钮
    def four_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.77)

    # 点击倒数第五个按钮
    def five_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.794)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.7)

    #点击倒数第六个按钮
    def six_from_last(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.573)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.64)

    #作品上传后分享列表滑动
    def upload_share_swipe(self):
        if self.y == 1920:
            self.driver.swip_move(self.x * 0.922, self.y * 0.232, self.x * 0.57, self.y * 0.232)
        elif self.y >= 2280:
            self.driver.swip_move(self.x * 0.857, self.y * 0.189, self.x * 0.496, self.y * 0.189)

    #作品站外分享
    def share_pyq(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)

    def share_wx_friend(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.315, self.y * 0.717)

    def share_QQ_zone(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.712)

    def share_sina(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.682, self.y * 0.712)

    def share_QQ_friend(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.869, self.y * 0.712)

    def share_message_friend(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.846)

    def share_copy_link(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.846)

    def share_download(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.31, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.311, self.y * 0.846)

    def share_forward(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.88, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.87, self.y * 0.846)

    def share_report(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.68, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.682, self.y * 0.846)

    #语聊间功能列表
    def chat_red(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.097, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.812)

    def chat_share(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.301, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.295, self.y * 0.812)

    def chat_message_friend(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.499, self.y * 0.812)

    def chat_blacklist(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.698, self.y * 0.812)

    def chat_manager(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.894, self.y * 0.812)

    def chat_games(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.1, self.y * 0.908)

    def chat_mic_num(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.295, self.y * 0.908)

    def chat_pia(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.496, self.y * 0.908)

    def chat_cp(self):
        if self.y == 1520:
            self.driver.tap(self.x * 0.497, self.y * 0.814)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.704, self.y * 0.908)

    def chat_share_pyq(self):
        self.driver.tap(self.x * 0.124, self.y * 0.8)

    def chat_share_wx_friend(self):
        self.driver.tap(self.x * 0.31, self.y * 0.8)

    def chat_share_QQ_zone(self):
        self.driver.tap(self.x * 0.5, self.y * 0.8)

    def chat_share_sina(self):
        self.driver.tap(self.x * 0.66, self.y * 0.8)

    def chat_share_QQ_friend(self):
        self.driver.tap(self.x * 0.87, self.y * 0.8)

    def chat_share_message_friend(self):
        self.driver.tap(self.x * 0.124, self.y * 0.912)

    def chat_share_copy_link(self):
        self.driver.tap(self.x * 0.31, self.y * 0.912)

    def chat_share_society(self):
        self.driver.tap(self.x * 0.5, self.y * 0.912)

    #屏幕居中二次确认弹窗
    def screen_confirm_buttem(self):
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)







