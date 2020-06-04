#https://www.acmicpc.net/problem/7453

import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
b = []
c = []
d = []

for _ in range(n):
    q,w,e,r = map(int,sys.stdin.readline().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)

first = []
for i in range(n):
    sum = a[i]
    for j in range(n):
        sum += b[j]
        first.append(sum)
        sum -= b[j]

second = []
for i in range(n):
    sum = c[i]
    for j in range(n):
        sum += d[j]
        second.append(sum)
        sum -= d[j]

first.sort()
second.sort()

counter = Counter(second)
ans = 0
for i in first:
    ans += counter[-i]
print(ans)