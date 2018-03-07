# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 20:14
# @Author  : 石头人m
# @File    : 【斐波那契】变态跳台阶.py

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        else:
            return pow(2, number - 1)
