# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 22:18
# @Author  : 石头人m
# @File    : 【字符串】构造回文.py

'''
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。
对于每组数据，输出一个整数，代表最少需要删除的字符个数。
'''
import sys


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(1, lena + 1):
        for j in range(1, lenb + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i][j - 1] > c[i - 1][j]:
                c[i][j] = c[i][j - 1]
            else:
                c[i][j] = c[i - 1][j]
    return c[lena][lenb]


if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        lens = len(line)
        line1 = line[::-1]
        if not line:
            break
        maxLcp = lcs(line, line1)
        print(lens - maxLcp)
'''
求原字符串和其反串的最大公共子串的长度(LCS)，
然后用原字符串的长度减去这个最大公共子串的长度就得到了最小编辑长度。
'''
