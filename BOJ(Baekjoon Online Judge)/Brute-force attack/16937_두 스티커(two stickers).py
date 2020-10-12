#https://www.acmicpc.net/problem/16937

import sys

h, w = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
sticker = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0

for i in range(n):
    r1 = sticker[i][0]
    c1 = sticker[i][1]
    for j in range(i+1,n):
        r2 = sticker[j][0]
        c2 = sticker[j][1]
        for f in range(2):
            for s in range(2):
                if r1 + r2 <= h and max(c1, c2) <= w:
                    temp = r1 * c1 + r2 * c2
                    if ans < temp:
                        ans = temp
                if max(r1, r2) <= h and c1 + c2 <= w:
                    temp = r1 * c1 + r2 * c2
                    if ans < temp:
                        ans = temp
                r2, c2 = c2, r2
            r1, c1 = c1, r1
print(ans)