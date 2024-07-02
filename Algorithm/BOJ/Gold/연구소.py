from collections import deque
import copy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def make_wall(count):  # [1] 벽 세우기
  if count == 3:
    virus()
    return
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        board[i][j] = 1
        make_wall(count + 1)
        board[i][j] = 0


def virus():  # [2] 바이러스 전파
  global result
  temp = copy.deepcopy(board)
  q = deque()
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        q.append((i, j))
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if temp[nx][ny] != 0:
        continue
      temp[nx][ny] = 2
      q.append((nx, ny)) 
  
  result = max(result, calculate(temp))

def calculate(temp):  # [3] 안전 영역 계산
  count = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        count += 1
  return count

make_wall(0)

print(result)