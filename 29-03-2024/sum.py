def sum(N, M):
    return ((M + N) * (M - N + 1 )) // 2
N, M = [int(num) for num in input().split()]
print(sum(N, M))
