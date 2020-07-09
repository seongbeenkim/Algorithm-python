#https://www.acmicpc.net/problem/11655

import sys

s = sys.stdin.readline().rstrip()
ans = ""
for i in s:
    x = ord(i)
    if ord('a') <= x <= ord('z'):
        x += 13
        if x > ord('z'):
            x -= ord('z')
            x = x + ord('a') - 1
        ans += chr(x)
    elif ord('A') <= x <= ord('Z'):
        x += 13
        if x > ord('Z'):
            x -= ord('Z')
            x = x + ord('A') - 1
        ans += chr(x)
    else:
        ans += i
print(ans)