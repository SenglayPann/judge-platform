
def gcd(a, b):
    if a < b:
        a, b = b , a
    res = a % b
    while res != 0:
        a = b
        b = res
        res =  a % b
    return b


def LCM(ls, i = 0):
    if i == len(ls) - 2:
        return (abs(ls[i] * ls[i + 1])) // gcd(ls[i], ls[i + 1])
    else: 
        next_lcm = LCM(ls, i + 1)
        return abs(ls[i] * next_lcm ) // gcd(ls[i], next_lcm)
    

print(LCM([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))