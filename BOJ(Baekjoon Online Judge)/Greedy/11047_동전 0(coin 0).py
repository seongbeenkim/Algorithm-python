#https://www.acmicpc.net/problem/11047

import sys

n, k = map(int,sys.stdin.readline().split())

a = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0

for i in range(n-1,-1,-1):
    if a[i] <= k:
        cnt += k//a[i]
        k -= (k//a[i]) * a[i]

print(cnt)