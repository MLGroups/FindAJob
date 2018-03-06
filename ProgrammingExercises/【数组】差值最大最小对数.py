# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 22:30
# @Author  : 石头人m
# @File    : 【数组】差值最大最小对数.py
'''
有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？
'''

while True:
    ary = [int(x) for x in input().split()]
    n = len(ary)
    if n < 2:
        print(0, 0)
    elif n == 2:
        print(1, 1)
    else:
        ary.sort()
        if ary[0] == ary[n - 1]:
            num = n * (n - 1) / 2
            print(num, num)
            continue
        dic = {}
        for i in range(n):
            k = ary[i]
            if k in dic:
                dic[k] += 1
            else:
                dic[k] = 1
        minN = 0
        lenDic = len(dic)
        if lenDic == n:
            min = ary[1] - ary[0]
            minN = 1
            for i in range(2, n):
                if ary[i] - ary[i - 1] == min:
                    minN += 1
                elif ary[i] - ary[i - 1] < min:
                    min = ary[i] - ary[i - 1]
                    minN = 1
        else:
            dicList = dic.values()
            for j in range(lenDic):
                if dicList[j] > 1:
                    minN += dicList[j] * (dicList[j] - 1) / 2
        n1 = dic[ary[0]]
        n2 = dic[ary[n - 1]]
        maxN = n1 * n2
        print(minN, maxN)

'''
1.先排序
     特殊情况：如果排完序之后发现数组中所有数都相同，直接输出结果
         结果为：差最大个数 = 差最小个数 = （n * (n-1))/2;(两两组合)
2.统计数组中每种数字的个数（这里用的map）
3.计算差最小个数
    3.1.如果数组中没有重复数字，说明最小差不为0，最小差肯定是数组中相邻两个数的差
        因此，遍历一边数组，计算并统计最小差。
    3.2.如果数组中有重复数字，说明最小差是0，此时，遍历一边map，数字个数不为0的
        数字会产生最小差0，利用公式计算即可
4.计算差最大个数
    只有一种情况，最大值与最小值的两两组合，即最大值个数 * 最小值个数
算法复杂度：排序O(nlogn), 统计O(n)
'''
