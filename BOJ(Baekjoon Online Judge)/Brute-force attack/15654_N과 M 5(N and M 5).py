#https://www.acmicpc.net/problem/15652
import sys

sys.setrecursionlimit(10**9)
n, m = map(int,sys.stdin.readline().split())
a = [0]+list(map(int,sys.stdin.readline().split()))
a.sort()
c = [False] * (n+1)
ans = [0] * m

def go(index,n,m):
    if index == m:
        sys.stdout.write(" ".join(map(str,ans)) + "\n")
        return
    for i in range(1,n+1):
        if c[i] == True:
            continue
        c[i] = True
        ans[index] = a[i]
        go(index+1,n,m)
        c[i] = False
go(0,n,m)


"""
sys.setrecursionlimit(10**6)


n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

def go(index,candi):
    if len(candi) == m:
        print(*candi)
        return

    for i in range(n):
        if a[i] not in candi:
            go(index+1,candi+[a[i]])

go(0,[])
"""