from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
  s = input()
  graph.append(list(s))
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  if graph[x][y] == '1':
    return
  global result
  queue = deque([(x, y)])
  graph[x][y] = '1'

  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = int(a) + dx[i]
      ny = int(b) + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == '1':
        continue
      graph[nx][ny] = '1'
      queue.append((str(nx), str(ny)))

  result += 1

for i in range(n):
  for j in range(m):
    bfs(i, j)

print(result)