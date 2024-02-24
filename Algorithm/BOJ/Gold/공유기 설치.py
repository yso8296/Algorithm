n, c = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))
array.sort()

def binary_search(start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    count = 1
    num = array[0]
    for i in range(1, n):
      if array[i] - num >= mid:
        count += 1
        num = array[i]
    if count >= c:
      result = max(result, mid)
      start = mid + 1
    else:
      end = mid - 1
  return result


print(binary_search(1, max(array) - min(array)))
  
