#https://www.acmicpc.net/problem/1912

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [0] * n
d[0] = a[0]
for i in range(1,n):
    d[i] = a[i]
    if d[i-1] > 0:
        d[i] += d[i-1]
print(max(d))

"""
t = int(sys.stdin.readline())
n = [0] + list(map(int,sys.stdin.readline().split()))
d = [0] * (t+1)
for i in range(len(n)):
    d[i] = n[i]
for i in range(1,t+1):
    if d[i-1] + d[i] >= d[i]:
        d[i] = d[i-1] + d[i]

ans = -1001
for i in d[1:]:
    if ans < i:
        ans = i
print(ans)
"""