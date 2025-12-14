class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p1, p2 = 0, 0 + k
        vowels = "aeiou"
        counter = 0
        counters = []
        for i in range(p1, p2):
            if s[i] in vowels:
                counter += 1
        max_vowels = counter
        if max_vowels == k:
            return k
        while p2 < len(s):
            p1 += 1
            p2 += 1
            if s[p1 - 1] in vowels:
                counter -= 1
            if s[p2 - 1] in vowels:
                counter += 1
            if counter == k:
                return k
            max_vowels = max(max_vowels, counter)
        return max_vowels
