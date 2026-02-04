def palindrome(word):
    if word == word[::-1]:
        return True
    
word = input()
if palindrome(word):
    print("Yes")
else:
    print("NO")