def solve(n):
    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    coin_ls = [1, 1]
    for day in range(2, n):
        if day % 2 == 0:
            coin_ls.append(coin_ls[day // 2])
        else:
            coin_ls.append(coin_ls[(day - 1) // 2] + coin_ls[(day - 1) // 2 + 1])
    return max(coin_ls)

print(solve(10))