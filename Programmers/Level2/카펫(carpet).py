# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    s = brown + yellow
    for j in range(s, 2, -1):
        if s % j == 0:
            i = s // j
            if yellow == (j - 2) * (i - 2):
                return [j, i]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
