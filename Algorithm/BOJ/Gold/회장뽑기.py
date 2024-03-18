n = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
array = []
result = INF
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0
while True:
  a, b = map(int, input().split())
  if a == -1 and b == -1:
    break
  graph[a][b] = 1
  graph[b][a] = 1
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(1, n + 1):
  score = 0
  count = 0
  for j in range(1, n + 1):
    if graph[i][j] != INF:
      score = max(score, graph[i][j])
      count += 1
    if count == n:
      result = min(result, score)

for i in range(1, n + 1):
  score = 0
  count = 0
  for j in range(1, n + 1):
    if graph[i][j] != INF:
      score = max(score, graph[i][j])
      count += 1
  if score == result and count == n:
    array.append(i)

print(result, len(array))
for i in array:
  print(i, end=" ")