n, x = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def binary_search_left(start, end, target):
  result = -1
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      end = mid - 1
      result = mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return result

def binary_search_right(start, end, target):
  result = -1
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      start = mid + 1
      result = mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return result

left = binary_search_left(0, n - 1, x)
right = binary_search_right(0, n - 1, x)
if left == -1 or right == -1:
  print(-1)
else:
  print(right - left + 1)

