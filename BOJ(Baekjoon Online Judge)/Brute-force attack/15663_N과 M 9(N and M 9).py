#https://www.acmicpc.net/problem/15663

import sys
from collections import Counter
"""
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

ans = []
check = [False] * (n+1)

def go(index,seq):
    if index == m and len(seq) == m:
        ans.append(tuple(seq))  # append(seq) 하지 않고 tuple 쓰는 이유 https://stackoverflow.com/questions/37136878/list-unhashable-but-tuple-hashable
        return
    if index >= len(a):
        return

    for i in range(len(a)):
        if check[i]:
            continue
        check[i] = True
        go(index+1,seq+[a[i]])
        check[i] = False
go(0,[])
d = list(set(ans))
d.sort()
for x in d:
    print(*x)
"""

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a = list(Counter(a).items())
a.sort()

num, check = map(list,zip(*a))
n = len(num)
def go(index,seq):
    if index == m and len(seq) == m:
        print(*seq)
        return
    for i in range(n):
        if check[i] > 0:
            check[i] -= 1
            go(index+1,seq+[num[i]])
            check[i] += 1
go(0,[])