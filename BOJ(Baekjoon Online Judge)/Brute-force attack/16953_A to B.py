#https://www.acmicpc.net/problem/16953

import sys

a, b = map(int,sys.stdin.readline().split())

def go(now, cnt):

    if now > b:
        return -1
    if now == b:
        return cnt

    multi_result = go(now * 2, cnt + 1)
    if multi_result != -1:
        return multi_result

    plus_result = go(now * 10 + 1, cnt + 1)
    if plus_result != -1:
        return plus_result

    return -1

res = go(a, 0)
if res != -1:
    res += 1
print(res)