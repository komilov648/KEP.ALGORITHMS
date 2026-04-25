n = int(input())
a = list(map(int, input().split()))
max_value = a.index(a)
min_index = a.index(min(a))

print(abs(max_value - min_index)-1)