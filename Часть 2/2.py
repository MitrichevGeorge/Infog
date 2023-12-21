def factor(n):
  if n > 1:
    return n * factor(n-1)
  return 1
def func(n,k):
  return factor(n)/(factor(k) * factor(n - k))
