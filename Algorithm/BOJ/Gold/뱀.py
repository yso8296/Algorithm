n = int(input())
k = int(input())
array = [[0] * (n + 1) for _ in range(n + 1)]
time_info = []
for _ in range(k):
  x, y = map(int, input().split())
  array[x][y] = 1
l = int(input())
for _ in range(l):
  x, c = input().split()
  time_info.append((int(x), c))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
cur_x = 1
cur_y = 1
dir = 1
time = 0
body_info = [(cur_x, cur_y)]
array[cur_x][cur_y] = 2
index = 0

while True:
  #1 이동
  time += 1
  nx = cur_x + dx[dir]
  ny = cur_y + dy[dir]
  #2 벽인지 확인
  if nx < 1 or nx > n or ny < 1 or ny > n:
    break 
  #3 자신의 몸인지 확인
  if array[nx][ny] == 2:
    break
  #4 사과 확인
  if array[nx][ny] == 1: # 사과라면
    array[nx][ny] = 2
    cur_x = nx
    cur_y = ny
    body_info.append((nx, ny))
  else:
    array[nx][ny] = 2
    cur_x = nx
    cur_y = ny
    px, py = body_info.pop(0)
    array[px][py] = 0
    body_info.append((nx, ny))
  #5 방향전환 확인
  if index < l and time == time_info[index][0]:
    if time_info[index][1] == 'L':
      dir = (dir - 1) % 4  
    elif time_info[index][1] == 'D':
      dir = (dir + 1) % 4
    index += 1
print(time)