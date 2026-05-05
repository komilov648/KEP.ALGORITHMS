def kwargv(**kwargv):
    s = 0
    for son in kwargv:
        s += 1

    return s

print(kwargv(a=2, b=4, c="a", d=None) == 4)
print(kwargv() == 0)