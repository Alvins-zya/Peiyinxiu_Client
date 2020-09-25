#encoding: utf-8
'''
@author:alvin.zhu
@file:Maolindang.py
@time:2020/9/23 15:00
@Description:猫铃铛活动

'''

import requests


def mao():
    data = 'uid=142711971&token=eec8d05700967d8ca04e75fa4e0b7bd6&type=0'
    url = "http://101.37.152.245:8082/info/OpenCard"
    req_date = {
        'uid':142711971,
        'token':'eec8d05700967d8ca04e75fa4e0b7bd6',
        'type':1
    }
    resp = requests.get(url,params=req_date)
    print(resp.json())


if __name__ == '__main__':
    mao()