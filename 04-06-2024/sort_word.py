import random
from string import ascii_lowercase

def generate(SEED, N):
    random.seed(SEED)
    S=[]
    for _ in range(N):
        length=random.randint(1, N-1)
        s=random.sample(ascii_lowercase, length)
        S.append("".join(s))
    return S




def sort_word(words, k):
    return sorted(words, key = lambda x : (len(x), x))[k]

# s, n, k = [int(input()) for _ in range(3)]

S = generate(2022, 10)
print(sort_word(S, 5))