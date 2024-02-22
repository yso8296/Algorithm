king, rock, n = input().split()
king = list(king)
rock = list(rock)
n = int(n)
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
alp = dict()
alp['A'] = 1
alp['B'] = 2
alp['C'] = 3
alp['D'] = 4
alp['E'] = 5
alp['F'] = 6
alp['G'] = 7
alp['H'] = 8
dict = dict()
dict['R'] = 0
dict['L'] = 1
dict['B'] = 2
dict['T'] = 3
dict['RT'] = 4
dict['LT'] = 5
dict['RB'] = 6
dict['LB'] = 7
king[0] = alp[king[0]]
rock[0] = alp[rock[0]]
king[1] = int(king[1])
rock[1] = int(rock[1])

for i in range(n):
  dir =  input()
  nx = king[1] + dx[dict[dir]]
  ny = king[0] + dy[dict[dir]]
  rock_x = rock[1]
  rock_y = rock[0]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  if nx == rock_x and ny == rock_y:
    rock_nx = rock_x + dx[dict[dir]]
    rock_ny = rock_y + dy[dict[dir]]
    if rock_nx < 1 or rock_nx > 8 or rock_ny < 1 or rock_ny > 8:
      continue
    else:
      rock[1] = rock_nx
      rock[0] = rock_ny
      king[1] = nx
      king[0] = ny
  else:
    king[1] = nx
    king[0] = ny

print(chr(ord('A') - 1 + king[0]) + str(king[1]))
print(chr(ord('A') - 1 + rock[0]) + str(rock[1]))

