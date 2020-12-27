#https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

first_student = [1, 2, 3, 4, 5]
second_student = [2, 1, 2, 3, 2, 4, 2, 5]
third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    n = len(answers)
    first_count = 0
    second_count = 0
    third_count = 0

    for i in range(n):
        if first_student[i % len(first_student)] == answers[i]:
            first_count += 1
        if second_student[i % len(second_student)] == answers[i]:
            second_count += 1
        if third_student[i % len(third_student)] == answers[i]:
            third_count += 1

    temp = [first_count, second_count, third_count]

    for index, value in enumerate(temp):
        if value == max(temp):
            answer.append(index+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))