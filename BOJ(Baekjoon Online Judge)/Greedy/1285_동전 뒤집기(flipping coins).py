#https://www.acmicpc.net/problem/1285

import sys

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 401
for k in range(1<<n): # 모든 행을 뒤집는 것에 대한 모든 경우의 수 = 2^n
    sum = 0
    for j in range(n): # 열
        cnt = 0
        for i in range(n): # 행
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