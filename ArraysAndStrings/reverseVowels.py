class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet=set("aeiouAEIOU")
        vowels=[c for c in s if c in vowelSet]
        res=""
        for c in s:
            if c in vowelSet:
                res+=vowels.pop()
            else:
                res+=c
        return res