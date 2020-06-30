import subprocess

reply = subprocess.getoutput('ping www.baidu.com')
print(reply)