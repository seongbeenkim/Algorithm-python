#https://www.acmicpc.net/problem/2015

import sys
from collections import defaultdict
n, k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

d = [0] * n
d[0] = a[0]
for i in range(1,n):
    d[i] = d[i-1] + a[i]

res = 0

cnt = defaultdict(int)
for i in range(n):
    if d[i] == k:
        res+=1
    res += cnt[d[i]-k]
    cnt[d[i]] += 1
print(res)