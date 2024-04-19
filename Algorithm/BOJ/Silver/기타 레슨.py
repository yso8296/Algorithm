n, m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search():
  start = max(array)
  end = int(1e9)
  result = int(1e9)

  while start <= end:
    num = 0
    sum = 0
    mid = (start + end) // 2
    for i in range(n):
      sum += array[i]
      if sum > mid:
        num += 1
        sum = array[i]
    if sum > 0:
      num += 1
    if num > m:
      start = mid + 1
    else:
      end = mid - 1
      result = min(result, mid)
  return result

print(binary_search())