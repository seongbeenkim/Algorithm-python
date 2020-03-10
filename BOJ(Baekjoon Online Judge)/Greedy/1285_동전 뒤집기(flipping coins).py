#https://www.acmicpc.net/problem/1285

import sys

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 401
for k in range(1<<n):
    sum = 0
    for j in range(n):
        cnt = 0
        for i in range(n):
            c = a[i][j]
            if (1<<i) & k:
                if c == "T":
                    c = "H"
                else:
                    c = "T"
            if c == "T":
                cnt += 1
        sum += min(n-cnt,cnt)
    if ans > sum:
        ans = sum
print(ans)