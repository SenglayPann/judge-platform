def primes(n, m):

    def isPrime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime_count = 0
    for i in range(m, n - 1, -1):
        if isPrime(i) == True:
            print(i, end = ' ')
            prime_count += 1

        if prime_count == 5:
            break

primes(2147483647, 4294967295)    