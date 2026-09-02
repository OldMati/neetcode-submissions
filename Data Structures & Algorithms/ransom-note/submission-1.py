class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransom = Counter(ransomNote)
        freq_magazine = Counter(magazine)
        for letter, freq in freq_ransom.items():
            if freq > freq_magazine[letter]:
                return False
        return True