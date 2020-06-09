#coding = utf-8
# import  subprocess
#
# filepath = 'C:\\Users\\PYX\\Desktop\\appium_port\\4725.bat'
# p = subprocess.Popen(filepath,shell= True,stdout=subprocess.PIPE)
# stdout,stderr = p.communicate()
def  test():
    from collections import Counter  # 引入Counter
    a = [29, 36, 57, 12, 79, 43, 23, 56, 28, 11, 14, 15, 16, 37, 24, 35, 17, 24, 33, 15, 39, 46, 52, 13]
    b = dict(Counter(a))
    for key, value in b.items():
        if value > 1:
            print(key)
    print([key for key, value in b.items() if value > 1])  # 只展示重复元素
    print({key: value for key, value in b.items() if value > 1})


if __name__=="__main__":
    test()