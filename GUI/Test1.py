import os
import re

def Get_app_pid():
    p = os.popen('adb shell ps | findstr "com.happyteam.dubbingshow"')
    outstr = p.readline()
    print(outstr.replace(" ",""))
    pid = re.findall(r'      (.*?) ', outstr)
    return pid
#
# def Get_app_uid():
#     P = Get_app_pid()
#     D = 'd772f3d1'
#     p = os.popen('adb -s %s shell cat /proc/%s/status | findstr Uid'%(D,P[0]))
#     out = p.read()
#     # list = []
#     # list.append(out)
#     # print(list)
#     uid = re.findall(r'Uid:\t(.*?)\t',out)
#     # return uid
#     print(uid)
# def Get_send_recv():
#     U = Get_app_uid()
#     send = os.popen('adb shell cat /proc/uid_stat/%s/tcp_snd'%(U[0]))
#     out = send.read()
#     send_Mb = int(int(out)/1024/1024)
#     print(send_Mb)
#     # recv = os.popen('adb shell cat/proc/uid_stat/%s/tcp_rcv'%(U[0]))
#     # # recv_Mb = int(recv/1024)
#     # print(recv)
if __name__ == '__main__':
    Get_app_pid()
    # Get_app_uid()
    # Get_send_recv()