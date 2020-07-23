#https://www.acmicpc.net/problem/15651
import sys

sys.setrecursionlimit(10**9)
n, m = map(int,sys.stdin.readline().split())
ans = [0] * m

def go(index,n,m):
    if index == m:
        sys.stdout.write(" ".join(map(str,ans)) + "\n")
        return
    for i in range(1,n+1):
        ans[index] = i
        go(index+1,n,m)
go(0,n,m)

"""
n, m = map(int,sys.stdin.readline().split())

def go(candi):

    if len(candi) == m:
        print(*candi)
        return

    for i in range(1,n+1):
        go(candi+[i])

for i in range(1,n+1):
    go([i])
"""