# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = []

    for ch in s:
        if len(answer) == 0:
            answer.append(ch)
        elif answer[-1] != ch:
            answer.append(ch)
        else:
            answer.pop()

    if len(answer) == 0:
        return 1

    return 0


print(solution("baaabaa"))
print(solution("cdcd"))
