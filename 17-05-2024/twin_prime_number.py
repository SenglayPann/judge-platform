def twin_prime(n):
    prev_prime = 3
    cnt = 0
    for num in range(5, n + 1):
        if is_prime(num):
            if num - 2 == prev_prime:
                print(prev_prime, num)
                cnt += 1
                prev_prime = num
    print(cnt)

def is_prime(n):
    for num in range(2, int(n ** .5) + 1):
        if n % num == 0:
            return False
    return True

twin_prime(10)