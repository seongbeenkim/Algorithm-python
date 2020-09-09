#https://www.acmicpc.net/problem/1865

import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n,m,w = map(int,sys.stdin.readline().split())
    path = []
    maximum = 2147383647
    dist = [maximum] * (n + 1) # 아무 값이나 넣어줘도 상관없다.
    for _ in range(m):
        s,e,t = map(int,sys.stdin.readline().split())
        path.append([s,e,t])
        path.append([e,s,t])
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        path.append([s,e,-t])
    dist[1] = 0 # 넣어줄 필요가 없다.
    negative = False
    for i in range(1,n+1):
        for s, e, t in path:
            if dist[e] > dist[s] + t: # dist[s] != maximum을 해줄 필요가 없다. 모든 정점이 연결되어 있다고 할 수도 없어서 해당 정점이 maximum이더라도 검사를 해주어 그 곳에서 시작되는 음의 사이클이 있는지만 찾기만 하면 되기 때문이다.
                dist[e] = dist[s] + t
                if i == n:
                    negative = True
    if negative:
        print("YES")
    else:
        print("NO")