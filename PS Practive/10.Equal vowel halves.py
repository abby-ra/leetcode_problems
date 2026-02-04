#Checking for Equal Number of Vowels in Both Halves of a String eg:helo output:helo has equal number of vowels in both halves of a string 


def equal_vowel(s):

    vow = "aeiouAEIOU"
    mid= len(s)//2

    frst = s[:mid]
    sec = s[mid:]

    count1 = sum(1 for i in frst if i in vow)
    count2 = sum(1 for i in sec if i in vow)

    if count1 == count2:
        return True
    return False

s = input()
print(equal_vowel(s))