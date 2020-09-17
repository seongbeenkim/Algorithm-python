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

"""
class sets():
    def __init__(self):
        self.s = 0
    def add(self,x):
        self.s = (self.s | (1<<x))
    def remove(self,x):
        self.s = (self.s & ~(1<<x))
    def check(self,x):
        if self.s & (1<<x):
            print(1)
        else:
            print(0)
    def toggle(self,x):
        self.s = (self.s ^ (1<<x))
    def all(self):
        self.s = (1<<21)-1
    def empty(self):
        self.s = 0

n = int(sys.stdin.readline())
s = sets()
for i in range(n):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0])
    if op == "add":
        s.add(x)
    elif op == "remove":
        s.remove(x)
    elif op == "check":
        s.check(x)
    elif op == "toggle":
        s.toggle(x)
    elif op == "all":
        s.all()
    else:
        s.empty()

"""