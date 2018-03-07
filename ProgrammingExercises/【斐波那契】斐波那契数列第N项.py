# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 19:33
# @Author  : 石头人m
# @File    : 【斐波那契】斐波那契数列第N项.py
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            print(0)
        else:
            listF = [1, 1]
            if n < 3:
                print(1)
            else:
                fN = 1
                sN = 1
                for i in range(n - 2):
                    listF.append(fN + sN)
                    fN = listF[i + 1]
                    sN = listF[i + 2]
                print(listF[n-1])


s = Solution()
s.Fibonacci(7)
