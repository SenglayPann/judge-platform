import re

def sum_divs(n):
    total = n + 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i: 
                total += (n // i)
    return total

n = int(re.search(r'\d+', "Enter a number: 20").group())
if (2 <= n <= 20) : 
    print("Sum of divisors:", sum_divs(n))