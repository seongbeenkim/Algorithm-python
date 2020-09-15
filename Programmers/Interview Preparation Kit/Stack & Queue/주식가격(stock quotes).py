#https://www.welcomekakao.com/learn/courses/30/lessons/42584

def solution(prices):
    n = len(prices)
    answer = [0] * n
    s = []
    s.append((0, prices[0]))

    for i in range(1, n - 1):
        if s[-1][1] <= prices[i]:
            s.append((i, prices[i]))
        else:
            while len(s) > 0 and s[-1][1] > prices[i]:
                idx, price = s.pop()
                answer[idx] = i - idx
            s.append((i, prices[i]))

    for idx, price in s:
        answer[idx] = n - 1 - idx
    return answer

print(solution([1, 2, 3, 2, 3]))