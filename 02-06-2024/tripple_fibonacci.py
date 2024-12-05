
# def tripbonacci(n):
#     if n <= 0:
#         return
#     if n == 1 or n == 2:
#         return 0
#     if n == 3:
#         return 1
#     return tripbonacci(n - 1) + tripbonacci(n - 2) + tripbonacci(n - 3)

# print(tripbonacci(100000))
# import sys

# sys.set_int_max_str_digits(50000)

# def tripbonacci(n):
#     if n <= 0:
#         return None
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 3
#     a, b, c = 1, 2 , 3
#     for _ in range(4, n + 1):
#         a, b, c, = b, c, a + b + c
#     return c


def tripbonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    MOD =  2 ** 32 - 1
    a, b , c = 1, 2, 3
    for _ in range(4, n + 1):
        a, b, c = b, c, (a + b + c) % MOD
    return c


print(tripbonacci(100000))