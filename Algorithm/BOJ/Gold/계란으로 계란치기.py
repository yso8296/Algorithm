n = int(input())
eggs = []
for _ in range(n):
  s, w = map(int, input().split())
  eggs.append([s, w])
result = 0

def crash(count):
  global result
  if count == n:
    temp = 0
    for i in range(n):
      if eggs[i][0] <= 0:
        temp += 1
    result = max(result, temp)
    return
  
  if eggs[count][0] <= 0:
    crash(count + 1)
    return
  check = False
  for i in range(n):
    if i != count and eggs[i][0] > 0:
      check = True
      eggs[count][0] -= eggs[i][1]
      eggs[i][0]  -= eggs[count][1]
      crash(count + 1)
      eggs[i][0] += eggs[count][1]
      eggs[count][0] += eggs[i][1]
  if check == False:
    crash(count + 1)

crash(0)
print(result)
      
 

