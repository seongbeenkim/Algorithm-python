#https://www.acmicpc.net/problem/1934
import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

num = int(sys.stdin.readline())

for i in range(num):
    a, b = list(map(int,sys.stdin.readline().rstrip().split()))
    g = gcd(a,b)
    print(a*b//g)