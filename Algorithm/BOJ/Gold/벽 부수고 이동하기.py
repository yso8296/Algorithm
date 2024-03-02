from collections import deque
import copy
n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited[0][0][0] = 1

  while q:
    x, y, z = q.popleft()
    if x == n - 1 and y == m - 1:
      print(visited[x][y][z])
      return
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if board[nx][ny] == 1 and z == 0:
        visited[nx][ny][1] = visited[x][y][0] + 1
        q.append((nx, ny, 1))
      elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
        visited[nx][ny][z] = visited[x][y][z] + 1
        q.append((nx, ny, z))
  print(-1)
bfs()
