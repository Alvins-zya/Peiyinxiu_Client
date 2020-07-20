#coding = utf-8
import re
s = 'OPPO R11'
f = open('Dev_list.txt')
line = f.readlines()

for s in line:
    for i in range(3):
        line = f.readline()
        if line:
            print(line)

