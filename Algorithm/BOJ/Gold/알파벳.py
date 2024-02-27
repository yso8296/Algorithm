import sys
n, m = map(int, input().split())
alp = set()
graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().strip()))
result = 0
alp.add(graph[0][0])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(num, x, y):
  global result
  result = max(result, num)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] in alp:
      continue
    alp.add(graph[nx][ny])
    dfs(num + 1, nx, ny)
    alp.remove(graph[nx][ny])

dfs(1, 0, 0)
print(result)
