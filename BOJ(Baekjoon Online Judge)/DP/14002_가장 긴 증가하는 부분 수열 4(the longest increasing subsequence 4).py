#https://www.acmicpc.net/problem/14002
import sys

t = int(sys.stdin.readline())
d = [0] * (t+1)
v = [-1] * (t+1)
a = [0] + list(map(int,sys.stdin.readline().split()))
for i in range(1,t+1):
    d[i] = 1
    for j in range(1,i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j
ans = max(d)
p = [i for i,x in enumerate(d) if x == ans][0]
print(ans)
def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p],end=' ')
go(p)
