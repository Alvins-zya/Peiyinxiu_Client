#coding=utf-8
import os
import subprocess
import threading
import re
import time
import sys



os.system('adb root')
time.sleep(2)
os.system('adb shell rm -r /sdcard/capture.pcap')
time.sleep(2)
os.system('adb shell')
time.sleep(2)
os.system('adb shell "su -c /system/xbin/tcpdump -i any -p -s 0 -w /sdcard/capture.pcap')
input('')
time.sleep(2)