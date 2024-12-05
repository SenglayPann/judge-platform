# import string

# def solve():
#     alpha = string.ascii_uppercase
#     result = ''
#     for i in range(1, len(alpha)):
#         result += ' '.join(alpha[:len(alpha) - i])
#         if i != len(alpha)  - 1:
#             result += '\n'
#     print(result)


# input('-')
# solve()

while True:
    n = input('-')
    if n == '':
        n = 26
        break
    elif int(n) <= 26:
        n = int(n)
        break


for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end = ' ')
    print()