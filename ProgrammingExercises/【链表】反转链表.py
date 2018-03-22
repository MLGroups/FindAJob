# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午5:19
# @Author  : 石头人m
# @File    : 【链表】反转链表.py

'''
输入一个链表，反转链表后，输出链表的所有元素。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        l = None
        while pHead:
            tmp = pHead.next
            pHead.next = l
            l = pHead
            pHead = tmp
        return l


'''
递归的方法其实是非常巧的，它利用递归走到链表的末端，然后再更新每一个node的next 值 ，实现链表的反转。
而newhead 的值没有发生改变，为该链表的最后一个结点，所以，反转后，我们可以得到新链表的head。
注意关于链表问题的常见注意点的思考：
1、如果输入的头结点是 NULL，或者整个链表只有一个结点的时候
2、链表断裂的考虑
'''
