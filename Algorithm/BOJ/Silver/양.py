from collections import deque
r, c = map(int, input().split())
sheep = 0
wolf = 0
graph = []
for _ in range(r):
  graph.append(list(input()))
for i in range(r):
  for j in range(c):
    if graph[i][j] == 'o':
      sheep += 1
    if graph[i][j] == 'v':
      wolf += 1
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def bfs(x, y):
  global sheep
  global wolf
  s = 0
  w = 0
  queue = deque()
  queue.append((x, y))
  if graph[x][y] == 'o':
    s += 1
  if graph[x][y] == 'v':
    w += 1
  graph[x][y] = '#'
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        continue
      if graph[nx][ny] == '#':
        continue
      if graph[nx][ny] == 'o':
        s += 1
      if graph[nx][ny] == 'v':
        w += 1
      graph[nx][ny] = '#'
      queue.append((nx, ny))
  if s > w:
    wolf -= w
  else:
    sheep -= s

for i in range(r):
  for j in range(c):
    if graph[i][j] != '#':
      bfs(i, j)

print(sheep, wolf)
      