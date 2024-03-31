n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
  a, b, c = map(int, input().split())
  if graph[a - 1][b - 1] <= c:
    print("Enjoy other party")
  else:
    print("Stay here")