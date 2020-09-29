#https://www.acmicpc.net/problem/2751

import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
print(*a, sep = '\n')