#https://www.acmicpc.net/problem/2343

import sys

n, m = map(int,sys.stdin.readline().split())

lessons = list(map(int,sys.stdin.readline().split()))

l = 1
r = sum(lessons)
ans = 2147483647

def check(mid):
    cnt = 1
    sum = lessons[0]

    for lesson in lessons[1:]:
        if mid < lesson:
            return False
        if sum + lesson <= mid:
            sum += lesson
        else:
            cnt += 1
            sum = lesson
    return cnt <= m # 꼭 m개여야 한다는 의미가 아니라 m개의 블루레이에 모든 동영상을 넣는 것이기 때문에 "<="

while l <= r:
    mid = (l+r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)

"""
n, m = map(int,sys.stdin.readline().split())

lessons = list(map(int,sys.stdin.readline().split()))
l = 0
for lesson in lessons:
    if l < lesson:
        l = lesson # 블루레이가 담을 수 있는 최소의 크기 찾기 
r = sum(lessons)
ans = 2147483647

def check(mid):
    cnt = 1
    sum = lessons[0]

    for lesson in lessons[1:]:
        if sum + lesson <= mid:
            sum += lesson
        else:
            cnt += 1
            sum = lesson
    return cnt <= m

while l <= r:
    mid = (l+r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
"""