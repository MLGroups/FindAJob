# -*- coding: utf-8 -*-
# @Time    : 18-4-16下午8:34
# @Author  : 石头人m
# @File    : 【WeBank】数组top-k.py


'''
4.求一个长度为n（n>10,000,000）的double数组的top-k（k<=n）元素，结果按倒序排列。
'''


def topK(doublelists, k):
    listk = list()
    for i in range(k):
        listk.append(0)

    for dblist in doublelists:
        for kk in range(k):
            if dblist > listk[kk]:
                listk.insert(kk, dblist)
                del listk[-1]
                break
    return listk


# test
testdoublelists = [1, 2, 3, 5, 9, 2, 0, 5, 6, 100]
print(topK(testdoublelists, 3))
# [100, 9, 6]
