#to find if all alphabets are repeated same no.of times.

def alpha_count(s):
    res = {}
    for char in s:
        if char in res:
            continue
        else:
            res[char] = s.count(char)

    return len(set(res.values())) == 1

s = input("Enter a string: ")
print(alpha_count(s))
        