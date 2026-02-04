#Check frequency of characters in a string

def check_frequency(s):
    freq = {}

    for char in s:
        if char not in freq:
            freq[char] = s.count(char)

    return freq

s = input("Enter a string: ")
freq = check_frequency(s)

for k, v in freq.items():
    print(f"'{k}': {v}", end=" ")