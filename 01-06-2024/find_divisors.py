
def solve(n):
    divs = []
    for div in range(1, int(n ** .5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div :
                divs.append(n // div)
    return divs

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
        True

num = int(input())

if not is_prime(num):
    for n in sorted(solve(num)):
        print(n)