# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午5:16
# @Author  : 石头人m
# @File    : 【链表】链表中倒数第k个结点.py

'''
输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k == 0:
            return None
        p1 = head
        p2 = head
        for i in range(k - 1):
            if p1.next:
                p1 = p1.next
            else:
                return None
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2


'''

设置两个指针 fast 、slow，fast先走k步，如果走不到第k步（nullptr节点是可以走到的，
但是nullptr节点没有next，所以只能走到nullptr），说明链表长度不够k，直接返回nullptr；
然后，令 fast 和 slow 开始同步往下移动，直到 fast 移动到nullptr，
此时slow就是倒数第 k 个节点的，返回即可。
'''
