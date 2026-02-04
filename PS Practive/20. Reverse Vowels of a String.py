class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_list = [c for c in s if c in vowels]
        res = []

        for c in s:
            if c in vowels:
                res.append(vowel_list.pop())
            else:
                res.append(c)

        return ''.join(res)
