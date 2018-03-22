# -*- coding: utf-8 -*-
# @Time    : 18-3-22下午5:20
# @Author  : 石头人m
# @File    : 【链表】合并两个排序的链表.py

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        mergeHead = ListNode(18)
        p = mergeHead
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
            else:
                mergeHead.next = pHead1
                pHead1 = pHead1.next

            mergeHead = mergeHead.next
        if pHead1:
            mergeHead.next = pHead1
        elif pHead2:
            mergeHead.next = pHead2
        return p.next


'''
比较两个链表的首结点，哪个小的的结点则合并到第三个链表尾结点，并向前移动一个结点。
步骤一结果会有一个链表先遍历结束，或者没有
第三个链表尾结点指向剩余未遍历结束的链表
返回第三个链表首结点
'''
