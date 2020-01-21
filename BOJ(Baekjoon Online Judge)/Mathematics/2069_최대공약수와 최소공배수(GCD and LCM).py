#https://www.acmicpc.net/problem/2069
import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a, b = list(map(int,sys.stdin.readline().rstrip().split()))
gcd = gcd(a,b)
print(gcd)
print(a*b//gcd)