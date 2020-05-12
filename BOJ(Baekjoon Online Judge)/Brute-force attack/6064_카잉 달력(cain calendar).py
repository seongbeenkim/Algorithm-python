#https://www.acmicpc.net/problem/6064

import sys

t = int(sys.stdin.readline())
for i in range(t):
    m,n,x,y = map(int,sys.stdin.readline().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)
