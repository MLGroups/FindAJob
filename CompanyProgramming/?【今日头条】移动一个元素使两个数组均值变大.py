# -*- coding: utf-8 -*-
# @Time    : 18-3-24下午8:14
# @Author  : 石头人m
# @File    : ?【今日头条】移动一个元素使两个数组均值变大.py

'''
两个数组，移动一个元素到另一个中，使得两个数组的均值都变大。
有多少种方法。
'''

import sys

line = sys.stdin.readline().strip()
values = map(int, line.split())
n = values[0]
m = values[1]

line = sys.stdin.readline().strip()
values1 = map(int, line.split())
line = sys.stdin.readline().strip()
values2 = map(int, line.split())

avg_1 = float(sum(values1)) / len(values1)
avg_2 = float(sum(values2)) / len(values2)

v_min_1 = list()
v_min_2 = list()

for i in values1:
    if i < avg_1:
        v_min_1.append(i)
for i in values2:
    if i < avg_2:
        v_min_2.append(i)

v_min_1 = sorted(v_min_1)
v_min_2 = sorted(v_min_2)
print(v_min_1)
print(v_min_2)

count = 0
if len(v_min_2) < len(values2):
    for i in v_min_2:
        print(avg_1, i)
        if i > avg_1 and i not in values1:
            count += 1

if len(v_min_1) < len(values1):
    for i in v_min_1:
        print(avg_2, i)
        if i > avg_2 and i not in values2:
            count += 1
print(count)
