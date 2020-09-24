#https://www.acmicpc.net/problem/12886

import sys
from collections import deque

a, b, c = map(int,sys.stdin.readline().split())
d = [[0] * 1501 for _ in range(1501)]
s = a + b + c

q = deque()
q.append((a,b))
d[a][b] = 1

while q:
    x, y = q.popleft()
    z = s-x-y

    for i in [x,y,z]:
        for j in [x,y,z]:
            if i == j:
                continue
            if i > j and d[i-j][j+j] == 0:
                q.append((i-j,j+j))
                d[i-j][j+j] = 1
if s % 3 != 0:
    print(0)
else:
    print(d[s//3][s//3])