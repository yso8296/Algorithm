dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(5)]
arr = []
result = 0

def dfs(x, y, num):
  global result
  if len(num) == 6:
    if num not in arr:
      arr.append(num)
      result += 1
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
      continue
    dfs(nx, ny, num + str(board[nx][ny]))
 
for i in range(5):
  for j in range(5):
    dfs(i, j, str(board[i][j]))

print(result)
