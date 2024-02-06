n = int(input())
direction = list(input().split())
x = 1
y = 1

for dir in direction:
  if dir == 'L':
    if y > 1:
      y -= 1
  elif dir == 'R':
    if y < n:
      y += 1
  elif dir == 'U':
    if x > 1:
      x -= 1
  elif dir == 'D':
    if x < n:
      x += 1

print(x, y)