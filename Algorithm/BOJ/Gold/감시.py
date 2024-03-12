import copy
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
cctv = []
for i in range(n):
  for j in range(m):
    if 1 <= graph[i][j] <= 5:
      cctv.append((graph[i][j], i, j))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [3, 0]],
  [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]]
]
result = int(1e9)

def simulation(graph, c, x, y):
  for i in c:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        break
      if graph[nx][ny] == 6:
        break
      if graph[nx][ny] == 0:
        graph[nx][ny] = -1

def dfs(graph, count):
  global result
  if count == len(cctv):
    cnt = 0
    for i in range(n):
      for j in range(m):
        if graph[i][j] == 0:
          cnt += 1
    result = min(result, cnt)
    return
  
  temp = copy.deepcopy(graph)
  c, x, y = cctv[count]
  for d in dir[c]:
    simulation(temp, d, x, y)
    dfs(temp, count + 1)
    temp = copy.deepcopy(graph)

dfs(graph, 0)
print(result)

  
