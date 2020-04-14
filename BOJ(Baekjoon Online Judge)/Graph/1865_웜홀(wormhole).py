#https://www.acmicpc.net/problem/1865

import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n,m,w = map(int,sys.stdin.readline().split())
    path = []
    for _ in range(m):
        s,e,t = map(int,sys.stdin.readline().split())
        path.append([s,e,t])
        path.append([e,s,t])
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        path.append([s,e,-t])
    dist = [0] * (n+1)
    negative = False
    for i in range(1,n+1):
        for s, e, t in path:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n:
                    negative = True
    if negative:
        print("YES")
    else:
        print("NO")