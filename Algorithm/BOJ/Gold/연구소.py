import copy
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
result = 0
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

#1 벽 세우기
def make_wall(count):
  if count == 3:
    virus()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        make_wall(count + 1)
        graph[i][j] = 0  

#2 바이러스 전파
def virus():
  temp = copy.deepcopy(graph)
  queue = deque()
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if temp[nx][ny] > 0:
        continue
      temp[nx][ny] = 2
      queue.append((nx, ny))
  
  calculate(temp)

#3 안전 영역 크기 계산
def calculate(temp):
  global result
  count = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        count += 1
  result = max(result, count)

make_wall(0)
print(result)