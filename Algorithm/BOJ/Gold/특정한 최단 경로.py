import heapq
INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
one, two = map(int, input().split())

def dijkstra(start):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

v = dijkstra(1)
v1 = dijkstra(one)
v2 = dijkstra(two)

result = min(v[one] + v1[two] + v2[n], v[two] + v2[one] + v1[n])
if result >= INF:
  print(-1)
else:
  print(result)
  