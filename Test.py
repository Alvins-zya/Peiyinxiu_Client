#coding=utf-8
import re
import string
my_str = '余额：3.1钻石'
num = map(re.findall(r"\d+\.?\d*",my_str))
print(num)
if num >3:
    print(1)
else:
    print(2)