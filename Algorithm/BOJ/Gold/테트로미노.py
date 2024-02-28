n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def dfs(x, y, score, count):
  global result
  if count == 4:
    result = max(score, result)
    return
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if visited[nx][ny]:
      continue
    visited[nx][ny] = 1
    dfs(nx, ny, score + graph[nx][ny], count + 1)
    visited[nx][ny] = 0

def exce(x, y):
  global result
  for i in range(4):
    temp = graph[x][y]
    for j in range(3):
      t = (i + j) % 4
      nx = x + dx[t]
      ny = y + dy[t]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        break
      temp += graph[nx][ny]
    
    result = max(result, temp)

for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, graph[i][j], 1)
    visited[i][j] = 0
    exce(i, j)

print(result)