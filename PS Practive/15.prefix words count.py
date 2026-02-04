#Given a sentence and a word. return the words in the sentence starts with the given word(Prefix)

def prefix(sen,word):
    
    s = sen.split()
    res = ""

    for i in s:
        if i.startswith(word):
            res += i + " "
    return res

sen = input("Enter the sentence: ")
word = input("Enter the prefix word: ")
print(prefix(sen,word))