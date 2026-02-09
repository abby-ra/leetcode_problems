#Good String & Bad string based on frequency

def good_bad_string(s):

    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = s.count(char)
    
    freq_val = list(freq.values())
    freq_set = set(freq_val)

    if len(freq_set) == 1:
        return "Good String"
    else:
        return "Bad String"
    
s = input("Enter a string: ")
print(good_bad_string(s))
