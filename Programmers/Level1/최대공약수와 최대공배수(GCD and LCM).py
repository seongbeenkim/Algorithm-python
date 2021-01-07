# https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]


# 1, 3 / 1, 2, 3, 4, 6 ,12
# 1, 2 / 1, 5
print(solution(3, 12))
print(solution(2, 5))
