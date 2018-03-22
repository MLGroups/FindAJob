# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午5:14
# @Author  : 石头人m
# @File    : 【数组】调整数组顺序使奇数位于偶数前面.py

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:
    def reOrderArray(self, array):
        # write code here
        list1 = list()
        list2 = list()
        for i in array:
            if i % 2 == 1:
                list1.append(i)
            else:
                list2.append(i)
        return list1 + list2
