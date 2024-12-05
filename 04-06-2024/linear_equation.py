def solve(a, b, c):
    x = c // 1
    y = (c - a * x) // b
    while a * x + b * y != c:
        x -= 1
        y = (c - a * x) // b
    return '{} {}'.format(x, y)
    


print(solve(1, 2, 3))