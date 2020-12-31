# -*- coding: utf-8 -*-
# @Time : 2020 12 26 17
# @Author : alvin
# @Email : 406096917@qq.com
# @File : test.py
# @Description:

import requests
import sys
from bs4 import BeautifulSoup
f = open('test_result_txt.txt', 'w', encoding='UTF-8')
server = 'http://www.biqukan.com/'
target = 'http://www.biqukan.com/1_1094/'
req = requests.get(target)
req.encoding = 'gbk'
html = req.text
bf = BeautifulSoup(html,'lxml')
texts = bf.find_all('div', class_= 'listmain')
a_bf = BeautifulSoup(str(texts[0]), 'lxml')
new = a_bf.find_all('a')
nums = len(new[12:])
for each  in new[12:-2]:
    result = each.string+'\t'+server + each.get('href')
    # lists.append(result)
    # print(result)
    f.write(str(result)+'\n')
f.close()

class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html,'lxml')
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),'lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[12:-2])
        for each in a[12:-2]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))



    def get_content(self, target):
        req = requests.get(target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='UTF-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__=='__main__':
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念.txt', dl.get_content(dl.urls[i]))
        sys.stdout.write('已下载：%.3f%%' % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
