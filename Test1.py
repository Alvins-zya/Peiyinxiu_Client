#coding=utf-8
import os
import subprocess
import threading
import re
import time
import sys

def excute(cmd):
    subprocess.Popen(cmd, shell=True)

def get_conn_dev():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr = p.read()
    print ("======启动APP======\n",outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

def main():
    connectdevice = get_conn_dev()
    commands = []

    for device in connectdevice:
        cmd = "adb -s %s shell am start -W -n com.happyteam.dubbingshow/.ui.StartActivity"%(device)
        commands.append(cmd)

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
        t = threading.Thread(target = excute, args = (commands[i],))
        threads.append(t)

    for i in range(threads_count):
        time.sleep(1)  # 防止adb连接出错
        threads[i].start()

    for i in range(threads_count):
        threads[i].join()


def action():
    list = get_conn_dev()
    commands = []

    for device in list:
        cmd = "adb -s %s shell am force-stop com.happyteam.dubbingshow" % (device)
        commands.append(cmd)

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
        t = threading.Thread(target=excute, args=(commands[i],))
        threads.append(t)

    for i in range(threads_count):
        time.sleep(1)  # 防止adb连接出错
        threads[i].start()

    for i in range(threads_count):
        threads[i].join()
if __name__=="__main__":
    for i in range(100):
        main()
        time.sleep(10)
        action()
        time.sleep(5)
    print('运行结束')
