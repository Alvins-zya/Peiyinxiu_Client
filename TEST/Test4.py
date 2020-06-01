#coding = utf-8
# import  subprocess
#
# filepath = 'C:\\Users\\PYX\\Desktop\\appium_port\\4725.bat'
# p = subprocess.Popen(filepath,shell= True,stdout=subprocess.PIPE)
# stdout,stderr = p.communicate()
import unittest
def test():
    try:
        print(1/1)
        return False
    except:
        return True


def test1():
    state = test()
    print(state)
if __name__=="__main__":
    test1()