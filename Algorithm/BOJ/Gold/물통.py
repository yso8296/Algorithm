from collections import deque
a, b, c = map(int, input().split())
result = []
visited = [[0] * (b + 1) for _ in range(a + 1)]
q = deque()

def pour(x, y):
  if not visited[x][y]:
    visited[x][y] = 1
    q.append((x, y))
    

def bfs():
  q.append((0, 0))
  visited[0][0] = 1
  while q:
    x, y = q.popleft()
    z = c - x - y
    if x == 0:
      result.append(z)
    
    water = min(x, b - y)
    pour(x - water, y + water)
    water = min(x, c - z)
    pour(x - water, y)
    water = min(y, a - x)
    pour(x + water, y - water)
    water = min(y, c - z)
    pour(x, y - water)
    water = min(z, a - x)
    pour(x + water, y)
    water = min(z, b - y)
    pour(x, y + water)
    
bfs()
result.sort()
for i in result:
  print(i, end = " ")