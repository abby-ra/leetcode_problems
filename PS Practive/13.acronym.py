#acronym

def scronym(s,first):
    word = s.split()
    acron = ""

    for i in word:
        acron += i[0]

    if acron == first:
        return True
    return False

s = input("Enter the string: ")
first = input("Enter the acronym: ")
print(scronym(s,first))
