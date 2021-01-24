# https://programmers.co.kr/learn/courses/30/lessons/60058

def divide(w):
    l = 0
    r = 0

    for i in range(len(w)):
        if w[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return w[:i + 1], w[i + 1:]


def isBalanced(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True


def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if isBalanced(u):
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
