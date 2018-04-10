# -*- coding: utf-8 -*-
# @Time    : 18-4-10下午8:57
# @Author  : 石头人m
# @File    : 【小米】擦黑板.py


'''
擦黑板
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
Steph 无聊的时候会在黑板上写一个数。之后，每次擦除末尾的数字，直到写下来的数被全部擦除。 每次擦除前，Steph 会将当前在黑板上的数累加到计算器中。 举个例子，如果 Steph 最初写在黑板上的数是 816，那么每次擦除前黑板上的数是816，81，8。最终计算器中的结果是 816 + 81 + 8 = 905。 假设给出一个数 S (1 <= S <= 10^18)，Steph 想知道能否找到一个数 x，当写在 x 在黑板上后，执行擦除过程后计算器中得到的结果是 S，我们将这样的S称为立方数。如果不能得到，输出 -1，如果能得到，输出最小的 x。

输入
一个正整数 S (1 <= S <= 10^18)

输出
最小的立方数（整型）

样例输入
905
样例输出
816

Hint
输入样例2
10
输出样例2
-1

https://blog.csdn.net/u010429424/article/details/78414665?locationNum=7&fps=1
'''


def count(t, j):
    p = 1
    sum = 0
    while (t > 0):
        sum += j * p
        p *= 10
        t -= 1
    return sum


def solution(k):
    lenn = len(str(k))
    num = list()
    for i in range(lenn):
        sum = 0
        j = 0
        for j in range(10):
            temp = count(lenn - i, 9 - j)
            if sum <= k - temp:
                sum += temp
                break
        num.append(9 - j)
        k -= sum
    if k != 0:
        return -1
    p = 1
    result = 0
    for i in range(lenn):
        result += num[lenn - i - 1] * p
        p *= 10
    return result


_num = long(raw_input())

res = solution(_num)

print str(res) + "\n"

'''
思路：
8 * (100 + 10 + 1) + 1 * (10 + 1) + 6 * 1 = 905
即：8 * 111 + 1 * 11 + 6 * 1 = 905，现在已知905，让我们求出8、1、6
相当于：111 * x + 11 * y + z = 905，求解出x = 8、y = 1、z = 6

用了枚举的思想，x、y、z的范围在【0-9】，枚举这些数字，直到找到满足条件的解。
首先从9到0枚举x，然后y，然后z…
'''
