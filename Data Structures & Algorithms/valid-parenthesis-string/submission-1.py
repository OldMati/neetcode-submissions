class Solution:
    def checkValidString(self, s: str) -> bool:
        # low - min possible number of unmatched (
        # high - max possible number of unmatched (
        low = high = 0
        
        for c in s:
            if c == '(':
                # low and max increases
                low += 1
                high += 1
            elif c == ')':
                # low and max decreases
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            # if too many closing brackets, return False
            if high < 0:
                return False
                
            if low < 0:
                low = 0

        return low == 0
        