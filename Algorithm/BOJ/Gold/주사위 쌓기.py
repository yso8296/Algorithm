n = int(input())
idx = [5, 3, 4, 1, 2, 0]
dice = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(6):
  floor = dice[0][i]
  top = dice[0][idx[i]]
  temp = 0
  for j in range(len(dice)):
    maxNum = 0
    for k in range(6):
      if dice[j][k] == top:
        floor = top
        top = dice[j][idx[k]]
        break
    for k in range(6):
      if dice[j][k] != floor and dice[j][k] != top:
        maxNum = max(maxNum, dice[j][k])
    temp += maxNum
  result = max(result, temp)

print(result)

     