# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 18:37
# @Author  : 石头人m
# @File    : 【排序】排序实现-python.py

# ==============================================冒泡============================================
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort2(array):
    for i in range(len(array) - 1):
        current_status = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                current_status = True
        if not current_status:
            break
    return array


# ==============================================插入============================================
def insert_sort(array):
    for i in range(1, len(array)):
        min = array[i]
        j = i - 1
        while j >= 0 and array[j] > min:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = min
    return array


# ==============================================选择============================================
def select_sort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
                array[i], array[min] = array[min], array[i]
    return array


# ==============================================希尔============================================
def shell_sort(li):
    """希尔排序"""
    gap = len(li) // 2
    while gap > 0:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap //= 2
    return li


# ==============================================归并============================================
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2  # python3 整数除法/会变浮点，改为//
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


# ==============================================堆============================================
def sift(array, left, right):
    """调整"""
    i = left  # 当前调整的小堆的父节点
    j = 2 * i + 1  # i的左孩子
    tmp = array[i]  # 当前调整的堆的根节点
    while j <= right:  # 如果孩子还在堆的边界内
        if j < right and array[j] < array[j + 1]:  # 如果i有右孩子,且右孩子比左孩子大
            j = j + 1  # 大孩子就是右孩子
        if tmp < array[j]:  # 比较根节点和大孩子，如果根节点比大孩子小
            array[i] = array[j]  # 大孩子上位
            i = j  # 新调整的小堆的父节点
            j = 2 * i + 1  # 新调整的小堆中I的左孩子
        else:  # 否则就是父节点比大孩子大，则终止循环
            break
    array[i] = tmp  # 最后i的位置由于是之前大孩子上位了，是空的，而这个位置是根节点的正确位置。


def heap(array):
    n = len(array)
    # 建堆，从最后一个有孩子的父亲开始，直到根节点
    for i in range(n // 2 - 1, -1, -1):
        # 每次调整i到结尾
        sift(array, i, n - 1)
    # 挨个出数
    for i in range(n - 1, -1, -1):
        # 把根节点和调整的堆的最后一个元素交换
        array[0], array[i] = array[i], array[0]
        # 再调整，从0到i-1
        sift(array, 0, i - 1)
    return array


# ==============================================快排============================================
def partition(array, left, right):
    tmp = array[left]
    while left < right:
        while left < right and array[right] >= tmp:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return left


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid - 1)
        quick_sort(array, mid + 1, right)
    return array


array = [1, 2, 4, 6, 4, 8, 4, 9, 100, 2]
print(bubble_sort(array))
print(bubble_sort2(array))
print(insert_sort(array))
print(select_sort(array))
print(shell_sort(array))
print(merge_sort(array))
print(heap(array))
print(quick_sort(array, 0, len(array) - 1))
