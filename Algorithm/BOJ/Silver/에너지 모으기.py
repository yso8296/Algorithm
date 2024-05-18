n = int(input())
arr = list(map(int, input().split()))
result = 0

def calc(energy):
  global result
  if len(arr) == 2:
    result = max(result, energy)
    return
  
  for i in range(1, len(arr) - 1):
    temp = arr[i - 1] * arr[i + 1]
    x = arr.pop(i)
    calc(energy + temp)
    arr.insert(i, x)

calc(0)
print(result)