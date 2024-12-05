def factP(n):
    res = 1
    print(str(n) + '!=(', end = '')
    for num in range(1, n + 1):
        res *= num
        print(num, end = '')
        if num != n:
            print('*', end = '')
    print(')=' + str(res))

factP(6)