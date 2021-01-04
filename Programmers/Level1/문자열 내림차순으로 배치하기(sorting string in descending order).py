# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    s = list(s)
    lower = sorted(s, reverse=True)
    return "".join(lower)


print(solution("Zbcdefg"))
