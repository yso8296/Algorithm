from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
eat = 0 # 먹은 물고기 수
shark = 2 # 상어 크기
time = 0 # 시간
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cur_x = 0
cur_y = 0
for i in range(n):
  for j in range(n):
    if board[i][j] == 9:
      cur_x = i
      cur_y = j

def bfs():
  temp = []
  global cur_x, cur_y, time, eat, shark
  # 1 북, 서, 동, 남 순으로 먹을 수 있는 물고기 탐색
  q = deque()
  q.append((cur_x, cur_y, 0))
  visited = [[0] * n for _ in range(n)]
  visited[cur_x][cur_y] = 1
  while q:
    x, y, t = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if visited[nx][ny]:
        continue
      # 2 먹을 물고기가 있으면 먹고 다시 탐색
      if board[nx][ny] != 0 and board[nx][ny] < shark:
        temp.append((nx, ny, t))
        visited[nx][ny] = 1
        q.append((nx, ny, t + 1))
      elif board[nx][ny] <= shark:
        visited[nx][ny] = 1
        q.append((nx, ny, t + 1))
  if temp:
    temp.sort(key = lambda x : (x[2], x[0], x[1]))
    nx = temp[0][0]
    ny = temp[0][1]
    t = temp[0][2]
    board[cur_x][cur_y] = 0
    board[nx][ny] = 9
    cur_x = nx
    cur_y = ny
    eat += 1
    if eat == shark:
      shark += 1
      eat = 0
    time += t + 1
    return True
  return False    

  # 3 먹을 물고기가 없다면 종료
while True:
  check = bfs()
  if check == False:
    break

print(time)