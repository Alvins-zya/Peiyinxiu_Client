import os,sys,re,time
import threading,subprocess


def check_device():
    dev = subprocess.check_output('adb devices').split("\r\n")
    if dev[1] == '':
        print('1')


if __name__=="__main__":
    check_device()
