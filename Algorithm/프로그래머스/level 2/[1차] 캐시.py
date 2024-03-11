from collections import deque

def solution(cacheSize, cities):
    result = 0
    q = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        if city.lower() in q:
            q.append(city.lower())
            q.remove(city.lower())
            result += 1
        else:
            if len(q) < cacheSize:
                q.append(city.lower())
                result += 5
            else:
                q.popleft()
                q.append(city.lower())
                result += 5
    return result