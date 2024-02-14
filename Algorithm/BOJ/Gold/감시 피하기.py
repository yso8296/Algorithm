from collections import deque
n = int(input())
graph = []
for _ in range(n):
  graph.append(list(input().split()))
check = False

def make_object(count): #1 장애물 세우기
  global check
  if count == 3:
    if simulation():
      check = True
      return
    return
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        make_object(count + 1)
        graph[i][j] = 'X'

def simulation():
  queue = deque()
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'T':
        queue.append((i, j))
  while queue: # 북 동 남 서 탐색
    x, y = queue.popleft()
    for nx in range(x - 1, -1, -1): # 북
      if graph[nx][y] == 'O':
        break
      if graph[nx][y] == 'S':
        return False
    for ny in range(y + 1, n): # 동
      if graph[x][ny] == 'O':
        break
      if graph[x][ny] == 'S':
        return False
    for nx in range(x + 1, n): # 남
      if graph[nx][y] == 'O':
        break
      if graph[nx][y] == 'S':
        return False
    for ny in range(y - 1, -1, -1): # 서
      if graph[x][ny] == 'O':
        break
      if graph[x][ny] == 'S':
        return False
  return True
      
make_object(0)
if check:
  print("YES")
else:
  print("NO")
  
  