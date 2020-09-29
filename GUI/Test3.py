#encoding: utf-8
'''
@author:alvin.zhu
@file:Test3.py
@time:2020/9/25 17:38
@Description:

'''
import os,re
from itertools import chain


def get_conn_dev():
    p = os.popen('adb devices')
    outstr = p.read()
    print(outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid


def get_dev_name():
    devs = get_conn_dev()
    dev_name = []
    for d in devs:
        dev = os.popen('adb -s %s shell getprop ro.product.model' % d)
        dev_name.append(dev.read().rstrip('\n'))
    return dev_name

def show_dev():
    devs = get_dev_name()
    dev_info = get_conn_dev()
    lists = list(chain.from_iterable(zip(devs, dev_info)))
    print(lists)

if __name__ == '__main__':
    # get_conn_dev()
    show_dev()