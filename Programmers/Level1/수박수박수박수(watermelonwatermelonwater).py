#https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    if n % 2 == 0:
        answer += "수박" * (n // 2)
    else:
        answer += ("수박" * (n // 2)) + "수"
    return answer

print(solution(3))
print(solution(4))