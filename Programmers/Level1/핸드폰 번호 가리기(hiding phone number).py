# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    n = len(phone_number)

    for i in range(n - 4):
        answer += "*"

    answer += phone_number[-4:]
    return answer

print(solution("01033334444"))
print(solution("027778888"))
