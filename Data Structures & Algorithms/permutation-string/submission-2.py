from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = Counter(s1)
        left = 0
        # letters = set(s1)
        letters = set(s1)
        n = len(s2)
        print(letters)
        print(s2)
        for right in range(n):
            if len(freq) == 0:
                return True
            
            char = s2[right]
            while char not in freq and left < right:
                # increase the freq of the element to remove
                if s2[left] in letters:
                    freq[s2[left]] = freq.get(s2[left], 0) + 1
                left += 1

            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    del freq[char]

            print(f'{left=} {right=} {char=} {freq=}')
        return len(freq) == 0

# find the frequencies of characters of s1

# use sliding window: decrease/pop frequencies from the counter as right moves, increase when left moves
# return true when len(freq) == 0; false if loop finished


# expand:
# if s2[right] not in letters, increase both to right + 1
# if s2[right] in freq, substract and move
# if s2[right] not in freq,


#s1:     a   b   c

# s2:     l   e   c   a   b   e   e