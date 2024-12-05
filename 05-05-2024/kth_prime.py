def is_prime(n):
    if n <  2:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


def kth_prime(A, B, K):
    primes = []
    for i in range(A, B + 1):
        if is_prime(i):
            primes.append(i)
    print(sum(primes))
    print(primes[K - 1] if 0 <= K <= len(primes) else -1)


A, B, K = map(int, input().split())

kth_prime(A, B, K)