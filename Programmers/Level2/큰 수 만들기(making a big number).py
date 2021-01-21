# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []

    for i, num in enumerate(number):
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1

        if k == 0:
            answer += number[i:]
            break

        answer.append(num)

    if k > 0:
        answer = answer[:-k]

    return "".join(answer)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
