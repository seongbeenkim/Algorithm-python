#https://www.acmicpc.net/problem/1978

import sys

def check_prime(num):
    if num < 2:
          return 0
    j = 2
    while j*j <= num:
        if num % j == 0:
            return 0
        else:
            j += 1
    return 1


num = int(sys.stdin.readline())
cnt = 0
prime = list(map(int,sys.stdin.readline().split()))
for i in prime:
    cnt += check_prime(i)
print(cnt)