n = int(input())
like = [[] for _ in range(n * n + 1)]
order = []
board = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n * n):
  a, b, c, d, e = map(int, input().split())
  order.append(a)
  like[a].append(b)
  like[a].append(c)
  like[a].append(d)
  like[a].append(e)

def calc_near(num):
  temp = [[0] * n for _ in range(n)]
  max_num = 0
  count_max = 0
  for i in range(n): 
    for j in range(n):
      if board[i][j] in like[num]:
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
          if board[nx][ny] == 0:
            temp[nx][ny] += 1
            max_num = max(max_num, temp[nx][ny])
  for i in range(n):
    for j in range(n):
      if temp[i][j] == max_num and board[i][j] == 0:
        count_max += 1
  if count_max == 1: # 1
    for i in range(n):
      for j in range(n):
        if temp[i][j] == max_num and board[i][j] == 0:
          board[i][j] = num
  else: # 2
    x, y = 0, 0
    empty_count = 0
    empty = 0
    for i in range(n):
      for j in range(n):
        if temp[i][j] == max_num and board[i][j] == 0:
          empty = 0
          for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
              continue
            if board[nx][ny] == 0:
              empty += 1
          if empty > empty_count and board[i][j] == 0:
            x, y = i, j
            empty_count = empty
    if empty_count == 0:
      for i in range(n):
        for j in range(n):
          if temp[i][j] == max_num and board[i][j] == 0:
            board[i][j] = num
            return
    board[x][y] = num
    print(board)

def simulation():
  for i in order:
    calc_near(i)

simulation()
result = 0
print(board)
for i in range(n):
  for j in range(n):
    count = 0
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if board[nx][ny] in like[board[i][j]]:
         count += 1
    if count == 1:
      result += 1
    elif count == 2:
      result += 10
    elif count == 3:
      result += 100
    elif count == 4:
      result += 1000
print(result)
      

