# import os,sys,re,time
# def getTotalPss():
#     lines = os.popen("adb shell dumpsys meminfo com.happyteam.dubbingshow ").readlines() #逐行读取
#     total = "TOTAL"
#     for line in lines:
#         if re.findall(total, line): # 找到TOTAL 这一行
#             lis = line.split(" ")  #将这一行，按空格分割成一个list
#             while '' in lis:       # 将list中的空元素删除
#                 lis.remove('')
#     return (lis[1]) #返回总共内存使用
# def run():
#     while True:
#         try:
#             mem = getTotalPss()
#         except :
#             mem ='error'
#         print("mem: " + str(mem) + ' KB')
#         time.sleep(1)
#
#
#
# if __name__=="__main__":
#     run()
