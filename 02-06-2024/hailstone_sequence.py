def collatz(n):
    if n < 0:
        return []
    if n == 1:
        return [n] 
    if n % 2 == 0:
        return [n] + collatz(n // 2)
    return [n] + collatz(3 * n + 1)


print(max(collatz(3)))