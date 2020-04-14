'''
author:Alvins.zhu
time:2019年6月3日
function:Login

New:
time:2019年12月25日15:25:55
function:优化完成
'''
# coding = utf-8
import random
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
# 获取当前项目的根路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()

def Chat_notices():
    '''点击进入聊天界面'''
    OP.find_id('com.happyteam.dubbingshow:id/userhead').click()
    time.sleep(2)
    for i in range(3):
        '''发送文字'''
        word = random.choice(['蒹葭苍苍，白露为霜。所谓伊人，在水一方。溯洄从之，道阻且长；溯游从之，宛在水中央。蒹葭凄凄，白露未晞...',
                              '关关雎鸠，在河之洲。窈窕淑女，君子好逑。参差荇菜，左右流之。窈窕淑女，寤寐求之。求之不得，寤寐思服。',
                              '氓之蚩蚩，抱布贸丝。匪来贸丝，来即我谋。送子涉淇，至于顿丘。匪我愆期，子无良媒。将子无怒，秋以为期',
                              '采薇采薇，薇亦作止。曰归曰归，岁亦莫止。靡家靡室，猃狁之故。不遑启居，猃狁之故。采薇采薇，薇亦柔止。',
                              '静女其姝，俟我于城隅。爱而不见，搔首踟蹰。静女其娈，贻我彤管。彤管有炜，说怿女美。自牧归荑，洵美且异',
                              '硕鼠硕鼠，无食我黍！三岁贯女，莫我肯顾。逝将去女，适彼乐土。乐土乐土，爰得我所？硕鼠硕鼠，无食我麦'])
        OP.find_id('com.happyteam.dubbingshow:id/editContent').send_keys(word)
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btn_send').click()
        time.sleep(2)
    time.sleep(2)
    '''切换语音'''
    OP.find_id('com.happyteam.dubbingshow:id/btn_change_input_mode').click()
    time.sleep(2)
    '''发送语音'''
    Voice = OP.find_id('com.happyteam.dubbingshow:id/btn_record_voice')
    TouchAction(devc).long_press(Voice, duration=10000).wait(5000).perform()
    time.sleep(4)

    '''点击播放语音'''
    try:
        OP.find_id('com.happyteam.dubbingshow:id/btn_play_sound_content_layout').click()
        time.sleep(5)
    except:
        pass
    time.sleep(2)
    '''发送图片'''
    OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/photo').click()
    time.sleep(2)
    '''随机选择一张图片'''
    choice = OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')
    select_photo = random.randint(1, int(len(choice)-1))
    OP.find_ids('com.happyteam.dubbingshow:id/cb_select_tag')[select_photo].click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/next_step_tv').click()
    time.sleep(4)
    '''选择作品'''
    OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/film').click()
    try:
        OP.wait_id('com.happyteam.dubbingshow:id/filmBg')
        time.sleep(2)
        '''选择视频'''
        OP.find_id('com.happyteam.dubbingshow:id/filmBg').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/btnSelect').click()
        time.sleep(4)
    except(NoSuchElementException, TimeoutException):
        print("作品列表加载失败")
        time.sleep(2)
        OP.back()
    time.sleep(2)
    '''发红包'''
    OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/redpacket').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/cash_num').send_keys("1")
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/btnSubmit').click()
    time.sleep(6)
    try:
        OP.find_id('com.happyteam.dubbingshow:id/generate_red_packet')
        OP.back()
    except:
        pass
    time.sleep(2)
    try:
        OP.find_id('com.happyteam.dubbingshow:id/red_packet')
        OP.find_id('com.happyteam.dubbingshow:id/red_packet').click()
        time.sleep(2)
        OP.find_id('com.happyteam.dubbingshow:id/open_red_packet_btn').click()
        try:
            OP.wait_id('com.happyteam.dubbingshow:id/user_head')
            time.sleep(2)
            OP.back()
        except(TimeoutException, NoSuchElementException):
            print("红包领取失败")
    except(NoSuchElementException, TimeoutException):
        print("无红包")
    time.sleep(2)
    print('社团邀请')
    OP.find_id('com.happyteam.dubbingshow:id/show_action').click()
    time.sleep(2)
    OP.find_id('com.happyteam.dubbingshow:id/union_inviter').click()
    try:
        OP.wait_id('com.happyteam.dubbingshow:id/user_image')
        time.sleep(2)
        '''选择社团'''
        OP.find_id('com.happyteam.dubbingshow:id/userName').click()
        time.sleep(3)
    except(NoSuchElementException, TimeoutException):
        print("社团列表未显示有社团")
        time.sleep(2)
        OP.back()
    time.sleep(2)
    '''退出聊天详情界面'''
    OP.back()
    '''返回聊天列表主界面'''
    time.sleep(2)

# if __name__=="__main__":
#     for i in range(10):
#         Chat_notices()
#         time.sleep(1)