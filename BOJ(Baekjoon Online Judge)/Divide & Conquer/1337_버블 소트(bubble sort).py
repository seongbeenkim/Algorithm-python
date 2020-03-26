#https://www.acmicpc.net/problem/1377

import sys
read = lambda : sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

a = []
n = int(read())
for i in range(n):
    a.append((int(read()), i))
a.sort()

ans = []
for i in range(n):
    ans.append(a[i][1] - i)
write(max(ans)+1)
