#https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = sorted(list(str(n)), reverse=True)
    return int("".join(answer))

print(solution(118372))