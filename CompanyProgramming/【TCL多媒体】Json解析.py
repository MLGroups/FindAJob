# -*- coding: utf-8 -*-
# @Time    : 18-3-25下午12:47
# @Author  : 石头人m
# @File    : 【TCL多媒体】Json解析.py

'''
已知json格式的字符格式是{父键1:{键1:[值1,值2,值3,值4,值5],名称2:[值1,值2,...],
父键2:{键1:[值1,值2,值3,值4,值5],名称2:[值1,值2,...]}
求，输入“父键x.键x”，可以得到所对应的值

输入：
{Sound1:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]},Sound2:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]},Sound3:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]}}
Sound1.Music
3
输出：
66
'''

json_r = raw_input()
jian = raw_input().split('.')
weizhi = int(raw_input())

# print(json_r)
# print(jian)
# print(weizhi)

json_s = json_r.split(']},')
json_s[0] = json_s[0][1:]
json_s[-1] = json_s[-1][:-2]

for i in range(len(json_s) - 1):
    json_s[i] = json_s[i] + ']'

# print(json_s)
'''
[
'Sound1:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]', 
'Sound2:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]', 
'Sound3:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]'
]
'''
first = ''
for i in json_s:
    l = len(jian[0])
    if i[:l] == jian[0]:
        first = i
        break

# print(first)
'''
Sound1:{Stand:[50,50,50,50,50],Music:[75,60,66,60,75]
'''
first_s = first.split(':{')
# print(first_s)
'''
['Sound1', 'Stand:[50,50,50,50,50],Music:[75,60,66,60,75]']
'''

second = first_s[1]
# print(second)
'''
Stand:[50,50,50,50,50],Music:[75,60,66,60,75]
'''
second_s = second.split('],')
for i in range(len(second_s) - 1):
    second_s[i] = second_s[i] + ']'
# print(second_s)
'''
[
'Stand:[50,50,50,50,50]', 
'Music:[75,60,66,60,75]']
'''
third = ''
for j in second_s:
    l2 = len(jian[1])
    if j[:l2] == jian[1]:
        third = j

# print(third)
'''
Music:[75,60,66,60,75]
'''
third_s = third.split(':')
# print(third_s)

arr = third_s[1][1:-1].split(',')
print(int(arr[weizhi - 1]))
