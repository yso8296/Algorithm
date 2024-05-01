import heapq
t = int(input())
INF = int(1e9)

def dijkstra(distance, graph, start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  distance = [INF] * (n + 1)
  count = 0
  result = 0
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))
  dijkstra(distance, graph, c)
  for i in distance:
    if i != INF:
      count += 1
      result = max(result, i)
  print(count, result)

  

