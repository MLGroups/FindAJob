# -*- coding: utf-8 -*-
# @Time    : 18-4-16下午8:33
# @Author  : 石头人m
# @File    : 【WeBank】单链表倒数第K个元素.py


'''
3.请写程序定义一个单向链表的数据结构
请写程序在单向链表中求出倒数第N个元素的值，并分析算法复杂度。
'''


class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


def getK(head, k):
    # k=0或链表为空
    if k == 0 or head == None:
        return None
    pA = head
    pB = head
    while k > 1 and pA != None:
        pA = pA.next
        k -= 1
    # 节点数小于k
    if k > 1 or pA == None:
        return None
    while pA.next != None:
        pA = pA.next
        pB = pB.next
    return pB.val


# 测试
ahead = ListNode()
bhead = ListNode()
chead = ListNode()
dhead = ListNode()

ahead.val = 1
bhead.val = 2
chead.val = 3
dhead.val = 4

ahead.next = bhead
bhead.next = chead
chead.next = dhead
print(getK(ahead, 2))
# 3
