#https://www.acmicpc.net/problem/2606

import sys

computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())
parent = [i for i in range(computer+1)]
def find(x):
    if x == parent[x]:
        return x

    y = find(parent[x])
    parent[x] = y
    return y

def union(x,y):
    x = find(x)
    y = find(y)
    parent[y] = x

for i in range(network):
    x,y = map(int,sys.stdin.readline().split())
    union(x,y)
cnt = 0
for i in range(2,computer+1):
    res = find(i)
    if res == find(1):
        cnt+=1
print(cnt)