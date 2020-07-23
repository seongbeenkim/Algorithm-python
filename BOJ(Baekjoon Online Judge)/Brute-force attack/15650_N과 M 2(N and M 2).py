#https://www.acmicpc.net/problem/15650
import sys

n, m = map(int,sys.stdin.readline().split())
ans = [0] * m

def go(index,n,m,l):
    if index == m:
        sys.stdout.write(" ".join(map(str,ans)) + "\n")
        return
    for i in range(l+1,n+1):
        ans[index] = i
        go(index+1,n,m,ans[index])
go(0,n,m,0)

"""
n, m = map(int,sys.stdin.readline().split())

def go(index,candi):

    if len(candi) == m:
        print(*candi)
        return

    for i in range(1,n+1):
        if i not in candi:
            is_bigger = True
            for j in candi:
                if i <= j:
                    is_bigger = False
                    break
            if not is_bigger:
                continue
            go(index,candi+[i])

for i in range(1,n+1):
    go(i,[i])
"""