n = int(input())
array = list(map(int, input().split()))

def binary_search(start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
      return mid
    elif array[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1
  return -1

print(binary_search(0, n - 1))