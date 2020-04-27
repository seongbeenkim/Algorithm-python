#https://www.acmicpc.net/problem/15664

import sys
from collections import Counter
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
a = list(Counter(a).items())
num, cnt = map(list,zip(*a))
ans = [0] * m

def go(index,start,num,cnt):
    if index == m:
        print(*ans)
        return

    for i in range(start,len(num)):
        if cnt[i] > 0:
            cnt[i] -= 1
            ans[index] = num[i]
            go(index+1,i,num,cnt)
            cnt[i] += 1

go(0,0,num,cnt)
"""
a.sort()

a = [0] * m
c = [False] * n
d = []

def go(index,start):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(start,n):
        if c[i]:
            continue
        c[i] = True
        a[index] = a[i]
        go(index+1,i+1)
        c[i] = False
go(0,0)
d = sorted(list(set(d)))
for x in d:
    print(*x)
"""

