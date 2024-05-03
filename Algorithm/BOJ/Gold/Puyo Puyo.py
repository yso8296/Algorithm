from collections import deque
n = 12
m = 6
board = []
for _ in range(n):
  board.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
result = 0

def bfs(cur_x, cur_y, color):
  q = deque()
  q.append((cur_x, cur_y))
  count = 1
  temp = deque()
  temp.append((cur_x, cur_y))

  while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if board[nx][ny] == '.' or visited[nx][ny]:
        continue
      if board[nx][ny] == color:
        count += 1
        q.append((nx, ny))
        temp.append((nx, ny))
  if count >= 4:
    for x, y in temp:
      board[x][y] = '.'
    return 1
  return 0

def down():
  for i in range(n - 2, -1, -1):
    for j in range(m):
      if board[i][j] != '.':
        idx = i + 1
        color = board[i][j]
        while idx < n and board[idx][j] == '.':
          board[idx][j] = color
          board[idx - 1][j] = '.'
          idx += 1

while True:
  count = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] != '.' and not visited[i][j]:
        visited = [[0] * m for _ in range(n)]
        count += bfs(i, j, board[i][j])
  if count != 0:
    result += 1
  else:
    break
  down()

print(result)



  
        