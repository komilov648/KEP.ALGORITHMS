
a = int(input())
b = int(input())


start = min(a, b)
end = max(a, b)

count = 0


for i in range(start, end + 1):
    if i % 4 == 0:
        count += 1


print(count)
