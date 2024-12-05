def sieve_of_erathosesnes(n):
    sieve = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n ** .5 ) + 1):
        if  sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve

def solve(A, B):
    max_prime = int(B ** .5) + 1
    primes = [i for i, is_prime in enumerate(sieve_of_erathosesnes(B)) if is_prime]

    almost_primes = set()
    for prime in primes:
        power = prime * prime
        while power <= B:
            if power >= A:
                almost_primes.add(power)
            power *= prime;
    return len(almost_primes)

A, B = map(int, input().split())
print(solve(A, B))