#https://www.acmicpc.net/problem/1561

import sys

n, m = map(int,sys.stdin.readline().split())
ride = list(map(int,sys.stdin.readline().split()))

l = 1
r = n * max(ride)

time = 0

if n <= m:
    print(n)
    
else:

    while l <= r:
        mid = (l+r) // 2
        candi = [0] * (m + 1)

        cnt = m

        for i in range(m):
            cnt += mid//ride[i]

        if cnt >= n: # n명 이상을 태울 수 있는 경우도 정답이 될 수 있으니 ">="
            time = mid
            r = mid - 1
        else:
            l = mid + 1

    cnt = m

    for i in range(m):
        cnt += (time-1) // ride[i] # n명을 태우는 시간 1분 전 탑승 인원 구하기

    for i in range(m):
        if time % ride[i] == 0:
            cnt += 1
        if cnt == n:
            print(i+1)
            break