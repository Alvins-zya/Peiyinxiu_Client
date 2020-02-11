from appium import webdriver
import time
import yaml
import os
from tomorrow import threads


def start_appium(port, udid):
    a = os.popen('netstat -ano | findstr "%s" '% port)
    time.sleep(2)
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)
        # s = t1.split(" ")
        # s1 = [i for i in s if i != '']
        # pip = s1[-1].replace("\n", "")
    else:
        # 启动appium服务
        # appium -a 127.0.0.1 -p 4740 -U emulator-5554 127.0.0.1:62001 --no-reset
        os.system("appium -a 127.0.0.1 -p %s -U %s --no-reset" % (port, udid))

def get_desired_caps(devicesName):
    '''
    从yaml读取desired_caps配置信息
    参数name:设备名称,如：夜神/雷电
    :return: desired_caps字典格式
    '''
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlpath = os.path.join(curpath, "desired.yaml")
    print("配置地址：%s" % yamlpath)
    f = open(yamlpath, "r", encoding="utf-8")
    a = f.read()
    f.close()
    # 把yaml文件转字典
    d = yaml.load(a)
    for i in d:
        if devicesName in i["desc"]:
            print(i)
            # 启动服务
            devicesName = i['desired_caps']['udid']
            print(devicesName)
            start_appium(port=i['port'], udid=devicesName)
            return (i['desired_caps'], i['port'])


if __name__=="__main__":
