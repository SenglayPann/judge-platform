

def count_anagram(words):
    anagram = dict()
    for word in words:
        ana_word = ''.join(sorted(word))
        if ana_word in anagram.keys():
            anagram[ana_word].append(word)
        else:
            anagram[ana_word] = [word]

    key_ls = sorted([i[0] for i in anagram.values()])
    key_ls = list(map(lambda x : ''.join(sorted(x)), key_ls))
    result = ''
    for ana in key_ls:
        result += str(anagram[ana][0]) + ' ' + str(len(anagram[ana]))
        if ana != key_ls[len(key_ls) - 1]:
            result += ' '
    return result

n = int(input())

words = []

for i in range(n):
    words.append(input())

print(count_anagram(words))
