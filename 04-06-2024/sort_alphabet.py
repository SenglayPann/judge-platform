st = ''.join([i for i in '6  AaBbCc' if not i.isdigit()]).strip()
upper = ''
lower = ''
for ch in st:
    if ch.isupper():
        upper += ch
    else:
        lower += ch
print(upper + ' ' + lower[::-1])
