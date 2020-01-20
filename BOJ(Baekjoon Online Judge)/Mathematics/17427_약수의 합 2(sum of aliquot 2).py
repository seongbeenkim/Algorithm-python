#https://www.acmicpc.net/problem/17427

import sys

num = int(sys.stdin.readline().rstrip())
sum = 0
for i in range(1,num+1):
    sum += (num//i) * i
print(sum)