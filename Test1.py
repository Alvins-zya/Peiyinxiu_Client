import os
import time
import json
import hashlib
import requests
from pprint import pprint

def Phone_login():
    data = 'accessToken=E10ADC3949BA59ABBE56E057F20F883E&appkey=193dd7cc7845df55&countryCode=86&mobile=18655449538&token=&type=6&uid=149046387&userId=0|d62bcbe08764808e'
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
        'mobile':'18655449538',
        'token':'',
        'type':'6',
        'uid':'149046387',
        'userId':0,
        'sign':sign
    }
    resq = requests.post(req_url,params = req_data,headers = req_headers)
    print(resq.text)

def get_message():
    data = 'appkey=193dd7cc7845df55&friendUserId=16685645&token=dad28e3f555fc001b2f9c7fb0feecb08&userId=149046387|d62bcbe08764808e'
    sign = hashlib.md5(data.encode('utf-8')).hexdigest()

    req_header = {'Content-Tyoe': 'application:json',
           'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'}

    req_url = 'http://a.api1.peiyinxiu.com/api/Message/GetSingleMessages'

    req_data = {
        'appkey' :'193dd7cc7845df55',
        'friendUserId' : '16685645',
        'token' : 'dad28e3f555fc001b2f9c7fb0feecb08',
        'userId' : '149046387',
        'sign' :sign
    }

    reqs = requests.get(req_url, params= req_data, headers = req_header)
    # print(reqs.json())
    info  = json.loads(reqs.text)

    get_data = info['data']
    # print(get_data)
    content = [x ['content'] for x in get_data]
    pprint(content)


def clear_message():
    data = 'appkey=193dd7cc7845df55&maxMsgId=523037&toId=16685645&token=dad28e3f555fc001b2f9c7fb0feecb08&userId=149046387|d62bcbe08764808e'
    sign = hashlib.md5(data.encode('utf-8')).hexdigest()
    req_header = {
        'Content-Tyoe': 'application:json',
        'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
    }
    req_data = {
        'appkey':'193dd7cc7845df55',
        'maxMsgId' : 523037,
        'toId' :16685645,
        'token' :'dad28e3f555fc001b2f9c7fb0feecb08',
        'userId' :149046387,
        'sign' : sign
    }
    req_url = 'http://a.api1.peiyinxiu.com/api/Message/ClearMessages'

    params = json.dumps(req_data)
    resq = requests.post(req_url, json=params, headers=req_header)
    print(resq)
if __name__=="__main__":
    # Phone_login()
    get_message()
    # clear_message()