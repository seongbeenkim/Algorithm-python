#https://www.acmicpc.net/problem/1037

import sys

num = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
print(min(a)*max(a))