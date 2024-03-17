import heapq
n, m, r = map(int, input().split())
item = list(map(int, input().split()))
result = 0
INF = int(1e9)
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

for i in range(1, n + 1):
  sum = 0
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, i))
  distance[i] = 0
  while q:
    dist, d = heapq.heappop(q)
    if dist > distance[d]:
      continue
    for j in graph[d]:
      cost = dist + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost
        heapq.heappush(q, (cost, j[0]))
  for j in range(1, n + 1):
    if distance[j] <= m:
      sum += item[j - 1]
  result = max(result, sum)

print(result)

  