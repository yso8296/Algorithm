from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
visited = [([0] * n) for _ in range(n)]

def bfs(st, en): # 하루 동안의 인구 이동
  visited[st][en] = 1
  queue = deque()
  divide = [(st, en)]
  queue.append((st, en))
  sum = graph[st][en]
  num = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if visited[nx][ny] == 0 and abs(graph[x][y] - graph[nx][ny]) >= l and abs(graph[x][y] - graph[nx][ny]) <= r:
        sum += graph[nx][ny]
        num += 1
        visited[nx][ny] = 1
        queue.append((nx, ny))
        divide.append((nx, ny))
  result = int(sum / num)
  for x, y in divide:
    graph[x][y] = result

def population_move():
  count = 0
  while True:
    check = [arr[:] for arr in graph] # 인구 이동 여부
    check_count = 0
    for i in range(n):
      for j in range(n):
        if visited[i][j] == 0:
          bfs(i, j)
    for i in range(n):
      for j in range(n):
        if check[i][j] == graph[i][j]:
          check_count += 1
    if check_count == n * n:
      return count
    else:
      for i in range(n):
        for j in range(n):
          visited[i][j] = 0
      count += 1

print(population_move())
        

