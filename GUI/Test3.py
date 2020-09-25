#encoding: utf-8
'''
@author:alvin.zhu
@file:Test3.py
@time:2020/9/25 17:38
@Description:

'''
import os,re

def get_dev_name():
    devs = get_conn_dev()
    for d in devs:
        dev = os.popen('adb -s %s shell getprop ro.product.model'%d)
        print(dev.read())


def get_conn_dev():
    p = os.popen('adb devices')
    outstr = p.read()
    # print(outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

if __name__ == '__main__':
    # get_conn_dev()
    get_dev_name()