# coding: utf-8
import fileinput
import re
import time
import sys

file_path = "myBase.ini"
file_path = r"C:\Users\PYX\AppData\Local\wjjsoft\nyfedit7\myBase.ini"
to_change = {"App.UserLic.FirstUseOn=": str(int(time.time()))}
for line in fileinput.input([file_path], inplace=1):
    for key in  to_change.keys():
        if re.match(key,line):
            sys.stdout.write(f"{key}{to_change[key]}\n")
            sys.stdout.flush()
            break
        else:
            sys.stdout.write(line)
            sys.stdout.flush()
fileinput.close()
print("done!")
