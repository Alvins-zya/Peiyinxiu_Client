import subprocess
import re
import logging
import time
import os


package='com.happyteam.dubbingshow'#填写测试包名

def getmem(package):
    cmd = r'adb shell dumpsys meminfo '+package+' | findstr "TOTAL"'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    str_out=map(str,out)
    number=[]
    for i in str_out:
         number.append(int( re.findall('\d+', i)[0]))#正则匹配出字符串中的数字列表，按选择列表[0]的数字大写排序
    print(number[0])

if __name__=="__main__":
    while True:
        logging.info(getmem(package))
        time.sleep(1)