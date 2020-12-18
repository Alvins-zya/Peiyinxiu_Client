#coding =utf-8
import os,sys,socket
def check_port(host,port):
    '''检测端口是否被占用'''
    #创建socket对象
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available'%port)
        print(msg)
    else:
        print('port %s is already use'%port)
        os.popen('taskkill /F /t /IM node.exe')

if __name__== '__main__':
    host = '127.0.0.1'
    port = 4725
    check_port(host,port)