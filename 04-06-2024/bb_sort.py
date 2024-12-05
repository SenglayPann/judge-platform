def b_sort(ls, k):
    count = 0
    for i in range(len(ls) + 1):
        for j in range(i):
            if ls[j + 1] < ls[j]:
                ls[j + 1], ls[j] = ls[j], ls[j + 1] 
                count += 1
                if count == k:
                    return ' '.join([str(ls[j - 2]), str(ls[j])])
    return None
        

print(b_sort(list(map(lambda x : int(x), '50 40 70 10 30 20 60'.split())), 10))