#coding = utf-8
#防止中文显示乱码
#coding = gb18030
'''
配音秀客户端接口测试脚本上传封装
'''
from git import Repo
repo = Repo.init('E:\Peiyinxiu_appium\Interface')
repo.index.add(['*.py'])
repo.index.commit('2019年6月13日19:08:00')
remote = repo.remote()
remote.push('master')
input('=====配音秀客户端接口脚本上传结束====\n输入任意键结束:\n')


