#Longest word

def long_word(words):
    s = words.split()
    long = {}

    for i in s:
        long[i] = len(i)

    return max(long, key=long.get)

words = input()
print(long_word(words))