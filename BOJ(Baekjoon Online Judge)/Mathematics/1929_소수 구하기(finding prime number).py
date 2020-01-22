#https://www.acmicpc.net/problem/1929

import sys

a, b = list(map(int,sys.stdin.readline().rstrip().split()))
prime = []
is_prime = [False] * (b+1)

if a == 1:
    is_prime[a] = True
    a = 2

for i in range(2,a):
    if is_prime[i] == False:
        is_prime[i] = True
        j = 2*i
        while j <= b :
            is_prime[j] = True
            j += i

for i in range(a,b+1):
    if is_prime[i] == False:
        prime.append(i)
        print(i)
        is_prime[i] = True
        j = 2*i
        while j <= b:
            is_prime[j] = True
            j += i