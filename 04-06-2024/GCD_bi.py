def toBinary(n):
    res = ''
    if n == 0:
        res += '0'
        return res
    
    q = n // 2
    while q != 0:
        if n % 2 == 0:
            res += '0'
        else:
            res += '1'
        n = q
        q = n // 2
    res += '1'

    return res[::-1]



def GCD_bi(a, b):
    if a < b:
        a, b = b, a

    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return toBinary(b)

print(GCD_bi(3, 6))