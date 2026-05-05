def params(*args, **kwargs):
    s = 0
    for son in args:
        s += 1

    for son in kwargs:
        s += 1
        
    return s

print(params(2, 3, a=2, b=4, c="a", d=None) == 6)
print(params() == 0)