from collections import deque

# BFS 함수 정의
def bfs(start, festival, stores):
    queue = deque([start])
    visited = [False] * (len(stores) + 2)
    visited[0] = True

    while queue:
        current_pos = queue.popleft()

        # 현재 위치에서 페스티벌까지 갈 수 있는지 확인
        if abs(current_pos[0] - festival[0]) + abs(current_pos[1] - festival[1]) <= 1000:
            return "happy"

        # 모든 편의점에 대해 탐색
        for i, store in enumerate(stores, start=1):
            if not visited[i]:
                if abs(current_pos[0] - store[0]) + abs(current_pos[1] - store[1]) <= 1000:
                    queue.append(store)
                    visited[i] = True
    return "sad"

# 입력 받기
t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    n = int(input()) # 편의점의 개수
    home = tuple(map(int, input().split())) # 상근이의 집
    stores = [tuple(map(int, input().split())) for _ in range(n)] # 편의점들
    festival = tuple(map(int, input().split())) # 페스티벌 위치

    # BFS 탐색 후 결과 출력
    print(bfs(home, festival, stores))
