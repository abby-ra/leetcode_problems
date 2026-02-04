#Capitalize the First Letter of Each Word in Multiple Strings


def caps(s):
    return ''.join(word.capitalize() for word in s.split())

n = input()
print(caps(n))