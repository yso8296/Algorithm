import heapq
m, n = map(int, input().split())
INF = int(1e9)
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
distance = [[INF] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
  distance[0][0] = 0
  q = []
  heapq.heappush(q, (0, 0, 0))
  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      cost = dist + graph[nx][ny]
      if  cost < distance[nx][ny]:
        heapq.heappush(q, (cost, nx, ny))
        distance[nx][ny] = cost

dijkstra()
print(distance[n - 1][m - 1])