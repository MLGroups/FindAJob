# -*- coding: utf-8 -*-
# @Time    : 18-4-10下午8:55
# @Author  : 石头人m
# @File    : 【小米】寻找归一数字.py


'''
题目：寻找归一数字

有一类正整数我们叫做归一数字，对于任意一个归一数字 N，满足以下特性：
N 的每一位的平方和组成一个数，新数字的平方和再组成一个新数字，如此往复运算，直到最终结果为 1。
若一个数字能最终归一成 1，则该数字为归一数字，否则不是归一数字。
举例： 82可以分解为8^2 + 2^2 = 68，68继续分解为6^2 + 8^2 = 100，
100可以分解为1^2 + 0^2 + 0^2 = 1。所以82可以归一。

输入
一个正整数 N（0 < N < 100000000）

输出
输出N 是否为归一数的判断结果，若是则返回 'true'，否则返回 'false'（均为字符串）。

样例输入
1
其他的示例：
示例一：
82
示例二：
50

样例输出
true
其他的示例：
示例一：
true
示例二：
false
'''

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solution(num, digui_num):
    num_s = list(str(num))
    new_num = 0
    for num_ss in num_s:
        new_num += pow(int(num_ss), 2)
    if new_num == 1:
        return 'true'
    else:
        if digui_num < 100:
            digui_num += 1
            return solution(new_num, digui_num)
        else:
            return 'false'


# ******************************结束写代码******************************


_num = int(raw_input())

res = solution(_num, 0)

print(res + "\n")

'''
循环100次还没结果就是没有了。
100是随便试的，说不定10也行。。。
'''
