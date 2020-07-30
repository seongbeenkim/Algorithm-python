#https://www.acmicpc.net/problem/14391

import sys

n,m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
ans = 0
for s in range(1<<n*m):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if (s&(1<<k)) == 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i * m + j
            if (s & (1 << k)) != 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(sum,ans)
print(ans)


"""
n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 0
s = [[0] * m for _ in range(n)]

def count():
    total = 0

    # 가로 계산
    i = 0
    while i<n:
        j = 0
        temp = ''
        while j < m:
            if s[i][j] == 0:
                temp += a[i][j]
            else:
                if len(temp) > 0:
                    total += int(temp)
                    temp = ''
            j+=1
        if len(temp) > 0:
            total += int(temp)
        i+=1
    # 세로 계산
    j = 0
    while j < m:
        i = 0
        temp = ''
        while i < n:
            if s[i][j] == 1:
                temp += a[i][j]
            else:
                if len(temp) > 0:
                    total += int(temp)
                    temp = ''
            i+=1
        if len(temp) > 0:
            total += int(temp)
        j+=1

    return total


for k in range(0,1<<(n*m)):
    for i in range(n):
        cnt = 0
        for j in range(i*m,(i*m)+m):
            if k & (1<<j):
                s[i][cnt] = 1
            else:
                s[i][cnt] = 0
            cnt += 1
    ans = max(ans,count())
print(ans)
"""