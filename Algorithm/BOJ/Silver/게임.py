x, y = map(int, input().split())
initial_ratio = int(y * 100 / x)

def binary_search(start, end):
  while start <= end:
    mid = (start + end) // 2
    temp = int((y + mid) * 100 / (x + mid))
    if temp <= initial_ratio:
      start = mid + 1
    else:
      end = mid - 1
  return start

if initial_ratio >= 99:
  print(-1)
else:
  print(binary_search(0, 1000000000))