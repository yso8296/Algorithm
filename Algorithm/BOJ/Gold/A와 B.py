s = input()
t = input()

while len(t) > len(s):
  if t[-1] == 'A':
    t = t[0:-1]
  elif t[-1] == 'B':
    t = t[0:-1]
    t = t[::-1]
  if s == t:
    print(1)
    exit()
print(0)