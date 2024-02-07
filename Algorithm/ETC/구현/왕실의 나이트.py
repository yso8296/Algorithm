data = input()
move = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2)]
x = int(data[1])
y = ord(data[0]) - ord('a') + 1
result = 0

for step in move:
  nx = x + step[0]
  ny = y + step[1]
  if (1 <= nx <= 8) and (1 <= ny <= 8):
    result += 1

print(result) 