class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            cnt2[ord(s2[i]) - ord('a')] += 1
        
        matches = sum([cnt1[i] == cnt2[i] for i in range(26)])
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # add right
            idx = ord(s2[right]) - ord('a')
            cnt2[idx] += 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] - 1 == cnt1[idx]:
                matches -= 1
            
            # subtract left
            idx = ord(s2[left]) - ord('a')
            cnt2[idx] -= 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] + 1 == cnt1[idx]:
                matches -= 1
            
            left += 1
        return matches == 26