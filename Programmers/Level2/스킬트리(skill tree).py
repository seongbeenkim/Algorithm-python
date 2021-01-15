# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        i = ''
        is_wrong = False
        for j in skill_tree:
            if j in skill:
                if i == '':
                    if skill.find(j) != 0:
                        is_wrong = True
                        break
                    i = j
                else:
                    previous = skill.find(i)
                    current = skill.find(j)
                    if previous > current:
                        is_wrong = True
                        break
                    if abs(previous - current) > 1:
                        is_wrong = True
                        break
                    i = j

        if not is_wrong:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
