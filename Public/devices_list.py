#coding=utf-8
'''
create on 2020年2月21日
@author : Alvin_zhu
'''

import os
import re
def get_conn_dev():
    p = os.popen('adb devices')
    outstr = p.read()
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid
