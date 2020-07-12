#https://www.acmicpc.net/problem/1373

import sys
n = sys.stdin.readline().rstrip()
reverse_n = n[-1::-1]
x = 1
cnt = 1
num = 0
ans = []
for i in reverse_n:
    if i == '1':
        num = num + x*int(i)
    x *= 2
    cnt += 1
    if cnt == 4:
        cnt = 1
        x = 1
        ans.append(num)
        num = 0
if len(reverse_n) % 3 != 0:
    ans.append(num)
print(*ans[-1::-1], sep ="")

##print(oct(int(sys.stdin.readline().rstrip(),2))[2:])