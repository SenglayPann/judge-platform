def factP(n):
    for i in range(1, n + 1):
        print(i, end='')
        if i != n:
            print('*', end='')


factP(4)