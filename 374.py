
n = int(input())
numbers = list(map(int, input().split()))
min_value = min(numbers)
position = numbers.index(min_value) + 1
print(position)
