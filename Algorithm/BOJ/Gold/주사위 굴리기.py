n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
dice = [0, 0, 0, 0, 0, 0]
# 위:1 뒤:2 오:3 왼:4 앞:5 밑:6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move = list(map(int, input().split()))
def turn(dir):
  global dice
  a, b, c, d, e, f = dice
  if dir == 1:
    dice = [d, b, a, f, e, c]
  elif dir == 2:
    dice = [c, b, f, a, e, d]
  elif dir == 3:
    dice = [b, f, c, d, a, e]
  else:
    dice = [e, a, c, d, f, b]

for dir in move:
  nx = x + dx[dir - 1]
  ny = y + dy[dir - 1]
  if nx < 0 or nx >= n or ny < 0 or ny >= m:
    continue
  turn(dir)
  if board[nx][ny] == 0:
    board[nx][ny] = dice[5]
  else:
    dice[5] = board[nx][ny]
    board[nx][ny] = 0
  x = nx
  y = ny
  print(dice[0])

  
