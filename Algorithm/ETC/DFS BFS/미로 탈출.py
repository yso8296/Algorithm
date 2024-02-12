from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  queue = deque([(x, y)])
  graph[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1

bfs(0, 0)
print(graph[n - 1][m - 1])
  
  