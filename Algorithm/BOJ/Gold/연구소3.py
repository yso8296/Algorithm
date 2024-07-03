from collections import deque
import copy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
result = INF
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):    
  for j in range(n):
    if board[i][j] == 2:
      board[i][j] = '*'
    elif board[i][j] == 1:
      board[i][j] = '-'
    elif board[i][j] == 0:
      board[i][j] = -1

def virus(count):   # [1] 바이러스 m개 활성화
  global result
  if count == m:
    result = min(result, simulation())
    return
  
  for i in range(n):
    for j in range(n):
      if board[i][j] == '*':
        board[i][j] = 0
        virus(count + 1)
        board[i][j] = '*'

def simulation():   # [2] 시뮬레이션
  time = 0
  q = deque()
  temp = copy.deepcopy(board)
  for i in range(n):
    for j in range(n):
      if temp[i][j] == 0:
        q.append((i, j))
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if temp[nx][ny] == '-':
        continue
      if temp[nx][ny] == -1: 
        temp[nx][ny] = temp[x][y] + 1
        time = max(time, temp[nx][ny])
        q.append((nx, ny))
      elif temp[nx][ny] == '*':
        temp[nx][ny] = temp[x][y] + 1
        q.append((nx, ny))
  
  for i in range(n):
    for j in range(n):
      if temp[i][j] == -1:
        time = INF
        return time
  return time

virus(0)
if result == INF:
  print(-1)
else:
  print(result)