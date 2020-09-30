#https://www.acmicpc.net/problem/16917

import sys


a, b, c, x, y = map(int,sys.stdin.readline().split())
answer = 5000 * 200000

answer = 0

if (a+b) >= (c*2) and (x>1 and y>1):
    while x > 0 and y > 0:
        answer += c*2
        x-=1
        y-=1
while x > 0:
    if a>= c*2:
        answer += c*2
    else:
        answer += a
    x -= 1
while y > 0:
    if b >= c * 2:
        answer += c * 2
    else:
        answer += b
    y -= 1
print(answer)