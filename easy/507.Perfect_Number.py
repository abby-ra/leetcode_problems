class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i
                other = num // i
                if i != other:
                    total += other
            i += 1

        if total == num:
            return True
        else:
            return False
