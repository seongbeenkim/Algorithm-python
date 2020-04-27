#https://www.acmicpc.net/problem/15655

import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
ans = []
"""
def go(index,start,seq):
    if index == m:
        ans.append(seq)
        return
    if index > n:
        return
    for i in range(start,n):
        go(index+1,i+1,seq+[a[i]])
go(0,0,[])
for i in ans:
    print(*i)
"""
def go(index,seq):
    if len(seq) == m:
        ans.append(seq)
        return
    if index >= n:
        return
    go(index+1,seq+[a[index]])
    go(index+1,seq)
go(0,[])
for i in ans:
    print(*i)