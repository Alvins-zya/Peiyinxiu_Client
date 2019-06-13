#coding = utf-8
#防止中文显示乱码
#coding = gb18030
from git import Repo

repo = Repo.init('E:\Peiyinxiu_appium\Peiyinxiu_Client')
repo.index.add(['*.py'])
repo.index.commit('2019年6月13日19:08:00')
remote = repo.remote()
remote.push('master')
input('输入任意键结束:\n')


