#coding=utf-8
'''
create on 2020年2月9日
@author: Alvin_zhu
'''
import socket
import os
import time


def check_port(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host,port))
        s.shutdown(2)
    except OSError as msg:
        print('%s 端口没有被其他服务占用，可以使用' % port)
        print(msg)

    else:
        print('%s 端口被其他服务占用了!' % port)



def release_port(port):

    cmd_find = 'netstat -aon | findstr %s' % (port)
    print(cmd_find)

    result = os.popen(cmd_find).read()
    print(result)
    if str(port) and 'LISTENING' in result:
        i = result.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]
        print('pid: ', pid)
        time.sleep(1)
        cmd_kill ='taskkill -f -pid %s' % (pid)
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available!' % port)
#
if __name__=="__main__":
    host = '127.0.0.1'
    port = 4725
    check_port(host,port)
    time.sleep(2)
    release_port(port)
