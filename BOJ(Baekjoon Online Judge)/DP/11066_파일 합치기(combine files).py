#https://www.acmicpc.net/problem/11066
#https://mm5-gnap.tistory.com/64
#https://aerocode.net/109
import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())

def go(x,y):
    if x == y:
        return 0
    if d[x][y] != -1:
        return d[x][y]
    ans = d[x][y]
    cost = sum(a[x:y+1])
    for k in range(x,y):
        temp = go(x,k) + go(k+1,y) + cost
        if ans == -1 or ans > temp:
            ans = temp
    d[x][y] = ans
    return ans

for _ in range(t):
    n = int(sys.stdin.readline())
    a = [0] + list(map(int,sys.stdin.readline().split()))
    d = [[-1] * (n+1) for _ in range(n+1)]
    print(go(1,n))