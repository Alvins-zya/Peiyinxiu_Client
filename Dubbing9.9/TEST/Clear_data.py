#!usr/bin/python
# -*- coding:utf-8 -*-
# 把指定目录的apk安装到所有连接设备中
import os
import subprocess
import threading
import re
import time


def excute(cmd):
    subprocess.Popen(cmd, shell=True)

def get_conn_dev():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr = p.read()
    print (outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

def main():
    connectdevice = get_conn_dev()
    commands = []

    for device in connectdevice:
        cmd = "adb -s %s shell pm clear com.happyteam.dubbingshow" % (device)
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


if __name__ == '__main__':
    main()
