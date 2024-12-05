def APB2N(S, E):
    for p in range(S, E + 1):
        if is_prime(p):
            print(p)


def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(n ** .5) + 1):
        if n % num == 0:
            return False
    return True

APB2N(12, 24)