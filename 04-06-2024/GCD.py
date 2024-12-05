def GCD(a, b):
    if a < b:
        a, b = b, a

    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

print(GCD(24, 64))