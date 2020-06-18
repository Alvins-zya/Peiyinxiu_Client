#coding = utf-8
# import  subprocess
#
# filepath = 'C:\\Users\\PYX\\Desktop\\appium_port\\4725.bat'
# p = subprocess.Popen(filepath,shell= True,stdout=subprocess.PIPE)
# stdout,stderr = p.communicate()
from collections import Counter
def  test():
    peoples = [30, 60, 300, 500, 1000, 10000]
    P = 3
    assert P in peoples


if __name__=="__main__":
    test()