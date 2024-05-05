n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crain.sort(reverse=True)
box.sort(reverse=True)
result = 0

if box[0] > crain[0]:
  print(-1)
  exit()

while box:
  for c in crain:
    for b in box:
      if c >= b:
        box.remove(b)
        break
  result += 1

print(result)
        