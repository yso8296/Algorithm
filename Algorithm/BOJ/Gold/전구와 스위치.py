import copy
n = int(input())
arr1 = list(input())
arr2 = list(input())
result = int(1e9)
count = 0
temp = copy.deepcopy(arr1)

def switch(i):
  if arr1[i] == '0':
    return '1'
  else:
    return '0'
  
for i in range(1, n):
  if arr1[i - 1] != arr2[i - 1]:
    arr1[i - 1] = switch(i - 1)
    arr1[i] = switch(i)
    if i != n - 1:
      arr1[i + 1] = switch(i + 1)
    count += 1
if arr1 == arr2:
  result = count
count = 1
arr1 = copy.deepcopy(temp)

arr1[0] = switch(0)
arr1[1] = switch(1)
for i in range(1, n):
  if arr1[i - 1] != arr2[i - 1]:
    arr1[i - 1] = switch(i - 1)
    arr1[i] = switch(i)
    if i != n - 1:
      arr1[i + 1] = switch(i + 1)
    count += 1
if arr1 == arr2:
  result = min(result, count)

if result == int(1e9):
  print(-1)
else:
  print(result)
