def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    if is_prime(n):
        print(n, "is prime number.")
    else:
        print(n, "is a composite number.")

ls = [int(i) for i in "12\n710\n7\n257\n319".split("\n")]

for i in range(len(ls)):
    solve(ls[i])
    if i != len(ls) - 1:
        print()