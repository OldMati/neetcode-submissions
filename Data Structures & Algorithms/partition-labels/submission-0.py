class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqs = Counter(s)
        left = 0
        right = 0
        window = set(s[0])
        res = []

        while right < len(s):
            # if there are elements still to add to te window, expand
            freqs[s[right]] -= 1

            if not window:
                window = set(s[right])
                res.append(right - left)
                left = right
            
            if s[right] not in window:
                window.add(s[right])
            if freqs[s[right]] == 0:
                window.remove(s[right])

            right += 1
        
        res.append(right - left)
        return res

## IDEA: find the freqs of the letters using counter
# then, keep the set of the elements in the current window that still have instances left;
# increase the window until all the instances of the elements are in the window
# then create a new window and repeat
        