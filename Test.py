#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import os
import time
os.system('chcp 65001')
time.sleep(1)
os.system('e:')
time.sleep(1)
os.system('cd Peiyinxiu_appium\Peiyinxiu_Client ')
time.sleep(1)
dir = os.system('dir')
print(dir)
os.system('git add .')
time.sleep(5)
os.system('git commit -m "%s"'%(time.time()))
time.sleep(3)
os.system('git push -u origin master ')

