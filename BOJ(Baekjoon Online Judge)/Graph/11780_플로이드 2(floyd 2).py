#https://www.acmicpc.net/problem/11780

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 10**9
a = [[INF] * (n+1) for _ in range(n+1)]
next = [[-1] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    a[i][i] = 0

for _ in range(m):
    s, e, c = map(int,sys.stdin.readline().split())
    if a[s][e] > c:
        a[s][e] = c
        next[s][e] = e

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]
                next[i][j] = next[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j] == INF:
            a[i][j] = 0
        print(a[i][j], end =" ")
    print()

def go(x,y):
    if next[x][y] == -1:
        print(0)
        return

    q = []
    q.append(x)
    while x != y:
        x = next[x][y]
        q.append(x)

    print(len(q), end = " ")
    while q:
        print(q.pop(0), end = " ")
    print()
    return



for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or a[i][j] == 0:
            print(0)
        else:
            go(i,j)
