import heapq
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

def dijkstra(count):
  q = []
  heapq.heappush(q, (graph[0][0], 0, 0))
  distance[0][0] = graph[0][0]
  while q:
    cost, x, y = heapq.heappop(q)
    if cost > distance[x][y]:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      new_cost = cost + graph[nx][ny]
      if new_cost < distance[nx][ny]:
        distance[nx][ny] = new_cost
        heapq.heappush(q, (new_cost, nx, ny))
  print(f'Problem {count}: {distance[n - 1][n - 1]}')

while True:
  n = int(input())
  if n == 0:
    break
  count += 1
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  distance = [[INF] * n for _ in range(n)]
  dijkstra(count)