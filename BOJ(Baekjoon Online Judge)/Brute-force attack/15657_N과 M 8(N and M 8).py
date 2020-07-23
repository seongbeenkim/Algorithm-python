#https://www.acmicpc.net/problem/15656

import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
ans = [0] * m
def go(index,start):
    if index == m:
        print(*ans)
        return
    for i in range(start,n):
        ans[index] = a[i]
        go(index+1,i)
go(0,0)

"""
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

def go(index,candi):
    if len(candi) == m:
        print(*candi)
        return

    for i in range(n):
        if len(candi) == 0:
            go(index + 1, candi + [a[i]])
        elif candi[-1] <= a[i]:
            go(index+1,candi+[a[i]])

go(0,[])
"""