#https://www.acmicpc.net/problem/15650
import sys

n, m = map(int,sys.stdin.readline().split())
c = [False] * (n+1)
ans = [0] * m

def go(index,n,m,l):
    if index == m:
        sys.stdout.write(" ".join(map(str,ans)) + "\n")
        return
    for i in range(l,n+1):
        if c[i] == True:
            continue
        c[i] = True
        ans[index] = i
        go(index+1,n,m,ans[index])
        c[i] = False
go(0,n,m,1)