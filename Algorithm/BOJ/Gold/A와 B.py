s = list(input())
t = list(input())
check = False

while t:
  if t[-1] == 'A':
    t.pop()
  elif t[-1] == 'B':
    t.pop()
    t.reverse()
  if s == t:
    check = True
    break
if check:
  print(1)
else:
  print(0)