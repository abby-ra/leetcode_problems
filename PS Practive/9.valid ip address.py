#Valid IP adderess

def validIP(s):
    ip = s.split('.')
    
    if len(ip) !=4:
        return False
    else:
        for i in ip:
            if not i.isdigit():
                return False
            num = int(i)
            if num > 255 or num<0:
                return False
    return True

s = input("Enter an IP address: ")
print(validIP(s))