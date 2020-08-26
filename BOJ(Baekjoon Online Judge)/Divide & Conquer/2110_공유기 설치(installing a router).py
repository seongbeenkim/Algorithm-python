#https://www.acmicpc.net/problem/2110

import sys

n, c = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

start = 1
end = max(house)
ans = 0

def check(distance):
    cnt = 1
    install = house[0]

    for i in range(1,len(house)):
        if install + distance <= house[i]:
            cnt += 1
            install = house[i]
    return cnt >= c

while start <= end:
    mid = (start+end) // 2
    if check(mid):
        ans = max(mid,ans)
        start = mid + 1
    else:
        end = mid - 1

print(ans)