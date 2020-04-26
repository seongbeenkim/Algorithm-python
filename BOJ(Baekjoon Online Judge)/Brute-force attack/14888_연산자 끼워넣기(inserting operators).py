#https://www.acmicpc.net/problem/14888

import sys

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i] <= a[i-1]:
        i-=1
    if i == 0:
        return False
    j = len(a)-1
    while a[i-1] >= a[j]:
        j-=1
    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i<j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return True

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
operand = []

for i,x in enumerate(op):
    for _ in range(x):
        operand.append(i)
operand.sort()

def calc(a,operand):
    res = a[0]
    for i in range(n-1):
        if operand[i] == 0:
            res = res + a[i+1]
        elif operand[i] == 1:
            res = res - a[i+1]
        elif operand[i] == 2:
            res = res * a[i + 1]
        else:
            if res < 0:
                res = -(abs(res) // a[i+1])
            else:
                res = res // a[i + 1]
    return res

ans = []

while True:
    res = calc(a,operand)
    ans.append(res)
    if not next_permutation(operand):
        break
ans.sort()
print(ans[-1])
print(ans[0])

"""
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = (map(int,sys.stdin.readline().split()))

ans = []
def go(i, total, plus, minus, mul, div):
    if i == n:
        ans.append(total)
        return
    if plus > 0:
         go(i+1,total+a[i], plus-1, minus, mul, div)
    if minus > 0:
        go(i+1,total-a[i], plus, minus-1, mul, div)
    if mul > 0:
        go(i+1,total*a[i], plus, minus, mul-1, div)
    if div > 0:
        if total >= 0:
            go(i+1,total//a[i], plus, minus, mul, div-1)
        else:
            go(i+1,-(abs(total)//a[i]), plus, minus, mul, div-1)
go(1,a[0],plus,minus,mul,div)
ans.sort()
print(ans[-1])
print(ans[0])
"""