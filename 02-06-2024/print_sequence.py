# def solve(n):
#     for i in range(1, n + 1):
#         print(i)


# solve(20)

def solve(n):
    if n == 1:
        print(n, end = ' ')
    else:
        print(n, end = ' ')
        solve(n - 1)

solve(10)