#coding = utf-8
# import  subprocess
#
# filepath = 'C:\\Users\\PYX\\Desktop\\appium_port\\4725.bat'
# p = subprocess.Popen(filepath,shell= True,stdout=subprocess.PIPE)
# stdout,stderr = p.communicate()
import unittest
def test():
    i = 0
    try:
        if i ==1:
            pass
        else:
            pass
    except:
        raise ('失败')
        unittest.skip('hhh')
    print('1')

if __name__=="__main__":
    test()