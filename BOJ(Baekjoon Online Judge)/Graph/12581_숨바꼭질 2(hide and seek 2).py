#https://www.acmicpc.net/problem/12581

import sys
from collections import deque

sys.setrecursionlimit(10**6)

n, k = map(int,sys.stdin.readline().split())
MAX = 200001

d = [-1] * MAX
cnt = [0] * MAX

q = deque()
q.append(n)
d[n] = 0
cnt[n] = 1

while q:
    x = q.popleft()
    for i in [x+1,x-1,2*x]:
        if 0 <= i <= 200000:
            if d[i] == -1:
                d[i] = d[x] + 1
                q.append(i)
                cnt[i] = cnt[x]
            elif d[i] == d[x]+1:
                cnt[i] += cnt[x]

print(d[k])
print(cnt[k])