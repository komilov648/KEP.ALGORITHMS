def argv_int(*args):
  s = 0
  for son in args:
    if type(son) == int:
      s += 1

  return s

print(argv_int(2, 4, "a", 5.0, None) == 2)
print(argv_int() == 0) 