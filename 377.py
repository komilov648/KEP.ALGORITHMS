# n = int(input())
# a = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
counter = 0
for element in a:
    if a.count(element) == 2:
            counter += 1

print(int(counter / 2))