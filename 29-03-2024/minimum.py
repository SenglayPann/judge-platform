import random
SEED, MIN, MAX, N = 1987, 123, 4567, 89
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)
print(min(S), S.index(min(S)))