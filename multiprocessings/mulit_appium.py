#coding = utf-8
'''
create on 2020年2月9日
@author:Alvin_zhu

'''
import os
from time import ctime
import multiprocessing
import subprocess


devices_list = ['4ebc78fd', 'f249f9f2']

# def appium_start(host,port,udid):
#     bootstrap_port = str(port+1)
#     cmd = 'start /b appium -a ' + host +' -p ' + str(port) +' -bp ' + str(bootstrap_port) + ' -U ' + str(udid)
#     print('%s at %s' % (cmd,ctime()))
#
#     # os.system(cmd)
#     p = subprocess.call(cmd,shell=True,stdout=open('D:/GIT/Peiyinxiu_Client/multiprocessings/logs.log','w'),stderr=subprocess.STDOUT)
#     print(p)
# appium_process=[]
# for i in range(2):
#     host = '127.0.0.1'
#     port=4723+2*i
#     appium=multiprocessing.Process(target=appium_start,args=(host,port,devices_list[i]))
#     appium_process.append(appium)
# #
# if __name__ == '__main__':
#     # appium_start('127.0.0.1',4723)
#     for appium in appium_process:
#         appium.start()
#
#     for appium in appium_process:
#         appium.join()

def appium_start(host,port):
    bootstrap_port = str(port+1)
    cmd = 'start /c appium -a '+ host +' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    print(cmd)
    subprocess.call(cmd,shell=True,stdout=open('D:/GIT/Peiyinxiu_Client/multiprocessings/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)


if __name__=='__main__':
    host = '127.0.0.1'
    port = 4723
    appium_start(host,port)
