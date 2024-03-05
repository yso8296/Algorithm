v, e = map(int, input().split())
INF = int(1e9)
result = INF
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a][b] = c
for i in range(1, v + 1):
  for j in range(1, v + 1):
    if i == j:
      graph[i][j] = 0

for k in range(1, v + 1):
  for i in range(1, v + 1):
    for j in range(1, v + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, v + 1):
  for j in range(i, v + 1):
    if i == j:
      continue
    result = min(result, graph[i][j] + graph[j][i])

if result == INF:
  print(-1)
else:
  print(result)

