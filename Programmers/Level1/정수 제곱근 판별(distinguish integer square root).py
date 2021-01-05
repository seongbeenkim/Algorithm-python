# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    i = 1

    while i * i <= n:
        if i * i == n:
            return (i + 1) * (i + 1)

        i += 1
    return -1

print(solution(121))
print(solution(3))
