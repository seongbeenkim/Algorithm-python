# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations


def solution(expression):
    answer = 0
    operand = ['+', '-', '*']
    op_candidate = set()
    temp = ''
    splited_expression = []

    for ch in expression:
        if ch in operand:
            op_candidate.add(ch)
            splited_expression.append(temp)
            splited_expression.append(ch)
            temp = ''
        else:
            temp += ch

    splited_expression.append(temp)
    ops = list(permutations(op_candidate))

    for priority in ops:
        temp = splited_expression.copy()
        for op in priority:
            count = temp.count(op)
            while count > 0:
                i = temp.index(op)
                temp[i - 1] = str(eval("".join(temp[i - 1:i + 2])))
                temp.pop(i)
                temp.pop(i)
                count -= 1
        answer = max(answer, abs(int(temp[0])))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
