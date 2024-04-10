x, y = map(int, input().split())
left = 1
right = 1000000000
rate = (100 * y) // x
result = - 1

while left <= right:
  mid = (left + right) // 2
  new_rate = (100 * (y + mid) // (x + mid))
  if new_rate != rate:
    right = mid - 1
    result = mid
  else:
    left = mid + 1
print(result)
