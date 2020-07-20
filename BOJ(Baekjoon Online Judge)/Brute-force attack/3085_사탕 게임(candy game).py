#https://www.acmicpc.net/problem/3085

import sys

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = 0

def check(a):
    ans = 1
    for i in range(n):
        for j in range(n):
            cnt = 1
            k = j
            while k+1 < n and a[i][k] == a[i][k+1]:
                cnt += 1
                k+=1
            ans = max(cnt,ans)

    for j in range(n):
        for i in range(n):
            cnt = 1
            k = i
            while k+1 < n and a[k][j] == a[k+1][j]:
                cnt += 1
                k+=1
            ans = max(cnt,ans)
    return ans

"""
def check(a):
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(cnt,ans)

        cnt = 1
        for j in range(1,n):
            if a[j][i] == a[j-1][i]:
                cnt +=1
            else:
                cnt = 1
            ans = max(cnt,ans)
    return ans
"""


for i in range(n):
    for j in range(n):
        if j+1 < n and a[i][j] != a[i][j+1]:
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            ans = max(ans,check(a))
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        if i+1 < n and a[i][j] != a[i+1][j]:
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
            ans = max(ans,check(a))
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
print(ans)