# encoding = utf-8
'''
@author: alvin.zhu
@file :web_video_download.py
@time :2020/12/31 16:45
@Description:
'''
import json
from bs4 import BeautifulSoup
import sys
import requests
import pandas as pd

class downloader(object):

    def get_data(self,url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

        try:
            r = requests.get(url,headers = header)
            r.raise_for_status()
            return r.text
        except requests.HTTPError as e:
            print(e)
            print('HTTPError')
        except requests.RequestException as e:
            print(e)
        except:
            print("Unknown Error !")

    def parse_data(self, html):

        bsobj = BeautifulSoup(html,'lxml')
        info = []

        tbList = bsobj.find_all('table', attrs={'class' : 'tbspan'})

        for item in tbList:
            movie = []
            link = item.b.find_all('a')[1]
            name = link['title']

            url = 'https://www.dy2018.com' + link["href"]
            movie.append(name)
            movie.append(url)

            try:
                temp = BeautifulSoup(self.get_data(url), 'lxml')
                tbody = temp.find_all('tbody')

                for i in tbody:
                    download = i.a.text
                    movie.append(download)

                info.append(movie)
            except Exception as e:
                print(e)
        return info

    def save_data(self, data):
        filename = 'D:\FFOutput\movie.txt'

        dataframe = pd.DataFrame(data)
        dataframe.to_string(filename, mode='a', index=False, sep=',', header=False,encoding='utf-8')

    def main(self):
        for page in range(1,3):
            print('正在爬取：第' + str(page) + '页......')
            if page == 1:
                index = 'index'
            else:
                index = 'index_' + str(page)
            url = 'https://www.dy2018.com/3/'+ index +'.html'
            html = self.get_data(url)
            movies = self.parse_data(html)
            self.save_data(movies)
            print('第' + str(page) + '页完成！')

if __name__=='__main__':
    downloader().main()
