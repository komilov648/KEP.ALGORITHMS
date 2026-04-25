def calculate(a, b):
    
    start = min(a, b)
    end = max(a, b)
    
    
    return sum(range(start, end + 1))


print(calculate(1, 5)) # 1+2+3+4+5 = 15
print(calculate(5, 7)) # 5+6+7 = 18
