from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
result = int(1e9)

def bfs(cur_x, cur_y):
  q = deque()
  q.append((cur_x, cur_y))
  visited[cur_x][cur_y] = 1
  board[cur_x][cur_y] = count

  while q:  
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if visited[nx][ny]:
        continue
      if board[nx][ny] == 1:
        board[nx][ny] = count
        visited[nx][ny] = 1
        q.append((nx, ny))


def find(cur_x, cur_y):
  global result
  q = deque()
  q.append((cur_x, cur_y))
  island = board[cur_x][cur_y]
  visited = [[-1] * n for _ in range(n)] 
  visited[cur_x][cur_y] = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if board[nx][ny] != 0 and board[nx][ny] != island:
        result = min(result, visited[x][y])
        return
      if visited[nx][ny] >= 0:
        continue
      if board[nx][ny] == island:
        continue
      if board[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
      

for i in range(n):  # 섬 나누기(count 값으로 구분)
  for j in range(n):
    if board[i][j] == 1 and not visited[i][j]:
      count += 1
      bfs(i, j)

for i in range(n):     # 가장 짧은 다리 탐색
  for j in range(n):
    if board[i][j] != 0:
      find(i, j)

print(result)




    