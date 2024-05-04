from collections import deque
b, a = map(int, input().split())
n, m = map(int, input().split())
board = [[0] * (b + 1) for _ in range(a + 1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = [0] * (n + 1)
dict = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
idx = [(0, 0)]
for i in range(n):
  y, x, d = input().split()
  y = int(y)
  x = int(x)
  board[a - x + 1][y] = i + 1
  dir[i + 1] = dict[d]
  idx.append((a - x + 1, y))

for _ in range(m):
  robot, command, num = input().split()  
  robot = int(robot)
  num = int(num)
  cur_x, cur_y = idx[robot]
  cur_dir = dir[robot]
  for _ in range(num):
    if command == 'L':
      cur_dir = (cur_dir + 3) % 4
    elif command == 'R':
      cur_dir = (cur_dir + 1) % 4
    else:
      nx = cur_x + dx[cur_dir]
      ny = cur_y + dy[cur_dir]
      if nx < 1 or nx > a or ny < 1 or ny > b:
        print(f"Robot {robot} crashes into the wall")
        exit()
      if board[nx][ny] != 0:
        print(f"Robot {robot} crashes into robot {board[nx][ny]}")
        exit()
      board[nx][ny] = robot
      board[cur_x][cur_y] = 0
      cur_x = nx
      cur_y = ny
      idx[robot] = (nx, ny)
    dir[robot] = cur_dir

print("OK")    
