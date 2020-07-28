#https://www.acmicpc.net/problem/2529

import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
k = sys.stdin.readline().rstrip().split(" ")
ans = []
check = [False] * 10
def go(index,num):
    if index == n+1:
        for i in range(n):
            if k[i] == "<":
                if num[i] > num[i+1]:
                    return
            else:
                if num[i] < num[i+1]:
                    return
        ans.append(num)

    for i in range(10):
        if check[i] == True:
            continue
        check[i] = True
        go(index+1,num+str(i))
        check[i] = False
go(0,"")
ans.sort()
print(ans[-1] + "\n" + ans[0])

"""
n = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())
ans = []
def go(index,num,candi):
    if len(candi) == n+1:
        ans.append(candi)
        return
    if index >= n:
        return
    for i in range(10):
        if str(i) not in candi:
            if a[index] == "<" and num < i:
                go(index+1,i,candi+str(i))
            elif a[index] == ">" and num > i:
                go(index + 1, i, candi + str(i))

for i in range(10):
    go(0,i,str(i))

print(ans[-1],ans[0],sep="\n")
"""

"""
n = int(sys.stdin.readline())
op = sys.stdin.readline().split()
check = [False] * 10
ans = []

def go(index,candi,op):
    global ans
    if index == len(op) + 1:
        if len(candi) == len(op) + 1:
            for i in range(len(op)):
                if op[i] == "<":
                    if not (candi[i] < candi[i+1]):
                        return
                else:
                    if not (candi[i] > candi[i+1]):
                        return
            ans.append(candi)
        return

    for i in range(10):
        if check[i]:
            continue
        if index == 0:
            check[i] = True
            go(index+1,candi+str(i),op)
            check[i] = False
        else:
            if op[index-1] == "<" and int(candi[index-1]) < i:
                check[i] = True
                go(index + 1, candi + str(i), op)
                check[i] = False
            elif op[index-1] == ">" and int(candi[index-1]) > i:
                check[i] = True
                go(index + 1, candi + str(i), op)
                check[i] = False

go(0,"",op)
print(ans[-1],ans[0],sep='\n')
"""