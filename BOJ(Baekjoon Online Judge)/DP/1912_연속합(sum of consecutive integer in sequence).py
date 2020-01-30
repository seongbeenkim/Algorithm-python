#https://www.acmicpc.net/problem/1912

import sys

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