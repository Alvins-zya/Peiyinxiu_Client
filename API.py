#coding = utf-8
'''
author:alvins.zhu
time: 2019年9月29日
function：功能脚本调用接口数据校准

'''
import sys
import io
import json
import hashlib
import requests
from pprint import pprint
from itertools import chain
import random
import time
from urllib.parse import quote
from urllib import request
import ssl
from urllib import parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
time = int(round(time.time()*1000))#视频列表（detail_list）接口中的t参数

Appkey = '193dd7cc7845df55'
Token = '3889d15834f814edec30e9aa4695bb2f'
UserId = '16685645'
Sign_code = 'd62bcbe08764808e'
Header =  {'Content-Tyoe': 'application:json',
           'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'}


'''
获取国家手机区号列表信息
'''
def get_country(token, UserID):
    data = 'appkey=193dd7cc7845df55&token=%s&userId=%s|d62bcbe08764808e' % (token, UserID)
    signs = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/Api/User/GetCountryCodeList"
    req_headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
                    }
    req_data = {
        'appkey': '193dd7cc7845df55',
        'token': token,
        'userId': UserID,
        'sign': signs
    }
    resp = requests.get(req_url, params=req_data, headers=req_headers)
    # print(resp.status_code)
    # print(resp.text)
    get_info = json.loads(resp.text)
    get_data = get_info['data'][0]
    country = get_data['country_code_list']
    # for i in range(len(get_data)):
    #     country = get_data[i]['country_code_list']
    #     print(country)  # 按字母排序，列表所有国家列表
    # get_code = country[0]
    # print(get_code)
    name = [x['name'] for x in country]
    code = [x['code'] for x in country]
    # print(name)  # 取出列中name的值
    # print(code)  # 取出列中code的值
    return name,code


'''
国家区号搜索

'''
def Search_country(country):
    data = 'appkey=193dd7cc7845df55&keywords=%s&token=&userId=0|d62bcbe08764808e'%(country)
    sign = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/Api/User/SearchCountryCode"
    req_headers = {
        'Content-Tyoe':'application:json',
        'User-Agent':'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }
    req_data = {
        'appkey':'193dd7cc7845df55',
        'keywords':country,
        'token':'',
        'userId':'0',
        'sign':sign
    }
    resq = requests.get(req_url,params=req_data,headers = req_headers)
    get_info = json.loads(resq.text)
    get_data = get_info['data'][0]['name']#获取接口返回的msg内容
    # print(get_data)
    return get_data

'''
用户手机号登录获取用户登录记录信息

'''

def Login_history(phone,password):
    hmd5 = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
    '''
    获得的hmd5是小写，需要转成大写
    '''
    ps_transform = hmd5.upper()
    data ='appkey=193dd7cc7845df55&code=&countryCode=86&mobile=%s&password=%s&token=&userId=0|d62bcbe08764808e'%(phone,ps_transform)
    sign = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/Api/User/GetBindMobileUser"
    req_headers = {
        'Content-Tyoe': 'application:json',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }
    req_data = {
        'appkey':'193dd7cc7845df55',
        'code':'',
        'countryCode':'86',
        'mobile':phone,
        'password':ps_transform,
        'token':'',
        'userId':'0',
        'sign':sign
    }
    resq = requests.post(req_url,params=req_data,headers = req_headers)
    get_info = json.loads(resq.text)
    get_data = get_info['data']
    nick_name = [x['nick_name'] for x in get_data]
    user_id = [x['user_id'] for x in get_data]
    '''
    将nick_name、user_id两个list交叉合并成一个列表
    '''
    L = list(chain.from_iterable(zip(nick_name,user_id)))
    return L
'''
手机号登录
'''

def Phone_login():
    data = 'accessToken=E10ADC3949BA59ABBE56E057F20F883E&appkey=193dd7cc7845df55&countryCode=86&mobile=18072702677&token=&type=6&uid=4655861&userId=0|d62bcbe08764808e'
    sign = hashlib.md5(data.encode('UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/api/User/Login"
    req_headers = {
        'Content-Tyoe': 'application:json',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }
    req_data = {
        'accessToken':'E10ADC3949BA59ABBE56E057F20F883E',
        'appkey':'193dd7cc7845df55',
        'countryCode':'86',
        'mobile':'18072702677',
        'token':'',
        'type':'6',
        'uid':'4655861',
        'userId':0,
        'sign':sign
    }
    resq = requests.post(req_url,params = req_data,headers = req_headers)
    print(resq.text)

'''
获取首页作品列表数据
'''
def Home_works():
    data = 'appkey=193dd7cc7845df55&area=0&bannerGroupId=0&eventMaxId=0&gps=&isDrop=1&pg=1&t=1198&token=&userId=0|d62bcbe08764808e'
    sign = hashlib.md5(data.encode('UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/api/Film/HomeData"
    req_headers = {
        'Content-Tyoe': 'application:json',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }
    req_data = {
        'appkey':'193dd7cc7845df55',
        'area':0,
        'bannerGroupId':'0',
        'eventMaxId':'0',
        'gps':'',
        'isDrop':1,
        'pg':1,
        't':1198,
        'token':'',
        'userId':0,
        'sign':sign
    }
    resq = requests.get(req_url,params=req_data,headers = req_headers)
    info = json.loads(resq.text)
    data = info['data']['film']
    # print(resq.text)
    Video_name = [x ['title'] for x in data]
    Video_plays = [x ['play_count'] for x in data]
    Video_gold = [x ['good_count']for x in data]
    # print(Video_name,'\n',Video_plays,'\n',Video_gold)
    # print(resq.text)







'''
语聊列表中房间列表数据获取
'''
class Chat():
    def __init__(self):
        pass

    def Chat_room_list():
        data = 'appkey=193dd7cc7845df55&pg=1&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e'
        sign = hashlib.md5(data.encode('utf-8')).hexdigest()
        req_url = "http://a.api1.peiyinxiu.com/api/live/LiveList"
        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }
        req_data = {
            'appkey' : '193dd7cc7845df55',
            'pg' : 1,
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'userId' : 16685645,
            'sign' : sign
        }
        resq = requests.get(req_url,params= req_data, headers = req_headers)
        # print(resq.text)
        get_info = json.loads(resq.text)
        get_data = get_info['data']['list']
        Live_title = [x['title'] for x in get_data]
        Live_id = [x['live_id'] for x in get_data]
        dic = dict(zip(Live_title,Live_id))#将两个列表的值组合成字典
        print(dic)
        return dic
    '''
    获取语聊间详情信息
    '''
    def Chat_detail(self,Live_id):
        self.Id = Live_id
        data = 'appkey=193dd7cc7845df55&' \
               'liveId=%s&' \
               'pushToken=b0449721cd7db122c13f3da23d758d9f&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645|d62bcbe08764808e' % (self.Id)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()
        req_url = "http://a.api1.peiyinxiu.com/Api/live/Detail"
        req_headers = {
            'Content-Type' : 'application:json',
            'User-Agent' : 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'liveId' : self.Id,
            'pushToken' : 'b0449721cd7db122c13f3da23d758d9f',
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'userId' : 16685645,
             'sign' : sign
        }
        resq = requests.get(req_url, params= req_data, headers = req_headers)
        get_info = json.loads(resq.text)
        get_owner_ID = get_info['data']['owner_user']['user_id']
        get_other = get_info['data']['role_users']
        User_name = [x['user_name'] for x in get_other]
        # print(get_owner_ID)
        # print(User_name)
        return get_owner_ID,User_name

    '''
    获取礼物小时榜
    '''
    def gift_hour(self,Live_id,User_id):
        self.live = Live_id
        self.user = User_id

        data = 'appkey=193dd7cc7845df55&' \
               'liveId=%s&' \
               'roomUserId=%s&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645|d62bcbe08764808e' % (self.live, self.user)
        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = "http://a.api1.peiyinxiu.com/api/live/GetHourRankingList"
        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }
        resq_data = {
            'appkey': '193dd7cc7845df55',
            'liveId': self.live,
            'roomUserId': self.user,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign': sign
        }

        resq = requests.get(req_url, params= resq_data, headers = req_headers)
        # print(resq.text)
        get_info = json.loads(resq.text)
        get_data = get_info['data']['rankList']
        # print(get_data)
        list_name = [x['user_name'] for x in get_data]
        list_value = [x['gift_value'] for x in get_data]
        dic = dict(zip(list_name, list_value))
        print(dic)

    '''
    获取进场列表用户信息
    '''
    def Arrival_user(self,Live_ID):
        self.ID = Live_ID

        data = 'appkey=193dd7cc7845df55&' \
               'keywords=&' \
               'liveId=%s&' \
               'pg=1&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'type=1&' \
               'userId=16685645|d62bcbe08764808e' % (self.ID)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()
        req_url = "http://a.api1.peiyinxiu.com/Api/Live/GetLineUserList"

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_data  = {
            'appkey' : '193dd7cc7845df55',
            'keywords' : '',
            'liveId' : self.ID,
            'pg' : 1,
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'type' : 1,
            'userId' : 16685645,
            'sign' : sign
        }

        resq = requests.get(req_url, params= req_data, headers = req_headers)
        info = json.loads(resq.text)
        datas = info['data']
        User_name = [x['user_name'] for x in datas]
        print(User_name)


    '''
    获取贡献榜日榜、周榜
    '''
    def Contribution_list(self,way):
        data = 'appkey=193dd7cc7845df55&' \
               'classId=0&' \
               'pg=1&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645&' \
               'way=%s|d62bcbe08764808e' % (way)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = "http://a.api1.peiyinxiu.com/Api/RankingList/GetLiveRankingList"

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'classId' : 0,
            'pg': 1,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'way': way,
            'sign': sign,
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)
        info = json.loads(reqs.text)
        dates = info['data']
        name = [x['user_name'] for x in dates]
        golds = [x['gold2'] for x in dates]
        list = dict(zip(name,golds))
        print(list)

    '''
       获取收入榜日榜、周榜
    '''

    def Income_list(self, way):
        data = 'appkey=193dd7cc7845df55&' \
               'classId=1&' \
               'pg=1&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645&' \
               'way=%s|d62bcbe08764808e' % (way)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = "http://a.api1.peiyinxiu.com/Api/RankingList/GetLiveRankingList"

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 1,
            'pg': 1,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'way': way,
            'sign': sign,
        }

        reqs = requests.get(req_url, params=req_data, headers=req_headers)
        info = json.loads(reqs.text)
        dates = info['data']
        name = [x['user_name'] for x in dates]
        golds = [x['gold2'] for x in dates]
        list = dict(zip(name, golds))
        print(list)


    '''
    获取房间中第一页的礼物列表
    '''
    def live_gift(self):
        data = 'appkey=193dd7cc7845df55&' \
               'objectUserId=0&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645|d62bcbe08764808e'
        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = 'http://a.api1.peiyinxiu.com/Api/live/GetGifts'

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_data = {
            'appkey':'193dd7cc7845df55',
            'objectUserId' : 0,
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'userId' : 16685645,
            'sign' : sign
        }

        resq = requests.get(req_url, params= req_data, headers = req_headers)
        info = json.loads(resq.text)
        datas = info['data']
        gift_list = [x['name'] for x in datas]
        print(gift_list)



'''
频道列表主界面信息获取

'''
class Channel():
    def __init__(self):
        pass

    '''
    获取主界面信息
    
    '''
    def Channel_home(self):
        data = 'appkey=193dd7cc7845df55&pg=1&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = 'http://a.api1.peiyinxiu.com/Api/Film/ChannelHome'

        req_headers={
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_data = {
            'appkey': '193dd7cc7845df55',
            'pg': 1,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign': sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        # print(reqs.text)

        info = json.loads(reqs.text)

        #获取频道频道信息
        # Channels = info['data']['channelRecommendTagList']
        #
        # Cha_list = [x ['name'] for x in Channels]
        #
        # print(Cha_list)

        #获取视频列表信息
        lists = []
        film_ID = []
        Userid = []
        Video = info['data']['channelHotTagAndFilmList']
        # print(Videos1)
        for i in range(len(Video)):
            Videos = info['data']['channelHotTagAndFilmList'][i]
            # print(Videos)
            for x in range(3):
                Videos_list = Videos['channelHotFilmList'][x]['title']
                Video_id = Videos['channelHotFilmList'][x]['filmId']
                Video_user = Videos['channelHotFilmList'][x]['userId']
                lists.append(Videos_list)
                film_ID.append(Video_id)
                Userid.append(Video_user)

        name = random.choice(lists)#从list中随机获取作品名称

        num = lists.index(name)#取出作品名称的索引号

        F_id = film_ID[num]#取出作品名称对应的作品ID

        U_id = Userid[num]#取出作品名称对应的用户ID

        channel_code = [x ['code'] for x in Video]
        # print(channel_code)

        # Cod = channel_code.index(random.choice(channel_code))
        # Films = info['data']['channelHotTagAndFilmList'][Cod]['channelHotFilmList']
        # print(Films)
        New_list = []
        for i in range(0,len(lists),3):
            new = lists[i:i+3]
            New_list.append(new)
        # print(New_list[0])

        channel_list = dict(zip(channel_code, New_list))#将获取的频道code与作品名称列表合成一个字典。key:value1,value2.value3

        # pprint(channel_list)
        # print(name)
        for idx_temp ,list_value in enumerate(list(channel_list.values())):
            if isinstance(list_value, int):
                continue
            if name in list_value:
                idx = idx_temp
                break
        valuse =(channel_list[list(channel_list.keys())[idx]])#获取channel_list中匹配的作品名称列表，value
        key = list(channel_list.keys())[list(channel_list.values()).index(valuse)]#以values为value，获取channe_list中的key值
        # print(key)
        return name,F_id,U_id,key

        # pprint(list)
        # return list
    '''
    获取更多频道界面中的频道信息
    '''
    def channel_most(self):

        data = 'appkey=193dd7cc7845df55&keywords=&pg=1&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Film/SearchChannel'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'keywords' : '',
            'pg' : 1,
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'userId' : 16685645,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        # print(reqs.text)

        info = json.loads(reqs.text)

        datas = info['data']

        chanel_name_list = [x['name'] for x in datas]

        print(chanel_name_list)

    '''
    获取视频作品送礼用户列表信息
    '''
    def video_gift_list(self,video):
        self.name = video[0]
        print(self.name)
        self.Film = video[1]
        self.ID = video[2]

        data = 'appkey=193dd7cc7845df55&' \
               'objectId=%s&' \
               'objectType=0&' \
               'objectUserId=%s' \
               '&pg=1&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645|d62bcbe08764808e' % (self.Film,self.ID)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://a.api1.peiyinxiu.com/api/Gift/GetUserRanks'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'objectId' : self.Film,
            'objectType' : 0,
            'objectUserId' : self.ID,
            'pg' : 1,
            'token' : '824f319949e8ae6269556ed101fe88eb',
            'userId' : 16685645,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)
        info = json.loads(reqs.text)
        datas = info['data']['users']
        names = [x ['user_name'] for x in datas]
        Ids = [x ['user_id'] for x in datas]
        # print(names)
        # print(Ids)
        return names,Ids

    '''
    获取单个用户送礼详情
    '''
    def Gift_details(self,Film__video_id,send_user_ID):
        self.Film = Film__video_id[1]
        self.User = Film__video_id[2]
        self.send_user = send_user_ID[1][0]#获取作品送礼列表中用户的ID列表中的第一个用户的ID

        # print(self.Film)
        # print(self.User)
        # print(self.send_user)

        data = 'appkey=193dd7cc7845df55&' \
               'objectId=%s&' \
               'objectType=0&' \
               'objectUserId=%s&' \
               'sendUserId=%s&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'userId=16685645|d62bcbe08764808e' % (self.Film,self.User,self.send_user)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Gift/GetSendGifts'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'objectId' : self.Film,
            'objectType' : 0,
            'objectUserId': self.User,
            'sendUserId': self.send_user,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign': sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)
        # print(reqs.text)
        info = json.loads(reqs.text)
        datas = info['data']
        detail_gift = [x ['name'] for x in datas]
        print(detail_gift)


    '''
    获取点击进入视频详情返回的视频列表中的作品标题名称（上下滑动视频）
    '''
    def details_list(self,channel):
        self.code = channel[3]
        self.id = channel[1]
        data = 'appkey=193dd7cc7845df55&' \
               'channelCode=%s&' \
               'filmId=%s&' \
               'filmIds=%s&' \
               'pg=1&' \
               't=%s&' \
               'token=824f319949e8ae6269556ed101fe88eb&' \
               'type=4&' \
               'userId=16685645|d62bcbe08764808e' % (self.code,self.id,self.id,time)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/api/film/DetailList'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'channelCode': self.code,
            'filmId': self.id,
            'filmIds': self.id,
            'pg': 1,
            't': time,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'type': 4,
            'userId': 16685645,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)
        # print(reqs.text)
        info  = json.loads(reqs.text)
        datas = info['data']
        # pprint(datas)
        Video_titles = [x ['title'] for x in datas]
        print(Video_titles)

'''

首页排行榜

'''
class Leaderboard():
    '''
    首页进入排行榜后获取标签榜的tagID
    '''
    def GetRankingClassList(self,name):
        data = 'appkey=193dd7cc7845df55&token=1c421b5005166a65f00dd0154acba098&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://101.37.152.245:9094/Api/RankingList/GetRankingClassList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'token': '1c421b5005166a65f00dd0154acba098',
            'userId': 16685645,
            'sign': sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)
        print(reqs.text)
        info = json.loads(reqs.text)

        datas = info['data']
        # pprint(datas)

        '''
        输入标签榜显示的标签名称，获取标签榜的tagID
        '''
        Name = name
        for x in datas:
            if x.get('tag_name') == Name:
                ID = (x.get('tag_id'))
        print(ID)



    '''
    获取富豪榜-日、周、月榜列表
    '''
    def Regal(self,time):
        self.T = time #输入日、周、月参数值：1,2,3
        data = 'appkey=193dd7cc7845df55&classId=1&pg=1&token=1c421b5005166a65f00dd0154acba098&userId=16685645&way=%s|d62bcbe08764808e' %(self.T)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://101.37.152.245:9094/Api/RankingList/GetUserRankingList'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'classId': 1,
            'pg': 1,
            'token': '1c421b5005166a65f00dd0154acba098',
            'userId': 16685645,
            'way': self.T,
            'sign': sign,

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info  = json.loads(reqs.text)

        datas = info['data']

        User_name = [x ['user_name'] for x in datas]
        golds = [x ['desc'] for x in datas]
        dic = dict(zip(User_name,golds))#将榜单中的用户与消费金额合成一个字典列表
        print(dic)

    '''
    获取主播榜日、周、月榜单信息
    '''
    def Anchor_list(self,Time):
        self.T = Time  # 输入日、周、月参数值：1,2,3
        data = 'appkey=193dd7cc7845df55&classId=2&pg=1&token=1c421b5005166a65f00dd0154acba098&userId=16685645&way=%s|d62bcbe08764808e' % (self.T)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://101.37.152.245:9094/Api/RankingList/GetUserRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 2,
            'pg': 1,
            'token': '1c421b5005166a65f00dd0154acba098',
            'userId': 16685645,
            'way': self.T,
            'sign': sign,

        }

        reqs = requests.get(req_url, params=req_data, headers=req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        User_name = [x['user_name'] for x in datas]
        golds = [x['desc'] for x in datas]
        dic = dict(zip(User_name, golds))  # 将榜单中的用户与消费金额合成一个字典列表
        print(dic)


    '''
    获取社团榜日、周、月榜单信息
    '''
    def Society_list(self,Time):
        self.T = Time  # 输入日、周、月参数值：1,2,3
        data = 'appkey=193dd7cc7845df55&classId=3&pg=1&token=1c421b5005166a65f00dd0154acba098&userId=16685645&way=%s|d62bcbe08764808e' % (
            self.T)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://101.37.152.245:9094/Api/RankingList/GetUserRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 3,
            'pg': 1,
            'token': '1c421b5005166a65f00dd0154acba098',
            'userId': 16685645,
            'way': self.T,
            'sign': sign,

        }

        reqs = requests.get(req_url, params=req_data, headers=req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        User_name = [x['user_name'] for x in datas]
        golds = [x['desc'] for x in datas]
        dic = dict(zip(User_name, golds))  # 将榜单中的用户与消费金额合成一个字典列表
        print(dic)



    '''
    获取素材榜日、周、月榜单信息
    '''
    def Material_list(self,Time):
        self.T = Time  # 输入日、周、月参数值：1,2,3
        data = 'appkey=193dd7cc7845df55&classId=4&pg=1&token=1c421b5005166a65f00dd0154acba098&userId=16685645&way=%s|d62bcbe08764808e' % (
            self.T)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://101.37.152.245:9094/Api/RankingList/GetUserRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 4,
            'pg': 1,
            'token': '1c421b5005166a65f00dd0154acba098',
            'userId': 16685645,
            'way': self.T,
            'sign': sign,

        }

        reqs = requests.get(req_url, params=req_data, headers=req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        User_name = [x['user_name'] for x in datas]
        golds = [x['desc'] for x in datas]
        dic = dict(zip(User_name, golds))  # 将榜单中的用户与消费金额合成一个字典列表
        print(dic)


    '''
    获取作品榜列表信息
    '''
    def works_list(self):
        data = 'appkey=193dd7cc7845df55&classId=5&pg=1&tagId=0&token=3ef54a1b9978d185d943b03edc47f552&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/RankingList/GetFilmRankingList'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'classId': 5,
            'pg': 1,
            'tagId': 0,
            'token': '3ef54a1b9978d185d943b03edc47f552',
            'userId': 16685645,
            'sign': sign,
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        Titles = [x ['title'] for x in datas]

        print(Titles)


    '''
    获取标签榜列表中作品信息
    '''
    def label(self,tag):
        data = 'appkey=193dd7cc7845df55&classId=6&pg=1&tagId=%s&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e' % (tag)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers ={
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/RankingList/GetFilmRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 6,
            'pg': 1,
            'tagId': tag,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign,
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        Titles = [x ['title'] for x in datas]

        print(Titles)



    '''
    获取标签列表中标签信息
    '''

    def Lable_list(self):

        data = 'appkey=193dd7cc7845df55&pg=0&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Film/GetHotChannels'

        req_data = {
            'appkey' :'193dd7cc7845df55',
            'pg': 0,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign,
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        N = '声优'

        for x in datas:
            if x.get('name') == N:
                Code = x.get('code')
        print(Code)



    '''
    获取潜力榜作品列表信息
    '''
    def Potential_list(self):
        data = 'appkey=193dd7cc7845df55&classId=7&pg=1&tagId=0&token=3ef54a1b9978d185d943b03edc47f552&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/RankingList/GetFilmRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 7,
            'pg': 1,
            'tagId': 0,
            'token': '3ef54a1b9978d185d943b03edc47f552',
            'userId': 16685645,
            'sign': sign,
        }

        reqs = requests.get(req_url, params=req_data, headers=req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        Titles = [x['title'] for x in datas]

        print(Titles)


    '''
    获取社作榜作品列表信息
    '''
    def Social_list(self):
        data = 'appkey=193dd7cc7845df55&classId=8&pg=1&tagId=0&token=3ef54a1b9978d185d943b03edc47f552&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/RankingList/GetFilmRankingList'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 8,
            'pg': 1,
            'tagId': 0,
            'token': '3ef54a1b9978d185d943b03edc47f552',
            'userId': 16685645,
            'sign': sign,
        }

        reqs = requests.get(req_url, params=req_data, headers=req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        Titles = [x['title'] for x in datas]

        print(Titles)


'''
首页有声漫画
'''
class Comic():
    '''
    有声漫画推荐界面列表信息
    '''
    def recommend(self):
        data = 'appkey=193dd7cc7845df55&classId=8&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetHomeComicList_New'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 8,
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info = json.loads(reqs.text)

        datas = info['data']['comic_list']

        Title = [x ['title'] for x in datas]

        print(Title)


    '''
    有声漫画界面最新列表中的作品信息
    '''
    def Newest(self):
        data = 'appkey=193dd7cc7845df55&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetHomeNewestComicList'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x in datas]
        print(Title)



    '''
    获取分类列表中默认tab下的漫画列表信息
    '''
    def classification(self):
        data = 'appkey=193dd7cc7845df55&classId=0&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header ={
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetHomeComicList_New'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'classId': 0,
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign,

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']['comic_list']

        Title = [x ['title'] for x in datas ]

        print(Title)

    '''
    获取声漫收藏列表作品信息
    '''
    def Collection(self):
        data = 'appkey=193dd7cc7845df55&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetComicFavoriteList'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x in datas]

        print(Title)


    '''
    获取漫画库默认tab（全部）界面下漫画素材列表信息
    '''
    def Comic_Library(self):

        data = 'appkey=193dd7cc7845df55&classId=0&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'

        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetComicLibrary_new'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'classId': 0,
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign' : sign

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)
        info =json.loads(reqs.text)

        datas = info['data']['comic_list']

        Title = [x ['title'] for x in datas]

        print(Title)


    '''
    获取有声漫画中我的漫画的列表信息
    '''
    def My_comic(self):

        data = 'appkey=193dd7cc7845df55&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/MyComicList'

        req_data = {
            'appkey' : '193dd7cc7845df55',
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x in datas]

        print(Title)


    '''
    获取声漫搜索界面中的推荐声漫素材列表信息
    '''
    def Recommend_Comic(self):

        data = 'appkey=193dd7cc7845df55&classId=0&pg=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Comic/GetComicLibrary_new'

        req_data = {
            'appkey': '193dd7cc7845df55',
            'classId': 0,
            'pg': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']['comic_list']

        Title = [x ['title'] for x in datas]
        print(Title)


'''
首页曝光区
'''

def Exposure():

    data = 'appkey=193dd7cc7845df55&pg=1&token=3ef54a1b9978d185d943b03edc47f552&userId=16685645|d62bcbe08764808e'

    sign = hashlib.md5(data.encode('utf-8')).hexdigest()

    req_header ={
        'Content-Type': 'application:json',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }

    req_url = 'http://a.api1.peiyinxiu.com/Api/Exposure/GetExposureListAndTask'

    req_data = {
        'appkey' : '193dd7cc7845df55',
        'pg': 1,
        'token': '3ef54a1b9978d185d943b03edc47f552',
        'userId': 16685645,
        'sign': sign

    }

    reqs = requests.get(req_url, params= req_data, headers = req_header)

    info = json.loads(reqs.text)

    datas = info['data']['list']

    Title = [x ['title'] for x in datas]

    print(Title)


'''
data 坐标参数里的逗号被编码，导致无法请求成功，待解决。
'''
def Near():

    data = 'appkey=193dd7cc7845df55&gps=120.094985,30.308165&pg=1&t=0&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

    sign = hashlib.md5(data.encode('utf-8')).hexdigest()

    req_header = {
        'Content-Type': 'application/json',
        'Accept-Charset': 'utf-8',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }

    req_url = 'http://a.api1.peiyinxiu.com/Api/film/GetNearList?'

    req_data = {
        'appkey': '193dd7cc7845df55',
        'gps': '120.094985,30.308165',
        'pg': '1',
        't': '0',
        'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
        'userId': '16685645',
        'sign': sign
    }
    # params = parse.urlencode(req_data)
    # reqs = request.urlopen('http://a.api1.peiyinxiu.com/Api/film/GetNearList?%s' %(params))
    # print(reqs.read().decode('utf-8'))
    reqs = requests.get(req_url, params= req_data, headers = req_header)
    print(reqs.text)

    # info = json.loads(reqs.text)
    #
    # datas = info['data']
    #
    # Title = [x ['title'] for x in datas]
    #
    # print(Title)


'''
素材库合作广场
'''
class Coopera():
    '''
    获取广场界面中待合作作品名称信息
    '''
    def Square(self):

        data = 'appkey=193dd7cc7845df55&pg=1&roleGender=0&token=ae710f54f00fa97c18fd52d2942f4d2c&userGender=0&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers ={
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/api/Coopera/Square'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'pg': 1,
            'roleGender': 0,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userGender': 0,
            'userId': 16685645,
            'sign' :sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info  = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x  in  datas ]

        print(Title)

    '''
    获取合作广场热门tab下作品名称信息
    '''
    def Hot(self):

        data = 'appkey=193dd7cc7845df55&pg=1&roleGender=0&token=ae710f54f00fa97c18fd52d2942f4d2c&userGender=0&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_headers = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/api/Coopera/Hot'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'pg': 1,
            'roleGender': 0,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userGender': 0,
            'userId': 16685645,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_headers)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x in datas]

        print(Title)

    '''
    合作广场我的界面作品名称信息
    '''
    def My(self):

        data = 'appkey=193dd7cc7845df55&cid=0&from=1&token=ae710f54f00fa97c18fd52d2942f4d2c&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Type': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/api/Coopera/My'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'cid': 0,
            'from': 1,
            'token': 'ae710f54f00fa97c18fd52d2942f4d2c',
            'userId': 16685645,
            'sign': sign,

        }

        reqs =  requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x ['title'] for x in datas]

        print(Title)



'''
个人中心
'''
class Person_senter():
    '''
    粉丝列表用户名称获取
    '''
    def My_fans(self):
        data = 'appkey=193dd7cc7845df55&id=0&spaceUserId=16685645&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/User/GetFans'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'id': 0,
            'spaceUserId': 16685645,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign': sign

        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info  = json.loads(reqs.text)

        datas = info['data']

        Names = [x ['user_name'] for x in datas]

        print(Names)


    '''
    空间中的作品搜索
    '''
    def Zoom_search(self,name):
        Name = quote(name) #需要进行url编码才能正常MD5加密
        data = 'appkey=%s&keyword=%s&pg=1&searchUserId=%s&token=%s&userId=%s|%s'%(Appkey,Name,UserId,Token,UserId,Sign_code)
        sign = hashlib.md5(data.encode('utf-8')).hexdigest()
        print(sign)

        req_url = 'http://a.api1.peiyinxiu.com/Api/Film/SearchFilms'

        req_data = {
            'appkey' : Appkey,
            'keyword' : name,
            'pg' : 1,
            'searchUserId' : UserId,
            'token' : Token,
            'userId' : UserId,
            'sign' : sign
        }
        reqs = requests.get(req_url,params=req_data,headers = Header)
        print(reqs.json())


    '''
    个人中心关注用户数量统计对比
    '''

    def Person_Follow(self,spaceID, pg):
        data = 'appkey=193dd7cc7845df55&chat=0&keyword=&pg=%s&spaceUserId=%s&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e' % (pg, spaceID)

        sign = hashlib.md5(data.encode('UTF-8')).hexdigest()

        req_url = "http://a.api1.peiyinxiu.com/Api/User/GetFollows"

        req_headers = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_data = {
            'appkey': '193dd7cc7845df55',
            'chat': 0,
            'keyword': '',
            'pg': pg,
            'spaceUserId': spaceID,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign': sign
        }

        resq = requests.get(req_url, params=req_data, headers=req_headers)
        # print(resq.text)
        get_info = json.loads(resq.text)
        get_data = get_info['data']
        User_id = [x['user_id'] for x in get_data]
        User_name = [x['user_name'] for x in get_data]
        # print(User_name)
        return len(User_id)



    '''
    社团列表信息获取
    '''
    def Unions(self):
        data = 'appkey=193dd7cc7845df55&pg=1&spaceUserId=16685645&token=824f319949e8ae6269556ed101fe88eb&userId=16685645|d62bcbe08764808e'

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_header = {
            'Content-Tyoe': 'application:json',
            'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
        }

        req_url = 'http://a.api1.peiyinxiu.com/Api/Union/GetSpaceUnion'

        req_data = {
            'appkey':'193dd7cc7845df55',
            'pg': 1,
            'spaceUserId': 16685645,
            'token': '824f319949e8ae6269556ed101fe88eb',
            'userId': 16685645,
            'sign':sign
        }

        reqs = requests.get(req_url, params= req_data, headers = req_header)

        info = json.loads(reqs.text)

        datas = info['data']

        Names = [x ['user_name'] for x in datas]

        print(Names)


    '''上榜记录列表'''
    def On_the_list(self):
        data = 'appkey=%s&pg=1&spaceUserId=%s&token=%s&userId=%s|%s'%(Appkey,UserId,Token,UserId,Sign_code)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = 'http://a.api1.peiyinxiu.com/Api/RankingList/GetUserRankingRecord'

        req_data = {
            'appkey':Appkey,
            'pg': 1,
            'spaceUserId': UserId,
            'token': Token,
            'userId':UserId,
            'sign': sign
        }

        reqs = requests.get(req_url, params= req_data, headers = Header)

        info = json.loads(reqs.text)

        lists = info['data']['list']
        print(len(lists))
    '''
    个人作品
    '''
    def My_flims(self):
        data = 'appkey=%s&pg=1&spaceUserId=%s&token=%s&type=0&userId=%s|%s'%(Appkey,UserId,Token,UserId,Sign_code)

        sign = hashlib.md5(data.encode('utf-8')).hexdigest()

        req_url = 'http://a.api1.peiyinxiu.com/Api/Film/GetMyFilms'

        req_data = {
            'appkey': Appkey,
            'pg': 1,
            'spaceUserId': UserId,
            'token': Token,
            'type': 0,
            'userId': UserId,
            'sign': sign
        }

        reqs = requests.get(req_url, params=req_data, headers=Header)

        info = json.loads(reqs.text)

        datas = info['data']

        Title = [x['title'] for x in datas]

        return Title

    '''素材列表'''
    def P_sources(self):
        data = 'appkey=%s&v=9.7.492&suid=%s&uid=%s&id=0&isFilter=0&token=%s|%s'%(Appkey,UserId,UserId,Token,Sign_code)
        print(data)

        sign = hashlib.md5(data.encode('UTF-8')).hexdigest()

        req_url = 'http://a.api.peiyinxiu.com/v3.0/GetMySourceList'

        req_data = {
            'appkey':Appkey,
            'v' : '9.7.492',
            'suid' : UserId,
            'uid' : UserId,
            'id' : 0,
            'isFilter' : 0,
            'token' : Token,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = Header)
        print(reqs.text)


    '''获取钻石和金币余额'''
    def gold(self):
        data ='appkey=%s&spaceUserId=%s&token=%s&userId=%s|%s'%(Appkey,UserId,Token,UserId,Sign_code)
        sign = hashlib.md5(data.encode('utf-8')).hexdigest()
        req_url = 'http://a.api1.peiyinxiu.com/Api/user/GetMyInfo'
        req_data = {
            'appkey' :Appkey,
            'spaceUserId' : UserId,
            'token' : Token,
            'userId' : UserId,
            'sign' : sign
        }

        reqs = requests.get(req_url, params= req_data, headers = Header)
        # print(reqs.text)
        info = json.loads(reqs.text)
        get_data = info['data']
        # pprint(get_data)
        GOLD1 = get_data['gold']
        GOlD2 = get_data['gold2']
        return GOLD1,GOlD2




# if __name__=="__main__":
#     Search_country('zg')
    # get_country('',0)
    # Phone_login('18072702677','123456')
    # Home_works()
    # Phone_login()
    # Chat.Chat_room_list()
    # Chat().Chat_detail('2228729')
    # L = Chat().Chat_detail('2228729')
    # ID = L[0]
    # Chat().gift_hour(ID,'155165319')
    # Chat().Arrival_user('2228729')
    # Chat().Contribution_list('2')
    # Chat().Income_list('2')
    # Chat().live_gift()
    # Channel().Channel_home()
    # Channel().channel_most()
    # Vid = Channel().Channel_home()
    # Channel().video_gift_list(video=Vid)
    # Gift = Channel().video_gift_list(Vid)
    # Channel().Gift_details(Vid,Gift)
    # Channel().details_list(Vid)
    # Leaderboard().GetRankingClassList('动漫')
    # Leaderboard().Regal_day()
    # Leaderboard().Regal(3)
    # Leaderboard().Anchor_list('1')
    # Leaderboard().Society_list('1')
    # Leaderboard().Material_list('1')
    # Leaderboard().works_list()
    # Leaderboard().label('3')
    # Leaderboard().Lable_list()
    # Leaderboard().Potential_list()
    # Leaderboard().Social_list()
    # Comic().recommend()
    # Comic().Newest()
    # Comic().classification()
    # Comic().Collection()
    # Comic().Comic_Library()
    # Comic().My_comic()
    # Comic().Recommend_Comic()
    # Exposure()
    # Near()
    # Coopera().Square()
    # Coopera().Hot()
    # Coopera().My()
    # test()
    # Login_history('18655449538','1234567')
    # Person_senter().My_flims()
    # Person_senter().Person_Follow('16685645','1')
    # Person_senter().Zoom_search('过')
    # Person_senter().My_fans()
    # Person_senter().Unions()
    # Person_senter().On_the_list()
    # Person_senter().My_flims()
    # Person_senter().P_sources()
    # Person_senter().gold()
