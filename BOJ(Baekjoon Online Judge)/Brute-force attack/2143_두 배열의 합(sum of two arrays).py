#https://www.acmicpc.net/problem/2143

import sys
from collections import Counter

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

first = []
second = []

for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += a[j]
        first.append(sum)

for i in range(m):
    sum = 0
    for j in range(i,m):
        sum += b[j]
        second.append(sum)
first.sort()
second.sort()

c = Counter(second)
ans = 0
for num in first:
    ans += c[t-num]
print(ans)