n = input()
s = 0
for i in n[:: -1]:
    if i == "0":
       s += 1
    else:
        break
print(s)