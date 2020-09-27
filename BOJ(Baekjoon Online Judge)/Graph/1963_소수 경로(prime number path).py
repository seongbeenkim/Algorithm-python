#https://www.acmicpc.net/problem/1963

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())

    prime = [False] * (10000)
    check = [False] * (10000)

    d = {}

    for i in range(2,10000):
        if not check[i]:
            if i >= 1000:
                prime[i] = True
                check[i] = True
                d[i] = -1
            k = i**2
            while k <= 9999:
                check[k] = True
                k += i

    q = deque()
    q.append(a)
    d[a] = 0

    while q:
        x = q.popleft()
        s_x = str(x)
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                next = ''
                if i == 0:
                    next = str(j) + s_x[1:]
                elif i == 1:
                    next = s_x[:i] + str(j) + s_x[i+1:]
                elif i == 2:
                    next = s_x[:i] + str(j) + s_x[i+1:]
                elif i == 3:
                    next = s_x[:i] + str(j)
                num = int(next)
                if num in d and d[num] == -1 and prime[num]:
                    d[num] = d[x] + 1
                    q.append(num)

    if d[b] == -1:
        prime("impossible")
    else:
        print(d[b])