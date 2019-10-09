import os
import time
import json
import hashlib
import requests
from pprint import pprint

def get_country(token, UserID):
    data = 'appkey=193dd7cc7845df55&token=%s&userId=%s|d62bcbe08764808e' % (token, UserID)
    signs = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    req_url = "http://a.api1.peiyinxiu.com/Api/User/GetCountryCodeList"
    req_headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'dubbingshow/9.5.470/866177036554730(android7.1.1;OPPO%20R11;25;1080*1920;official)'
                    }
    print(signs)
    req_data = {
        'appkey': '193dd7cc7845df55',
        'token': token,
        'userId': UserID,
        'sign': signs
    }
    resp = requests.get(req_url, params=req_data, headers=req_headers)
    # print(resp.status_code)
    print(resp.text)
    get_info = json.loads(resp.text)
    get_data = get_info['data'][0]['country_code_list']
    print(get_data)#获取'data'列表中第一个列表中的‘country_code_list’列表内容
    # country = get_data['country_code_list']
    # for i in range(len(get_data)):
    #     country = get_data[i]['country_code_list']
    #     print(country)  # 按字母排序，列表所有国家列表
    # print(country)
    # get_code = country[0]
    # print(get_code)
    # name = [x['name'] for x in country]
    # code = [x['code'] for x in country]
    # print(name)  # 取出列中name的值
    # print(code)  # 取出列中code的值


    # userId = get_data['user_id']
    # userToken = get_data['token']

if __name__=="__main__":
    get_country('',0)