from collections import deque
r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robot_x = []
for i in range(r):
  for j in range(c):
    if board[i][j] == -1:
      robot_x.append(i)

def spread():
  q = deque()
  for i in range(r):  # 값 계산
    for j in range(c):
      if board[i][j] > 0:
        div = int(board[i][j] / 5)
        count = 0
        if div > 0:
          for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
              continue
            if board[nx][ny] == -1:
              continue
            count += 1
            q.append((nx, ny, div)) # 큐에 집어넣기
        board[i][j] -= (div * count)
  for x, y, z in q:
    board[x][y] += z
    
def clean():
  global board
  temp = [[0] * c for _ in range(r)]
  x = robot_x[0]
  for i in range(1, c - 1): # 위쪽부터 동
    temp[x][i + 1] = board[x][i]
  for i in range(x, 0, -1): # 북
    temp[i - 1][c - 1] = board[i][c - 1]
  for i in range(c - 1, 0, -1): # 서
    temp[0][i - 1] = board[0][i]    
  for i in range(0, x): # 남
    temp[i + 1][0] = board[i][0]
  temp[x][0] = -1
  for i in range(1, x):
    for j in range(1, c - 1):
      temp[i][j] = board[i][j]

  x = robot_x[1]
  for i in range(1, c - 1): # 동
    temp[x][i + 1] = board[x][i]
  for i in range(x, r - 1): # 남
    temp[i + 1][c - 1] = board[i][c - 1]
  for i in range(c - 1, 0, -1): # 서
    temp[r - 1][i - 1] = board[r - 1][i]
  for i in range(r - 1, x, -1): # 북
    temp[i - 1][0] = board[i][0]
  temp[x][0] = -1
  for i in range(x + 1, r - 1):
    for j in range(1, c - 1):
      temp[i][j] = board[i][j]
  board = [arr[:] for arr in temp]

for _ in range(t):
  spread()
  clean()

result = 0
for i in range(r):
  for j in range(c):
    if board[i][j] > 0:
      result += board[i][j]

print(result)


