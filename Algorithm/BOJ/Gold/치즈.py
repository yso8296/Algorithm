from collections import deque
n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
time = 0
cheeze = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
  global cheeze
  count = 0
  visited = [[0] * m for _ in range(n)]
  q = deque()
  q.append((0, 0))
  visited[0][0] = 1
  temp = deque()

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if visited[nx][ny] == 1:
        continue
      if board[nx][ny] == 0:
        q.append((nx, ny))
        visited[nx][ny] = 1
      if board[nx][ny] == 1 and (nx, ny) not in temp:
        temp.append((nx, ny))
  for x, y in temp:
    board[x][y] = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] == 1:
        count +=1
  if count == 0:
    cheeze = len(temp)
    return True
  return False

while True:
  time += 1
  if bfs() == True:
    print(time)
    print(cheeze)
    exit()

