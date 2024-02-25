n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1
a, b = map(int, input().split())
for i in range(n):
  for j in range(n):
    if i == j:
      graph[i][j] = 0

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][b] + graph[b][a]
if result >= INF:
  print(-1)
else:
  print(result)