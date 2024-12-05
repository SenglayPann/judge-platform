def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def solve(n, r):
    return factorial(n)  // factorial(n - r)


n, r = list(map(int, input().split()))
print(solve(n, r))


