#https://www.welcomekakao.com/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    citations.sort()
    n = len(citations)

    for i in range(n):
        cnt = n - i
        nth = citations[i]

        if cnt <= nth and n - cnt <= cnt:
            answer = max(cnt, answer)

    return answer

print(solution([3, 0, 6, 1, 5]))