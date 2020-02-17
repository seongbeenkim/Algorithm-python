#https://www.acmicpc.net/problem/1260

import sys,queue

n, m, start = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)

for i in range(m):
    u, v = map(int,sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1,n+1):
    a[i].sort()

def dfs(index):
    if check[index]:
        return
    check[index] = True
    sys.stdout.write(str(index) + " ")
    for i in a[index]:
        if check[i] == False:
            dfs(i)
def bfs(index):
    check = [False] * (n + 1)
    q = queue.Queue()
    q.put(index)
    check[index] = True
    while not q.empty():
        x = q.get()
        sys.stdout.write(str(x) + " ")
        for i in a[x]:
            if check[i] == False:
                check[i] = True
                q.put(i)
dfs(start)
sys.stdout.write("\n")
bfs(start)
sys.stdout.write("\n")