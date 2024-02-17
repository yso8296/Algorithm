n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def binary_search(start, end, target):
  result = 0
  while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in range(n):
      if array[i] > mid:
        sum += (array[i] - mid)
    if sum < target:
      end = mid - 1
    else:
      start = mid + 1
      result = max(result, mid)
  return result

print(binary_search(0, array[-1], m))