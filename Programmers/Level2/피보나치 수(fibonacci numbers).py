# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 2] + a[i - 1]
        a[i] %= 1234567
    return a[n]


print(solution(3))
print(solution(5))
