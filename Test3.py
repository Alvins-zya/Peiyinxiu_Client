#coding = utf-8
import subprocess
import re
import os
from time import ctime

import multiprocessing  # 导入多进程模块

def get_conn_dev():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr = p.read()
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

def appium_start(host, port,select_d):
    bootstrap_port = str(port + 1)

    # /b是不打开cmd命令窗口

    cmd = 'start  appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port) + ' -U ' + str(select_d)

    print('%s at %s' % (cmd, ctime()))

    # a是追加写入的方式

    subprocess.Popen(cmd, shell=True, stdout=open('E:/log' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# 构建appium进程组

appium_process = []

# 加载appium进程

for i in range(2):
    host = '127.0.0.1'

    port = 4723 + 2 * i

    dev = get_conn_dev()
    select_d = dev[i]

    # target指向方法，args指向参数，且必须是一个元组的形式

    appium = multiprocessing.Process(target=appium_start, args=(host, port,select_d))

    # 将进程从变量appium加载到进程内

    appium_process.append(appium)
    #
    # clost_cmd = 'taskkill /F /IM node.exe'
    # subprocess.Popen(clost_cmd, shell=True)

if __name__ == '__main__':

    # 并发启动appium服务，for循环开启多个appium服务，join主进程等待子进程结束

    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()

