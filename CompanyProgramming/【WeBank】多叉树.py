# -*- coding: utf-8 -*-
# @Time    : 18-4-16下午8:32
# @Author  : 石头人m
# @File    : 【WeBank】多叉树.py


'''
请写程序定义一个多叉树的数据结构
请写程序按层次遍历多叉树。
'''


# 定义节点结构
class node:

    def __init__(self, data):
        self._data = data  # 本节点数据
        self._children = []  # 本节点的子节点列表

    def getdata(self):
        return self._data

    def getchildren(self):
        return self._children

    def add(self, node):
        self._children.append(node)


# 定义树结构，根节点
class tree:

    def __init__(self, node):
        self._head = node


# 定义节点
a = node('A')
b = node('B')
c = node('C')
d = node('D')
e = node('E')
f = node('F')
g = node('G')
h = node('H')
i = node('I')
j = node('J')
k = node('K')
l = node('L')
m = node('M')
n = node('N')
o = node('O')
p = node('P')
# 定义树
a.add(b)
a.add(c)
b.add(d)
b.add(e)
b.add(f)
c.add(g)
c.add(h)
d.add(i)
e.add(j)
g.add(l)
g.add(m)
h.add(n)
i.add(k)
m.add(o)
n.add(p)

tree = tree(a)

# 树的根节点
head_node = tree._head

# 依次遍历的节点
list_node = []
list_node.append(head_node)

# 层次遍历结果
list_res = list()
while len(list_node) != 0:
    node_first = list_node[0]

    list_res.append(node_first.getdata())

    # 将字节点依次加入要遍历的列表
    for children in node_first.getchildren():
        list_node.append(children)

    # 删除已经获取值的第一个节点
    del list_node[0]

print(list_res)
