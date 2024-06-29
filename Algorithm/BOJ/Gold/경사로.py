n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
  num = board[i][0]
  check = True
  cnt = 0
  temp = 0
  for j in range(n):
    if board[i][j] == num:
     if temp == 0:
      cnt += 1
    elif abs(board[i][j] - num) > 1:
      check = False
      break
    elif board[i][j] > num:
      if cnt < m:
        check = False
        break
      else:
        cnt = 1
        num = board[i][j]
    else:
      if temp != 0:
        check = False
        break
      temp = m
      num = board[i][j]
      cnt = 0
    if temp != 0:
      temp -= 1
  if check == True and temp == 0:
    result += 1

for j in range(n):
  num = board[0][j]
  check = True
  cnt = 0
  temp = 0
  for i in range(n):
    if board[i][j] == num:
     if temp == 0:
      cnt += 1
    elif abs(board[i][j] - num) > 1:
      check = False
      break
    elif board[i][j] > num:
      if cnt < m:
        check = False
        break
      else:
        cnt = 1
        num = board[i][j]
    else:
      if temp != 0:
        check = False
        break
      temp = m
      num = board[i][j]
      cnt = 0
    if temp != 0:
      temp -= 1
  if check == True and temp == 0:
    result += 1

print(result)   
      