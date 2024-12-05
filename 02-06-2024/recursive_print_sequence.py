def solve(n, current = 0):
    if current == n:
        print(n)
    else:
        print(current)
        solve(n, current + 1)

solve(20)