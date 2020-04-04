#https://www.acmicpc.net/problem/10942

import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
d = [[-1] * (n) for i in range(n)]

for i in range(n):
    d[i][i] = 1

for i in range(n-1):
    if a[i] == a[i+1]:
        d[i][i+1] = 1

for k in range(2, n):
    for i in range(n-k):
        j = i+k
        if a[i] == a[j] and d[i+1][j-1] == 1:
            d[i][j] = 1
"""
def go(i,j):
    if i == j:
        return 1
    elif i == j+1:
        if a[i][j] == a[i][j+1]:
            return 1
        else:
            return 0
    if d[i][j] != -1:
        return d[i][j]
    if a[i] != a[j]:
        return 0
    else:
        d[i][j] = go(i+1,j-1)
    return d[i][j]
"""
for i in range(m):
    s, e = map(int,sys.stdin.readline().split())
    #print(go(s-1,e-1))
    print(1 if d[s-1][e-1] == 1 else 0)