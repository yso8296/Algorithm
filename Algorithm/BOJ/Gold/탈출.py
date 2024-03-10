from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))
visited_water = [[int(1e9)] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cur_x, cur_y = 0, 0 # 고슴도치 위치
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'D':
      visited_water[i][j] = int(1e9)
    if graph[i][j] == 'S':
      cur_x, cur_y = i, j
    if graph[i][j] == '*':
      visited_water[i][j] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def water_bfs():
  q = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == '*':
        q.append((i, j))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if visited_water[nx][ny] != int(1e9) or graph[nx][ny] == 'D' or graph[nx][ny] == 'X':
        continue
      visited_water[nx][ny] = visited_water[x][y] + 1
      q.append((nx, ny))

def bfs(cur_x, cur_y):
  q = deque()
  q.append((cur_x, cur_y))
  visited[cur_x][cur_y] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if  visited[nx][ny] > 0 or visited_water[nx][ny] <= visited[x][y] + 1 or graph[nx][ny] == 'X':
        continue
      if graph[nx][ny] == 'D':
        return visited[x][y]
      visited[nx][ny] = visited[x][y] + 1
      q.append((nx, ny))
  return "KAKTUS"

water_bfs()
print(bfs(cur_x, cur_y))