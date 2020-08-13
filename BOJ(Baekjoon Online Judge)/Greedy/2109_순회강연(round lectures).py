#https://www.acmicpc.net/problem/2109

import sys, heapq

n = int(sys.stdin.readline())
MAX = 0
lectures = []

for i in range(n):
    p, d = map(int,sys.stdin.readline().split())
    lectures.append((p,d))
    MAX = max(d,MAX)

lectures.sort(key = lambda x : (x[1],x[0]),reverse=True)

sum = 0
k = 0
h = []

for i in range(MAX,0,-1): # 해당 일안에만 해주면 되기 때문에 최대 일수부터 -1씩 하면서 구해주면 된다.
    while k < n and lectures[k][1] == i: # while문을 쓰는 이유는 같은 일수 d인 배열 값이 있을 수 있기 때문에
        heapq.heappush(h,-lectures[k][0])
        k += 1
    if h:
        sum += -heapq.heappop(h)
print(sum)