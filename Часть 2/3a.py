def grow(k):
  return k + 1
def func(n):
  krol = [0]
  for i in range(n):
    k = krol
    for j in k:
      if j > 1:
        krol.append(0)
    krol = list(map(grow,krol))
    while 4 in krol:
      krol.delete(4)
  return len(krol)
