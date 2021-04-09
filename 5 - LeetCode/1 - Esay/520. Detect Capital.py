class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        if word == word.lower():
            return True

        if word[0].isupper() and word[1:].islower():
            return True

        return False