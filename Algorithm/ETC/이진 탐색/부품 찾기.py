n = int(input())
data = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
data.sort()

def binary_search(start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if data[mid] == target:
      print("yes", end=' ')
      return
    elif data[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  print("no", end=' ')

for target in want:
  binary_search(0, n - 1, target)