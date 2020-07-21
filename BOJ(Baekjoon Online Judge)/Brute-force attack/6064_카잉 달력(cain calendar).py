#https://www.acmicpc.net/problem/6064

import sys

t = int(sys.stdin.readline())
for i in range(t):
    m,n,x,y = map(int,sys.stdin.readline().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)


"""
t = int(sys.stdin.readline())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a * b // gcd(a,b)

for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().split())
    i = 1
    j = 1
    cnt = 1
    max = lcm(m,n)

    while i != x:
        i += 1
        j += 1
        cnt += 1
        if j > n:
            j = 1

    while j != y:
        if cnt > max:
            break
        j = (j+m)%n
        if j == 0:
            j = n
        cnt += m

    if cnt > max:
        cnt = -1

    print(cnt)
"""