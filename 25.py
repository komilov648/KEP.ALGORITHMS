import math

def solve():
    a = float(input())
    b = float(input())
    
    discriminant = a**2 - 4*b
    sqrt_d = math.sqrt(discriminant)
    
    x = (a + sqrt_d) / 2
    y = (a - sqrt_d) / 2
    
    print(f"{x} {y}")

solve()
