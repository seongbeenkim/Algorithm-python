#https://www.acmicpc.net/problem/2606

import sys
from collections import deque

computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())
a = [[] for _ in range(computer+1)]
d = [-1 for _ in range(computer+1)]
check = [False for _ in range(computer+1)]

for i in range(network):
    x,y = map(int,sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)

def dfs(x):
    d[x] = 0
    check[x] = True
    for i in a[x]:
        if check[i] == False and d[i] == -1:
            dfs(i)


def bfs(x):
    q = deque()
    q.append(x)
    check[x] = True
    d[x] = 0

    while q:
        x = q.popleft()
        for i in a[x]:
            if check[i] == False and d[i] == -1:
                q.append(i)
                check[i] = True
                d[i] = d[x] + 1

dfs(1) #bfs(1)

cnt = 0
for i in check[2:]:
    if i == True:
        cnt += 1
print(cnt)