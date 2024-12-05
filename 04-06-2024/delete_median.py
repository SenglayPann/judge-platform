import random
def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)


def solve(s, k):
    for i in range(k):
        if i == k - 1:
            print(s[i])
        median = (len(s) - 1)// 2
        s.pop(median)

SEED, MIN, MAX, N, K = 2022, 10, 100, 15, 5
S = generate(SEED, MIN, MAX, N)
solve(S, K)
