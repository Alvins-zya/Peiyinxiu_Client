# encoding = utf-8
'''
@author: alvin.zhu
@file :
@time :2020/12/9 14:49
@Description:文本去重
'''
# -*- coding:utf-8 -*-
#! python2
import shutil
a=0
readDir = "D:\Git_pyhthon\Package_module\Elemets.txt"  #old
writeDir = "D:\Git_pyhthon\Package_module\\new_el" #new
# txtDir = "/home/Administrator/Desktop/１"
lines_seen = set()
outfile = open(writeDir, "w",encoding="UTF-8")
f = open(readDir, "r",encoding="UTF-8")
for line in f:
  if line not in lines_seen:
    a+=1
    outfile.write(line)
    lines_seen.add(line)
    # print(a)
    # print('\n')
outfile.close()
print("success")