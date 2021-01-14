# https://programmers.co.kr/learn/courses/30/lessons/62048


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


print(solution(8, 12))
