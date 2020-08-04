#https://www.acmicpc.net/problem/1707

import sys
from collections import deque

sys.setrecursionlimit(10**6)
def dfs(x,c):
    check[x] = c
    for i in a[x]:
        if check[i] == 0:
            if not dfs(i,3-c):
                return False
        elif check[i] == check[x]:
            return False
    return True

def bfs(x,c):
    q = deque()
    q.append(x)
    check[x] = c
    while q:
        x = q.popleft()
        c = check[x]
        for i in a[x]:
            if check[i] == 0:
                check[i] = 3-c
                q.append(i)
            elif check[i] == check[x]:
                return False
    return True

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    for i in range(m):
        u, v = map(int,sys.stdin.readline().split())
        a[u].append(v)
        a[v].append(u)
    for i in range(1,n+1):
        a[i].sort()
    ans = True

    for i in range(1,n+1):
        if check[i] == 0 and ans == True:
            if not bfs(i,1): #dfs(i,1)
                ans = False
    sys.stdout.write(('YES' if ans else 'NO')+ "\n")

"""
t = int(sys.stdin.readline())

for _ in range(t):

    v,e = map(int,sys.stdin.readline().split())
    arr = [[] for _ in range(v+1)]
    check = [False] * (v+1)
    color = [0] * (v+1)
    is_divided = True

    for i in range(e):
        a, b = map(int,sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1,v+1):
        if not check[i]:
            q = deque()
            q.append((i,1))
            check[i] = True
            color[i] = 1

            while q:
                x,col = q.popleft()
                for next in arr[x]:
                    if not check[next]:
                        check[next] = True
                        color[next] = 3-col
                        q.append((next,3-col))
                    else:
                        if color[next] == color[x]:
                            is_divided = False
                            break
        if not is_divided:
            break
    if is_divided:
        print("YES")
    else:
        print("NO")
"""