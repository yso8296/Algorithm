n, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def bfs():
  queue = []
  for i in range(n):
    for j in range(n):
      if graph[i][j] > 0:
        queue.append((graph[i][j], i, j, 0))
  queue.sort()

  while queue:
    num, x, y, z = queue.pop(0)
    if z == s:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] > 0:
        continue
      graph[nx][ny] = graph[x][y]
      queue.append((num, nx, ny, z + 1))
    
bfs()
print(graph[x - 1][y - 1])