#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    types = {}
    n = len(genres)

    for i in range(n):
        if genres[i] not in types:
            types[genres[i]] = 0
            types[genres[i]] += plays[i]
        else:
            types[genres[i]] += plays[i]

    t = sorted(types.items(), key=lambda x: x[1], reverse=True)

    for i in t:
        q = []
        for j in range(n):
            if genres[j] == i[0]:
                q.append((plays[j], j))
        q.sort(key=lambda x: (x[0], -x[1]))
        answer.append(q.pop()[1])
        if len(q) >= 1:
            answer.append(q.pop()[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))