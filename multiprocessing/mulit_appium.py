#coding = utf-8
'''
create on 2020年2月9日
@author:Alvin_zhu

'''
import os
from time import ctime
import multiprocessing

def appium_start(host,port):
    bootstrap_port = str(port+1)
    cmd = 'start /b appium -a ' + host +' -p ' + str(port) +' -bp ' + str(bootstrap_port)
    print('%s at %s' % (cmd,ctime()))

    os.system(cmd)

# appium_process=[]
# for i in range(2):
#     host = '127.0.0.1'
#     port=4723+2*i
#     appium=multiprocessing.Process(target=appium_start,args=(host,port))
#     appium_process.append(appium)
#
# if __name__ == '__main__':
#     for appium in appium_process:
#         appium.start()
#
#     for appium in appium_process:
#         appium.join()