def argv(*args):
    s = 0
    for arg in args:
        s += 1
    return s

print(argv(2, 4, "a", None)) 
print(argv())               