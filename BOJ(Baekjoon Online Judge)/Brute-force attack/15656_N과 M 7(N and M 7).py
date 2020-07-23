#https://www.acmicpc.net/problem/15656

import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
ans = [0] * (m)
a.sort()

def go(index):
    if index == m:
        print(*ans)
        return
    for i in range(n):
        ans[index] = a[i]
        go(index+1)
go(0)

"""
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

def go(index,candi):
    if len(candi) == m:
        print(*candi)
        return

    for i in range(n):
        go(index+1,candi+[a[i]])

go(0,[])
"""