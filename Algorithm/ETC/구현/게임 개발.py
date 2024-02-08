n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for i in range(n):
  array.append(list(map(int, input().split())))
result = 1
array[x - 1][y - 1] = 2
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
turn_count = 0

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if(array[nx][ny] == 0):
        array[nx][ny] = 2
        x = nx
        y = ny
        turn_count = 0
        result += 1
    else:
       turn_count += 1
    
    if turn_count == 4:
       nx = x - dx[(d + 2) % 4]
       ny = y - dy[(d + 2) % 4]
       if array[nx][ny] != 1:
          x = nx
          y = ny
          turn_count = 0
       else:
          break

print(result)