#https://www.acmicpc.net/problem/1541

import sys

a = sys.stdin.readline().rstrip()

ans = 0
temp = ''
is_minus = False

for i in range(len(a)):
    if '0' <= a[i] <= '9':
        temp += a[i]

    else:
        if a[i] == '+':
            if is_minus:
                ans -= int(temp)
            else:
                ans += int(temp)
            temp = ''
        else:
            if not is_minus:
                ans += int(temp)
            else:
                ans -= int(temp)
            temp = ''
            is_minus = True
if is_minus:
    ans -= int(temp)
else:
    ans += int(temp)
print(ans)
