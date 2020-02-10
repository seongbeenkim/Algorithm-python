#https://www.acmicpc.net/problem/11723

import sys

n = int(sys.stdin.readline())
s = 0
for i in range(n):
    op, *x = sys.stdin.readline().split()
    if len(x) > 0:
        x = int(x[0])-1
    if op == "add":
        s = (s | (1<<x))
    elif op == "remove":
        s = (s & ~(1<<x))
    elif op == "check":
        res = (s & (1 << x))
        if res > 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif op == "toggle":
        s = (s ^ (1 << x))
    elif op == "all":
        s = (1 << 20) - 1
    else:
        s = 0