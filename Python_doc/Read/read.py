#encoding: utf-8
'''
@author:alvin.zhu
@file:read.py
@time:2020/10/10 11:47
@Description:
read:
特点是：读取整个文件，将文件内容放到一个字符串变量中。
劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。

readline:
特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
缺点：比readlines慢得多

readtlines:
特点：一次性读取整个文件；自动将文件内容分析成一个行的列表。

'''
file = with open('test.txt','r',encoding='UTF-8')
Read = file.read()
print(Read,'\n')
# file = open('test.txt','r',encoding='UTF-8')
# Readline = file.readline()
# print(Readline)
# file = open('test.txt','r',encoding='UTF-8')
# Readlines = file.readlines()
# print(Readlines)

'''
Python3.0中的OSError: [Errno 22] Invalid argument: ‘D:\\pytorch\\crop\test\\list1.

在Python中想打开文件，发现出现OSError: [Errno 22]错误。

于是查资料发现树上是这么写的

f=open(r‘D:\pytorch\crop\test\list1.txt’)
突然觉着不对啊，之前看的一些文章好像是这么写的

f=open(‘D:\pytorch\crop\test\list1.txt’)
上网找资料，居然是转义字符在作怪。。。。。。

于是改成

f=open(‘D:/pytorch/crop/test/list1’)
成功运行~
'''