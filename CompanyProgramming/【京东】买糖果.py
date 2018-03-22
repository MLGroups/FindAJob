# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 13:47
# @Author  : 石头人m
# @File    :【京东】买糖果.py

'''
某糖果公司专门生产儿童糖果，它最受儿童欢迎的糖果有A1、A2两个序列，均采用盒式包装。
包装好的A1类糖果体积为一个存储单位，而包装好的A2类糖果体积正好是A1类的两倍。

这两类糖果之所以广受儿童欢迎，是因为糖果中含有公司独家研发的魔幻因子。
A1或A2序列中的糖果，看起来包装可能是一样的，但因为其中的魔幻因子含量不同被细分为不同的产品。
临近传统节日，公司的糖果供不应求。

作为一个精明的糖果分销商，小东希望能够借此大赚一笔，于是带着现金开着货车来公司提货。
货车的容量是确定的，小东希望采购的糖果能够尽可能装满货车，且糖果的魔幻因子总含量最高。
只要不超出货车容量，糖果总可以装入货车中。

小东希望你能帮她解决这一问题。

输入
输入中有多组测试数据。
每组测试数据的第一行有两个整数n和v，1<=n<=10^5, 1<=v<=10^9，n为可供选购糖果数量，v为货车的容量。
随后n行为糖果的具体信息，第一行编号为1，第二行编号为2，以此类推，最后一行编号为n。
每行包含两个整数ti和pi，1<=ti<=2, 1<=pi<=10^4，ti为糖果所属的序列，1为A1、2为A2，pi则是其中的魔幻因子含量。

输出
对每组测试数据，先在单独的一行中输出能采购的糖果中的魔幻因子最高含量，
之后在单独的行中按编号从小到大的顺序输出以空格分隔的糖果编号，若有多组糖果组合均能满足要求，
输出编号最小的组。若没有糖果能够满足要求，则在第一行中输出0，第二行输出“No”。

'''
while True:
    n, v = map(int, raw_input().split())
    bonbon = []
    for i in range(n):
        t, p = map(int, raw_input().split())
        if bonbon == []:
            bonbon.append((1, t, p))
        else:
            for j in range(i):
                if float(bonbon[j][2]) / bonbon[j][1] < float(p) / t:
                    bonbon.insert(j, (i + 1, t, p))
                    break
            if len(bonbon) != i + 1:
                bonbon.append((i + 1, t, p))
    sum = 0
    i = 0
    ser = []
    magic = 0
    while sum <= v and i < n:
        sum += bonbon[i][1]
        if sum > v:
            sum -= bonbon[i][1]
            break
        else:
            ser.append(bonbon[i][0])
            magic += bonbon[i][2]
        i += 1
    if i != n and sum != v:
        j = i - 1
        while j >= 0 and bonbon[j][1] != 1:
            j -= 1
        k = i + 1
        while k < n and bonbon[k][1] != 1:
            k += 1
        if j >= 0 and k < n:
            if bonbon[j][2] + bonbon[k][2] > bonbon[i][2]:
                ser.append(bonbon[k][0])
                magic += bonbon[k][2]
            elif bonbon[j][2] + bonbon[k][2] == bonbon[i][2]:
                if min(bonbon[j][0], bonbon[k][0]) > bonbon[i][0]:
                    ser.append(bonbon[i][0])
                    ser.pop(ser.index(bonbon[j][0]))
                    magic += bonbon[i][2] - bonbon[j][2]
                else:
                    ser.append(bonbon[k][0])
                    magic += bonbon[k][2]
            else:
                ser.append(bonbon[i][0])
                ser.pop(ser.index(bonbon[j][0]))
                magic += bonbon[i][2] - bonbon[j][2]
        elif j >= 0:
            if (bonbon[j][2] == bonbon[i][2] and bonbon[j][0] > bonbon[i][0]) or bonbon[j][2] < bonbon[i][2]:
                ser.append(bonbon[i][0])
                ser.pop(ser.index(bonbon[j][0]))
                magic += bonbon[i][2] - bonbon[j][2]
        elif k < n:
            ser.append(bonbon[k][0])
            magic += bonbon[k][2]
    print magic
    if ser == []:
        print 'No'
    else:
        print ' '.join(map(str, sorted(ser)))
