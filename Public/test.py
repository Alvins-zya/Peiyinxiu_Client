#coding = utf-8
import time
import os,sys,re
import threading
import subprocess

def get_conn_dev():
    p = os.popen('adb devices')
    outstr = p.read()
    # print(outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid


def Excute(cmd):
    print(cmd)
    subprocess.Popen(cmd,shell= True)

def runs():
    devs = get_conn_dev()
    threads = []
    cmd_list = []
    for dev in devs:
        cmd = 'adb -s %s shell monkey -p com.happyteam.dubbingshow -s 100 --pct-touch 50 --pct-motion 50 --throttle 300  -v -v -v 1000'%(dev)
        print(cmd)
        cmd_list.append(cmd)

    threads_count = len(cmd_list)

    for i in range(threads_count):
        t = threading.Thread(target=Excute(cmd),args=(cmd_list[i]),)
        threads.append(t)

    for i in range(threads_count):
        time.sleep(1)
        threads[i].start()

if __name__=="__main__":
    runs()




