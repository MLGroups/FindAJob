# -*- coding: utf-8 -*-
# @Time    : 18-3-31下午9:04
# @Author  : 石头人m
# @File    : 【360】画板.py

'''
题目：画板

题目描述：
沫璃有一个画板，画板可以抽象成有100行每行100个像素点的正方形。
沫璃在画板上画画，她一共画了n次，每次将一个矩形涂上颜色。
沫璃想知道一共有多少个像素点被她涂过颜色。若一个像素点被涂了k次，那么认为有k个像素点被涂过颜色。

输入
第一行一个数T(T<=100)，表示数据组数。
对于每组数据，第一行一个整数n , (1<=n<=100)
接下来n行，每行4个整数x1, y1, x2, y2 (1 <= x1 <= x2 <= 100, 1 <= y1 <= y2 <= 100)，
表示矩形的两个对角所对应的像素点的坐标。

输出
对于每组数据，输出一行，表示沫璃一共涂了多少个像素点。

样例输入
2
2
1 1 2 3
2 2 3 3
2
1 1 3 3
1 1 3 3

样例输出
10
18
'''

T = int(raw_input())
res = list()
for i in range(T):
    n = int(raw_input())
    count = 0
    for j in range(n):
        line = raw_input().split()
        count += (abs(int(line[2]) - int(line[0]) + 1) * abs(int(line[3]) - int(line[1]) + 1))
    res.append(count)

for re in res:
    print(re)
