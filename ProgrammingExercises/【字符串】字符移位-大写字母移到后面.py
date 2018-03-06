# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 21:47
# @Author  : 石头人m
# @File    : 【字符串】字符移位-大写字母移到后面.py

'''
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？

输入：
hxKLAGLLzPyTxsFsrUnnSKQBHdQQrOyaEYJRgiJbHIDXFcQkFmIhPNKIBfHxXDBdKAvgZiBLVwnlxJAHmttsSJkZhSmQneNVoKoIYZRjPqsrFFaaqZbyNyeRjVKVFrCGdfycidTqbyQcpAtdRGzzBAaKoqybWMOyhrCQdwcRwQQpQavTnAbjriVwxJOrTYJVGYSWzKYeNAGqBzkJLucabNYvyVFxAGKLfqHXNttaqZfncEdTroGMzZnDbvZBBaRbJvuYIvlWrKaaGrvtyxrsCUOqxdwCrmVEeDrLKZKFJVRmrLsmbmOGUJyfdZIrFhuSwJQGRTYMLxKQNMaCavatlQIRZmFQvyWgQTVENxUcPKQCaUQbjyfaNuwoNdTBNldgrtPUcQodqsuJOdDpUczJWCZaasDdEYJkvituMHrCmZQSlRjIefVisatIUtfxBeKnHPyvWUKzRliFsYWgeXogiEgXDbfxAybwFuqFyEvjfIHEPDPKqEiGUtZhdDIDBGKpvBFyqHeEEhAToAbqHEpIdIhIGBtWjGHiQRctZxQQYkfFoWUbqZyIcjRPQBilHrnqNBzFmoRUYCSrGkawJCcOrMceegISpIpSGVjbngWVMTYtGoAlQFPFyOFAxndJZNfKDTwFIxisKTjyjchidXpYgLfoBOLriuIAHmAbQwoHBgbdUYBHlDQGZJASsHszOEPthLVnYbNqWegmONexfdsTVYHgtDmlyugefOBsqmgNDBoxkkhVHfvrYooVOyxDJQJLjYSngksbTopoPJFsKQzHePLukXyYTYCeW
输出：
hxzyxssrnndryagibckmhfxdvgiwnlxmttskhmneoojqsraaqbyyejrdfycidqbycptdzzaoqybyhrdwcwpavnbjriwxrzeqzkucabvyxfqttaqfncdroznbvabvuvlraarvtyxrsqxdwrmermrsmbmyfdrhuwxaavatlmvygxcabjyfauwodldgrtcodqsudpczaasdkviturmljefisattfxenyvzlisgeogigbfxybwuqyvjfqithdpvyqehobqpdhtjictxkfobqycjilrnqzmorkawcrceegppjbngtolyxndfwxisjyjchidpgforiumbwogbdlsszthnbqegmexfdsgtmlyugefsqmgoxkkhfvrooyxjngksboposzeukyeKLAGLLPTFUSKQBHQQOEYJRJHIDXFQFIPNKIBHXDBKAZBLVJAHSJZSQNVKIYZRPFFZNRVKVFCGTQARGBAKWMOCQRQQQTAVJOTYJVGYSWKYNAGBJLNYVFAGKLHXNZETGMZDZBBRJYIWKGCUOCVEDLKZKFJVRLOGUJZIFSJQGRTYMLKQNMCQIRZFQWQTVENUPKQCUQNNTBNPUQJODUJWCZDEYJMHCZQSRIVIUBKHPWUKRFYWXEXDAFFEIHEPDPKEGUZDIDBGKBFHEEATAHEIIIGBWGHQRZQQYFWUZIRPQBHNBFRUYCSGJCOMISISGVWVMTYGAQFPFOFAJZNKDTFIKTXYLBOLIAHAQHBUYBHDQGZJASHOEPLVYNWONTVYHDOBNDBVHYVODJQJLYSTPJFKQHPLXYTYCW

'''
s = list(input())
l = len(s)
i = 0
big = 0
while i + big < l:
    if s[i].isupper():
        big = big + 1
        tc = s[i]
        for j in range(l - i - 1):
            s[i + j] = s[i + j + 1]
        s[l - 1] = tc
        i = i
    else:
        i = i + 1
print(''.join(s))

# 我的输出：
# hxzyxssrnndryagibckmhfxdvgiwnlxmttskhmneoojqsraaqbyyejrdfycidqbycptdzzaoqybyhrdwcwpavnbjriwxrzeqzkucabvyxfqttaqfncdroznbvabvuvlraarvtyxrsqxdwrmermrsmbmyfdrhuwxaavatlmvygxcabjyfauwodldgrtcodqsudpczaasdkviturmljefisattfxenyvzlisgeogigbfxybwuqyvjfqithdpvyqehobqpdhtjictxkfobqycjilrnqzmorkawcrceegppjbngtolyxndfwxisjyjchidpgforiumbwogbdlsszthnbqegmexfdsgtmlyugefsqmgoxkkhfvrooyxjngksboposzeukyeKLAGLLPTFUSKQBHQQOEYJRJHIDXFQFIPNKIBHXDBKAZBLVJAHSJZSQNVKIYZRPFFZNRVKVFCGTQARGBAKWMOCQRQQQTAVJOTYJVGYSWKYNAGBJLNYVFAGKLHXNZETGMZDZBBRJYIWKGCUOCVEDLKZKFJVRLOGUJZIFSJQGRTYMLKQNMCQIRZFQWQTVENUPKQCUQNNTBNPUQJODUJWCZDEYJMHCZQSRIVIUBKHPWUKRFYWXEXDAFFEIHEPDPKEGUZDIDBGKBFHEEATAHEIIIGBWGHQRZQQYFWUZIRPQBHNBFRUYCSGJCOMISISGVWVMTYGAQFPFOFAJZNKDTFIKTXYLBOLIAHAQHBUYBHDQGZJASHOEPLVYNWONTVYHDOBNDBVHYVODJQJLYSTPJFKQHPLXYTYCW

'''
1.判断字符是大写：'s'.isupper()。
1.str不能用形如：str[i] = str[i+1]来改变字符串，字符串是不能改变的。
2.list转str：''.join(list)。
'''
