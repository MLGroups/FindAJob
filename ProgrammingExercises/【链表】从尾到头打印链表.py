# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 19:44
# @Author  : 石头人m
# @File    : 【链表】从尾到头打印链表.py
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        r = []
        while listNode:
            r.insert(0, listNode.val)
            listNode = listNode.next
        return r
