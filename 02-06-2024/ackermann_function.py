count = 0

def ack(n, m):

    global count
    count +=1

    if n == 0:
        return m + 1
    if n > 0 and m == 0:
        return ack(n - 1, 1)
    if n > 0 and m > 0:
        return ack(n - 1, ack(n , m - 1))
    
res = ack(3, 3)
print(res)
print(count)