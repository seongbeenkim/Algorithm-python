#https://www.acmicpc.net/problem/1931

import sys

n = int(sys.stdin.readline())
meeting = []
for i in range(n):
    meeting.append(list(map(int,sys.stdin.readline().split())))

meeting.sort(key=lambda x: (x[1],x[0]))

cnt = 0
end = 0
for m in meeting:
    if end <= m[0]:
        cnt += 1
        end = m[1]
print(cnt)