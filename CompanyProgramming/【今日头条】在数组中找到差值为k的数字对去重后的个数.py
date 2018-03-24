# -*- coding: utf-8 -*-
# @Time    : 18-3-24下午9:08
# @Author  : 石头人m
# @File    : 【今日头条】在数组中找到差值为k的数字对去重后的个数.py

'''
题目描述：
在n个元素的数组中，找到差值为k的数字对去重后的个数

输入描述：
第一行：n和k，n表示数字个数，k表示差值

输出描述：
差值为k的数字对去重后的个数
'''
import sys

line = sys.stdin.readline().strip()
values = map(int, line.split())
n = values[0]
k = values[1]

line2 = sys.stdin.readline().strip()
values2 = map(int, line2.split())

dui = [i + k for i in values2]
duishu = set(values2) & set(dui)

print(len(duishu))
