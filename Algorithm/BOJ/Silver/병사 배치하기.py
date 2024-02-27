n = int(input())
array = list(map(int, input().split()))
array.reverse()
result = 0

for i in range(n):
  temp = 1
  max_num = array[i]
  for j in range(i, n):
    if array[j] > max_num:
      temp += 1
      max_num = array[j]
  result = max(result, temp)

print(n - result)
