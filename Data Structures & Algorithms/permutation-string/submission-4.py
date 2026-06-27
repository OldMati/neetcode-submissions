from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = Counter(s1)
        left = 0
        letters = set(s1)
        n = len(s2)
        print(letters)
        print(s2)
        for right in range(n):
            if len(freq) == 0:
                return True
            
            char = s2[right]
            while char not in freq and left <= right:
                #if s2[left] in letters:
                freq[s2[left]] = freq.get(s2[left], 0) + 1
                left += 1

            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    del freq[char]

            print(f'{left=} {right=} {char=} {freq=}')
        return len(freq) == 0
