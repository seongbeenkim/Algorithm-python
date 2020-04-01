#https://www.acmicpc.net/problem/1655

import sys, heapq

n = int(sys.stdin.readline())

l = []
r = []

for i in range(n):
    a = int(sys.stdin.readline())

    if len(l) == 0 or len(r) == 0:
        heapq.heappush(l,(-a,a))
    else:
        if a <= l[0][1]:
            heapq.heappush(l,(-a,a))
        elif a >= r[0][1]:
            heapq.heappush(r,(a,a))
        else:
            heapq.heappush(l,(-a, a))
    while not (len(l) == len(r) or len(l) == len(r)+1):
        if len(l) > len(r):
            to_min = heapq.heappop(l)[1]
            heapq.heappush(r,(to_min,to_min))
        else:
            to_max = heapq.heappop(r)[1]
            heapq.heappush(l, (-to_max, to_max))
    print(l[0][1])
