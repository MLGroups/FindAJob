# -*- coding: utf-8 -*-
# @Time    : 18-4-10下午8:56
# @Author  : 石头人m
# @File    : 【小米】爬楼梯.py


'''
题目：爬楼梯
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB

题目描述：
在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。 请问计算出你可以采用多少种不同的方式爬完这个楼梯。

输入
一个正整数（n <= 50），表示这个楼梯一共有多少阶

输出
一个正整数，表示有多少种不同的方式爬完这个楼梯

样例输入
5
样例输出
8

Hint
输入样例2
10
输出样例
89
'''


def solution(n):
    arr = list()
    arr.append(1)
    arr.append(2)

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(n - 2):
            arr.append(arr[i + 1] + arr[i])
        return arr[n - 1]


_n = int(raw_input())

res = solution(_n)

print str(res) + "\n"

'''
斐波那契数列，递归超时，用数组优化，把前面的值存下来，省去重复递归。
'''
