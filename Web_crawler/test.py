# encoding = utf-8
'''
@author: alvin.zhu
@file :test.py
@time :2020/12/31 17:50
@Description:
'''
from urllib import request
import ssl

#ssl免验证
#创建一个不需要验证的上下文
ssl._create_default_https_context=ssl._create_unverified_context
#而不是ssl._create_unverified_context()

# ssl._create_default_https_context = ssl._create_unverified_context
# base_url='http://www.12306.cn/mormhweb/'  #不报错
base_url = "https://www.dytt8.net/index.htm" #urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]

response = request.urlopen(base_url,cert = 'C:\Users\PYX\Desktop\dy.cer','‪C:\Users\PYX\Desktop\dy.cer')
print(response.text)