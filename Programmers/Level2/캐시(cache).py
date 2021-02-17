# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = []

    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.pop()
            answer += 5
        else:
            cache.pop(cache.index(city))
            answer += 1

        cache.insert(0, city)  # 가장 최근에 사용된 것을 맨 앞에 추가한다

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
