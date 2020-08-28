#https://www.acmicpc.net/problem/1300

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

l = 1
r = n*n
ans = 0

while l <= r:
    mid = (l+r) // 2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    print(l,mid,r,cnt)
    if cnt == k:
        ans = mid
        r = mid - 1
    elif cnt > k: # ans = mid를 해주는 이유는 한 수가 여러 개 있으면 cnt > k 라도 우리가 찾는 값일 수 있기 때문이다.
        ans = mid # 그리고 mid 값이 배열안에 존재하지 않을 수도 있는데 이러한 경우를 대비해서도 ans = mid를 해준다.
        r = mid - 1
    else:
        l = mid + 1

print(ans)