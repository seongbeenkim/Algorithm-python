#https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

house = []
chicken = []
ans = 2147383647

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append([i,j])

        elif a[i][j] == 2:
            chicken.append([i,j])

def get_distance(m_chicken,z):

    sum = 0
    for i, j in house:
        temp = 100
        for k in range(m):
            temp = min(abs(chicken[m_chicken[k]][0]-i) + abs(chicken[m_chicken[k]][1]-j),temp)
        sum += temp

    return sum

combi = combinations([k for k in range(len(chicken))],m)

for i in combi:
    temp = get_distance(i,m)
    ans = min(temp,ans)

print(ans)