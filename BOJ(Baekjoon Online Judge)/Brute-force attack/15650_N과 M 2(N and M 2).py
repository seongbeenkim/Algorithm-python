#https://www.acmicpc.net/problem/15650
import sys

n, m = map(int,sys.stdin.readline().split())
ans = [0] * m

def go(index,n,m,l):
    if index == m:
        sys.stdout.write(" ".join(map(str,ans)) + "\n")
        return
    for i in range(l+1,n+1):
        ans[index] = i
        go(index+1,n,m,ans[index])
go(0,n,m,0)