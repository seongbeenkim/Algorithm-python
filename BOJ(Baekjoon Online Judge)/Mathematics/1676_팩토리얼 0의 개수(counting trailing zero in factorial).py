#https://www.acmicpc.net/problem/1676

import sys

count = 0
num = int(sys.stdin.readline())
i = 5
while num >= i:
    count += num // i
    i *= 5
print(count)