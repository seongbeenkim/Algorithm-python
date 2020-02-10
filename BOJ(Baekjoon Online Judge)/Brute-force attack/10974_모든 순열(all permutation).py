#https://www.acmicpc.net/problem/10974
"""
import sys

n = int(sys.stdin.readline())
check = [False] * (n+1)

def go(index,a):
    if index == n:
        print(" ".join(a))
        return

    for i in range(1,n+1):
        if check[i] == True:
            continue
        check[i] = True
        go(index+1,a+str(i))
        check[i] = False

go(0,"")
"""
import sys

n = int(sys.stdin.readline())
a = list(range(1,n+1))

def go():
    i = n - 1

    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1

    while a[j] <= a[i-1]:
        j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    j = n - 1K
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1

    return True

while True:
    print(" ".join(map(str,a)))
    if not go():
        break