#encoding: utf-8
'''
@author:alvin.zhu
@file:strip.py
@time:2020/9/26 15:45
@Description:
strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
Python中有三个去除头尾字符、空白符的函数，它们依次为:
strip： 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
lstrip：用来去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
rstrip：用来去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)

注意：这些函数都只会删除头和尾的字符，中间的不会删除。

用法分别为：
string.strip([chars])
string.lstrip([chars])
string.rstrip([chars])

参数chars是可选的，当chars为空，默认删除string头尾的空白符(包括\n、\r、\t、' ')
当chars不为空时，函数会被chars解成一个个的字符，然后将这些字符去掉。

它返回的是去除头尾字符(或空白符)的string副本，string本身不会发生改变。
它返回的是去除头尾字符(或空白符)的string副本，string本身不会发生改变。

'''
str = "*****this is **string** example....wow!!!*****"
print (str.strip( '*' ))  # 指定字符串 *

str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12