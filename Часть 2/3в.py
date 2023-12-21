def grow(k):
  return k + 1
def func(m,n,k):
  krol = [0]
  for i in range(n):
    k = krol
    for j in k:
      if j >= m:
        krol.append(0)
    krol = list(map(grow,krol))
    while n in krol:
      krol.delete(n)
  return len(krol)
