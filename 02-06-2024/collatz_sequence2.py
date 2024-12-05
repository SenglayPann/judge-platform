operation_count = 0

def collatz(n):
    global operation_count
    operation_count += 1
    if n < 1:
        return None
    if n == 1:
        return operation_count - 1
    if n % 2 == 0:
        return collatz(n // 2)
    return collatz((n + 1) // 2)
    
print(collatz(10))