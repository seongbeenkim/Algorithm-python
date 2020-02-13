#https://www.acmicpc.net/problem/14889

import sys

n = int(sys.stdin.readline())
s = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
ans = 2147483647
for i in range(1 << ((n//2)-1) ,1<<n):
    start = []
    link = []
    for j in range(n):
        if i & (1 << j):
            start += [j]
        else:
            link += [j]

    if len(start) == len(link):
        start_sum = 0
        link_sum = 0

        for k in range(n//2):
            for l in range(k+1,n//2):
                if k == (n/2)-1 and l == (n//2)-1:
                    continue
                start_sum += s[start[k]][start[l]] + s[start[l]][start[k]]

                link_sum += s[link[k]][link[l]] + s[link[l]][link[k]]

                res = abs(start_sum - link_sum)
                if ans > res:
                    ans = res
print(res)