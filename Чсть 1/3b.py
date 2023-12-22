def func(s):
  r = []
  for i in s:
    if r.count(i)>1:
      r.dlete(i)
    else:
      r.append(i)
  return r
