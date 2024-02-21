n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 1
for i in range(len(array)):
  if array[i] <= result:
    result += array[i]
  else:
    break

print(result)