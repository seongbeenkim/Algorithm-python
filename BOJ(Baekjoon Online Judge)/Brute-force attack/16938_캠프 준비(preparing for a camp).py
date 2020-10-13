#https://www.acmicpc.net/problem/16938

import sys

n,l,r,x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

answer = 0

def go(i,start,res):
    global answer

    if len(res) >= 2 and l <= sum(res) <= r and max(res) - min(res) >= x:
        answer += 1

    if i >= n:
        return

    for j in range(start,n):
        go(i+1,j+1,res + [a[j]])
go(0,0,[])
print(answer)