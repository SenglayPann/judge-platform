def fibonacci_numbers(n):
    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_numbers(20))