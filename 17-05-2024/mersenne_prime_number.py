# def is_prime(n):
#     if n <= 1:
#         return False
#     for num in range(2, int(n ** 0.5) + 1):
#         if n % num == 0:
#             return False
#     return True

# def mersenne_prime_number(n):
#     num = 2
#     while True:
#         if is_prime(num):
#             mersenne_num = 2 ** num - 1
#             if mersenne_num > n:
#                 break
#             if is_prime(mersenne_num):
#                 print(mersenne_num)
#         num += 1

# n = int(input())

# mersenne_prime_number(n)


def sum_divs(n):
    total = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total + n + 1
print("Enter a number:")
n = int(input())
print("Sum of divisors:")
print(sum_divs(n))