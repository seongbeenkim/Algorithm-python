#https://www.acmicpc.net/problem/15661

import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = 2147483647

def count(start,link):
    global ans
    s = 0
    l = 0
    for i in start:
        for j in start:
            if i == j:
                continue
            s += a[i][j]

    for i in link:
        for j in link:
            if i == j:
                continue
            l += a[i][j]

    ans = min(ans,abs(s-l))
for i in range(1, 1<<n):
    start = []
    link = []
    for j in range(n):
        if i & (1<<j):
            start.append(j)
        else:
            link.append(j)

    if len(start) > 0 and len(link) > 0:
        count(start,link)
print(ans)