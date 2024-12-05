def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

factors = prime_factors(1234567890)
i = 0
N = 1234567890
num = N
divisors = []
while i < len(factors) - 1 :
    if num % factors[i] == 0:
        divisors.append(num // factors[i])
        divisors.append(num // factors[i])
        num //= factors[i]
    else:
        i += 1

print(factors)
print(sum(divisors) + N + 1)