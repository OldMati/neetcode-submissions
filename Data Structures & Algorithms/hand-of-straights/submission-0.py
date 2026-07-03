class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        num_of_groups = len(hand) / groupSize
        if not num_of_groups == int(num_of_groups):
            return False
        
        freqs = Counter(hand)
        hand.sort()

        for num in hand:
            # if used all already, continue
            if freqs[num] <= 0:
                continue
            freqs[num] -= 1
            # else start a new group, try to fill it
            for j in range(num + 1, num + groupSize):
                # if no number to fill a group, return False
                if j not in freqs or freqs[j] == 0:
                    print('cant create a group from', num, ' fails on ', j)
                    print(freqs)
                    return False
                
                # else use it for this group and decrease freq
                freqs[j] -= 1
            print(f'created group from {num} to {num+groupSize}')

        return True