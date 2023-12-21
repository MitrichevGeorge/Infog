def factor(n):
  if(n > 1):
    return n * factor(n)
  return n
