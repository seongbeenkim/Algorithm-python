#https://www.acmicpc.net/problem/2294

import sys

n, k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
d = [100001] * (k+1)
d[0] = 0

for i in range(n):
    for j in range(a[i],k+1):
        if j-a[i] >= 0 and d[j-a[i]] != 100001:
            if d[j] == 100001 or d[j] > d[j-a[i]] + 1:
                d[j] = d[j-a[i]]+1

print(d[k])


"""
n, k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
d = [100001] * (k+1)
d[0] = 0

for i in range(n):
    for j in range(a[i],k+1):
        if j-a[i] >= 0 and d[j-a[i]] != 100001:
            if i == 0:
                d[j] = d[j-a[i]]+1
            else:
                d[j] = min(d[j],d[j-a[i]]+1)
if d[k] == 100001:
    print(-1)
else:
    print(d[k])
"""

"""
n, k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
d = [100001] * (k+1)
d[0] = 0

for i in range(n):
    for j in range(a[i],k+1):
        d[j] = min(d[j],d[j-a[i]]+1)
if d[k] == 100001:
    print(-1)
else:
    print(d[k])

"""