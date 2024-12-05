def collatz(n):
    if n < 1:
        return []
    if n == 1:
        return [n]
    if n % 2 == 0:
        return [n] + collatz(n // 2)
    return [n] + collatz((3 * n ) + 1)


def solve(S, E):
    largest_seq_count = 0
    largest_num = None
    for seq in range(S, E + 1):
        current_collatz = len(collatz(seq))
        if current_collatz > largest_seq_count:
            largest_seq_count = current_collatz
            largest_num = seq
    print(largest_num)
    print(largest_seq_count)
        
solve(123, 321)