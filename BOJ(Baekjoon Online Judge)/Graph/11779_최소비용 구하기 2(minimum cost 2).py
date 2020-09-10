#https://www.acmicpc.net/problem/1916

import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = [[] for _ in range(n+1)]
INF = 100000001
dist = [INF] * (n+1)
check = [False] * (n+1)
v = [-1] * (n+1)
for i in range(m):
    s, e, c = map(int,sys.stdin.readline().split())
    a[s].append([e,c])
start, end = map(int,sys.stdin.readline().split())

dist[start] = 0
q = []
heapq.heappush(q,[0,start])
while q:
    c, s = heapq.heappop(q)
    if dist[s] < c:
        continue
    if check[s] == False:
        for e, t in a[s]:
            if dist[s] != INF and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                heapq.heappush(q,[dist[e],e])
                check[s] = True

print(dist[end])

x = end
stack = []
while x != -1:
    stack.append(x)
    x = v[x]
print(len(stack))
print(*stack[::-1])

"""
ans = []
while v[end] != 0:
    ans.append(end)
    end = v[end]
ans.append(end)
ans.reverse()
print(len(ans))
print(*ans)
"""