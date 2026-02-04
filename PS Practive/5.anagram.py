#anagram with removing the special character or space 
def clean(s):
    return ''.join(char.lower() for char in s if char.isalnum())

def anaram(s1,s2):
    return sorted(clean(s1)) == sorted(clean(s2))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(anaram(s1,s2))