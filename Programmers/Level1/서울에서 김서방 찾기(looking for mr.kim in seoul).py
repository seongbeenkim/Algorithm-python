# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = "김서방은 {}에 있다"

    for i, name in enumerate(seoul):
        if name != "Kim":
            continue
        return answer.format(i)


print(solution(["Jane", "Kim"]))
