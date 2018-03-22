# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午9:28
# @Author  : 石头人m
# @File    : 【美团】数字字符.py

'''
题目描述：
在十进制表示中，任意一个正整数都可以用字符‘0’-‘9’表示出来。
但是当‘0’-‘9’这些字符每种字符的数量有限时，可能有些正整数就无法表示出来了。
比如你有两个‘1’ ，一个‘2’ ，那么你能表示出 11，12，121 等等，但是无法表示出 10，122，200 等数。

现在你手上拥有一些字符，它们都是‘0’-‘9’的字符。
你可以选出其中一些字符然后将它们组合成一个数字，那么你所无法组成的最小的正整数是多少？

输入
第一行包含一个由字符’0’-‘9’组成的字符串，表示你可以使用的字符。
· 1 ≤字符串长度≤ 1000

输出
输出你所无法组成的最小正整数。


样例输入
55
样例输出
1

Hint
Input Sample 2
123456789
Output Sample 2
10
'''

# s = '123456789'
s = raw_input()
ss = []
count_0 = 0  # 0的个数
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 其他非0的个数
for i in list(s):
    ss.append(int(i))

ss = sorted(ss)  # 排序
l = 0
if ss[0] > 1:  # 如果没有1,最小的就是1
    print(1)
else:
    for i in range(len(ss) - 1):
        if ss[i + 1] - ss[i] > 1:  # 如果2-9中缺少某个数，最小的就是缺少的最小那个数
            print(ss[i] + 1)
            l = 1
            break
    if l == 0:
        if ss[-1] < 9:  # 最大的一个数小于九，那么就是最大的那个数加1
            print(ss[-1] + 1)
        else:  # 1-9均包含在输入内
            if ss[0] != 0:  # 如果没有0,最小的就是10
                print(10)
            else:
                for si in ss:
                    if si == 0:
                        count_0 += 1  # 0的个数
                    if si != 0:
                        count[si - 1] += 1  # 其他数字的个数

                # print('count:',count)
                count_min = sorted(count)[0]  # 个数最少的那个数的个数
                # print('count_min',count_min)
                for j in range(len(count)):
                    if count[j] == count_min:
                        ss_min = j + 1  # 最小的那个数
                        break
                # print('ss_min:',ss_min)
                res = ss_min
                if count_0 >= count_min:  # 如果0不是最少的个数
                    for k in range(count_min):
                        res += ss_min * (10 ** (k + 1))
                    print(res)
                elif count_0 < count_min:  # 如果0的个数最少
                    res = res * (10 ** (count_0 + 1))
                    print(res)
