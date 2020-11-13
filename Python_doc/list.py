#encoding: utf-8
'''
@author:alvin.zhu
@file:list.py
@time:2020/10/29 13:36
@Description:列表（list）比较操作教程

'''
# 一、相等比较
# 1.1
# 同顺序列表比较
# 顺序相同直接用“ == ”进行比较即可
# 不同顺序列表进行比较
# “ == ”只有成员、成员位置都相同时才返回True，但有时候我们希望只要成员相同、即使成员位置不同也能返回True。
list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
list1 == list2





# 2.1.1
# 使用列表sort()
# 方法进行排序后比较
# 列表本身有sort()
# 内置方法，可对自身成员进行排序；注意sort()
# 方法对自身造成改变。

list1 = ["one", "two", "three"]
list2 = ["one", "three", "two"]
list1.sort() == list2.sort()
print(list1)

# 2.1.2
# 使用sorted()
# 方法进行排序后比较
# 上一小节介绍的sort()
# 方法会对列表成员进行重排，但有时候我们并不希望列表本身被改动。
#
# 我们可以用一下变量将原先的列表保存起来，但更好的做法是使用sorted()
# 方法，sorted()
# 不改变列表原本顺序而是新生成一个排序后的列表并返回。

list1 = ["one", "two", "three"]
list2 = ["one", "three", "two"]
sorted(list1) == sorted(list2)
print(list1)
sorted(list1)

# 二、包含比较
# 直接用列表本身进行包含类比较，只能用遍历的方法这是比较麻烦的，使用set()
# 转成集合进行包含比较就简单多了。
# 2.1
# 判断列表是否包含另一列表
list1 = ["one", "two", "three"]
list2 = ["one", "three", "two", "four"]
set(list1).issubset(set(list2))
set(list2).issuperset(set(list1))

# 2.2
# 获取两个列表相同成员（交集）

list1 = ["one", "two", "three", "five"]
list2 = ["one", "three", "two", "four"]
set(list1).intersection(set(list2))

# 2.3
# 获取两个列表不同成员

list1 = ["one", "two", "three", "five"]
list2 = ["one", "three", "two", "four"]
set(list1).symmetric_difference(set(list2))

# 2.4
# 获取一个列表中不是另一个列表成员的成员（差集）

list1 = ["one", "two", "three", "five"]
list2 = ["one", "three", "two", "four"]
set(list1).difference(set(list2))
set(list2).difference(set(list1))

# 2.5
# 获取两个列表所有成员（并集）

list1 = ["one", "two", "three", "five"]
list2 = ["one", "three", "two", "four"]
set(list1).union(set(list2))