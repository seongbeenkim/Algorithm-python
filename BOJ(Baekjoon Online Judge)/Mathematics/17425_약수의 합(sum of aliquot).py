#https://www.acmicpc.net/problem/17425

import sys

max = 1000000
d = [0] * (max+1) # index : 0 ~ max
s = [0] * (max+1)

for i in range(1,max+1): # index : 1 ~ max
    j = 1
    while i*j <= max:
        d[i*j] += i
        j += 1

for i in range(1,max+1):
    s[i] = s[i-1] + d[i]

num = int(sys.stdin.readline())
for i in range(num):
    n = int(sys.stdin.readline())
    print(s[n])
