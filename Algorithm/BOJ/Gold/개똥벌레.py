n, h = map(int, input().split())
down = [0] * (h + 1)
up = [0] * (h + 1)
count = 0
min_value = n
for i in range(n):
  size = int(input())
  if i % 2 == 0:
    down[size] += 1
  else:
    up[size] += 1
for i in range(h - 1, 0, -1):
  down[i] += down[i + 1]
  up[i] += up[i + 1]

for i in range(1, h + 1):
  if min_value > down[i] + up[h - i + 1]:
    min_value = down[i] + up[h - i + 1]
    count = 1
  elif min_value == down[i] + up[h - i + 1]:
    count += 1

print(min_value, count)

