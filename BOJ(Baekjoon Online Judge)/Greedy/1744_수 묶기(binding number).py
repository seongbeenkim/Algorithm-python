#https://www.acmicpc.net/problem/1744

import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort(reverse=True)
init = 10001
ans = 0
cnt = 0
x = init
y = init
is_minus = False
for i in range(len(a)):
    if a[i] <= 0:
        is_minus = True
        break
    elif a[i] > 0:
        if x == init:
            x = a[i]
        else:
            y = a[i]
        cnt += 1
        if cnt == 2:
            if x == 1 or y == 1: # 2개가 골라졌는데 하나라도 1이면 곱하는 것보다 더하는 것이 이득이다.
                ans += x+y
            else:
                ans += (x*y)
            x = init
            y = init
            cnt = 0

if x != init:
    ans += x

if is_minus: # 0이하의 값이 존재할 경우
    x = init
    y = init
    b = a[i:] # a가 내림차순으로 정렬되어있기 때문에
    b.sort() # 음수의 절대값이 큰 순으로 정렬하기 위해서 오름차순으로 다시 정렬해준다.
    cnt = 0
    for j in range(len(b)):
        if x == init:
            x = b[j]
        else:
            y = b[j]
        cnt += 1
        if cnt == 2:
            ans += (x * y)
            x = init
            y = init
            cnt = 0

    if x != init:
        ans += x
print(ans)