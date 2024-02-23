from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == '1':
        continue
      graph[nx][ny] = '1'
      queue.append((nx, ny))

count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == '0':
      bfs(i, j)
      count += 1

print(count)
  
