# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午5:07
# @Author  : 石头人m
# @File    : 【位运算】二进制中1的个数.py

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''


class Solution:
    def NumberOf1(self, n):
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count


class Solution2:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0, 32)])


'''
把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.
那么一个整数的二进制有多少个1，就可以进行多少次这样的操作。
'''
